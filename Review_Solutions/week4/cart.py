from ball import Ball

class Cart:
    def __init__(self):
        self.balls = []

    def add_ball(self, ball):
        for something in self.balls:
            if something.color == ball.color:
                print("Ball Exits")
                return
        else:
            self.balls.append(ball)
            print(f"Added...")

    def total_balls(self):
        return len(self.balls)

    def show_cart(self):
        for ball in self.balls:
           print(ball)