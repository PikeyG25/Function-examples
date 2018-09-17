#Parker Gowans
#9/17/18
import math

def test_avg():
    test1= float(input("what was your first test score?"))
    test2= float(input("what was your second test score?"))
    test3= float(input("what was your third test score?"))
    test4= float(input("what was your fourth test score?"))
    test5= float(input("what was your fifth test score?"))
    test6= float(input("what was your sixth test score?"))
    test7= float(input("what was your seventh test score?"))
    test8= float(input("what was your eighth test score?"))
    test9= float(input("what was your ninth test score?"))
    test10= float(input("what was your tenth test score?"))

    number=test1+test2+test3+test4+test5+test6+test7+test8+test9+test10
    test_avg = number/10
    return test_avg

avg=test_avg()
print(avg)
