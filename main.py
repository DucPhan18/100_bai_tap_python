import math

print("Link đề: https://hocpython.org/100baitap/")
print("Chon bài tập để chạy (1-100): ")
run = int(input("Chọn bài : "))

def baitap1():
    print(
        "Đề bài: Nhập vào số n, hãy nhân n lên cho 3, rồi cộng 1 sau đó in kết quả ra màn hình"
    )
    print("Running...")
    n = int(input("Nhập n : "))
    print(n, "x 3 + 1 = ", n * 3 + 1)


def baitap2():
    print(
        "Đề bài: Nhập vào số n, hãy mũ 2 rồi chia cho 3, sau đó in kết quả ra màn hình"
    )
    print("Running...")
    n = int(input("Nhập n : "))
    print(n, "^ 2 / 3 = ", n**2 / 3)


def baitap3():
    print("Đề bài: Nhập vào nhiệt độ c, in ra nhiệt độ F")
    print("Running...")
    a = float(input("Nhập độ C : "))
    print(a, "độ C = ", a * 9 / 5 + 32, "độ F")

def baitap4():
    print("Đề bài: Nhập vào một số nguyên a, nếu a chia hết cho 2 thì in ra True, ngược lại in ra False")
    print("Running...")
    a = int(input("Nhập a : "))
    if a % 2 == 0:
        print("True")
    else:
        print("False")

def baitap5():
    print("Đề bài: Nhập vào số nguyên a, nếu a là số chia hết cho 3 và nằm trong khoảng từ 50 - 100 thì in ra True, ngược lại in ra False")
    print("Running...")
    a = int(input("Nhập a : "))
    if a % 3 == 0 and 50 < a < 100:
        print("True")
    else:
        print("False")

def baitap6():
    print("Đề bài: Nhập vào số nguyên a, nếu a là số chia hết cho 5 nhưng KHÔNG nằm trong khoảng từ 20 - 70 thì in ra True, ngược lại in ra False")
    print("Running...")
    a = int(input("Nhập a : "))
    if a % 5 == 0 and a < 20 or a > 70:
        print("True")
    else:
        print("False")

def baitap7():
    print("Đề bài: Nhập vào nguyên a và b, nếu 1 trong 2 số a và b chia hết cho 2 thì in ra True, ngược lại in ra False")
    print("Running...")
    a = int(input("Nhập a : "))
    b = int(input("Nhâp b : "))
    if a % 2 == 0 or b % 2 == 0:
        print("True")
    else:
        print("False")

def baitap8():
    print("Đề bài: Nhập vào số thực a, kiểm tra xem a có phải là số nguyên hay không, nếu có thì in ra True, ngược lại in ra False")
    print("Running...")
    a = float(input("Nhập a : "))
    check = int(a)
    print(a == check)

def baitap9():
    print("Đề bài: Nhập vào số nguyên a, kiểm tra xem a có phải là số chính phương hay không, nếu có thì in ra True, ngược lại in ra False")
    print("Running...")
    a = float(input("Nhập a : "))
    a = math.sqrt(a)
    check = round(a)
    print(a == check)

def baitap10():
    print("Đề bài: Nhập vào lương tháng này nhận được, ta phải đưa cho vợ 90% số tiền lương đó. Hãy in ra lương ta giữ lại")
    print("Running...")
    luong = float(input("Số tiền lương tháng này : "))
    print("Số tiền bạn được giữ :", luong * 0.1, "đồng")

def baitap11():
    print("Đề bài: Nhập vào 3 số a, b, c. In ra kết quả là tổng của ba số đó")
    print("Running...")
    a = float(input("Nhập a : "))
    b = float(input("Nhập b : "))
    c = float(input("Nhập c : "))
    print("Tổng ba số là", a + b + c)

def baitap12():
    print("Đề bài:")
    print("Nhập vào 3 số a, b, c. Tính và in ra d = (a + b)^c. ")
    print("Nếu d là số trong khoảng từ 100 - 200 thì in ra True, ngược lại in ra False.")
    print("Running...")
    a = float(input("Nhập a : "))
    b = float(input("Nhập b : "))
    c = float(input("Nhập c : "))
    d = float((a + b)**c)
    print("d = (a + b)^c")
    print("=> d =", d)
    print( 100< d <200 )

def baitap13():
    print("Đề bài: Nhập vào số nguyên dương a, nếu a lớn hơn 10 thì ta in ra đây là số lớn hơn 10")
    print("Running...")
    a = int(input("Nhập a : "))
    if a > 10:
        print("Đây là số lớn hơn 10")

def baitap14():
    print("Đề bài: Nhập vào số nguyên dương a, nếu a là số chẵn thì in ra đây là số chẵn, ngược lại in ra đây là số lẻ")
    print("Running...")
    a = int(input("Nhập a : "))
    if a % 2 == 0:
        print("Đây là số chẵn")
    else:
        print("Đây là số lẻ")

def baitap15():
    print("Đề bài: Nhập vào 3 số thực dương a, b, c. Kiểm tra xem a, b, c có cấu thành độ dài của 1 tam giác được không")
    print("Running...")



if run == 1:
    baitap1()
elif run == 2:
    baitap2()
elif run == 3:
    baitap3()
elif run == 4:
    baitap4()
elif run == 5:
    baitap5()
elif run == 6:
    baitap6()
elif run == 7:
    baitap7()
elif run == 8:
    baitap8()
elif run == 9:
    baitap9()
elif run == 10:
    baitap10()
elif run == 11:
    baitap11()
elif run == 12:
    baitap12()
elif run == 13:
    baitap13()
elif run == 14:
    baitap14()
elif run == 15:
    baitap15()