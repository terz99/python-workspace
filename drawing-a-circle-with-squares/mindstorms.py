import turtle

def draw_square(brad):

	cnt = 4
	while cnt:
		brad.forward(100)
		brad.right(90)
		cnt -= 1

def draw_circle(t):
	t.circle(100)

def draw_triangle(t):

	cnt = 3
	while cnt:
		cnt -= 1
		t.right(180-60)
		t.forward(100)

def draw_rhombus(t):

	color_list = ['yellow', 'pink', 'pink', 'yellow']
	i = 0
	cnt = 2
	while cnt:
		cnt -= 1
		t.color(color_list[i])
		t.forward(100)
		t.right(60)
		t.color(color_list[i+1])
		t.forward(100)
		t.right(120)
		i += 2


window = turtle.Screen()
window.bgcolor('red')

t = turtle.Turtle()
t.color('yellow')
t.shape('turtle')
t.speed('fastest')
t.setheading(270)
t.width(5)
cnt = 72
while cnt:
	cnt -= 1
	draw_rhombus(t)
	t.right(5)
t.color('green')
t.width(10)
t.forward(400)

window.exitonclick()