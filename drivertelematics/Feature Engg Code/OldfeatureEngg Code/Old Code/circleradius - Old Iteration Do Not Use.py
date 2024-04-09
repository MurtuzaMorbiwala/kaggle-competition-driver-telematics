
import numpy as np
import matplotlib.pyplot as plt

def circleradius(A,B,C):
 
 a = np.linalg.norm(C - B)
 b = np.linalg.norm(C - A)
 c = np.linalg.norm(B - A)
 s = (a + b + c) / 2
 R = a*b*c / 4 / np.sqrt(s * (s - a) * (s - b) * (s - c))
 b1 = a*a * (b*b + c*c - a*a)
 b2 = b*b * (a*a + c*c - b*b)
 b3 = c*c * (a*a + b*b - c*c)
 P = np.column_stack((A, B, C)).dot(np.hstack((b1, b2, b3)))
 P /= b1 + b2 + b3
 return R,P




A = np.array([100, 0])
B = np.array([-100,0])
C = np.array([0, 100])


coords = zip(A,B,C)
x = coords[0]
y = coords[1]


R,P = circleradius(A,B,C)




print x,y,R,P

plt.scatter(x,y)


circle=plt.Circle(P,R,fc='y')

plt.gca().add_patch(circle)

plt.scatter(P[0],P[1])

plt.axis('scaled')

plt.show()              
