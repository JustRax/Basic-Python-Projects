from turtle import *

hideturtle()
bgcolor('pink')
color('red')
pensize(4)
left(51)
begin_fill()
forward(133)
circle(50, 200)
right(140)
circle(50, 200)
forward(133)
end_fill()

# Position for "I Love You" text
penup()
goto(0, 250)
pendown()
write("I", move=False, align="center", font=("Arial", 20, "italic"))

# Position for "M. B. L" text
penup()
goto(0, -200)  # Adjusted Y position to place the text under the heart
write("BISCUIT", move=True, align="center", font=("Arial", 20, "italic"))
pendown()
done()
4