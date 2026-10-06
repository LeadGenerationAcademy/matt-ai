# Formulas

Cell references point at the CSV files in this folder (same sheet names).

## Annual Overview

One line per row; consecutive rows with the same formula pattern are listed once.

- row 17 (Revenue): B17 =January!B48; E17 =February!B45; H17 =March!B48; K17 =April!B47; N17 =May!B48; Q17 =June!B47; V17 =B17+E17+H17; Y17 =V17+V23+V29+V35
- row 18 (Expenses): B18 =January!G48; E18 =February!G45; H18 =March!G48; K18 =April!G47; N18 =May!G48; Q18 =June!G47; V18 =B18+E18+H18; Y18 =V18+V24+V30+V36
- row 19 (Profit): B19 =January!H48; E19 =February!H45; H19 =March!H48; K19 =April!H47; N19 =May!H48; Q19 =June!H47; V19 =B19+E19+H19; Y19 =V19+V25+V31+V37
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
- row 17: B17 =$B$52+$H$52; C17 =February!C45; D17 =B17-C17; E17 =$E$52+$K$52; F17 =February!F45; G17 =E17-F17; H17 =B17+E17; I17 =C17+F17; J17 =H17-I17; K17 =February!B45; L17 =February!H45
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
- row 52 (Total): B52 =SUM(B32:B51); E52 =SUM(E32:E51); H52 =SUM(H32:H51); K52 =SUM(K32:K51)

## Bank Balance

One line per row; consecutive rows with the same formula pattern are listed once.

- row 16: H16 =SUM(B16:G16)

## January

One line per row; consecutive rows with the same formula pattern are listed once.

- row 17: B17 =SUMIFS($I$73:$I$1000,$A$73:$A$1000,$A17,$C$73:$C$1000,"Income"); C17 =SUMIFS($I$73:$I$1000,$A$73:$A$1000,$A17,$B$73:$B$1000,C$16,$C$73:$C$1000,"Expense"); D17 =SUMIFS($I$73:$I$1000,$A$73:$A$1000,$A17,$B$73:$B$1000,D$16,$C$73:$C$1000,"Expense"); E17 =SUMIFS($I$73:$I$1000,$A$73:$A$1000,$A17,$B$73:$B$1000,E$16,$C$73:$C$1000,"Expense"); F17 =D17+E17; G17 =F17+C17; H17 =B17-G17
- row 48 (Total): B48 =SUM(B17:B47); C48 =SUM(C17:C47); D48 =SUM(D17:D47); E48 =SUM(E17:E47); F48 =SUM(F17:F47); G48 =SUM(G17:G47); H48 =SUM(H17:H47)
- row 53: A53 =D$16; B53 =SUMIFS($I$73:$I$1000,$B$73:$B$1000,A53,$C$73:$C$1000,"Income"); C53 =IFERROR(B53/$A$68,0); D53 =C53*30
- row 54: A54 =E$16; B54 =SUMIFS($I$73:$I$1000,$B$73:$B$1000,A54,$C$73:$C$1000,"Income"); C54 =IFERROR(B54/$A$68,0); D54 =C54*30
- row 55 (Insert your entity here): B55 =IF(A55="","",SUMIFS($I$73:$I$1000,$B$73:$B$1000,A55,$C$73:$C$1000,"Income")); C55 =IFERROR(IF(A55="","",B55/$A$68),0); D55 =IF(A55="","",C55*30)
- row 60: A60 =D$16; B60 =SUMIFS($I$73:$I$1000,$B$73:$B$1000,A60,$C$73:$C$1000,"Expense"); C60 =IFERROR(B60/$A$68,0); D60 =C60*30
- row 61: A61 =E$16; B61 =SUMIFS($I$73:$I$1000,$B$73:$B$1000,A61,$C$73:$C$1000,"Expense"); C61 =IFERROR(B61/$A$68,0); D61 =C61*30
- row 62: A62 =C$16; B62 =SUMIFS($I$73:$I$1000,$B$73:$B$1000,A62,$C$73:$C$1000,"Expense"); C62 =IFERROR(B62/$A$68,0); D62 =C62*30
- row 63 (Insert your entity here): B63 =IF(A63="","",SUMIFS($I$73:$I$1000,$B$73:$B$1000,A63,$C$73:$C$1000,"Expense")); C63 =IFERROR(IF(A63="","",B63/$A$68),0); D63 =IF(A63="","",C63*30)
- row 68: B68 =B53+B54; C68 =B60+B61; D68 =B68-C68; E68 =B62; F68 =D68-E68
- row 73: I73 =IF(OR(F73="",H73=""),"",F73*H73)

## February

One line per row; consecutive rows with the same formula pattern are listed once.

- row 16 (Personal): D16 =January!D$16; E16 =January!E$16
- row 17: B17 =SUMIFS($I$70:$I$1000,$A$70:$A$1000,$A17,$C$70:$C$1000,"Income"); C17 =SUMIFS($I$70:$I$1000,$A$70:$A$1000,$A17,$B$70:$B$1000,C$16,$C$70:$C$1000,"Expense"); D17 =SUMIFS($I$70:$I$1000,$A$70:$A$1000,$A17,$B$70:$B$1000,D$16,$C$70:$C$1000,"Expense"); E17 =SUMIFS($I$70:$I$1000,$A$70:$A$1000,$A17,$B$70:$B$1000,E$16,$C$70:$C$1000,"Expense"); F17 =D17+E17; G17 =F17+C17; H17 =B17-G17
- row 45 (Total): B45 =SUM(B17:B44); C45 =SUM(C17:C44); D45 =SUM(D17:D44); E45 =SUM(E17:E44); F45 =SUM(F17:F44); G45 =SUM(G17:G44); H45 =SUM(H17:H44)
- row 50: A50 =D$16; B50 =SUMIFS($I$70:$I$1000,$B$70:$B$1000,A50,$C$70:$C$1000,"Income"); C50 =IFERROR(B50/$A$65,0); D50 =C50*30
- row 51: A51 =E$16; B51 =SUMIFS($I$70:$I$1000,$B$70:$B$1000,A51,$C$70:$C$1000,"Income"); C51 =IFERROR(B51/$A$65,0); D51 =C51*30
- row 52 (Insert your entity here): B52 =IF(A52="","",SUMIFS($I$70:$I$1000,$B$70:$B$1000,A52,$C$70:$C$1000,"Income")); C52 =IFERROR(IF(A52="","",B52/$A$65),0); D52 =IF(A52="","",C52*30)
- row 57: A57 =D$16; B57 =SUMIFS($I$70:$I$1000,$B$70:$B$1000,A57,$C$70:$C$1000,"Expense"); C57 =IFERROR(B57/$A$65,0); D57 =C57*30
- row 58: A58 =E$16; B58 =SUMIFS($I$70:$I$1000,$B$70:$B$1000,A58,$C$70:$C$1000,"Expense"); C58 =IFERROR(B58/$A$65,0); D58 =C58*30
- row 59: A59 =C$16; B59 =SUMIFS($I$70:$I$1000,$B$70:$B$1000,A59,$C$70:$C$1000,"Expense"); C59 =IFERROR(B59/$A$65,0); D59 =C59*30
- row 60 (Insert your entity here): B60 =IF(A60="","",SUMIFS($I$70:$I$1000,$B$70:$B$1000,A60,$C$70:$C$1000,"Expense")); C60 =IFERROR(IF(A60="","",B60/$A$65),0); D60 =IF(A60="","",C60*30)
- row 65: B65 =B50+B51; C65 =B57+B58; D65 =B65-C65; E65 =B59; F65 =D65-E65
- row 70: I70 =IF(OR(F70="",H70=""),"",F70*H70)

## March

One line per row; consecutive rows with the same formula pattern are listed once.

- row 16 (Personal): D16 =January!D$16; E16 =January!E$16
- row 17: B17 =SUMIFS($I$73:$I$1000,$A$73:$A$1000,$A17,$C$73:$C$1000,"Income"); C17 =SUMIFS($I$73:$I$1000,$A$73:$A$1000,$A17,$B$73:$B$1000,C$16,$C$73:$C$1000,"Expense"); D17 =SUMIFS($I$73:$I$1000,$A$73:$A$1000,$A17,$B$73:$B$1000,D$16,$C$73:$C$1000,"Expense"); E17 =SUMIFS($I$73:$I$1000,$A$73:$A$1000,$A17,$B$73:$B$1000,E$16,$C$73:$C$1000,"Expense"); F17 =D17+E17; G17 =F17+C17; H17 =B17-G17
- row 48 (Total): B48 =SUM(B17:B47); C48 =SUM(C17:C47); D48 =SUM(D17:D47); E48 =SUM(E17:E47); F48 =SUM(F17:F47); G48 =SUM(G17:G47); H48 =SUM(H17:H47)
- row 53: A53 =D$16; B53 =SUMIFS($I$73:$I$1000,$B$73:$B$1000,A53,$C$73:$C$1000,"Income"); C53 =IFERROR(B53/$A$68,0); D53 =C53*30
- row 54: A54 =E$16; B54 =SUMIFS($I$73:$I$1000,$B$73:$B$1000,A54,$C$73:$C$1000,"Income"); C54 =IFERROR(B54/$A$68,0); D54 =C54*30
- row 55 (Insert your entity here): B55 =IF(A55="","",SUMIFS($I$73:$I$1000,$B$73:$B$1000,A55,$C$73:$C$1000,"Income")); C55 =IFERROR(IF(A55="","",B55/$A$68),0); D55 =IF(A55="","",C55*30)
- row 60: A60 =D$16; B60 =SUMIFS($I$73:$I$1000,$B$73:$B$1000,A60,$C$73:$C$1000,"Expense"); C60 =IFERROR(B60/$A$68,0); D60 =C60*30
- row 61: A61 =E$16; B61 =SUMIFS($I$73:$I$1000,$B$73:$B$1000,A61,$C$73:$C$1000,"Expense"); C61 =IFERROR(B61/$A$68,0); D61 =C61*30
- row 62: A62 =C$16; B62 =SUMIFS($I$73:$I$1000,$B$73:$B$1000,A62,$C$73:$C$1000,"Expense"); C62 =IFERROR(B62/$A$68,0); D62 =C62*30
- row 63 (Insert your entity here): B63 =IF(A63="","",SUMIFS($I$73:$I$1000,$B$73:$B$1000,A63,$C$73:$C$1000,"Expense")); C63 =IFERROR(IF(A63="","",B63/$A$68),0); D63 =IF(A63="","",C63*30)
- row 68: B68 =B53+B54; C68 =B60+B61; D68 =B68-C68; E68 =B62; F68 =D68-E68
- row 73: I73 =IF(OR(F73="",H73=""),"",F73*H73)

## April

One line per row; consecutive rows with the same formula pattern are listed once.

- row 16 (Personal): D16 =January!D$16; E16 =January!E$16
- row 17: B17 =SUMIFS($I$72:$I$1000,$A$72:$A$1000,$A17,$C$72:$C$1000,"Income"); C17 =SUMIFS($I$72:$I$1000,$A$72:$A$1000,$A17,$B$72:$B$1000,C$16,$C$72:$C$1000,"Expense"); D17 =SUMIFS($I$72:$I$1000,$A$72:$A$1000,$A17,$B$72:$B$1000,D$16,$C$72:$C$1000,"Expense"); E17 =SUMIFS($I$72:$I$1000,$A$72:$A$1000,$A17,$B$72:$B$1000,E$16,$C$72:$C$1000,"Expense"); F17 =D17+E17; G17 =F17+C17; H17 =B17-G17
- row 47 (Total): B47 =SUM(B17:B46); C47 =SUM(C17:C46); D47 =SUM(D17:D46); E47 =SUM(E17:E46); F47 =SUM(F17:F46); G47 =SUM(G17:G46); H47 =SUM(H17:H46)
- row 52: A52 =D$16; B52 =SUMIFS($I$72:$I$1000,$B$72:$B$1000,A52,$C$72:$C$1000,"Income"); C52 =IFERROR(B52/$A$67,0); D52 =C52*30
- row 53: A53 =E$16; B53 =SUMIFS($I$72:$I$1000,$B$72:$B$1000,A53,$C$72:$C$1000,"Income"); C53 =IFERROR(B53/$A$67,0); D53 =C53*30
- row 54 (Insert your entity here): B54 =IF(A54="","",SUMIFS($I$72:$I$1000,$B$72:$B$1000,A54,$C$72:$C$1000,"Income")); C54 =IFERROR(IF(A54="","",B54/$A$67),0); D54 =IF(A54="","",C54*30)
- row 59: A59 =D$16; B59 =SUMIFS($I$72:$I$1000,$B$72:$B$1000,A59,$C$72:$C$1000,"Expense"); C59 =IFERROR(B59/$A$67,0); D59 =C59*30
- row 60: A60 =E$16; B60 =SUMIFS($I$72:$I$1000,$B$72:$B$1000,A60,$C$72:$C$1000,"Expense"); C60 =IFERROR(B60/$A$67,0); D60 =C60*30
- row 61: A61 =C$16; B61 =SUMIFS($I$72:$I$1000,$B$72:$B$1000,A61,$C$72:$C$1000,"Expense"); C61 =IFERROR(B61/$A$67,0); D61 =C61*30
- row 62 (Insert your entity here): B62 =IF(A62="","",SUMIFS($I$72:$I$1000,$B$72:$B$1000,A62,$C$72:$C$1000,"Expense")); C62 =IFERROR(IF(A62="","",B62/$A$67),0); D62 =IF(A62="","",C62*30)
- row 67: B67 =B52+B53; C67 =B59+B60; D67 =B67-C67; E67 =B61; F67 =D67-E67
- row 72: I72 =IF(OR(F72="",H72=""),"",F72*H72)

## May

One line per row; consecutive rows with the same formula pattern are listed once.

- row 16 (Personal): D16 =January!D$16; E16 =January!E$16
- row 17: B17 =SUMIFS($I$73:$I$1000,$A$73:$A$1000,$A17,$C$73:$C$1000,"Income"); C17 =SUMIFS($I$73:$I$1000,$A$73:$A$1000,$A17,$B$73:$B$1000,C$16,$C$73:$C$1000,"Expense"); D17 =SUMIFS($I$73:$I$1000,$A$73:$A$1000,$A17,$B$73:$B$1000,D$16,$C$73:$C$1000,"Expense"); E17 =SUMIFS($I$73:$I$1000,$A$73:$A$1000,$A17,$B$73:$B$1000,E$16,$C$73:$C$1000,"Expense"); F17 =D17+E17; G17 =F17+C17; H17 =B17-G17
- row 48 (Total): B48 =SUM(B17:B47); C48 =SUM(C17:C47); D48 =SUM(D17:D47); E48 =SUM(E17:E47); F48 =SUM(F17:F47); G48 =SUM(G17:G47); H48 =SUM(H17:H47)
- row 53: A53 =D$16; B53 =SUMIFS($I$73:$I$1000,$B$73:$B$1000,A53,$C$73:$C$1000,"Income"); C53 =IFERROR(B53/$A$68,0); D53 =C53*30
- row 54: A54 =E$16; B54 =SUMIFS($I$73:$I$1000,$B$73:$B$1000,A54,$C$73:$C$1000,"Income"); C54 =IFERROR(B54/$A$68,0); D54 =C54*30
- row 55 (Insert your entity here): B55 =IF(A55="","",SUMIFS($I$73:$I$1000,$B$73:$B$1000,A55,$C$73:$C$1000,"Income")); C55 =IFERROR(IF(A55="","",B55/$A$68),0); D55 =IF(A55="","",C55*30)
- row 60: A60 =D$16; B60 =SUMIFS($I$73:$I$1000,$B$73:$B$1000,A60,$C$73:$C$1000,"Expense"); C60 =IFERROR(B60/$A$68,0); D60 =C60*30
- row 61: A61 =E$16; B61 =SUMIFS($I$73:$I$1000,$B$73:$B$1000,A61,$C$73:$C$1000,"Expense"); C61 =IFERROR(B61/$A$68,0); D61 =C61*30
- row 62: A62 =C$16; B62 =SUMIFS($I$73:$I$1000,$B$73:$B$1000,A62,$C$73:$C$1000,"Expense"); C62 =IFERROR(B62/$A$68,0); D62 =C62*30
- row 63 (Insert your entity here): B63 =IF(A63="","",SUMIFS($I$73:$I$1000,$B$73:$B$1000,A63,$C$73:$C$1000,"Expense")); C63 =IFERROR(IF(A63="","",B63/$A$68),0); D63 =IF(A63="","",C63*30)
- row 68: B68 =B53+B54; C68 =B60+B61; D68 =B68-C68; E68 =B62; F68 =D68-E68
- row 73: I73 =IF(OR(F73="",H73=""),"",F73*H73)

## June

One line per row; consecutive rows with the same formula pattern are listed once.

- row 16 (Personal): D16 =January!D$16; E16 =January!E$16
- row 17: B17 =SUMIFS($I$72:$I$1000,$A$72:$A$1000,$A17,$C$72:$C$1000,"Income"); C17 =SUMIFS($I$72:$I$1000,$A$72:$A$1000,$A17,$B$72:$B$1000,C$16,$C$72:$C$1000,"Expense"); D17 =SUMIFS($I$72:$I$1000,$A$72:$A$1000,$A17,$B$72:$B$1000,D$16,$C$72:$C$1000,"Expense"); E17 =SUMIFS($I$72:$I$1000,$A$72:$A$1000,$A17,$B$72:$B$1000,E$16,$C$72:$C$1000,"Expense"); F17 =D17+E17; G17 =F17+C17; H17 =B17-G17
- row 47 (Total): B47 =SUM(B17:B46); C47 =SUM(C17:C46); D47 =SUM(D17:D46); E47 =SUM(E17:E46); F47 =SUM(F17:F46); G47 =SUM(G17:G46); H47 =SUM(H17:H46)
- row 52: A52 =D$16; B52 =SUMIFS($I$72:$I$1000,$B$72:$B$1000,A52,$C$72:$C$1000,"Income"); C52 =IFERROR(B52/$A$67,0); D52 =C52*30
- row 53: A53 =E$16; B53 =SUMIFS($I$72:$I$1000,$B$72:$B$1000,A53,$C$72:$C$1000,"Income"); C53 =IFERROR(B53/$A$67,0); D53 =C53*30
- row 54 (Insert your entity here): B54 =IF(A54="","",SUMIFS($I$72:$I$1000,$B$72:$B$1000,A54,$C$72:$C$1000,"Income")); C54 =IFERROR(IF(A54="","",B54/$A$67),0); D54 =IF(A54="","",C54*30)
- row 59: A59 =D$16; B59 =SUMIFS($I$72:$I$1000,$B$72:$B$1000,A59,$C$72:$C$1000,"Expense"); C59 =IFERROR(B59/$A$67,0); D59 =C59*30
- row 60: A60 =E$16; B60 =SUMIFS($I$72:$I$1000,$B$72:$B$1000,A60,$C$72:$C$1000,"Expense"); C60 =IFERROR(B60/$A$67,0); D60 =C60*30
- row 61: A61 =C$16; B61 =SUMIFS($I$72:$I$1000,$B$72:$B$1000,A61,$C$72:$C$1000,"Expense"); C61 =IFERROR(B61/$A$67,0); D61 =C61*30
- row 62 (Insert your entity here): B62 =IF(A62="","",SUMIFS($I$72:$I$1000,$B$72:$B$1000,A62,$C$72:$C$1000,"Expense")); C62 =IFERROR(IF(A62="","",B62/$A$67),0); D62 =IF(A62="","",C62*30)
- row 67: B67 =B52+B53; C67 =B59+B60; D67 =B67-C67; E67 =B61; F67 =D67-E67
- row 72: I72 =IF(OR(F72="",H72=""),"",F72*H72)

## July

One line per row; consecutive rows with the same formula pattern are listed once.

- row 16 (Personal): D16 =January!D$16; E16 =January!E$16
- row 17: B17 =SUMIFS($I$73:$I$1000,$A$73:$A$1000,$A17,$C$73:$C$1000,"Income"); C17 =SUMIFS($I$73:$I$1000,$A$73:$A$1000,$A17,$B$73:$B$1000,C$16,$C$73:$C$1000,"Expense"); D17 =SUMIFS($I$73:$I$1000,$A$73:$A$1000,$A17,$B$73:$B$1000,D$16,$C$73:$C$1000,"Expense"); E17 =SUMIFS($I$73:$I$1000,$A$73:$A$1000,$A17,$B$73:$B$1000,E$16,$C$73:$C$1000,"Expense"); F17 =D17+E17; G17 =F17+C17; H17 =B17-G17
- row 48 (Total): B48 =SUM(B17:B47); C48 =SUM(C17:C47); D48 =SUM(D17:D47); E48 =SUM(E17:E47); F48 =SUM(F17:F47); G48 =SUM(G17:G47); H48 =SUM(H17:H47)
- row 53: A53 =D$16; B53 =SUMIFS($I$73:$I$1000,$B$73:$B$1000,A53,$C$73:$C$1000,"Income"); C53 =IFERROR(B53/$A$68,0); D53 =C53*30
- row 54: A54 =E$16; B54 =SUMIFS($I$73:$I$1000,$B$73:$B$1000,A54,$C$73:$C$1000,"Income"); C54 =IFERROR(B54/$A$68,0); D54 =C54*30
- row 55 (Insert your entity here): B55 =IF(A55="","",SUMIFS($I$73:$I$1000,$B$73:$B$1000,A55,$C$73:$C$1000,"Income")); C55 =IFERROR(IF(A55="","",B55/$A$68),0); D55 =IF(A55="","",C55*30)
- row 60: A60 =D$16; B60 =SUMIFS($I$73:$I$1000,$B$73:$B$1000,A60,$C$73:$C$1000,"Expense"); C60 =IFERROR(B60/$A$68,0); D60 =C60*30
- row 61: A61 =E$16; B61 =SUMIFS($I$73:$I$1000,$B$73:$B$1000,A61,$C$73:$C$1000,"Expense"); C61 =IFERROR(B61/$A$68,0); D61 =C61*30
- row 62: A62 =C$16; B62 =SUMIFS($I$73:$I$1000,$B$73:$B$1000,A62,$C$73:$C$1000,"Expense"); C62 =IFERROR(B62/$A$68,0); D62 =C62*30
- row 63 (Insert your entity here): B63 =IF(A63="","",SUMIFS($I$73:$I$1000,$B$73:$B$1000,A63,$C$73:$C$1000,"Expense")); C63 =IFERROR(IF(A63="","",B63/$A$68),0); D63 =IF(A63="","",C63*30)
- row 68: B68 =B53+B54; C68 =B60+B61; D68 =B68-C68; E68 =B62; F68 =D68-E68
- row 73: I73 =IF(OR(F73="",H73=""),"",F73*H73)

## August

One line per row; consecutive rows with the same formula pattern are listed once.

- row 16 (Personal): D16 =January!D$16; E16 =January!E$16
- row 17: B17 =SUMIFS($I$73:$I$1000,$A$73:$A$1000,$A17,$C$73:$C$1000,"Income"); C17 =SUMIFS($I$73:$I$1000,$A$73:$A$1000,$A17,$B$73:$B$1000,C$16,$C$73:$C$1000,"Expense"); D17 =SUMIFS($I$73:$I$1000,$A$73:$A$1000,$A17,$B$73:$B$1000,D$16,$C$73:$C$1000,"Expense"); E17 =SUMIFS($I$73:$I$1000,$A$73:$A$1000,$A17,$B$73:$B$1000,E$16,$C$73:$C$1000,"Expense"); F17 =D17+E17; G17 =F17+C17; H17 =B17-G17
- row 48 (Total): B48 =SUM(B17:B47); C48 =SUM(C17:C47); D48 =SUM(D17:D47); E48 =SUM(E17:E47); F48 =SUM(F17:F47); G48 =SUM(G17:G47); H48 =SUM(H17:H47)
- row 53: A53 =D$16; B53 =SUMIFS($I$73:$I$1000,$B$73:$B$1000,A53,$C$73:$C$1000,"Income"); C53 =IFERROR(B53/$A$68,0); D53 =C53*30
- row 54: A54 =E$16; B54 =SUMIFS($I$73:$I$1000,$B$73:$B$1000,A54,$C$73:$C$1000,"Income"); C54 =IFERROR(B54/$A$68,0); D54 =C54*30
- row 55 (Insert your entity here): B55 =IF(A55="","",SUMIFS($I$73:$I$1000,$B$73:$B$1000,A55,$C$73:$C$1000,"Income")); C55 =IFERROR(IF(A55="","",B55/$A$68),0); D55 =IF(A55="","",C55*30)
- row 60: A60 =D$16; B60 =SUMIFS($I$73:$I$1000,$B$73:$B$1000,A60,$C$73:$C$1000,"Expense"); C60 =IFERROR(B60/$A$68,0); D60 =C60*30
- row 61: A61 =E$16; B61 =SUMIFS($I$73:$I$1000,$B$73:$B$1000,A61,$C$73:$C$1000,"Expense"); C61 =IFERROR(B61/$A$68,0); D61 =C61*30
- row 62: A62 =C$16; B62 =SUMIFS($I$73:$I$1000,$B$73:$B$1000,A62,$C$73:$C$1000,"Expense"); C62 =IFERROR(B62/$A$68,0); D62 =C62*30
- row 63 (Insert your entity here): B63 =IF(A63="","",SUMIFS($I$73:$I$1000,$B$73:$B$1000,A63,$C$73:$C$1000,"Expense")); C63 =IFERROR(IF(A63="","",B63/$A$68),0); D63 =IF(A63="","",C63*30)
- row 68: B68 =B53+B54; C68 =B60+B61; D68 =B68-C68; E68 =B62; F68 =D68-E68
- row 73: I73 =IF(OR(F73="",H73=""),"",F73*H73)

## September

One line per row; consecutive rows with the same formula pattern are listed once.

- row 16 (Personal): D16 =January!D$16; E16 =January!E$16
- row 17: B17 =SUMIFS($I$72:$I$1000,$A$72:$A$1000,$A17,$C$72:$C$1000,"Income"); C17 =SUMIFS($I$72:$I$1000,$A$72:$A$1000,$A17,$B$72:$B$1000,C$16,$C$72:$C$1000,"Expense"); D17 =SUMIFS($I$72:$I$1000,$A$72:$A$1000,$A17,$B$72:$B$1000,D$16,$C$72:$C$1000,"Expense"); E17 =SUMIFS($I$72:$I$1000,$A$72:$A$1000,$A17,$B$72:$B$1000,E$16,$C$72:$C$1000,"Expense"); F17 =D17+E17; G17 =F17+C17; H17 =B17-G17
- row 47 (Total): B47 =SUM(B17:B46); C47 =SUM(C17:C46); D47 =SUM(D17:D46); E47 =SUM(E17:E46); F47 =SUM(F17:F46); G47 =SUM(G17:G46); H47 =SUM(H17:H46)
- row 52: A52 =D$16; B52 =SUMIFS($I$72:$I$1000,$B$72:$B$1000,A52,$C$72:$C$1000,"Income"); C52 =IFERROR(B52/$A$67,0); D52 =C52*30
- row 53: A53 =E$16; B53 =SUMIFS($I$72:$I$1000,$B$72:$B$1000,A53,$C$72:$C$1000,"Income"); C53 =IFERROR(B53/$A$67,0); D53 =C53*30
- row 54 (Insert your entity here): B54 =IF(A54="","",SUMIFS($I$72:$I$1000,$B$72:$B$1000,A54,$C$72:$C$1000,"Income")); C54 =IFERROR(IF(A54="","",B54/$A$67),0); D54 =IF(A54="","",C54*30)
- row 59: A59 =D$16; B59 =SUMIFS($I$72:$I$1000,$B$72:$B$1000,A59,$C$72:$C$1000,"Expense"); C59 =IFERROR(B59/$A$67,0); D59 =C59*30
- row 60: A60 =E$16; B60 =SUMIFS($I$72:$I$1000,$B$72:$B$1000,A60,$C$72:$C$1000,"Expense"); C60 =IFERROR(B60/$A$67,0); D60 =C60*30
- row 61: A61 =C$16; B61 =SUMIFS($I$72:$I$1000,$B$72:$B$1000,A61,$C$72:$C$1000,"Expense"); C61 =IFERROR(B61/$A$67,0); D61 =C61*30
- row 62 (Insert your entity here): B62 =IF(A62="","",SUMIFS($I$72:$I$1000,$B$72:$B$1000,A62,$C$72:$C$1000,"Expense")); C62 =IFERROR(IF(A62="","",B62/$A$67),0); D62 =IF(A62="","",C62*30)
- row 67: B67 =B52+B53; C67 =B59+B60; D67 =B67-C67; E67 =B61; F67 =D67-E67
- row 72: I72 =IF(OR(F72="",H72=""),"",F72*H72)

## October

One line per row; consecutive rows with the same formula pattern are listed once.

- row 16 (Personal): D16 =January!D$16; E16 =January!E$16
- row 17: B17 =SUMIFS($I$73:$I$1000,$A$73:$A$1000,$A17,$C$73:$C$1000,"Income"); C17 =SUMIFS($I$73:$I$1000,$A$73:$A$1000,$A17,$B$73:$B$1000,C$16,$C$73:$C$1000,"Expense"); D17 =SUMIFS($I$73:$I$1000,$A$73:$A$1000,$A17,$B$73:$B$1000,D$16,$C$73:$C$1000,"Expense"); E17 =SUMIFS($I$73:$I$1000,$A$73:$A$1000,$A17,$B$73:$B$1000,E$16,$C$73:$C$1000,"Expense"); F17 =D17+E17; G17 =F17+C17; H17 =B17-G17
- row 48 (Total): B48 =SUM(B17:B47); C48 =SUM(C17:C47); D48 =SUM(D17:D47); E48 =SUM(E17:E47); F48 =SUM(F17:F47); G48 =SUM(G17:G47); H48 =SUM(H17:H47)
- row 53: A53 =D$16; B53 =SUMIFS($I$73:$I$1000,$B$73:$B$1000,A53,$C$73:$C$1000,"Income"); C53 =IFERROR(B53/$A$68,0); D53 =C53*30
- row 54: A54 =E$16; B54 =SUMIFS($I$73:$I$1000,$B$73:$B$1000,A54,$C$73:$C$1000,"Income"); C54 =IFERROR(B54/$A$68,0); D54 =C54*30
- row 55 (Insert your entity here): B55 =IF(A55="","",SUMIFS($I$73:$I$1000,$B$73:$B$1000,A55,$C$73:$C$1000,"Income")); C55 =IFERROR(IF(A55="","",B55/$A$68),0); D55 =IF(A55="","",C55*30)
- row 60: A60 =D$16; B60 =SUMIFS($I$73:$I$1000,$B$73:$B$1000,A60,$C$73:$C$1000,"Expense"); C60 =IFERROR(B60/$A$68,0); D60 =C60*30
- row 61: A61 =E$16; B61 =SUMIFS($I$73:$I$1000,$B$73:$B$1000,A61,$C$73:$C$1000,"Expense"); C61 =IFERROR(B61/$A$68,0); D61 =C61*30
- row 62: A62 =C$16; B62 =SUMIFS($I$73:$I$1000,$B$73:$B$1000,A62,$C$73:$C$1000,"Expense"); C62 =IFERROR(B62/$A$68,0); D62 =C62*30
- row 63 (Insert your entity here): B63 =IF(A63="","",SUMIFS($I$73:$I$1000,$B$73:$B$1000,A63,$C$73:$C$1000,"Expense")); C63 =IFERROR(IF(A63="","",B63/$A$68),0); D63 =IF(A63="","",C63*30)
- row 68: B68 =B53+B54; C68 =B60+B61; D68 =B68-C68; E68 =B62; F68 =D68-E68
- row 73: I73 =IF(OR(F73="",H73=""),"",F73*H73)

## November

One line per row; consecutive rows with the same formula pattern are listed once.

- row 16 (Personal): D16 =January!D$16; E16 =January!E$16
- row 17: B17 =SUMIFS($I$72:$I$1000,$A$72:$A$1000,$A17,$C$72:$C$1000,"Income"); C17 =SUMIFS($I$72:$I$1000,$A$72:$A$1000,$A17,$B$72:$B$1000,C$16,$C$72:$C$1000,"Expense"); D17 =SUMIFS($I$72:$I$1000,$A$72:$A$1000,$A17,$B$72:$B$1000,D$16,$C$72:$C$1000,"Expense"); E17 =SUMIFS($I$72:$I$1000,$A$72:$A$1000,$A17,$B$72:$B$1000,E$16,$C$72:$C$1000,"Expense"); F17 =D17+E17; G17 =F17+C17; H17 =B17-G17
- row 47 (Total): B47 =SUM(B17:B46); C47 =SUM(C17:C46); D47 =SUM(D17:D46); E47 =SUM(E17:E46); F47 =SUM(F17:F46); G47 =SUM(G17:G46); H47 =SUM(H17:H46)
- row 52: A52 =D$16; B52 =SUMIFS($I$72:$I$1000,$B$72:$B$1000,A52,$C$72:$C$1000,"Income"); C52 =IFERROR(B52/$A$67,0); D52 =C52*30
- row 53: A53 =E$16; B53 =SUMIFS($I$72:$I$1000,$B$72:$B$1000,A53,$C$72:$C$1000,"Income"); C53 =IFERROR(B53/$A$67,0); D53 =C53*30
- row 54 (Insert your entity here): B54 =IF(A54="","",SUMIFS($I$72:$I$1000,$B$72:$B$1000,A54,$C$72:$C$1000,"Income")); C54 =IFERROR(IF(A54="","",B54/$A$67),0); D54 =IF(A54="","",C54*30)
- row 59: A59 =D$16; B59 =SUMIFS($I$72:$I$1000,$B$72:$B$1000,A59,$C$72:$C$1000,"Expense"); C59 =IFERROR(B59/$A$67,0); D59 =C59*30
- row 60: A60 =E$16; B60 =SUMIFS($I$72:$I$1000,$B$72:$B$1000,A60,$C$72:$C$1000,"Expense"); C60 =IFERROR(B60/$A$67,0); D60 =C60*30
- row 61: A61 =C$16; B61 =SUMIFS($I$72:$I$1000,$B$72:$B$1000,A61,$C$72:$C$1000,"Expense"); C61 =IFERROR(B61/$A$67,0); D61 =C61*30
- row 62 (Insert your entity here): B62 =IF(A62="","",SUMIFS($I$72:$I$1000,$B$72:$B$1000,A62,$C$72:$C$1000,"Expense")); C62 =IFERROR(IF(A62="","",B62/$A$67),0); D62 =IF(A62="","",C62*30)
- row 67: B67 =B52+B53; C67 =B59+B60; D67 =B67-C67; E67 =B61; F67 =D67-E67
- row 72: I72 =IF(OR(F72="",H72=""),"",F72*H72)

## December

One line per row; consecutive rows with the same formula pattern are listed once.

- row 16 (Personal): D16 =January!D$16; E16 =January!E$16
- row 17: B17 =SUMIFS($I$73:$I$1000,$A$73:$A$1000,$A17,$C$73:$C$1000,"Income"); C17 =SUMIFS($I$73:$I$1000,$A$73:$A$1000,$A17,$B$73:$B$1000,C$16,$C$73:$C$1000,"Expense"); D17 =SUMIFS($I$73:$I$1000,$A$73:$A$1000,$A17,$B$73:$B$1000,D$16,$C$73:$C$1000,"Expense"); E17 =SUMIFS($I$73:$I$1000,$A$73:$A$1000,$A17,$B$73:$B$1000,E$16,$C$73:$C$1000,"Expense"); F17 =D17+E17; G17 =F17+C17; H17 =B17-G17
- row 48 (Total): B48 =SUM(B17:B47); C48 =SUM(C17:C47); D48 =SUM(D17:D47); E48 =SUM(E17:E47); F48 =SUM(F17:F47); G48 =SUM(G17:G47); H48 =SUM(H17:H47)
- row 53: A53 =D$16; B53 =SUMIFS($I$73:$I$1000,$B$73:$B$1000,A53,$C$73:$C$1000,"Income"); C53 =IFERROR(B53/$A$68,0); D53 =C53*30
- row 54: A54 =E$16; B54 =SUMIFS($I$73:$I$1000,$B$73:$B$1000,A54,$C$73:$C$1000,"Income"); C54 =IFERROR(B54/$A$68,0); D54 =C54*30
- row 55 (Insert your entity here): B55 =IF(A55="","",SUMIFS($I$73:$I$1000,$B$73:$B$1000,A55,$C$73:$C$1000,"Income")); C55 =IFERROR(IF(A55="","",B55/$A$68),0); D55 =IF(A55="","",C55*30)
- row 60: A60 =D$16; B60 =SUMIFS($I$73:$I$1000,$B$73:$B$1000,A60,$C$73:$C$1000,"Expense"); C60 =IFERROR(B60/$A$68,0); D60 =C60*30
- row 61: A61 =E$16; B61 =SUMIFS($I$73:$I$1000,$B$73:$B$1000,A61,$C$73:$C$1000,"Expense"); C61 =IFERROR(B61/$A$68,0); D61 =C61*30
- row 62: A62 =C$16; B62 =SUMIFS($I$73:$I$1000,$B$73:$B$1000,A62,$C$73:$C$1000,"Expense"); C62 =IFERROR(B62/$A$68,0); D62 =C62*30
- row 63 (Insert your entity here): B63 =IF(A63="","",SUMIFS($I$73:$I$1000,$B$73:$B$1000,A63,$C$73:$C$1000,"Expense")); C63 =IFERROR(IF(A63="","",B63/$A$68),0); D63 =IF(A63="","",C63*30)
- row 68: B68 =B53+B54; C68 =B60+B61; D68 =B68-C68; E68 =B62; F68 =D68-E68
- row 73: I73 =IF(OR(F73="",H73=""),"",F73*H73)
