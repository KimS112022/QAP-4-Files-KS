#  ONE STOP INSURANCE COMPANY - A PROGRAM TO ENTER AND CALCULATE NEW INSURANCE POLICY INFO FOR IT'S CUSTOMERS
#  AUTHOR:  KIMBERLEY SNOW                         DATE:  NOV 26, 2022


import datetime
import FormatValues as FV

Today = datetime.datetime.now()

# CONSTANTS SET UP IN A DEFAULT FILE
    # Open the defaults file and read the values into variables

f = open("OSICDef.dat", "r")
NEXT_POL_NUM = int(f.readline())
BASIC_PREMIUM = float(f.readline())
ADDL_VEHICLE_DIS = float(f.readline())
LIABILITY_RATE = float(f.readline())
GLASS_RATE = float(f.readline())
LOANER_RATE = float(f.readline())
HST_RATE = float(f.readline())
PROCESS_FEE = float(f.readline())
f.close()

"""
#  TESTING DEFAULT VALUES
print(NEXT_POL_NUM)
print(BASIC_PREMIUM)
print(ADDL_VEHICLE_DIS)
print(LIABILITY_RATE)
print(GLASS_RATE)
print(LOANER_RATE)
print(HST_RATE)
print(PROCESS_FEE)
"""

while True:

    #  USER INPUT

    Cust_FN = input("Please Enter Clients First Name (End to quit):  ").title()
    if Cust_FN == "End":
        break
    Cust_LN = input("Please Enter Client's Last Name:  ").title()
    Str_Add = input("Please Enter Client's Street Address:  ")
    City = input("Please Enter Client's City:  ")
    Prov = input("Please Enter Client's Province:  ")
    Postal = input("Please Enter Client's Postal Code (L#L-#L#):  ")
    Phone = input("Please Enter Client's Phone Number:  ")
    Num_Cars = int(input("Please Enter the Number of Cars Being Insured:  "))
    Liability_Option = input("Does Client Wish to Include Extra Liability (Y = Yes, N = N0): ").upper()
    Glass_Option = input("Does Client Wish to Include Glass Coverage (Y = Yes, N = No):  ").upper()
    Loaner_Option = input("Does Client Wish to Include Optional Loaner Car (Y = Yes, N = No):  ").upper()
    Payment_Option = input("Does Client Wish to Pay in Full or Monthly (F = Full, M = Monthly):  ").upper()

    Liability_Fee = 0
    Glass_Fee = 0
    Loaner_Fee = 0
    TotalExtraFees = 0

    #  CALCULATIONS
    
    if Num_Cars >= 2:
        Basic_Rate = BASIC_PREMIUM + ((BASIC_PREMIUM * .75) * Num_Cars)
    else:
        Basic_Rate = BASIC_PREMIUM

    if Liability_Option == "Y":
        Liability_Fee = LIABILITY_RATE * Num_Cars

    if Glass_Option == "Y":
        Glass_Fee = GLASS_RATE * Num_Cars

    if Loaner_Option == "Y":
        Loaner_Fee = LOANER_RATE * Num_Cars

    TotalExtraFees = Liability_Fee + Glass_Fee + Loaner_Fee

    TotalPremium = Basic_Rate + TotalExtraFees
    HST = TotalPremium * HST_RATE
    TotalPremiumCost = TotalPremium + HST

    # RECEIPT FORMATTING
    #        1         2         3         4
    # 34567890123456789012345678901234567890
    print()
    print("       ONE STOP INSURANCE COMPANY")
    print("             POLICY RECEIPT")
    print(f"{FV.FDateL(Today):^40s}")
    print()
    print("CLIENT DETAILS:")
    print(Cust_FN, Cust_LN)
    print(Str_Add)
    print(City, Prov, Postal)
    print(Phone)

    print("========================================")
    print("POLICY DETAILS")
    print(f"Number Of Cars To Be Insured:         {Num_Cars:>2d}")
    print(f"Basic Rate Total:              {FV.FDollar2(Basic_Rate):<10s}")
    print()
    print(f"Optional Liability Total:        {FV.FDollar2(Liability_Fee):<10s}")
    print(f"Optional Glass Total:            {FV.FDollar2(Glass_Fee):<10s}")
    print(f"Optional Loaner Total:           {FV.FDollar2(Loaner_Fee):<10s}")
    print("                              __________")
    print(f"Total Extra Fees:                {FV.FDollar2(TotalExtraFees):<10s}")
    print("                              __________")
    print(f"Total Premium:                 {FV.FDollar2(TotalPremium):<10s}")
    print(f"HST:                               {FV.FDollar2(HST):<10s}")
    print("                              __________")
    print(f"Total Premium Cost:            {FV.FDollar2(TotalPremiumCost):<10s}")
    print("                              ==========")
    print("PAYMENT DETAILS:")
    if Payment_Option == "M":
        MonthlyPmtOption = 0
        MonthlyPymtOption = (TotalPremium + PROCESS_FEE) / 8
        print(f"Monthly Fee - 8 Payments:     {FV.FDollar2(MonthlyPymtOption):>10s} ")
    else:
        print(f"Please Pay The Full Amount of:{FV.FDollar2(TotalPremiumCost):>10s}")
    print("========================================")
    print(f"  Thank you, {Cust_FN}, for choosing")
    print("           ONE STOP INSURANCE")
    print("      Safe Travels In All You Do!!")

    f = open("Policies.dat", "a")

    f.write("{}, ".format(str(NEXT_POL_NUM)))
    f.write("{} ".format(Cust_FN))
    f.write("{}, ".format(Cust_LN))
    f.write("{}, ".format(Str_Add))
    f.write("{}, ".format(City))
    f.write("{}, ".format(Prov))
    f.write("{}, ".format(Postal))
    f.write("{}, ".format(Phone))
    f.write("{}, ".format(str(Num_Cars)))
    f.write("{}, ".format(str(Liability_Option)))
    f.write("{}, ".format(str(Glass_Option)))
    f.write("{}, ".format(str(Loaner_Option)))
    f.write("{}, ".format(str(Payment_Option)))
    f.write("{}\n".format(str(FV.FDollar2(TotalPremiumCost))))

    f.close()

    print()
    print("POLICY INFORMATION PROCESSED AND SAVED.")
    NEXT_POL_NUM += 1

f = open("OSICDef.dat", "w")
f.write("{}\n".format(str(NEXT_POL_NUM)))
f.write("{}\n".format(str(BASIC_PREMIUM)))
f.write("{}\n".format(str(ADDL_VEHICLE_DIS)))
f.write("{}\n".format(str(LIABILITY_RATE)))
f.write("{}\n".format(str(GLASS_RATE)))
f.write("{}\n".format(str(LOANER_RATE)))
f.write("{}\n".format(str(HST_RATE)))
f.write("{}\n".format(str(PROCESS_FEE)))
f.close()
