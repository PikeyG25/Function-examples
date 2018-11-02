num_1 = ""
num_temp = ""
num_final = ""

while True:
    num_1 = input("Enter an integer: ")
    if num_1.isdigit():
        num_final = num_temp + num_1
        num_temp = num_final
    else:
        print(num_final)
        break
