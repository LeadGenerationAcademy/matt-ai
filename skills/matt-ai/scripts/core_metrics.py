#!/usr/bin/env python3
"""Matt's Core Metrics, calculated exactly the way his tracking sheets calculate them.

Definitions come from the Dashboard tabs of these templates (see assets/templates/):
  net-margin-tracker-template          Net Profit = Revenue - Expenses; Net Margin = Net Profit / Revenue
  monthly-churn-and-average-retainer   Churn Rate = Cancelled / Clients At Start; relationship months = 1 / churn
  close-rate-tracker-template          Close Rate = Closed Won / Qualified Calls (calls that happened AND were qualified,
                                       not calls booked). Show Rate = Shown / Booked. Qualification Rate = Qualified / Shown.
                                       Offer Rate = Offers / Qualified. Offer Close Rate = Closed Won / Offers.
  cost-per-call-template               Total Acquisition Spend = Ad Spend + Other Expenses.
                                       Cost Per Call Booked / Shown / Qualified = Total Acquisition Spend / that count.

    python3 core_metrics.py inputs.json
    python3 core_metrics.py --template     (empty inputs to fill in; leave out anything you do not have)
    python3 core_metrics.py --test

Only the metrics whose inputs were given are returned. Rates are decimals (0.2 = 20%).
"""
import json, sys

TEMPLATE = {
    "revenue": 0, "expenses": 0,
    "clients_at_start": 0, "new_clients": 0, "cancelled_clients": 0, "median_monthly_retainer": 0,
    "applications": 0, "calls_booked": 0, "calls_shown": 0, "qualified_calls": 0, "offers_sent": 0, "closed_won": 0,
    "ad_spend": 0, "other_acquisition_expenses": 0,
}


def div(a, b):
    return a / b if b else None


def metrics(i):
    g = lambda k: i.get(k) or 0
    out = {}
    if g("revenue"):
        np_ = g("revenue") - g("expenses")
        out["net_profit"] = np_
        out["net_margin"] = div(np_, g("revenue"))
    if g("clients_at_start"):
        churn = div(g("cancelled_clients"), g("clients_at_start"))
        out["clients_at_end"] = g("clients_at_start") + g("new_clients") - g("cancelled_clients")
        out["monthly_churn_rate"] = churn
        if churn:
            months = 1 / churn
            out["avg_client_relationship_months"] = months
            if g("median_monthly_retainer"):
                out["avg_ltv_per_client"] = g("median_monthly_retainer") * months
    if g("calls_booked"):
        out["call_booked_rate"] = div(g("calls_booked"), g("applications"))
        out["show_rate"] = div(g("calls_shown"), g("calls_booked"))
        out["qualification_rate"] = div(g("qualified_calls"), g("calls_shown"))
        out["offer_rate"] = div(g("offers_sent"), g("qualified_calls"))
        out["offer_close_rate"] = div(g("closed_won"), g("offers_sent"))
        out["close_rate"] = div(g("closed_won"), g("qualified_calls"))
    if g("ad_spend") or g("other_acquisition_expenses"):
        spend = g("ad_spend") + g("other_acquisition_expenses")
        out["total_acquisition_spend"] = spend
        out["cost_per_call_booked"] = div(spend, g("calls_booked"))
        out["cost_per_call_shown"] = div(spend, g("calls_shown"))
        out["cost_per_qualified_call"] = div(spend, g("qualified_calls"))
        out["cost_per_customer"] = div(spend, g("closed_won"))
        if g("revenue"):
            out["roas"] = div(g("revenue"), g("ad_spend"))
    return {k: v for k, v in out.items() if v is not None}


def self_test():
    # Cost Per Call dashboard example, January: 29131.36 ad spend + 11209.12 other, 209 booked -> 193.0167
    m = metrics({"ad_spend": 29131.36, "other_acquisition_expenses": 11209.12, "calls_booked": 209, "calls_shown": 129, "qualified_calls": 107})
    assert abs(m["cost_per_call_booked"] - 193.0167) < 0.01, m
    assert abs(m["total_acquisition_spend"] - 40340.48) < 0.01, m
    # Net Margin dashboard example, January: 185001.2417 revenue, 75038.10182 expenses -> 0.59439
    m = metrics({"revenue": 185001.2417, "expenses": 75038.10182})
    assert abs(m["net_margin"] - 0.594391) < 0.0001, m
    # Churn dashboard example, February: 11 at start, 6 new, 2 cancelled -> 0.181818, 15 at end
    m = metrics({"clients_at_start": 11, "new_clients": 6, "cancelled_clients": 2})
    assert abs(m["monthly_churn_rate"] - 0.181818) < 0.0001 and m["clients_at_end"] == 15, m
    # Close Rate dashboard example, week of Aug 3: 152 apps, 35 booked, 23 shown, 13 qualified, 13 offers, 5 closed
    m = metrics({"applications": 152, "calls_booked": 35, "calls_shown": 23, "qualified_calls": 13, "offers_sent": 13, "closed_won": 5})
    assert abs(m["close_rate"] - 5 / 13) < 1e-9 and abs(m["show_rate"] - 23 / 35) < 1e-9, m
    print("self-test passed: matches the four dashboard examples")


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__); sys.exit(0)
    if sys.argv[1] == "--template":
        print(json.dumps(TEMPLATE, indent=2)); sys.exit(0)
    if sys.argv[1] == "--test":
        self_test(); sys.exit(0)
    print(json.dumps(metrics(json.load(open(sys.argv[1]))), indent=2))
