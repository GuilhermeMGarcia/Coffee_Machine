class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here
        self.area = 1 / 2 * leg_1 * leg_2


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
right_triangle_area = RightTriangle(input_c, input_a, input_b)
if input_a ** 2 + input_b ** 2 == input_c ** 2:
    print(f'{right_triangle_area.area:.{1}f}')
else:
    print('Not right')