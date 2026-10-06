#!/usr/bin/env python3
"""Reverse Engineering calculators, rebuilt from two of Matt's sheets.

1. profit   = "Reverse Engineering Sheet Template" (Five Quick Wins, Quick Win #3)
              Net profit goal -> revenue, clients, calls, closers, setters, daily ad spend.
2. scaling  = "Scaling Reverse Engineering Template" (Facebook Ads Phase #2, Step #5)
              Lifetime revenue goal -> clients, shows, booked calls, applications, clicks, ad spend.

Both take an Actual and a Goal column and report the % difference, exactly like the sheets.

    python3 reverse_engineering.py profit inputs.json
    python3 reverse_engineering.py scaling inputs.json
    python3 reverse_engineering.py profit --example      (the sheet's own example)
    python3 reverse_engineering.py profit --template     (empty inputs to fill in)
    python3 reverse_engineering.py --test

inputs.json shape: {"actual": {...}, "goal": {...}}. Rates are decimals (0.2 = 20%).
"""
import json, sys


def div(a, b):
    return a / b if b else 0.0


def pct_diff(actual, goal):
    return div(goal - actual, abs(actual))


# ---------------- profit (Five Quick Wins) ----------------
PROFIT_TEMPLATE = {
    "net_profit_goal": 1000000, "net_margin": 0.15, "monthly_churn_rate": 0.18,
    "median_monthly_retainer": 3000, "close_rate_booked_call": 0.2, "working_days_per_year": 260,
    "calls_closer_takes_per_week": 25, "calls_setter_books_per_week": 12.5, "cost_per_call_ads": 500,
}
PROFIT_EXAMPLE = {
    "actual": dict(PROFIT_TEMPLATE),
    "goal": {"net_profit_goal": 1000000, "net_margin": 0.4, "monthly_churn_rate": 0.07,
             "median_monthly_retainer": 5000, "close_rate_booked_call": 0.3, "working_days_per_year": 260,
             "calls_closer_takes_per_week": 25, "calls_setter_books_per_week": 12.5, "cost_per_call_ads": 200},
}


def profit_column(i):
    revenue = div(i["net_profit_goal"], i["net_margin"])
    relationship_months = div(1, i["monthly_churn_rate"])
    ltv = i["median_monthly_retainer"] * relationship_months
    clients = div(revenue, ltv)
    calls = div(clients, i["close_rate_booked_call"])
    per_day = div(calls, i["working_days_per_year"])
    per_week = calls / 52
    per_month = calls / 12
    return {
        "net_profit_goal": i["net_profit_goal"], "net_margin": i["net_margin"], "revenue_required": revenue,
        "monthly_churn_rate": i["monthly_churn_rate"], "avg_client_relationship_months": relationship_months,
        "median_monthly_retainer": i["median_monthly_retainer"], "avg_ltv_per_client": ltv,
        "clients_required": clients, "close_rate_booked_call": i["close_rate_booked_call"],
        "calls_required": calls, "working_days_per_year": i["working_days_per_year"],
        "calls_per_day_required": per_day, "calls_per_week_required": per_week, "calls_per_month_required": per_month,
        "calls_closer_takes_per_week": i["calls_closer_takes_per_week"],
        "closers_required": div(per_week, i["calls_closer_takes_per_week"]),
        "calls_setter_books_per_week": i["calls_setter_books_per_week"],
        "appt_setters_required": div(per_week, i["calls_setter_books_per_week"]),
        "cost_per_call_ads": i["cost_per_call_ads"], "daily_ad_spend_required": per_day * i["cost_per_call_ads"],
    }


# ---------------- scaling (Facebook Ads Phase 2) ----------------
SCALING_TEMPLATE = {
    "lifetime_revenue_goal": 10000000, "customer_lifetime_revenue": 20000, "close_rate_shown_calls": 0.15,
    "show_rate_booked_calls": 0.55, "call_booked_rate_applications": 0.45, "application_rate_outbound_clicks": 0.06,
    "cost_per_outbound_click": 6.0,
}
SCALING_EXAMPLE = {
    "actual": dict(SCALING_TEMPLATE),
    "goal": {"lifetime_revenue_goal": 10000000, "customer_lifetime_revenue": 20000, "close_rate_shown_calls": 0.2,
             "show_rate_booked_calls": 0.625, "call_booked_rate_applications": 0.5,
             "application_rate_outbound_clicks": 0.08, "cost_per_outbound_click": 5.0},
}


def scaling_column(i):
    clients = div(i["lifetime_revenue_goal"], i["customer_lifetime_revenue"])
    shows = div(clients, i["close_rate_shown_calls"])
    booked = div(shows, i["show_rate_booked_calls"])
    applications = div(booked, i["call_booked_rate_applications"])
    clicks = div(applications, i["application_rate_outbound_clicks"])
    spend = clicks * i["cost_per_outbound_click"]
    return {
        "lifetime_revenue_goal": i["lifetime_revenue_goal"], "customer_lifetime_revenue": i["customer_lifetime_revenue"],
        "clients_needed": clients, "close_rate_shown_calls": i["close_rate_shown_calls"], "shows_needed": shows,
        "show_rate_booked_calls": i["show_rate_booked_calls"], "calls_booked_needed": booked,
        "call_booked_rate_applications": i["call_booked_rate_applications"], "applications_needed": applications,
        "application_rate_outbound_clicks": i["application_rate_outbound_clicks"], "outbound_clicks_needed": clicks,
        "cost_per_outbound_click": i["cost_per_outbound_click"], "total_ad_spend_required": spend,
        "average_daily_ad_spend_365": spend / 365, "ad_spend_per_booked_call": div(spend, booked),
        "ad_spend_per_client": div(spend, clients),
    }


def run(kind, inputs):
    fn = profit_column if kind == "profit" else scaling_column
    tmpl = PROFIT_TEMPLATE if kind == "profit" else SCALING_TEMPLATE
    a = dict(tmpl); a.update(inputs.get("actual", {}))
    g = dict(tmpl); g.update(inputs.get("goal", {}))
    actual, goal = fn(a), fn(g)
    return {k: {"actual": actual[k], "goal": goal[k], "pct_difference": pct_diff(actual[k], goal[k])} for k in actual}


def self_test():
    p = run("profit", PROFIT_EXAMPLE)
    s = run("scaling", SCALING_EXAMPLE)
    checks = [  # from the sheets' Example tabs
        (p["revenue_required"]["actual"], 6666666.667), (p["revenue_required"]["goal"], 2500000),
        (p["avg_ltv_per_client"]["actual"], 16666.667), (p["avg_ltv_per_client"]["goal"], 71428.571),
        (p["clients_required"]["actual"], 400), (p["clients_required"]["goal"], 35),
        (p["calls_required"]["actual"], 2000), (p["calls_per_week_required"]["actual"], 38.4615),
        (p["closers_required"]["actual"], 1.5385), (p["appt_setters_required"]["goal"], 0.17949),
        (p["daily_ad_spend_required"]["actual"], 3846.1538), (p["daily_ad_spend_required"]["goal"], 89.7436),
        (p["calls_required"]["pct_difference"], -0.94167),
        (s["clients_needed"]["actual"], 500), (s["shows_needed"]["actual"], 3333.333), (s["shows_needed"]["goal"], 2500),
        (s["calls_booked_needed"]["actual"], 6060.606), (s["applications_needed"]["actual"], 13468.013),
        (s["outbound_clicks_needed"]["actual"], 224466.891), (s["total_ad_spend_required"]["actual"], 1346801.347),
        (s["total_ad_spend_required"]["goal"], 500000), (s["average_daily_ad_spend_365"]["actual"], 3689.8667),
        (s["ad_spend_per_booked_call"]["actual"], 222.2222), (s["ad_spend_per_client"]["goal"], 1000),
        (s["total_ad_spend_required"]["pct_difference"], -0.62875),
    ]
    bad = [(got, want) for got, want in checks if abs(got - want) > max(0.01, abs(want) * 0.0005)]
    if bad:
        for got, want in bad:
            print(f"MISMATCH: sheet {want} vs script {got}")
        sys.exit(1)
    print(f"self-test passed: {len(checks)} values match the two sheets' Example tabs")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__); sys.exit(0)
    if args[0] == "--test":
        self_test(); sys.exit(0)
    kind = args[0]
    if kind not in ("profit", "scaling") or len(args) < 2:
        print(__doc__); sys.exit(1)
    if args[1] == "--template":
        print(json.dumps({"actual": PROFIT_TEMPLATE if kind == "profit" else SCALING_TEMPLATE,
                          "goal": PROFIT_TEMPLATE if kind == "profit" else SCALING_TEMPLATE}, indent=2)); sys.exit(0)
    inputs = (PROFIT_EXAMPLE if kind == "profit" else SCALING_EXAMPLE) if args[1] == "--example" else json.load(open(args[1]))
    print(json.dumps(run(kind, inputs), indent=2))
