#!/usr/bin/env python3
"""Unit Economics Model, rebuilt from Matt's "Unit Economics Model Spreadsheet Template".

Source sheet: assets/templates/unit-economics-model-spreadsheet-template/ (formulas.md has every cell).
Targets from the sheet: Unit Economics Multiple 2X+, Gross Margin 80%+, Effective Hourly Rate $250+.

Run with a JSON file of inputs, or --example to run the sheet's own filled example:
    python3 unit_economics.py inputs.json
    python3 unit_economics.py --example
    python3 unit_economics.py --template      (prints an empty inputs.json to fill in)

Every input the sheet marks "Manual input" is an input here. Rates are decimals (0.6 = 60%).
"""
import json, sys

TEMPLATE = {
    "cost_per_click": 10.0,
    "application_rate": 0.08,            # applications / clicks
    "call_booked_rate": 0.5,             # booked calls / applications
    "show_rate": 0.6,                    # shows / booked calls
    "close_rate_live_calls": 0.2,        # closes / shows
    "gross_cash_collected_per_sale": 10000.0,
    "payment_processing_rate": 0.03,     # sheet uses 3%
    "closer_commission_rate": 0.10,      # of net cash collected (sheet: 10%)
    "setter_commission_rate": 0.10,      # of net cash collected (sheet: 10%)
    "months_of_delivery_covered_upfront": 3.0,
    "monthly_ad_spend": 20000.0,
    "other_acquisition_costs_per_customer": 0.0,
    "other_fulfillment_costs_per_customer": 0.0,
    # list of tech costs: name, department (Acquisition / Fulfillment / Management), monthly cost
    "tech_costs": [["Landing Page Builder", "Acquisition", 49], ["CRM", "Acquisition", 99]],
    # list of salaries: name, department, monthly salary, hourly rate
    "salaries": [["Founder / Media Buyer", "Acquisition", 8000, 50.0], ["Fulfillment Team Member", "Fulfillment", 2000, 12.5]],
    # every step in a full delivery, with minutes required
    "delivery_steps": [["Kickoff call", 60], ["Build landing page", 120]],
}

EXAMPLE = {
    "cost_per_click": 10.0, "application_rate": 0.08, "call_booked_rate": 0.5, "show_rate": 0.6,
    "close_rate_live_calls": 0.2, "gross_cash_collected_per_sale": 10000.0, "payment_processing_rate": 0.03,
    "closer_commission_rate": 0.10, "setter_commission_rate": 0.10, "months_of_delivery_covered_upfront": 3.0,
    "monthly_ad_spend": 20000.0, "other_acquisition_costs_per_customer": 0.0, "other_fulfillment_costs_per_customer": 0.0,
    "tech_costs": [
        ["Landing Page Builder", "Acquisition", 49], ["Email Marketing Tool", "Acquisition", 30], ["CRM", "Acquisition", 99],
        ["SMS Tool", "Acquisition", 25], ["Dialing Tool", "Acquisition", 30], ["Call Booking / Calendar Tool", "Acquisition", 12],
        ["VSL / Video Hosting", "Acquisition", 20], ["Zoom / Call Recording", "Acquisition", 15], ["Loom", "Acquisition", 12],
        ["Zapier / Automation", "Acquisition", 30], ["Project Management Tool", "Fulfillment", 10], ["AI Tools", "Fulfillment", 40]],
    "salaries": [
        ["Founder / Media Buyer", "Acquisition", 8000, 50.0], ["Appointment Setter (Base)", "Acquisition", 1500, 9.38],
        ["Closer (Base)", "Acquisition", 2000, 12.5], ["Creative Strategist", "Acquisition", 3000, 18.75],
        ["Video Editor 1", "Acquisition", 1500, 9.38], ["Video Editor 2", "Acquisition", 1500, 9.38],
        ["Video Editor 3", "Acquisition", 1500, 9.38], ["CRM Champion", "Fulfillment", 2000, 12.5],
        ["PM Champion", "Management", 2500, 15.62], ["Proof Champion", "Fulfillment", 1500, 9.38],
        ["Tech Person", "Fulfillment", 2500, 15.62], ["Fulfillment Team Member", "Fulfillment", 2000, 12.5]],
    "delivery_steps": [
        ["Send onboarding form", 10], ["Chase missing onboarding information", 20], ["Kickoff call", 60],
        ["Get ad account access", 15], ["Set up pixel and conversion events", 45], ["Write ad copy from winning angles", 90],
        ["Brief video editor", 20], ["Review and fix ad edits", 45], ["Build landing page from template", 120],
        ["Send landing page for client approval", 10], ["Chase client approval", 15], ["Make client revisions", 45],
        ["Launch campaigns", 30], ["Check campaigns after 72 hours", 20], ["Monthly optimization calls (3)", 180],
        ["Weekly reports (12)", 240], ["New ad batches (3)", 270]],
}


def div(a, b):
    """Sheet uses IFERROR(x/y, 0): a zero denominator gives 0, not a crash."""
    return a / b if b else 0.0


def model(i):
    # Funnel costs (sheet rows 2-10, column B)
    cost_per_call = div(div(i["cost_per_click"], i["application_rate"]), i["call_booked_rate"])
    cost_per_live_call = div(cost_per_call, i["show_rate"])
    ad_cost_per_customer = div(cost_per_live_call, i["close_rate_live_calls"])

    # Cash (rows 20-22)
    gross = i["gross_cash_collected_per_sale"]
    fees = gross * i["payment_processing_rate"]
    net = gross - fees
    months = i["months_of_delivery_covered_upfront"]

    # Customers per month (rows 23-25)
    customers = div(i["monthly_ad_spend"], ad_cost_per_customer)

    # Cost tables (rows 28-49)
    tech = {"Acquisition": 0.0, "Fulfillment": 0.0, "Management": 0.0}
    for _, dept, cost in i["tech_costs"]:
        tech[dept] = tech.get(dept, 0.0) + cost
    sal = {"Acquisition": 0.0, "Fulfillment": 0.0, "Management": 0.0}
    hourly = []
    for _, dept, monthly, rate in i["salaries"]:
        sal[dept] = sal.get(dept, 0.0) + monthly
        if dept == "Fulfillment":
            hourly.append(rate)
    avg_fulfillment_hourly = sum(hourly) / len(hourly) if hourly else 0.0
    delivery_minutes = sum(m for _, m in i["delivery_steps"])
    delivery_hours = delivery_minutes / 60

    # Acquisition labor + software per customer (rows 2-4, columns D/F)
    closer = net * i["closer_commission_rate"]
    setter = net * i["setter_commission_rate"]
    acq_salaries_per_customer = div(sal["Acquisition"], customers)
    acq_software_per_customer = div(tech["Acquisition"], customers)
    acq_labor_total = closer + setter + acq_salaries_per_customer
    acq_software_total = acq_software_per_customer + i["other_acquisition_costs_per_customer"]

    # Fulfillment per customer (rows 12-18)
    fulfillment_labor = delivery_hours * avg_fulfillment_hourly
    management = div(sal["Management"], customers) * months
    fulfillment_software = div(tech["Fulfillment"], customers) * months
    fulfillment_labor_total = fulfillment_labor + management
    fulfillment_total = fulfillment_labor_total + fulfillment_software + i["other_fulfillment_costs_per_customer"]

    # Unit economics (rows 20-26, column F)
    acquisition_total = ad_cost_per_customer + acq_labor_total + acq_software_total
    multiple = div(net, acquisition_total + fulfillment_total)
    gross_margin = div(gross - fulfillment_total, gross)
    effective_hourly = div(gross, delivery_hours)

    # Monthly totals (rows 53-75)
    calls = div(i["monthly_ad_spend"], cost_per_call)
    applications = div(calls, i["call_booked_rate"])
    shows = calls * i["show_rate"]
    closes = shows * i["close_rate_live_calls"]
    cost_per_customer = div(div(cost_per_call, i["show_rate"]), i["close_rate_live_calls"])
    costs_per_sale = (ad_cost_per_customer + closer + setter + acq_software_per_customer
                      + acq_salaries_per_customer + i["other_acquisition_costs_per_customer"] + fulfillment_total)
    profit_per_sale = net - costs_per_sale
    roas = div(gross, ad_cost_per_customer)
    net_roas = div(gross, costs_per_sale)

    return {
        "funnel": {
            "cost_per_call": cost_per_call, "cost_per_live_call": cost_per_live_call,
            "ad_cost_per_customer": ad_cost_per_customer, "cost_per_customer": cost_per_customer,
        },
        "per_customer_costs": {
            "ad_spend": ad_cost_per_customer, "closer_commission": closer, "setter_commission": setter,
            "acquisition_salaries": acq_salaries_per_customer, "acquisition_software": acq_software_per_customer,
            "acquisition_total": acquisition_total,
            "fulfillment_labor": fulfillment_labor, "management_and_supervision": management,
            "fulfillment_software": fulfillment_software, "fulfillment_total": fulfillment_total,
        },
        "cash_per_sale": {"gross": gross, "payment_fees": fees, "net": net},
        "unit_economics": {
            "unit_economics_multiple": multiple, "target_multiple": "2X+",
            "gross_margin": gross_margin, "target_gross_margin": "80%+",
            "total_delivery_hours": delivery_hours,
            "effective_hourly_rate": effective_hourly, "target_effective_hourly_rate": "$250+",
            "average_profit_per_sale": profit_per_sale, "roas": roas, "net_roas": net_roas,
        },
        "monthly": {
            "ad_spend": i["monthly_ad_spend"], "applications": applications, "calls": calls, "shows": shows,
            "closes": closes, "customers": customers,
            "gross_cash_collected": gross * closes, "net_cash_collected": net * closes,
            "total_costs": costs_per_sale * closes, "net_profit": profit_per_sale * closes,
        },
    }


def self_test():
    r = model(EXAMPLE)
    checks = {  # values read from the sheet's Filled Example tab
        ("funnel", "cost_per_call"): 250.0,
        ("funnel", "cost_per_live_call"): 416.6667,
        ("funnel", "ad_cost_per_customer"): 2083.3333,
        ("per_customer_costs", "acquisition_salaries"): 1979.1667,
        ("per_customer_costs", "acquisition_software"): 33.5417,
        ("per_customer_costs", "fulfillment_labor"): 257.2917,
        ("per_customer_costs", "management_and_supervision"): 781.25,
        ("per_customer_costs", "fulfillment_software"): 15.625,
        ("per_customer_costs", "acquisition_total"): 6036.0417,
        ("per_customer_costs", "fulfillment_total"): 1054.1667,
        ("unit_economics", "unit_economics_multiple"): 1.3681,
        ("unit_economics", "gross_margin"): 0.8946,
        ("unit_economics", "total_delivery_hours"): 20.5833,
        ("unit_economics", "effective_hourly_rate"): 485.83,
        ("monthly", "customers"): 9.6,
        ("monthly", "applications"): 160, ("monthly", "calls"): 80, ("monthly", "shows"): 48,
    }
    bad = [(k, v, r[k[0]][k[1]]) for k, v in checks.items() if abs(r[k[0]][k[1]] - v) > max(0.01, abs(v) * 0.0005)]
    if bad:
        for k, want, got in bad:
            print(f"MISMATCH {k}: sheet {want} vs script {got}")
        sys.exit(1)
    print(f"self-test passed: {len(checks)} values match the sheet's Filled Example")


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__); sys.exit(0)
    if sys.argv[1] == "--template":
        print(json.dumps(TEMPLATE, indent=2)); sys.exit(0)
    if sys.argv[1] == "--test":
        self_test(); sys.exit(0)
    inputs = EXAMPLE if sys.argv[1] == "--example" else json.load(open(sys.argv[1]))
    merged = dict(TEMPLATE); merged.update(inputs)
    print(json.dumps(model(merged), indent=2))
