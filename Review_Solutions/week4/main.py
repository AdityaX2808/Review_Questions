from ball import Ball
from cart import Cart

def main():
    bucket1 = Cart()

    ball1 = Ball(1 , "Red")
    ball2 = Ball(2 , "Blue")
    ball3 = Ball(3 , "Green")
    ball4 = Ball(3 , "Green")
    ball5 = Ball(5 , "Pink")
    ball6 = Ball(7 , "Purple")

    bucket1.add_ball(ball1)
    bucket1.add_ball(ball2)
    bucket1.add_ball(ball3)
    bucket1.add_ball(ball4)

    bucket1.show_cart()

    print(bucket1.total_balls())

    bucket2 = Cart()

    bucket2.add_ball(ball4)
    bucket2.add_ball(ball5)
    bucket2.add_ball(ball6)

    bucket2.show_cart()

    print(bucket2.total_balls())

if __name__ == "__main__":
    main()