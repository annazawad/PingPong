
import turtle

window = turtle.Screen()
window.title("PingPong Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0) #zeby nie chodzilo za wolno

class pad(turtle.Turtle):
    def __init__(self,a,b,v,color,position,shape):
        super().__init__()
        self.penup()
        self.speed(v)
        self.color(color)
        self.shape(shape)
        self.shapesize(stretch_wid=a, stretch_len=b)
        self.goto(position)

    def go_up(self):
        y = self.ycor()
        y += 20
        self.sety(y)  # ustawia pad A na współrzednej y

    def go_down(self):
        y = self.ycor()
        y -= 20
        self.sety(y)  # ustawia pad A na współrzednej y


pad_A = pad(5,1,1,"white", (-350, 0), "square")
pad_B = pad(5,1,1,"white", (350, 0), "square")
ball = pad(1,1,0,"white",(0,0),"circle")
ball.dx = 0.5
ball.dy = 0.5

window.listen()
window.onkeypress(pad_A.go_up,"w")
window.onkeypress(pad_A.go_down,"s")
window.onkeypress(pad_B.go_up,"Up")
window.onkeypress(pad_B.go_down,"Down")

#wynik
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0,270)
pen.write("Player A: 0  Player B: 0", align = "center", font = ("ariel", 20, "normal"))
score_a = 0
score_b = 0
#główna pętla kodu
while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 295:
        ball.sety(295)
        ball.dy *= -1

    if ball.ycor() < -295:
        ball.sety(-295)
        ball.dy *= -1

    if ball.xcor() > 395:
        ball.goto(0,0)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("ariel", 20, "normal"))


    if ball.xcor() < -395:
        ball.goto(0,0)
        score_b += 1
        ball.dx *= -1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("ariel", 20, "normal"))


    if (ball.xcor() == 340 and ball.ycor() <pad_B.ycor() +70 and ball.ycor()> pad_B.ycor() -70):
        ball.dx *= -1

    if (ball.xcor() == -340 and ball.ycor() <pad_A.ycor() +70 and ball.ycor()> pad_A.ycor() -70):
        ball.dx *= -1
