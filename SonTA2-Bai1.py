from datetime import date
def calculateAge(birthDate): 
        today = date.today()
        age = today.year - birthDate.year - ((today.month, today.day) <(birthDate.month, birthDate.day))
        return age
while True:    
    try:
        Date_of_birth=input('nhap ngay thang nam sinh dinh dang dd:mm:yyyy:')
        mang=Date_of_birth.split(':')
        print(calculateAge(date(int(mang[2]), int(mang[1]), int(mang[0]))), "Tuổi")
        break
    except:
        print("Ngày không chính xác! Nhập Lại!") 