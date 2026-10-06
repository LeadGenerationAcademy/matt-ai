# Formulas

Cell references point at the CSV files in this folder (same sheet names).

## Blank Template

One line per row; consecutive rows with the same formula pattern are listed once.

- row 2 (Acquisition Software Per Customer): F2 =IFERROR(SUMIF($B$29:$B$48,"Acquisition",$C$29:$C$48)/D25,0)
- row 4 (Acquisition Salaries Per Customer): D4 =IFERROR(SUMIF($E$29:$E$48,"Acquisition",$F$29:$F$48)/D25,0)
- row 5 (Cost Per Call): B5 =IFERROR(B2/B3/B4,0)
- row 8 (Cost Per Live Call): B8 =IFERROR(B5/B6,0)
- row 10 (Total Ad Costs (Per Customer)): B10 =IFERROR(B8/B9,0); D10 =SUM(D2:D9); F10 =SUM(F2:F9)
- row 12 (Fulfillment Labor Per Customer): B12 =IFERROR(J49/60*AVERAGEIF($E$29:$E$48,"Fulfillment",$G$29:$G$48),0); D12 =IFERROR(SUMIF($B$29:$B$48,"Fulfillment",$C$29:$C$48)/D25*B23,0)
- row 13 (Managers & Supervision Per Customer): B13 =IFERROR(SUMIF($E$29:$E$48,"Management",$F$29:$F$48)/D25*B23,0)
- row 18 (Total): B18 =SUM(B12:B17); D18 =SUM(D12:D17); F18 =SUM(F12:F17)
- row 20 (Cash Collected): D20 =B20*D25; F20 =B22
- row 21 (Payment Processing Fees): D21 =B21*D25; F21 =B10+D10+F10
- row 22 (Net Cash Collected): B22 =B20-B21; D22 =B22*D25; F22 =B18+D18+F18
- row 23 (Monthly Spend): D23 =B53; F23 =IFERROR(F20/(F21+F22),0)
- row 24 (Ad Spend Per Customer): D24 =B10; F24 =IFERROR((B20-F22)/B20,0)
- row 25 (Customers): D25 =IFERROR(D23/D24,0); F25 =IFERROR(J49/60,0)
- row 26 (Effective Hourly Rate): F26 =IFERROR(B20/F25,0)
- row 49 (Total): C49 =SUM(C29:C48); F49 =SUM(F29:F48); J49 =SUM(J29:J48)
- row 54 (Call Booked Rate): B54 =B4; D54 =IFERROR(D55/B54,0)
- row 55 (Cost Per Call): B55 =B5; D55 =IFERROR(B53/B55,0)
- row 56 (Show Rate): B56 =B6; D56 =D55*B56
- row 59 (Cost Per Live Call): B59 =IFERROR(B55/B56,0)
- row 60 (Cost Per Customer): B60 =IFERROR(B55/B56/B58,0); D60 =D58
- row 62 (Gross Cash Collected Per Sale): B62 =B20; D62 =B62*D60
- row 66 (Closer Costs Per Sale): B66 =D2; D66 =B66*D60
- row 68 (Acquisition Software Costs Per Sale): B68 =F2; D68 =B68*D60
- row 69 (Acquisition Salaries Per Sale): B69 =D4; D69 =B69*D60
- row 70 (Other Acquisition Costs Per Sale): B70 =F3; D70 =B70*D60
- row 72 (Average Costs Per Sale): B72 =SUM(B65:B71); D72 =SUM(D65:D71)
- row 73 (Average Profit Per Sale): B73 =B64-B72; D73 =D64-D72
- row 74 (ROAS): B74 =IFERROR(B62/B65,0); D74 =IFERROR(D62/D65,0)
- row 79 (Ad Spend): B79 =B53
- row 80 (Cost Per Call [WORST]): B80 =B5; C80 =IFERROR(B79/B80,0)
- row 81 (Show Rate): B81 =B6; C81 =C80*B81
- row 84 (Cash Collected Per Sale): B84 =B20; C84 =C83*B84; E84 =C83; G84 =IFERROR(B79/E84,0)
- row 85 (ROAS): C85 =IFERROR(C84/B79,0)
- row 86 (Fixed Costs): C86 =C49
- row 87 (Team Costs): C87 =F49
- row 88 (Sales): C88 =E84*(D2+D3)
- row 89 (Total Cost): C89 =B79+C86+C87+C88
- row 90 (Net Profit): C90 =C84-C89
- row 91 (Net ROAS): C91 =IFERROR(C84/C89,0)

## Filled Example

One line per row; consecutive rows with the same formula pattern are listed once.

- row 2 (Acquisition Software Per Customer): F2 =IFERROR(SUMIF($B$29:$B$48,"Acquisition",$C$29:$C$48)/D25,0)
- row 4 (Acquisition Salaries Per Customer): D4 =IFERROR(SUMIF($E$29:$E$48,"Acquisition",$F$29:$F$48)/D25,0)
- row 5 (Cost Per Call): B5 =IFERROR(B2/B3/B4,0)
- row 8 (Cost Per Live Call): B8 =IFERROR(B5/B6,0)
- row 10 (Total Ad Costs (Per Customer)): B10 =IFERROR(B8/B9,0); D10 =SUM(D2:D9); F10 =SUM(F2:F9)
- row 12 (Fulfillment Labor Per Customer): B12 =IFERROR(J49/60*AVERAGEIF($E$29:$E$48,"Fulfillment",$G$29:$G$48),0); D12 =IFERROR(SUMIF($B$29:$B$48,"Fulfillment",$C$29:$C$48)/D25*B23,0)
- row 13 (Managers & Supervision Per Customer): B13 =IFERROR(SUMIF($E$29:$E$48,"Management",$F$29:$F$48)/D25*B23,0)
- row 18 (Total): B18 =SUM(B12:B17); D18 =SUM(D12:D17); F18 =SUM(F12:F17)
- row 20 (Cash Collected): D20 =B20*D25; F20 =B22
- row 21 (Payment Processing Fees): D21 =B21*D25; F21 =B10+D10+F10
- row 22 (Net Cash Collected): B22 =B20-B21; D22 =B22*D25; F22 =B18+D18+F18
- row 23 (Monthly Spend): D23 =B53; F23 =IFERROR(F20/(F21+F22),0)
- row 24 (Ad Spend Per Customer): D24 =B10; F24 =IFERROR((B20-F22)/B20,0)
- row 25 (Customers): D25 =IFERROR(D23/D24,0); F25 =IFERROR(J49/60,0)
- row 26 (Effective Hourly Rate): F26 =IFERROR(B20/F25,0)
- row 49 (Total): C49 =SUM(C29:C48); F49 =SUM(F29:F48); J49 =SUM(J29:J48)
- row 54 (Call Booked Rate): B54 =B4; D54 =IFERROR(D55/B54,0)
- row 55 (Cost Per Call): B55 =B5; D55 =IFERROR(B53/B55,0)
- row 56 (Show Rate): B56 =B6; D56 =D55*B56
- row 59 (Cost Per Live Call): B59 =IFERROR(B55/B56,0)
- row 60 (Cost Per Customer): B60 =IFERROR(B55/B56/B58,0); D60 =D58
- row 62 (Gross Cash Collected Per Sale): B62 =B20; D62 =B62*D60
- row 66 (Closer Costs Per Sale): B66 =D2; D66 =B66*D60
- row 68 (Acquisition Software Costs Per Sale): B68 =F2; D68 =B68*D60
- row 69 (Acquisition Salaries Per Sale): B69 =D4; D69 =B69*D60
- row 70 (Other Acquisition Costs Per Sale): B70 =F3; D70 =B70*D60
- row 72 (Average Costs Per Sale): B72 =SUM(B65:B71); D72 =SUM(D65:D71)
- row 73 (Average Profit Per Sale): B73 =B64-B72; D73 =D64-D72
- row 74 (ROAS): B74 =IFERROR(B62/B65,0); D74 =IFERROR(D62/D65,0)
- row 79 (Ad Spend): B79 =B53
- row 80 (Cost Per Call [WORST]): B80 =B5; C80 =IFERROR(B79/B80,0)
- row 81 (Show Rate): B81 =B6; C81 =C80*B81
- row 84 (Cash Collected Per Sale): B84 =B20; C84 =C83*B84; E84 =C83; G84 =IFERROR(B79/E84,0)
- row 85 (ROAS): C85 =IFERROR(C84/B79,0)
- row 86 (Fixed Costs): C86 =C49
- row 87 (Team Costs): C87 =F49
- row 88 (Sales): C88 =E84*(D2+D3)
- row 89 (Total Cost): C89 =B79+C86+C87+C88
- row 90 (Net Profit): C90 =C84-C89
- row 91 (Net ROAS): C91 =IFERROR(C84/C89,0)
