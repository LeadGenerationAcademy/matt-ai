# Formulas

Cell references point at the CSV files in this folder (same sheet names).

## Messaging Audit

One line per row; consecutive rows with the same formula pattern are listed once.

- row 15 (At least 80% matched the majority of your ICP characteristics): K15 =IFERROR(COUNTIF(E$15:E$1014,"Yes")/$K$20,""); M15 =IF($K$20=0,"",IF(K15>=L15,"PASS","FAIL"))
- row 16 (At least 80% were financially qualified): K16 =IFERROR(COUNTIF(F$15:F$1014,"Yes")/$K$20,""); M16 =IF($K$20=0,"",IF(K16>=L16,"PASS","FAIL"))
- row 17 (At least 80% had decision-making power): K17 =IFERROR(COUNTIF(G$15:G$1014,"Yes")/$K$20,""); M17 =IF($K$20=0,"",IF(K17>=L17,"PASS","FAIL"))
- row 18 (At least 50% purchased within seven days of the calls): K18 =IFERROR(COUNTIF(H$15:H$1014,"Yes")/$K$20,""); M18 =IF($K$20=0,"",IF(K18>=L18,"PASS","FAIL"))
- row 20 (Calls logged): K20 =COUNTA(E15:E1014)
- row 21 (Tests passed): K21 =COUNTIF(M15:M18,"PASS")&" / 4"

## Messaging Audit Example

One line per row; consecutive rows with the same formula pattern are listed once.

- row 14 (At least 80% matched the majority of your ICP characteristics): K14 =IFERROR(COUNTIF(E$14:E$1013,"Yes")/$K$19,""); M14 =IF($K$19=0,"",IF(K14>=L14,"PASS","FAIL"))
- row 15 (At least 80% were financially qualified): K15 =IFERROR(COUNTIF(F$14:F$1013,"Yes")/$K$19,""); M15 =IF($K$19=0,"",IF(K15>=L15,"PASS","FAIL"))
- row 16 (At least 80% had decision-making power): K16 =IFERROR(COUNTIF(G$14:G$1013,"Yes")/$K$19,""); M16 =IF($K$19=0,"",IF(K16>=L16,"PASS","FAIL"))
- row 17 (At least 50% purchased within seven days of the calls): K17 =IFERROR(COUNTIF(H$14:H$1013,"Yes")/$K$19,""); M17 =IF($K$19=0,"",IF(K17>=L17,"PASS","FAIL"))
- row 19 (Calls logged): K19 =COUNTA(E14:E1013)
- row 20 (Tests passed): K20 =COUNTIF(M14:M17,"PASS")&" / 4"
