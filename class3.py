

# haverice = True
# # havespoon = False ## จะrunแล้วไม่ขึ้นเพราะไม่มีช้อน
# # havespoon = True ## runแล้วมีoutputเป็นกินข้าวเพราะเป็น True
# havespoon = False
# havehand = True


# if haverice:
#     if havespoon:
#         print("กินข้าว")
#     elif havehand:
#         print("กินข้าวเหนียว")


# score = int(input("Enter Your Score : "))

# if score >= 0:
#     if score <= 100:
#         if score >= 80: # 80 - 100
#             print("Grade A")
#         if score >= 70:
#             if score < 80: # 70 - 79
#                 print("Grade B")
#         if score >= 60:
#             if score < 70: # 60 - 69
#                 print("Grade C")
#         if score >= 50:
#             if score < 60: # 50 - 59
#                 print("Grade D")
#         if score < 50: # < 50
#             print("Grade F")         


# for i in range(1,10,2):
#     print(i)

# # (1,10,2)
# # start = 1
# # stop = 10
# # step = 2
    

# i = 0
# while i < 5 :
#     print(i)
#     i =  i + 1



while True:
    choice = int(input("กรอก 1) เพื่อบวกเลข , กรอก 2) เพื่อออก , : " ))

    if choice == 1 :
        plus = int(input("จำนวนเลขที่ต้องการจะบวก"))
        sum = 0

        for i in range(plus):
            num1 = int(input("กรอกเลข"))
            sum = sum + num1

        print("ผลลัพธ์ = " , sum)
    
    if choice == 2:
        print("บ้าย บาย")
        break
