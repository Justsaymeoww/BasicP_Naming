print("Book Store")
user = input("What's Your Name : ")
choice = int(input("What's you want to do 1.)Buy 2.)Borrow 3.)Exit : "))
print("------------------------------------------------------------------")

def show_book(book_list):
    for book in book_list:
        print("Book:",book["book_name"],"Category:",book["group"],"Price:",book["price"] ,"Bath" , "Quantity:", book["quan"])

def borrow_book(book_borrow):
    for book in book_borrow:
        print("Book:",book["book_name"],"Category:",book["group"], "Quantity:", book["quan"])

#def show_price(price_book):
#    for book in price_book:
#        print("Book:",book["book_name"],"Price:",book["price"])

Action = ['นักฆ่าในเงามืด',270]
Drama = ["ใต้ร่มไม้ในวันฝนตก" ,270]
Horror = ["คืนที่สิบสาม",120]
Romance = ["รักในคราบฝน" , 230]
Romance2 = ["หัวใจในวันธรรมดา" , 180]
Sci_Fi = ["เมืองไร้การเวลา",300]

def main():
    book = [
        {"book_name" : "นักฆ่าในเงามืด" , "group" : "Action" , "price" : 270 , "quan" : 2 },
        {"book_name" : "ใต้ร่มไม้ในวันฝนตก" , "group" : "Drama" , "price" : 270 , "quan" : 3 },
        {"book_name" : "คืนที่สิบสาม" , "group" : "Horror" , "price" : 120 , "quan" : 1 },
        {"book_name" : "รักในคราบฝน" , "group" : "Romance" , "price" : 230 , "quan" : 4 },
        {"book_name" : "หัวใจในวันธรรมดา" , "group" : "Romance" , "price" : 180 , "quan" : 2 },
        {"book_name" : "เมืองไร้การเวลา" , "group" : "Sci-Fi" , "price" : 300 , "quan" : 5 }
    ]
    while True:
        if choice == 1:
            show_book(book)
            print("------------------------------------------------------------------")
            print("1.นักฆ่าในเงามืด  2.ใต้ร่มไม้ในวันฝนตก 3.คืนที่สิบสาม 4.รักในคราบฝน 5.หัวใจในวันธรรมดา 6.เมืองไร้การเวลา")
            buy = int(input("Which book do you want to buy :"))
            if buy == 1:
                print("Book :",Action[0],"Price:",Action[1])
                print("------------------------------------------------------------------")
            elif buy ==2 :
                print("Book :",Drama[0],"Price:",Drama[1])
                print("------------------------------------------------------------------")
            elif buy ==3 :
                print("Book :",Horror[0],"Price:",Horror[1])
                print("------------------------------------------------------------------")
            elif buy ==4 :
                print("Book :",Romance[0],"Price:",Romance[1])
                print("------------------------------------------------------------------")
            elif buy ==5 :
                print("Book :",Romance2[0],"Price:",Romance2[1])
                print("------------------------------------------------------------------")
            elif buy ==6:
                print("Book :",Sci_Fi[0],"Price:",Sci_Fi[1])
                print("------------------------------------------------------------------")
            else:
                print("Pls try again")
            print("Enjoy your book", user,"!")

        if choice == 2 :
            borrow_book(book)
            print("------------------------------------------------------------------")
            print("1.นักฆ่าในเงามืด  2.ใต้ร่มไม้ในวันฝนตก 3.คืนที่สิบสาม 4.รักในคราบฝน 5.หัวใจในวันธรรมดา 6.เมืองไร้การเวลา")
            borrow = int(input("Which book do you want to borrow :"))
            date = int(input("What's date did you borrow :"))
            if borrow == 1:
                print("You borrow ", Action[0], "on",date)
                print("------------------------------------------------------------------")
            elif borrow ==2 :
                print("You borrow ", Drama[0], "on",date )
                print("------------------------------------------------------------------")
            elif borrow ==3 :
                print("You borrow ", Horror[0], "on",date)
                print("------------------------------------------------------------------")
            elif borrow ==4 :
                print("You borrow ", Romance[0], "on",date )
                print("------------------------------------------------------------------")
            elif borrow ==5 :
                print("You borrow ", Romance2[0], "on",date )
                print("------------------------------------------------------------------")
            elif borrow ==6:
                print("You borrow ", Sci_Fi[0], "on",date )
                print("------------------------------------------------------------------")
            else:
                print("Pls try again")
            print("Enjoy your book", user,"Please return within 3 days ")


        if choice == 3:
            print("Thank you",user,"!")
        break

            
main()
