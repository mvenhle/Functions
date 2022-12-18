name1 = "Jacky"
weight1 = 95
height1 = 2

name2 = "William"
weight2 = 85
height2 = 1.5

name3 = "Coco"
weight3 = 100
height3 = 2.3


def bmi_cal(name, weight, height):
    bmi = weight / (height ** 2)
    if bmi < 25:
        return name + " is not overweight"
    else:
        return name + " is overweight"


result1 = bmi_cal(name1, weight1, height1)
result2 = bmi_cal(name2, weight2, height2)
result3 = bmi_cal(name3, weight3, height3)


print(result1)
print(result2)
print(result3)

