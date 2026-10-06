# Formulas

Cell references point at the CSV files in this folder (same sheet names).

## Client Data

One line per row; consecutive rows with the same formula pattern are listed once.

- row 16: F16 =IF(A16="","",IF(E16="",(TODAY()-D16)/30.44,(E16-D16)/30.44)); H16 =IF(A16="","",COUNTIFS(Payments!$C$14:$C$2007,B16)); I16 =IF(A16="","",SUMIFS(Payments!$D$14:$D$2007,Payments!$C$14:$C$2007,B16))

## Monthly Churn Dashboard

One line per row; consecutive rows with the same formula pattern are listed once.

- row 15 (January): B15 =0; C15 =SUMPRODUCT((MONTH('Client Data'!$D$15:$D$1014)=1)*('Client Data'!$D$15:$D$1014<>"")); D15 =SUMPRODUCT((MONTH('Client Data'!$E$15:$E$1014)=1)*('Client Data'!$E$15:$E$1014<>"")); E15 =B15+C15-D15; F15 =IFERROR(D15/B15,0); G15 =SUMPRODUCT((MONTH(Payments!$A$14:$A$2013)=1)*(Payments!$A$14:$A$2013<>"")*Payments!$D$14:$D$2013); H15 =SUMPRODUCT((MONTH(Payments!$A$14:$A$2013)=1)*(Payments!$A$14:$A$2013<>"")); I15 =IFERROR(G15/H15,0)
- row 16 (February): B16 =E15; C16 =SUMPRODUCT((MONTH('Client Data'!$D$15:$D$1014)=2)*('Client Data'!$D$15:$D$1014<>"")); D16 =SUMPRODUCT((MONTH('Client Data'!$E$15:$E$1014)=2)*('Client Data'!$E$15:$E$1014<>"")); E16 =B16+C16-D16; F16 =IFERROR(D16/B16,0); G16 =SUMPRODUCT((MONTH(Payments!$A$14:$A$2013)=2)*(Payments!$A$14:$A$2013<>"")*Payments!$D$14:$D$2013); H16 =SUMPRODUCT((MONTH(Payments!$A$14:$A$2013)=2)*(Payments!$A$14:$A$2013<>"")); I16 =IFERROR(G16/H16,0)
- row 17 (March): B17 =E16; C17 =SUMPRODUCT((MONTH('Client Data'!$D$15:$D$1014)=3)*('Client Data'!$D$15:$D$1014<>"")); D17 =SUMPRODUCT((MONTH('Client Data'!$E$15:$E$1014)=3)*('Client Data'!$E$15:$E$1014<>"")); E17 =B17+C17-D17; F17 =IFERROR(D17/B17,0); G17 =SUMPRODUCT((MONTH(Payments!$A$14:$A$2013)=3)*(Payments!$A$14:$A$2013<>"")*Payments!$D$14:$D$2013); H17 =SUMPRODUCT((MONTH(Payments!$A$14:$A$2013)=3)*(Payments!$A$14:$A$2013<>"")); I17 =IFERROR(G17/H17,0)
- row 18 (April): B18 =E17; C18 =SUMPRODUCT((MONTH('Client Data'!$D$15:$D$1014)=4)*('Client Data'!$D$15:$D$1014<>"")); D18 =SUMPRODUCT((MONTH('Client Data'!$E$15:$E$1014)=4)*('Client Data'!$E$15:$E$1014<>"")); E18 =B18+C18-D18; F18 =IFERROR(D18/B18,0); G18 =SUMPRODUCT((MONTH(Payments!$A$14:$A$2013)=4)*(Payments!$A$14:$A$2013<>"")*Payments!$D$14:$D$2013); H18 =SUMPRODUCT((MONTH(Payments!$A$14:$A$2013)=4)*(Payments!$A$14:$A$2013<>"")); I18 =IFERROR(G18/H18,0)
- row 19 (May): B19 =E18; C19 =SUMPRODUCT((MONTH('Client Data'!$D$15:$D$1014)=5)*('Client Data'!$D$15:$D$1014<>"")); D19 =SUMPRODUCT((MONTH('Client Data'!$E$15:$E$1014)=5)*('Client Data'!$E$15:$E$1014<>"")); E19 =B19+C19-D19; F19 =IFERROR(D19/B19,0); G19 =SUMPRODUCT((MONTH(Payments!$A$14:$A$2013)=5)*(Payments!$A$14:$A$2013<>"")*Payments!$D$14:$D$2013); H19 =SUMPRODUCT((MONTH(Payments!$A$14:$A$2013)=5)*(Payments!$A$14:$A$2013<>"")); I19 =IFERROR(G19/H19,0)
- row 20 (June): B20 =E19; C20 =SUMPRODUCT((MONTH('Client Data'!$D$15:$D$1014)=6)*('Client Data'!$D$15:$D$1014<>"")); D20 =SUMPRODUCT((MONTH('Client Data'!$E$15:$E$1014)=6)*('Client Data'!$E$15:$E$1014<>"")); E20 =B20+C20-D20; F20 =IFERROR(D20/B20,0); G20 =SUMPRODUCT((MONTH(Payments!$A$14:$A$2013)=6)*(Payments!$A$14:$A$2013<>"")*Payments!$D$14:$D$2013); H20 =SUMPRODUCT((MONTH(Payments!$A$14:$A$2013)=6)*(Payments!$A$14:$A$2013<>"")); I20 =IFERROR(G20/H20,0)
- row 21 (July): B21 =E20; C21 =SUMPRODUCT((MONTH('Client Data'!$D$15:$D$1014)=7)*('Client Data'!$D$15:$D$1014<>"")); D21 =SUMPRODUCT((MONTH('Client Data'!$E$15:$E$1014)=7)*('Client Data'!$E$15:$E$1014<>"")); E21 =B21+C21-D21; F21 =IFERROR(D21/B21,0); G21 =SUMPRODUCT((MONTH(Payments!$A$14:$A$2013)=7)*(Payments!$A$14:$A$2013<>"")*Payments!$D$14:$D$2013); H21 =SUMPRODUCT((MONTH(Payments!$A$14:$A$2013)=7)*(Payments!$A$14:$A$2013<>"")); I21 =IFERROR(G21/H21,0)
- row 22 (August): B22 =E21; C22 =SUMPRODUCT((MONTH('Client Data'!$D$15:$D$1014)=8)*('Client Data'!$D$15:$D$1014<>"")); D22 =SUMPRODUCT((MONTH('Client Data'!$E$15:$E$1014)=8)*('Client Data'!$E$15:$E$1014<>"")); E22 =B22+C22-D22; F22 =IFERROR(D22/B22,0); G22 =SUMPRODUCT((MONTH(Payments!$A$14:$A$2013)=8)*(Payments!$A$14:$A$2013<>"")*Payments!$D$14:$D$2013); H22 =SUMPRODUCT((MONTH(Payments!$A$14:$A$2013)=8)*(Payments!$A$14:$A$2013<>"")); I22 =IFERROR(G22/H22,0)
- row 23 (September): B23 =E22; C23 =SUMPRODUCT((MONTH('Client Data'!$D$15:$D$1014)=9)*('Client Data'!$D$15:$D$1014<>"")); D23 =SUMPRODUCT((MONTH('Client Data'!$E$15:$E$1014)=9)*('Client Data'!$E$15:$E$1014<>"")); E23 =B23+C23-D23; F23 =IFERROR(D23/B23,0); G23 =SUMPRODUCT((MONTH(Payments!$A$14:$A$2013)=9)*(Payments!$A$14:$A$2013<>"")*Payments!$D$14:$D$2013); H23 =SUMPRODUCT((MONTH(Payments!$A$14:$A$2013)=9)*(Payments!$A$14:$A$2013<>"")); I23 =IFERROR(G23/H23,0)
- row 24 (October): B24 =E23; C24 =SUMPRODUCT((MONTH('Client Data'!$D$15:$D$1014)=10)*('Client Data'!$D$15:$D$1014<>"")); D24 =SUMPRODUCT((MONTH('Client Data'!$E$15:$E$1014)=10)*('Client Data'!$E$15:$E$1014<>"")); E24 =B24+C24-D24; F24 =IFERROR(D24/B24,0); G24 =SUMPRODUCT((MONTH(Payments!$A$14:$A$2013)=10)*(Payments!$A$14:$A$2013<>"")*Payments!$D$14:$D$2013); H24 =SUMPRODUCT((MONTH(Payments!$A$14:$A$2013)=10)*(Payments!$A$14:$A$2013<>"")); I24 =IFERROR(G24/H24,0)
- row 25 (November): B25 =E24; C25 =SUMPRODUCT((MONTH('Client Data'!$D$15:$D$1014)=11)*('Client Data'!$D$15:$D$1014<>"")); D25 =SUMPRODUCT((MONTH('Client Data'!$E$15:$E$1014)=11)*('Client Data'!$E$15:$E$1014<>"")); E25 =B25+C25-D25; F25 =IFERROR(D25/B25,0); G25 =SUMPRODUCT((MONTH(Payments!$A$14:$A$2013)=11)*(Payments!$A$14:$A$2013<>"")*Payments!$D$14:$D$2013); H25 =SUMPRODUCT((MONTH(Payments!$A$14:$A$2013)=11)*(Payments!$A$14:$A$2013<>"")); I25 =IFERROR(G25/H25,0)
- row 26 (December): B26 =E25; C26 =SUMPRODUCT((MONTH('Client Data'!$D$15:$D$1014)=12)*('Client Data'!$D$15:$D$1014<>"")); D26 =SUMPRODUCT((MONTH('Client Data'!$E$15:$E$1014)=12)*('Client Data'!$E$15:$E$1014<>"")); E26 =B26+C26-D26; F26 =IFERROR(D26/B26,0); G26 =SUMPRODUCT((MONTH(Payments!$A$14:$A$2013)=12)*(Payments!$A$14:$A$2013<>"")*Payments!$D$14:$D$2013); H26 =SUMPRODUCT((MONTH(Payments!$A$14:$A$2013)=12)*(Payments!$A$14:$A$2013<>"")); I26 =IFERROR(G26/H26,0)
- row 32: A32 =IFERROR(AVERAGE(F15:F26),0); B32 =IFERROR(1/A32,0); C32 =IFERROR(AVERAGE('Client Data'!$G$15:$G$1014),0); D32 =B32*C32

## Client Data Example

One line per row; consecutive rows with the same formula pattern are listed once.

- row 15 (Cold Call): F15 =IF(A15="","",IF(E15="",(TODAY()-D15)/30.44,(E15-D15)/30.44)); H15 =IF(A15="","",COUNTIFS(Payments!$C$14:$C$2007,B15)); I15 =IF(A15="","",SUMIFS(Payments!$D$14:$D$2007,Payments!$C$14:$C$2007,B15))
