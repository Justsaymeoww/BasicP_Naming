distance = int(input("Please Enter Your Distance : "))

if distance < 5 :
    print("Cant sent under 5 km.")
elif distance <= 50 :
    print ("Your cost is 10 Bath")
elif distance <= 100 :
    print ("Your cost is 15 Bath")
elif distance <= 300 :
    print ("Your cost is 25 Bath")
elif distance <= 500 :
    print ("Your cost is 35 Bath")
elif distance > 500 :
    print ("Your cost is 45 Bath")
else:
    print("Please Enter Your Distance Again")