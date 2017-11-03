import turtle
cam=turtle.Turtle()
turtle.colormode(255)
cam.speed(1100000000000)
turtle.bgcolor("black")

for times in range(256):
    cam.right(271)
    cam.color(0,0,times)
    cam.circle(times)
for times in range(4):
    cam.right(90)
    for times in range(200):
        cam.color(255-times,0,0)
        cam.circle(255-times)
        cam.color("orange")
        cam.circle(times)
