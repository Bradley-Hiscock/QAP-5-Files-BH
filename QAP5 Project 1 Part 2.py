# Program Description: This program is the detailed report for One Stop Insurance Co
#                      to show only customers who make monthly payments
# Written on:          July 31, 2023
# Written by:          Bradley Hiscock

# ************************ Imports ***************************

import datetime
import FormatValues as FV

# ************************ CONSTANTS *************************

EXTRA_LIABILITY_RATE = 130.00
GLASS_COVERAGE_RATE = 86.00
OPTIONAL_LOANER_RATE = 58.00
HST_RATE = 0.15
PROCESSING_FEE = 39.99

# ************************ Main Program **********************

CurrDate = datetime.datetime.now()

print(f"ONE STOP INSURANCE COMPANY")
print(f"MONTHLY PAYMENT LISTING AS OF {FV.FDateM(CurrDate)}")
print()
print(f"POLICY CUSTOMER             TOTAL                 TOTAL       MONTHLY")
print(f"NUMBER NAME                PREMIUM      HST       COST        PAYMENT")
print(f"=====================================================================")

TotPolCtr = 0
TotTotPrem = 0
TotHST = 0
TotTotal = 0
TotMonPay = 0
f = open("Policies.dat", "r")
for CustDataLine in f:
    CustLine = CustDataLine.split(",")
    PolNum = CustLine[0]
    CustName = CustLine[2] + " " + CustLine[3]
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
    HST = TotPrem * HST_RATE
    Total = TotPrem + HST
    MonPay = (Total + PROCESSING_FEE) / 12

    TotTotPrem = TotTotPrem + TotPrem
    TotHST = TotHST + HST
    TotTotal = TotTotal + Total
    TotMonPay = TotMonPay + MonPay

    if CustLine[13] == " Monthly":
        print(f"{PolNum:<4s} {CustName:<20s}  {FV.FDollar2(TotPrem):>9s}   {FV.FDollar2(HST):>7s}   {FV.FDollar2(Total):>9s}  {FV.FDollar2(MonPay):>9s}")
        TotPolCtr += 1

print(f"=====================================================================")
print(f"Total Policies: {TotPolCtr:<3d}       {FV.FDollar2(TotTotPrem):>10s} {FV.FDollar2(TotHST):>9s}  {FV.FDollar2(TotTotal):>10s} {FV.FDollar2(TotMonPay):>10s}")
