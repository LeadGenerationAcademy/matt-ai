# Formulas

Cell references point at the CSV files in this folder (same sheet names).

## Annual Overview

One line per row; consecutive rows with the same formula pattern are listed once.

- row 17 (Revenue): B17 =January!B48; E17 =Febuary!B45; H17 =March!B48; K17 =April!B47; N17 =May!B48; Q17 =June!B47; V17 =B17+E17+H17; Y17 =V17+V23+V29+V35
- row 18 (Expenses): B18 =January!G48; E18 =Febuary!G45; H18 =March!G48; K18 =April!G47; N18 =May!G48; Q18 =June!G47; V18 =B18+E18+H18; Y18 =V18+V24+V30+V36
- row 19 (Profit): B19 =January!H48; E19 =Febuary!H45; H19 =March!H48; K19 =April!H47; N19 =May!H48; Q19 =June!H47; V19 =B19+E19+H19; Y19 =V19+V25+V31+V37
- row 20 (Net Margin): B20 =IFERROR(B19/B17,0); E20 =IFERROR(E19/E17,0); H20 =IFERROR(H19/H17,0); K20 =IFERROR(K19/K17,0); N20 =IFERROR(N19/N17,0); Q20 =IFERROR(Q19/Q17,0); V20 =IFERROR(V19/V17,0); Y20 =IFERROR(Y19/Y17,0)
- row 23 (Revenue): B23 =July!B48; E23 =August!B48; H23 =September!B47; K23 =October!B48; N23 =November!B47; Q23 =December!B48; V23 =K17+N17+Q17
- row 24 (Expenses): B24 =July!G48; E24 =August!G48; H24 =September!G47; K24 =October!G48; N24 =November!G47; Q24 =December!G48; V24 =K18+N18+Q18
- row 25 (Profit): B25 =July!H48; E25 =August!H48; H25 =September!H47; K25 =October!H48; N25 =November!H47; Q25 =December!H48; V25 =K19+N19+Q19
- row 26 (Net Margin): B26 =IFERROR(B25/B23,0); E26 =IFERROR(E25/E23,0); H26 =IFERROR(H25/H23,0); K26 =IFERROR(K25/K23,0); N26 =IFERROR(N25/N23,0); Q26 =IFERROR(Q25/Q23,0); V26 =IFERROR(V25/V23,0)
- row 29 (Revenue): V29 =B23+E23+H23
- row 32 (Net Margin): V32 =IFERROR(V31/V29,0)
- row 35 (Revenue): V35 =K23+N23+Q23
- row 38 (Net Margin): V38 =IFERROR(V37/V35,0)

## Planned vs. Actual

One line per row; consecutive rows with the same formula pattern are listed once.

- row 16: B16 =$B$52+$H$52; C16 =January!C48; D16 =B16-C16; E16 =$E$52+$K$52; F16 =January!F48; G16 =E16-F16; H16 =B16+E16; I16 =C16+F16; J16 =H16-I16; K16 =January!B48; L16 =January!H48
- row 17: B17 =$B$52+$H$52; C17 =Febuary!C45; D17 =B17-C17; E17 =$E$52+$K$52; F17 =Febuary!F45; G17 =E17-F17; H17 =B17+E17; I17 =C17+F17; J17 =H17-I17; K17 =Febuary!B45; L17 =Febuary!H45
- row 18: B18 =$B$52+$H$52; C18 =March!C48; D18 =B18-C18; E18 =$E$52+$K$52; F18 =March!F48; G18 =E18-F18; H18 =B18+E18; I18 =C18+F18; J18 =H18-I18; K18 =March!B48; L18 =March!H48
- row 19: B19 =$B$52+$H$52; C19 =April!C47; D19 =B19-C19; E19 =$E$52+$K$52; F19 =April!F47; G19 =E19-F19; H19 =B19+E19; I19 =C19+F19; J19 =H19-I19; K19 =April!B47; L19 =April!H47
- row 20: B20 =$B$52+$H$52; C20 =May!C48; D20 =B20-C20; E20 =$E$52+$K$52; F20 =May!F48; G20 =E20-F20; H20 =B20+E20; I20 =C20+F20; J20 =H20-I20; K20 =May!B48; L20 =May!H48
- row 21: B21 =$B$52+$H$52; C21 =June!C47; D21 =B21-C21; E21 =$E$52+$K$52; F21 =June!F47; G21 =E21-F21; H21 =B21+E21; I21 =C21+F21; J21 =H21-I21; K21 =June!B47; L21 =June!H47
- row 22: B22 =$B$52+$H$52; C22 =July!C48; D22 =B22-C22; E22 =$E$52+$K$52; F22 =July!F48; G22 =E22-F22; H22 =B22+E22; I22 =C22+F22; J22 =H22-I22; K22 =July!B48; L22 =July!H48
- row 23: B23 =$B$52+$H$52; C23 =August!C48; D23 =B23-C23; E23 =$E$52+$K$52; F23 =August!F48; G23 =E23-F23; H23 =B23+E23; I23 =C23+F23; J23 =H23-I23; K23 =August!B48; L23 =August!H48
- row 24: B24 =$B$52+$H$52; C24 =September!C47; D24 =B24-C24; E24 =$E$52+$K$52; F24 =September!F47; G24 =E24-F24; H24 =B24+E24; I24 =C24+F24; J24 =H24-I24; K24 =September!B47; L24 =September!H47
- row 25: B25 =$B$52+$H$52; C25 =October!C48; D25 =B25-C25; E25 =$E$52+$K$52; F25 =October!F48; G25 =E25-F25; H25 =B25+E25; I25 =C25+F25; J25 =H25-I25; K25 =October!B48; L25 =October!H48
- row 26: B26 =$B$52+$H$52; C26 =November!C47; D26 =B26-C26; E26 =$E$52+$K$52; F26 =November!F47; G26 =E26-F26; H26 =B26+E26; I26 =C26+F26; J26 =H26-I26; K26 =November!B47; L26 =November!H47
- row 27: B27 =$B$52+$H$52; C27 =December!C48; D27 =B27-C27; E27 =$E$52+$K$52; F27 =December!F48; G27 =E27-F27; H27 =B27+E27; I27 =C27+F27; J27 =H27-I27; K27 =December!B48; L27 =December!H48
- row 52 (Total): B52 =SUM(B32:B51); E52 =SUM(E32:E51)

## Bank Balance

One line per row; consecutive rows with the same formula pattern are listed once.

- row 17: H17 =SUM(B17:G17)

## January

One line per row; consecutive rows with the same formula pattern are listed once.

- row 17: B17 =SUMIFS($I$70:$I$995,$A$70:$A$995,A17,$C$70:$C$995,"Income"); C17 =SUMIFS($I$70:$I$995,$A$70:$A$995,A17,$B$70:$B$995,"Personal",$C$70:$C$995,"Expense"); D17 =SUMIFS($I$70:$I$995,$A$70:$A$995,A17,$B$70:$B$995,"Summit Digital Marketing",$C$70:$C$995,"Expense"); E17 =SUMIFS($I$70:$I$995,$A$70:$A$995,A17,$B$70:$B$995,"Ironclad Supplements",$C$70:$C$995,"Expense"); F17 =D17+E17; G17 =F17+C17; H17 =B17-G17
- row 48 (Total): B48 =SUM(B17:B47); C48 =SUM(C17:C47); D48 =SUM(D17:D47); E48 =SUM(E17:E47); F48 =SUM(F17:F47); G48 =SUM(G17:G47); H48 =SUM(H17:H47)
- row 52 (Summit Digital Marketing): B52 =SUMIFS($I$70:$I$995,$B$70:$B$995,A52,$C$70:$C$995,"Income"); C52 =IFERROR(B52/$A$65,0); D52 =C52*30
- row 54: B54 =IF(A54="","",SUMIFS($I$70:$I$995,$B$70:$B$995,A54,$C$70:$C$995,"Income")); C54 =IFERROR(IF(A54="","",B54/$A$65),0); D54 =IF(A54="","",C54*30)
- row 58 (Summit Digital Marketing): B58 =SUMIFS($I$70:$I$995,$B$70:$B$995,A58,$C$70:$C$995,"Expense"); C58 =IFERROR(B58/$A$65,0); D58 =C58*30
- row 61: B61 =IF(A61="","",SUMIFS($I$70:$I$995,$B$70:$B$995,A61,$C$70:$C$995,"Expense")); C61 =IFERROR(IF(A61="","",B61/$A$65),0); D61 =IF(A61="","",C61*30)
- row 65: B65 =B52+B53; C65 =B58+B59; D65 =B65-C65; E65 =B60; F65 =D65-E65
- row 70 (AED): I70 =IF(OR(F70="",H70=""),"",F70*H70)

## Febuary

One line per row; consecutive rows with the same formula pattern are listed once.

- row 17: B17 =SUMIFS($I$67:$I$995,$A$67:$A$995,A17,$C$67:$C$995,"Income"); C17 =SUMIFS($I$67:$I$995,$A$67:$A$995,A17,$B$67:$B$995,"Personal",$C$67:$C$995,"Expense"); D17 =SUMIFS($I$67:$I$995,$A$67:$A$995,A17,$B$67:$B$995,"Summit Digital Marketing",$C$67:$C$995,"Expense"); E17 =SUMIFS($I$67:$I$995,$A$67:$A$995,A17,$B$67:$B$995,"Ironclad Supplements",$C$67:$C$995,"Expense"); F17 =D17+E17; G17 =F17+C17; H17 =B17-G17
- row 45 (Total): B45 =SUM(B17:B44); C45 =SUM(C17:C44); D45 =SUM(D17:D44); E45 =SUM(E17:E44); F45 =SUM(F17:F44); G45 =SUM(G17:G44); H45 =SUM(H17:H44)
- row 49 (Summit Digital Marketing): B49 =SUMIFS($I$67:$I$995,$B$67:$B$995,A49,$C$67:$C$995,"Income"); C49 =IFERROR(B49/$A$62,0); D49 =C49*30
- row 51: B51 =IF(A51="","",SUMIFS($I$67:$I$995,$B$67:$B$995,A51,$C$67:$C$995,"Income")); C51 =IFERROR(IF(A51="","",B51/$A$62),0); D51 =IF(A51="","",C51*30)
- row 55 (Summit Digital Marketing): B55 =SUMIFS($I$67:$I$995,$B$67:$B$995,A55,$C$67:$C$995,"Expense"); C55 =IFERROR(B55/$A$62,0); D55 =C55*30
- row 58: B58 =IF(A58="","",SUMIFS($I$67:$I$995,$B$67:$B$995,A58,$C$67:$C$995,"Expense")); C58 =IFERROR(IF(A58="","",B58/$A$62),0); D58 =IF(A58="","",C58*30)
- row 62: B62 =B49+B50; C62 =B55+B56; D62 =B62-C62; E62 =B57; F62 =D62-E62
- row 67 (USD): I67 =IF(OR(F67="",H67=""),"",F67*H67)

## March

One line per row; consecutive rows with the same formula pattern are listed once.

- row 17: B17 =SUMIFS($I$70:$I$995,$A$70:$A$995,A17,$C$70:$C$995,"Income"); C17 =SUMIFS($I$70:$I$995,$A$70:$A$995,A17,$B$70:$B$995,"Personal",$C$70:$C$995,"Expense"); D17 =SUMIFS($I$70:$I$995,$A$70:$A$995,A17,$B$70:$B$995,"Summit Digital Marketing",$C$70:$C$995,"Expense"); E17 =SUMIFS($I$70:$I$995,$A$70:$A$995,A17,$B$70:$B$995,"Ironclad Supplements",$C$70:$C$995,"Expense"); F17 =D17+E17; G17 =F17+C17; H17 =B17-G17
- row 48 (Total): B48 =SUM(B17:B47); C48 =SUM(C17:C47); D48 =SUM(D17:D47); E48 =SUM(E17:E47); F48 =SUM(F17:F47); G48 =SUM(G17:G47); H48 =SUM(H17:H47)
- row 52 (Summit Digital Marketing): B52 =SUMIFS($I$70:$I$995,$B$70:$B$995,A52,$C$70:$C$995,"Income"); C52 =IFERROR(B52/$A$65,0); D52 =C52*30
- row 54: B54 =IF(A54="","",SUMIFS($I$70:$I$995,$B$70:$B$995,A54,$C$70:$C$995,"Income")); C54 =IFERROR(IF(A54="","",B54/$A$65),0); D54 =IF(A54="","",C54*30)
- row 58 (Summit Digital Marketing): B58 =SUMIFS($I$70:$I$995,$B$70:$B$995,A58,$C$70:$C$995,"Expense"); C58 =IFERROR(B58/$A$65,0); D58 =C58*30
- row 61: B61 =IF(A61="","",SUMIFS($I$70:$I$995,$B$70:$B$995,A61,$C$70:$C$995,"Expense")); C61 =IFERROR(IF(A61="","",B61/$A$65),0); D61 =IF(A61="","",C61*30)
- row 65: B65 =B52+B53; C65 =B58+B59; D65 =B65-C65; E65 =B60; F65 =D65-E65
- row 70 (USD): I70 =IF(OR(F70="",H70=""),"",F70*H70)

## April

One line per row; consecutive rows with the same formula pattern are listed once.

- row 17: B17 =SUMIFS($I$69:$I$995,$A$69:$A$995,A17,$C$69:$C$995,"Income"); C17 =SUMIFS($I$69:$I$995,$A$69:$A$995,A17,$B$69:$B$995,"Personal",$C$69:$C$995,"Expense"); D17 =SUMIFS($I$69:$I$995,$A$69:$A$995,A17,$B$69:$B$995,"Summit Digital Marketing",$C$69:$C$995,"Expense"); E17 =SUMIFS($I$69:$I$995,$A$69:$A$995,A17,$B$69:$B$995,"Ironclad Supplements",$C$69:$C$995,"Expense"); F17 =D17+E17; G17 =F17+C17; H17 =B17-G17
- row 47 (Total): B47 =SUM(B17:B46); C47 =SUM(C17:C46); D47 =SUM(D17:D46); E47 =SUM(E17:E46); F47 =SUM(F17:F46); G47 =SUM(G17:G46); H47 =SUM(H17:H46)
- row 51 (Summit Digital Marketing): B51 =SUMIFS($I$69:$I$995,$B$69:$B$995,A51,$C$69:$C$995,"Income"); C51 =IFERROR(B51/$A$64,0); D51 =C51*30
- row 53: B53 =IF(A53="","",SUMIFS($I$69:$I$995,$B$69:$B$995,A53,$C$69:$C$995,"Income")); C53 =IFERROR(IF(A53="","",B53/$A$64),0); D53 =IF(A53="","",C53*30)
- row 57 (Summit Digital Marketing): B57 =SUMIFS($I$69:$I$995,$B$69:$B$995,A57,$C$69:$C$995,"Expense"); C57 =IFERROR(B57/$A$64,0); D57 =C57*30
- row 60: B60 =IF(A60="","",SUMIFS($I$69:$I$995,$B$69:$B$995,A60,$C$69:$C$995,"Expense")); C60 =IFERROR(IF(A60="","",B60/$A$64),0); D60 =IF(A60="","",C60*30)
- row 64: B64 =B51+B52; C64 =B57+B58; D64 =B64-C64; E64 =B59; F64 =D64-E64
- row 69 (USD): I69 =IF(OR(F69="",H69=""),"",F69*H69)

## May

One line per row; consecutive rows with the same formula pattern are listed once.

- row 17: B17 =SUMIFS($I$70:$I$995,$A$70:$A$995,A17,$C$70:$C$995,"Income"); C17 =SUMIFS($I$70:$I$995,$A$70:$A$995,A17,$B$70:$B$995,"Personal",$C$70:$C$995,"Expense"); D17 =SUMIFS($I$70:$I$995,$A$70:$A$995,A17,$B$70:$B$995,"Summit Digital Marketing",$C$70:$C$995,"Expense"); E17 =SUMIFS($I$70:$I$995,$A$70:$A$995,A17,$B$70:$B$995,"Ironclad Supplements",$C$70:$C$995,"Expense"); F17 =D17+E17; G17 =F17+C17; H17 =B17-G17
- row 48 (Total): B48 =SUM(B17:B47); C48 =SUM(C17:C47); D48 =SUM(D17:D47); E48 =SUM(E17:E47); F48 =SUM(F17:F47); G48 =SUM(G17:G47); H48 =SUM(H17:H47)
- row 52 (Summit Digital Marketing): B52 =SUMIFS($I$70:$I$995,$B$70:$B$995,A52,$C$70:$C$995,"Income"); C52 =IFERROR(B52/$A$65,0); D52 =C52*30
- row 54: B54 =IF(A54="","",SUMIFS($I$70:$I$995,$B$70:$B$995,A54,$C$70:$C$995,"Income")); C54 =IFERROR(IF(A54="","",B54/$A$65),0); D54 =IF(A54="","",C54*30)
- row 58 (Summit Digital Marketing): B58 =SUMIFS($I$70:$I$995,$B$70:$B$995,A58,$C$70:$C$995,"Expense"); C58 =IFERROR(B58/$A$65,0); D58 =C58*30
- row 61: B61 =IF(A61="","",SUMIFS($I$70:$I$995,$B$70:$B$995,A61,$C$70:$C$995,"Expense")); C61 =IFERROR(IF(A61="","",B61/$A$65),0); D61 =IF(A61="","",C61*30)
- row 65: B65 =B52+B53; C65 =B58+B59; D65 =B65-C65; E65 =B60; F65 =D65-E65
- row 70 (USD): I70 =IF(OR(F70="",H70=""),"",F70*H70)

## June

One line per row; consecutive rows with the same formula pattern are listed once.

- row 17: B17 =SUMIFS($I$69:$I$995,$A$69:$A$995,A17,$C$69:$C$995,"Income"); C17 =SUMIFS($I$69:$I$995,$A$69:$A$995,A17,$B$69:$B$995,"Personal",$C$69:$C$995,"Expense"); D17 =SUMIFS($I$69:$I$995,$A$69:$A$995,A17,$B$69:$B$995,"Summit Digital Marketing",$C$69:$C$995,"Expense"); E17 =SUMIFS($I$69:$I$995,$A$69:$A$995,A17,$B$69:$B$995,"Ironclad Supplements",$C$69:$C$995,"Expense"); F17 =D17+E17; G17 =F17+C17; H17 =B17-G17
- row 47 (Total): B47 =SUM(B17:B46); C47 =SUM(C17:C46); D47 =SUM(D17:D46); E47 =SUM(E17:E46); F47 =SUM(F17:F46); G47 =SUM(G17:G46); H47 =SUM(H17:H46)
- row 51 (Summit Digital Marketing): B51 =SUMIFS($I$69:$I$995,$B$69:$B$995,A51,$C$69:$C$995,"Income"); C51 =IFERROR(B51/$A$64,0); D51 =C51*30
- row 53: B53 =IF(A53="","",SUMIFS($I$69:$I$995,$B$69:$B$995,A53,$C$69:$C$995,"Income")); C53 =IFERROR(IF(A53="","",B53/$A$64),0); D53 =IF(A53="","",C53*30)
- row 57 (Summit Digital Marketing): B57 =SUMIFS($I$69:$I$995,$B$69:$B$995,A57,$C$69:$C$995,"Expense"); C57 =IFERROR(B57/$A$64,0); D57 =C57*30
- row 60: B60 =IF(A60="","",SUMIFS($I$69:$I$995,$B$69:$B$995,A60,$C$69:$C$995,"Expense")); C60 =IFERROR(IF(A60="","",B60/$A$64),0); D60 =IF(A60="","",C60*30)
- row 64: B64 =B51+B52; C64 =B57+B58; D64 =B64-C64; E64 =B59; F64 =D64-E64
- row 69 (USD): I69 =IF(OR(F69="",H69=""),"",F69*H69)

## July

One line per row; consecutive rows with the same formula pattern are listed once.

- row 17: B17 =SUMIFS($I$70:$I$995,$A$70:$A$995,A17,$C$70:$C$995,"Income"); C17 =SUMIFS($I$70:$I$995,$A$70:$A$995,A17,$B$70:$B$995,"Personal",$C$70:$C$995,"Expense"); D17 =SUMIFS($I$70:$I$995,$A$70:$A$995,A17,$B$70:$B$995,"Summit Digital Marketing",$C$70:$C$995,"Expense"); E17 =SUMIFS($I$70:$I$995,$A$70:$A$995,A17,$B$70:$B$995,"Ironclad Supplements",$C$70:$C$995,"Expense"); F17 =D17+E17; G17 =F17+C17; H17 =B17-G17
- row 48 (Total): B48 =SUM(B17:B47); C48 =SUM(C17:C47); D48 =SUM(D17:D47); E48 =SUM(E17:E47); F48 =SUM(F17:F47); G48 =SUM(G17:G47); H48 =SUM(H17:H47)
- row 52 (Summit Digital Marketing): B52 =SUMIFS($I$70:$I$995,$B$70:$B$995,A52,$C$70:$C$995,"Income"); C52 =IFERROR(B52/$A$65,0); D52 =C52*30
- row 54: B54 =IF(A54="","",SUMIFS($I$70:$I$995,$B$70:$B$995,A54,$C$70:$C$995,"Income")); C54 =IFERROR(IF(A54="","",B54/$A$65),0); D54 =IF(A54="","",C54*30)
- row 58 (Summit Digital Marketing): B58 =SUMIFS($I$70:$I$995,$B$70:$B$995,A58,$C$70:$C$995,"Expense"); C58 =IFERROR(B58/$A$65,0); D58 =C58*30
- row 61: B61 =IF(A61="","",SUMIFS($I$70:$I$995,$B$70:$B$995,A61,$C$70:$C$995,"Expense")); C61 =IFERROR(IF(A61="","",B61/$A$65),0); D61 =IF(A61="","",C61*30)
- row 65: B65 =B52+B53; C65 =B58+B59; D65 =B65-C65; E65 =B60; F65 =D65-E65
- row 70 (USD): I70 =IF(OR(F70="",H70=""),"",F70*H70)

## August

One line per row; consecutive rows with the same formula pattern are listed once.

- row 17: B17 =SUMIFS($I$70:$I$995,$A$70:$A$995,A17,$C$70:$C$995,"Income"); C17 =SUMIFS($I$70:$I$995,$A$70:$A$995,A17,$B$70:$B$995,"Personal",$C$70:$C$995,"Expense"); D17 =SUMIFS($I$70:$I$995,$A$70:$A$995,A17,$B$70:$B$995,"Summit Digital Marketing",$C$70:$C$995,"Expense"); E17 =SUMIFS($I$70:$I$995,$A$70:$A$995,A17,$B$70:$B$995,"Ironclad Supplements",$C$70:$C$995,"Expense"); F17 =D17+E17; G17 =F17+C17; H17 =B17-G17
- row 48 (Total): B48 =SUM(B17:B47); C48 =SUM(C17:C47); D48 =SUM(D17:D47); E48 =SUM(E17:E47); F48 =SUM(F17:F47); G48 =SUM(G17:G47); H48 =SUM(H17:H47)
- row 52 (Summit Digital Marketing): B52 =SUMIFS($I$70:$I$995,$B$70:$B$995,A52,$C$70:$C$995,"Income"); C52 =IFERROR(B52/$A$65,0); D52 =C52*30
- row 54: B54 =IF(A54="","",SUMIFS($I$70:$I$995,$B$70:$B$995,A54,$C$70:$C$995,"Income")); C54 =IFERROR(IF(A54="","",B54/$A$65),0); D54 =IF(A54="","",C54*30)
- row 58 (Summit Digital Marketing): B58 =SUMIFS($I$70:$I$995,$B$70:$B$995,A58,$C$70:$C$995,"Expense"); C58 =IFERROR(B58/$A$65,0); D58 =C58*30
- row 61: B61 =IF(A61="","",SUMIFS($I$70:$I$995,$B$70:$B$995,A61,$C$70:$C$995,"Expense")); C61 =IFERROR(IF(A61="","",B61/$A$65),0); D61 =IF(A61="","",C61*30)
- row 65: B65 =B52+B53; C65 =B58+B59; D65 =B65-C65; E65 =B60; F65 =D65-E65
- row 70 (USD): I70 =IF(OR(F70="",H70=""),"",F70*H70)

## September

One line per row; consecutive rows with the same formula pattern are listed once.

- row 17: B17 =SUMIFS($I$69:$I$995,$A$69:$A$995,A17,$C$69:$C$995,"Income"); C17 =SUMIFS($I$69:$I$995,$A$69:$A$995,A17,$B$69:$B$995,"Personal",$C$69:$C$995,"Expense"); D17 =SUMIFS($I$69:$I$995,$A$69:$A$995,A17,$B$69:$B$995,"Summit Digital Marketing",$C$69:$C$995,"Expense"); E17 =SUMIFS($I$69:$I$995,$A$69:$A$995,A17,$B$69:$B$995,"Ironclad Supplements",$C$69:$C$995,"Expense"); F17 =D17+E17; G17 =F17+C17; H17 =B17-G17
- row 47 (Total): B47 =SUM(B17:B46); C47 =SUM(C17:C46); D47 =SUM(D17:D46); E47 =SUM(E17:E46); F47 =SUM(F17:F46); G47 =SUM(G17:G46); H47 =SUM(H17:H46)
- row 51 (Summit Digital Marketing): B51 =SUMIFS($I$69:$I$995,$B$69:$B$995,A51,$C$69:$C$995,"Income"); C51 =IFERROR(B51/$A$64,0); D51 =C51*30
- row 53: B53 =IF(A53="","",SUMIFS($I$69:$I$995,$B$69:$B$995,A53,$C$69:$C$995,"Income")); C53 =IFERROR(IF(A53="","",B53/$A$64),0); D53 =IF(A53="","",C53*30)
- row 57 (Summit Digital Marketing): B57 =SUMIFS($I$69:$I$995,$B$69:$B$995,A57,$C$69:$C$995,"Expense"); C57 =IFERROR(B57/$A$64,0); D57 =C57*30
- row 60: B60 =IF(A60="","",SUMIFS($I$69:$I$995,$B$69:$B$995,A60,$C$69:$C$995,"Expense")); C60 =IFERROR(IF(A60="","",B60/$A$64),0); D60 =IF(A60="","",C60*30)
- row 64: B64 =B51+B52; C64 =B57+B58; D64 =B64-C64; E64 =B59; F64 =D64-E64
- row 69 (USD): I69 =IF(OR(F69="",H69=""),"",F69*H69)

## October

One line per row; consecutive rows with the same formula pattern are listed once.

- row 17: B17 =SUMIFS($I$70:$I$995,$A$70:$A$995,A17,$C$70:$C$995,"Income"); C17 =SUMIFS($I$70:$I$995,$A$70:$A$995,A17,$B$70:$B$995,"Personal",$C$70:$C$995,"Expense"); D17 =SUMIFS($I$70:$I$995,$A$70:$A$995,A17,$B$70:$B$995,"Summit Digital Marketing",$C$70:$C$995,"Expense"); E17 =SUMIFS($I$70:$I$995,$A$70:$A$995,A17,$B$70:$B$995,"Ironclad Supplements",$C$70:$C$995,"Expense"); F17 =D17+E17; G17 =F17+C17; H17 =B17-G17
- row 48 (Total): B48 =SUM(B17:B47); C48 =SUM(C17:C47); D48 =SUM(D17:D47); E48 =SUM(E17:E47); F48 =SUM(F17:F47); G48 =SUM(G17:G47); H48 =SUM(H17:H47)
- row 52 (Summit Digital Marketing): B52 =SUMIFS($I$70:$I$995,$B$70:$B$995,A52,$C$70:$C$995,"Income"); C52 =IFERROR(B52/$A$65,0); D52 =C52*30
- row 54: B54 =IF(A54="","",SUMIFS($I$70:$I$995,$B$70:$B$995,A54,$C$70:$C$995,"Income")); C54 =IFERROR(IF(A54="","",B54/$A$65),0); D54 =IF(A54="","",C54*30)
- row 58 (Summit Digital Marketing): B58 =SUMIFS($I$70:$I$995,$B$70:$B$995,A58,$C$70:$C$995,"Expense"); C58 =IFERROR(B58/$A$65,0); D58 =C58*30
- row 61: B61 =IF(A61="","",SUMIFS($I$70:$I$995,$B$70:$B$995,A61,$C$70:$C$995,"Expense")); C61 =IFERROR(IF(A61="","",B61/$A$65),0); D61 =IF(A61="","",C61*30)
- row 65: B65 =B52+B53; C65 =B58+B59; D65 =B65-C65; E65 =B60; F65 =D65-E65
- row 70 (USD): I70 =IF(OR(F70="",H70=""),"",F70*H70)

## November

One line per row; consecutive rows with the same formula pattern are listed once.

- row 17: B17 =SUMIFS($I$69:$I$995,$A$69:$A$995,A17,$C$69:$C$995,"Income"); C17 =SUMIFS($I$69:$I$995,$A$69:$A$995,A17,$B$69:$B$995,"Personal",$C$69:$C$995,"Expense"); D17 =SUMIFS($I$69:$I$995,$A$69:$A$995,A17,$B$69:$B$995,"Summit Digital Marketing",$C$69:$C$995,"Expense"); E17 =SUMIFS($I$69:$I$995,$A$69:$A$995,A17,$B$69:$B$995,"Ironclad Supplements",$C$69:$C$995,"Expense"); F17 =D17+E17; G17 =F17+C17; H17 =B17-G17
- row 47 (Total): B47 =SUM(B17:B46); C47 =SUM(C17:C46); D47 =SUM(D17:D46); E47 =SUM(E17:E46); F47 =SUM(F17:F46); G47 =SUM(G17:G46); H47 =SUM(H17:H46)
- row 51 (Summit Digital Marketing): B51 =SUMIFS($I$69:$I$995,$B$69:$B$995,A51,$C$69:$C$995,"Income"); C51 =IFERROR(B51/$A$64,0); D51 =C51*30
- row 53: B53 =IF(A53="","",SUMIFS($I$69:$I$995,$B$69:$B$995,A53,$C$69:$C$995,"Income")); C53 =IFERROR(IF(A53="","",B53/$A$64),0); D53 =IF(A53="","",C53*30)
- row 57 (Summit Digital Marketing): B57 =SUMIFS($I$69:$I$995,$B$69:$B$995,A57,$C$69:$C$995,"Expense"); C57 =IFERROR(B57/$A$64,0); D57 =C57*30
- row 60: B60 =IF(A60="","",SUMIFS($I$69:$I$995,$B$69:$B$995,A60,$C$69:$C$995,"Expense")); C60 =IFERROR(IF(A60="","",B60/$A$64),0); D60 =IF(A60="","",C60*30)
- row 64: B64 =B51+B52; C64 =B57+B58; D64 =B64-C64; E64 =B59; F64 =D64-E64
- row 69 (USD): I69 =IF(OR(F69="",H69=""),"",F69*H69)

## December

One line per row; consecutive rows with the same formula pattern are listed once.

- row 17: B17 =SUMIFS($I$70:$I$995,$A$70:$A$995,A17,$C$70:$C$995,"Income"); C17 =SUMIFS($I$70:$I$995,$A$70:$A$995,A17,$B$70:$B$995,"Personal",$C$70:$C$995,"Expense"); D17 =SUMIFS($I$70:$I$995,$A$70:$A$995,A17,$B$70:$B$995,"Summit Digital Marketing",$C$70:$C$995,"Expense"); E17 =SUMIFS($I$70:$I$995,$A$70:$A$995,A17,$B$70:$B$995,"Ironclad Supplements",$C$70:$C$995,"Expense"); F17 =D17+E17; G17 =F17+C17; H17 =B17-G17
- row 48 (Total): B48 =SUM(B17:B47); C48 =SUM(C17:C47); D48 =SUM(D17:D47); E48 =SUM(E17:E47); F48 =SUM(F17:F47); G48 =SUM(G17:G47); H48 =SUM(H17:H47)
- row 52 (Summit Digital Marketing): B52 =SUMIFS($I$70:$I$995,$B$70:$B$995,A52,$C$70:$C$995,"Income"); C52 =IFERROR(B52/$A$65,0); D52 =C52*30
- row 54: B54 =IF(A54="","",SUMIFS($I$70:$I$995,$B$70:$B$995,A54,$C$70:$C$995,"Income")); C54 =IFERROR(IF(A54="","",B54/$A$65),0); D54 =IF(A54="","",C54*30)
- row 58 (Summit Digital Marketing): B58 =SUMIFS($I$70:$I$995,$B$70:$B$995,A58,$C$70:$C$995,"Expense"); C58 =IFERROR(B58/$A$65,0); D58 =C58*30
- row 61: B61 =IF(A61="","",SUMIFS($I$70:$I$995,$B$70:$B$995,A61,$C$70:$C$995,"Expense")); C61 =IFERROR(IF(A61="","",B61/$A$65),0); D61 =IF(A61="","",C61*30)
- row 65: B65 =B52+B53; C65 =B58+B59; D65 =B65-C65; E65 =B60; F65 =D65-E65
- row 70 (USD): I70 =IF(OR(F70="",H70=""),"",F70*H70)
