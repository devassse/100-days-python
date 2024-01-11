#Paint Calc
import math
def paint_calc(height, width, cover):
    num_cans = (height * width) / cover
    round_up_cans = math.ceil(num_cans)
    print(f"You will need {round_up_cans} cans to Paint!")

test_h = input("Height of the Wall: ")
test_w = input("Width of the Wall: ")
coverage = input("Number: ")

paint_calc(test_h, test_w, coverage)