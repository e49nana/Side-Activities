import turtle

# Create the window
window = turtle.Screen()
window.title("Green Square")

# Create the pen
pen = turtle.Turtle()
pen.color("green")
pen.pensize(3)

# Draw the square
for _ in range(4):
    pen.forward(100)
    pen.right(90)

# Keep the window open
window.mainloop()
