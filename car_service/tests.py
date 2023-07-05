registration_number = "С 9999 СA"

test_number = registration_number.split()

if len(test_number[0]) < 1 or len(test_number[1]) < 4 or len(test_number[2]) < 1 or test_number[1].isdigit:
    print('NOt ok')
else:
    print("ok")