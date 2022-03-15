import math
def paint_calc(width, height, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You'll need {num_of_cans} cans of paint.")
test_h = int(input("Height: "))
test_w = int(input("Width: "))
coverage = 5
paint_calc(width=test_w, height=test_h, cover=coverage)