def validate_number(number):
    if type(number) != int:
        return "ข้อมูลไม่ได้เป็น Integer"
    elif number < 0:
        return "จำนวนเลขต้องมากกว่าหรือเท่ากับ 0 "
    else:
        people = number
        van = 0
        car = 0

        while people >= 0:
            if people >= 11:
                people -= 11
                van += 1
            elif people >= 4:
                people -= 4
                car += 1
            else:
                break
        return (people, van, car)


def display_result(result):
    if isinstance(result, str):
        print(result)
    else:
        people, van, car = result
        print("จำนวนรถตู้ที่ใช้: ", van, "คัน\nจำนวนรถเก๋งที่ใช้: ", car, "คัน\nจำนวนผู้โดยสารที่เหลือ: ", people, "คน")
