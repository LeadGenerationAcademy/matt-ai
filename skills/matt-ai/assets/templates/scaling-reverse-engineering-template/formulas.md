# Formulas

Cell references point at the CSV files in this folder (same sheet names).

## Reverse Engineering

One line per row; consecutive rows with the same formula pattern are listed once.

- row 17 (Lifetime Revenue Goal): D17 =IFERROR((C17-B17)/ABS(B17),0)
- row 19 (Clients Needed): B19 =IFERROR(B17/B18,0); C19 =IFERROR(C17/C18,0); D19 =IFERROR((C19-B19)/ABS(B19),0)
- row 21 (Close Rate (Shown Calls)): D21 =IFERROR((C21-B21)/ABS(B21),0)
- row 22 (Shows Needed): B22 =IFERROR(B19/B21,0); C22 =IFERROR(C19/C21,0); D22 =IFERROR((C22-B22)/ABS(B22),0)
- row 23 (Show Rate (Booked Calls)): D23 =IFERROR((C23-B23)/ABS(B23),0)
- row 24 (Calls Booked Needed): B24 =IFERROR(B22/B23,0); C24 =IFERROR(C22/C23,0); D24 =IFERROR((C24-B24)/ABS(B24),0)
- row 26 (Call-Booked Rate (Applications)): D26 =IFERROR((C26-B26)/ABS(B26),0)
- row 27 (Applications Needed): B27 =IFERROR(B24/B26,0); C27 =IFERROR(C24/C26,0); D27 =IFERROR((C27-B27)/ABS(B27),0)
- row 28 (Application Rate (Outbound Clicks)): D28 =IFERROR((C28-B28)/ABS(B28),0)
- row 29 (Outbound Clicks Needed): B29 =IFERROR(B27/B28,0); C29 =IFERROR(C27/C28,0); D29 =IFERROR((C29-B29)/ABS(B29),0)
- row 31 (Cost Per Outbound Click): D31 =IFERROR((C31-B31)/ABS(B31),0)
- row 32 (Total Ad Spend Required): B32 =IFERROR(B29*B31,0); C32 =IFERROR(C29*C31,0); D32 =IFERROR((C32-B32)/ABS(B32),0)
- row 33 (Average Daily Ad Spend (365 Days)): B33 =IFERROR(B32/365,0); C33 =IFERROR(C32/365,0); D33 =IFERROR((C33-B33)/ABS(B33),0)
- row 34 (Ad Spend Per Booked Call): B34 =IFERROR(B32/B24,0); C34 =IFERROR(C32/C24,0); D34 =IFERROR((C34-B34)/ABS(B34),0)

## Reverse Engineering Example

One line per row; consecutive rows with the same formula pattern are listed once.

- row 17 (Lifetime Revenue Goal): D17 =IFERROR((C17-B17)/ABS(B17),0)
- row 19 (Clients Needed): B19 =IFERROR(B17/B18,0); C19 =IFERROR(C17/C18,0); D19 =IFERROR((C19-B19)/ABS(B19),0)
- row 21 (Close Rate (Shown Calls)): D21 =IFERROR((C21-B21)/ABS(B21),0)
- row 22 (Shows Needed): B22 =IFERROR(B19/B21,0); C22 =IFERROR(C19/C21,0); D22 =IFERROR((C22-B22)/ABS(B22),0)
- row 23 (Show Rate (Booked Calls)): D23 =IFERROR((C23-B23)/ABS(B23),0)
- row 24 (Calls Booked Needed): B24 =IFERROR(B22/B23,0); C24 =IFERROR(C22/C23,0); D24 =IFERROR((C24-B24)/ABS(B24),0)
- row 26 (Call-Booked Rate (Applications)): D26 =IFERROR((C26-B26)/ABS(B26),0)
- row 27 (Applications Needed): B27 =IFERROR(B24/B26,0); C27 =IFERROR(C24/C26,0); D27 =IFERROR((C27-B27)/ABS(B27),0)
- row 28 (Application Rate (Outbound Clicks)): D28 =IFERROR((C28-B28)/ABS(B28),0)
- row 29 (Outbound Clicks Needed): B29 =IFERROR(B27/B28,0); C29 =IFERROR(C27/C28,0); D29 =IFERROR((C29-B29)/ABS(B29),0)
- row 31 (Cost Per Outbound Click): D31 =IFERROR((C31-B31)/ABS(B31),0)
- row 32 (Total Ad Spend Required): B32 =IFERROR(B29*B31,0); C32 =IFERROR(C29*C31,0); D32 =IFERROR((C32-B32)/ABS(B32),0)
- row 33 (Average Daily Ad Spend (365 Days)): B33 =IFERROR(B32/365,0); C33 =IFERROR(C32/365,0); D33 =IFERROR((C33-B33)/ABS(B33),0)
- row 34 (Ad Spend Per Booked Call): B34 =IFERROR(B32/B24,0); C34 =IFERROR(C32/C24,0); D34 =IFERROR((C34-B34)/ABS(B34),0)
