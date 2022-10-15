nitrate = str(input("How much nitrate is there? "))
nitrate = float(nitrate)

if nitrate >= 10:
    print("For "+str(nitrate)+" nitrate, dose 3ml.")

elif nitrate > 2.5:
    print("For "+str(nitrate)+" nitrate, dose 2ml.")

elif 1 < nitrate < 2.5:
    print("For "+str(nitrate)+" nitrate, dose 1ml.")

elif 1 > nitrate < 2.5:
    print("For "+str(nitrate)+" nitrate, dose 0.5ml.")

else:
    print("Error.")
