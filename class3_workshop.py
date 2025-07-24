## step1 
Moodeng_Blood = 50
Gun = 20
Sword = 10
Hand = 5



## step2
while True:
    choice = int(input("Enter 1 )>>>Battle With Moodeng , Enter 2>>>) Exit : "))
    # step3
    if choice == 1:
        print("Weapon 1)Gun 2)Sword 3)Hand")
        Round = int(input("Enter Amount of Round : "))

    #step4
        for i in range (1,Round+1):
            print("Round",i)
            Weapon = int(input("Choose Your Weapon , 1) Gun(20) , 2)Sword(10) , 3)Hand(5) : "))
        
            if Weapon == 1:
                print("Player choose Gun!")
                Moodeng_Blood = Moodeng_Blood - Gun
                print("Moodeng Blood is " , Moodeng_Blood)
        
            if Weapon == 2:
                print("Player choose Sword!")
                Moodeng_Blood = Moodeng_Blood - Sword
                print("Moodeng Blood is " , Moodeng_Blood)
        
            if Weapon == 3:
                print("Player choose Hand!")
                Moodeng_Blood = Moodeng_Blood - Hand
                print("Moodeng Blood is " , Moodeng_Blood)
            
            if Moodeng_Blood <0 :
                Moodeng_Blood = 20
                print("Moodeng Blood Return To ", Moodeng_Blood)

            
        if Moodeng_Blood == 0:
            print("Moodeng Die !")
        if Moodeng_Blood > 0:
            print ("Player Die !")
    break
            
        
    
    if choice == 2:
        print("Player Exit")
        break

                    
            
            

        
        

        

