# ฟังก์ชันแสดงรายชื่อหนังทั้งหมดในระบบ
def show_movies(movie_list):
    for movie in movie_list:
        print("Movie : ", movie["movie_name"])
    # TODO: วนลูปแสดงชื่อหนังพร้อมราคาตั๋ว

# ฟังก์ชันตรวจสอบอายุตามข้อจำกัดของหนัง
def check_age(user_age, age_restriction):
    # TODO: ถ้า age_restriction เป็น 'G' ให้ผ่านเลย
    if age_restriction == G:
        pass
    # ถ้าไม่ใช่ ให้ดึงเลขอายุขั้นต่ำมาเปรียบเทียบกับ user_age
    else:
        if age_restriction <= user_age:
            print ("You Cant Watch This Movie")
            main()
    # ถ้าไม่ใช่ ให้ดึงเลขอายุขั้นต่ำมาเปรียบเทียบกับ user_age

# ฟังก์ชันคำนวณราคาตั๋วโดยขึ้นกับประเภทหนัง
def calculate_price(base_price, genre):
    if genre == "Sci-Fi" :
        base_price + 50
    return base_price
    else :
        return base_price



    
    # TODO: ถ้า genre เป็น 'Sci-Fi' บวกเพิ่ม 50 บาท
    # ถ้าไม่ใช่ คืนราคาเดิม

# ฟังก์ชันสำหรับการซื้อบัตรชมหนัง
def buy_ticket(movie_list):
    while True:
    # TODO: 
    # 1. เรียก show_movies เพื่อแสดงรายชื่อหนัง
     show_movies = movie_list
    # 2. รับค่าตัวเลือกหนังจากผู้ใช้ (1-5)
     user_select = int(input("Select Movie : "))
    # 3. รับอายุผู้ใช้
        age = int(input("Your Age : "))
        check_age()
    
        
        
    # 4. ตรวจสอบอายุผ่าน check_age
    #    - ถ้าไม่ผ่าน ให้แสดงข้อความว่าอายุน้อยเกินไปและ return ออกจากฟังก์ชัน
    # 5. ให้ผู้ใช้เลือกเสียงพากย์ (1 = พากย์ไทย, 2 = Soundtrack)
    # 6. คำนวณราคาตั๋วโดยใช้ calculate_price
    # 7. แสดงผลการซื้อบัตร พร้อมชื่อหนัง, เสียงที่เลือก, ราคาตั๋ว

def main():
    # TODO: สร้างรายการหนังเป็น list ของ dict โดยเก็บข้อมูล movie_name, ticket_price, genre, age_restriction
    movies = [
        {'movie_name': 'Avengers Endgame', 'ticket_price': 300, 'genre': 'Action', 'age_restriction': '13'},
        {'movie_name': 'Inception', 'ticket_price': 280, 'genre': 'Sci-Fi', 'age_restriction': '13'},
        {'movie_name': 'It', 'ticket_price': 180, 'genre': 'Horror', 'age_restriction': '18'},
        {'movie_name': 'The Notebook', 'ticket_price': 250, 'genre': 'Romantic', 'age_restriction': '13'},
        {'movie_name': 'Harry Potter and the Sorcerer\'s Stone', 'ticket_price': 260, 'genre': 'Fantasy', 'age_restriction': 'G'}
    ]

    while True:
        print("Cinema System")
        print("1.Show Movie List")
        print("2.Buy Ticket")
        
            menu = int(input("Enter : "))

            if menu == 1:
             return show_movies()
            elif menu == 2:
                return buy_ticket()
            else:
                print("Please Try Agian")
            


    # TODO: ตรวจสอบเมนูที่เลือก
    # ถ้าเลือก 1 ให้เรียก show_movies พร้อมส่ง movies
    # ถ้าเลือก 2 ให้เรียก buy_ticket พร้อมส่ง movies
    # ถ้าเลือกอื่น ให้แสดงข้อความว่าเมนูไม่ถูกต้อง

# เรียก main เพื่อเริ่มโปรแกรม
main()