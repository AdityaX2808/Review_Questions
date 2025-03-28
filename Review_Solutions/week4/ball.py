class Ball:
    def __init__(self , id , color):
        self.id = id
        self.color = color

    def __str__(self):
        return f"ball_id: {self.id} , ball_color: {self.color}"    