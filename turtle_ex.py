import math;
import turtle;
bob = turtle.Turtle();
#bob.fd(100);
#bob.lt(90);
#bob.fd(100);
#bob.lt(90);
#bob.fd(100);
#bob.lt(90);
#bob.fd(100);
#bob.lt(90);
#print(bob)
#turtle.mainloop();




def square(t, length):
	for i in range(4):
		bob.fd(length);
		bob.lt(90);

def polygon(t, n, length):
	angle = 360/n
	for i in range(n):
		bob.fd(length);
		bob.lt(angle);
		
def circle(t, r):
	circumference = 2 * math.pi * r
	n = 50
	length = circumference / n
	polygon(t, n, length)



print(square(bob,-100))

print(polygon(bob,5, 100))

print(polygon(bob,8, 100))


print(polygon(bob,15, -100))

print (circle(bob, 20))

print (circle(bob, -50))

turtle.mainloop()
