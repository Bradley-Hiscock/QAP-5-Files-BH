# Program Description: A detailed report for One Stop Insurance Co.
# Written on:          July 31, 2023
# Written by:          Bradley Hiscock

# ****************** Libraries ************************

import datetime
import FormatValues as FV

# ****************** CONSTANTS ************************

EXTRA_LIABILITY_RATE = 130.00
GLASS_COVERAGE_RATE = 86.00
OPTIONAL_LOANER_RATE = 58.00

# ****************** Main Program *********************

CurrDate = datetime.datetime.now()

print(f"ONE STOP INSURANCE COMPANY")
print(f"POLICE LISTING AS OF {FV.FDateM(CurrDate)}")
print()
print(f"POLICY CUSTOMER                POLICY     INSURANCE     EXTRA      TOTAL")
print(f"NUMBER NAME                     DATE       PREMIUM      COSTS     PREMIUM")
print(f"=========================================================================")

TotPolCtr = 0
TotInsPrem = 0
TotExCosts = 0
TotTotPrem = 0
f = open("Policies.dat", "r")
for CustDataLine in f:
    CustLine = CustDataLine.split(",")
    PolNum = CustLine[0].strip()
    CustName = CustLine[2] + CustLine[3]
    PolDate = CustLine[1]
    InsPrem = float(CustLine[14])
    NumCars = int(CustLine[9])

    if CustLine[10] == " Y":
        ExLia = EXTRA_LIABILITY_RATE * NumCars
    else:
        ExLia = 0

    if CustLine[11] == " Y":
        GlassCover = GLASS_COVERAGE_RATE * NumCars
    else:
        GlassCover = 0

    if CustLine[12] == " Y":
        Loaner = OPTIONAL_LOANER_RATE
    else:
        Loaner = 0

    ExCosts = ExLia + GlassCover + Loaner
    TotPrem = InsPrem + ExCosts

    print(f" {PolNum} {CustName:<20s}   {PolDate}  {FV.FDollar2(InsPrem):>9s}  {FV.FDollar2(ExCosts):>9s}  {FV.FDollar2(TotPrem):>9s}")
    TotPolCtr += 1
    TotInsPrem = TotInsPrem + InsPrem
    TotExCosts = TotExCosts + ExCosts
    TotTotPrem = TotTotPrem + TotPrem

f.close()
print(f"=========================================================================")
print(f"Total Policies: {TotPolCtr:<3d}                      {FV.FDollar2(TotInsPrem):>10s} {FV.FDollar2(TotExCosts):>10s} {FV.FDollar2(TotTotPrem):>10s}")
