import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.gridspec as gridspec

def f(x,y):
    r=np.sqrt(x**2+y**2)
    return 1+0.5/(r**3)-3/(2*r)

def g(x,y):
    r=np.sqrt(x**2+y**2)
    return 1-0.25/(r**3)-3/(4*r)

def vx(x,y,u):
    r=np.sqrt(x**2+y**2)
    #if r>1:
    a= x**2*f(x,y)+y**2*g(x,y)
    a=u*a/r**2
    return a
    #else:
        #return 0

def vy(x,y,u):
    r=np.sqrt(x**2+y**2)
    #if r>1:
    a=f(x,y)-g(x,y)
    a=x*y*a/r**2
    return a*u
    #else:
        #return 0


w=3
u=1
Y, X = np.mgrid[-w:w:100j, -w:w:100j]
radio=np.sqrt(X**2+Y**2)
U=vx(X,Y,u)
V=vy(X,Y,u)
U[radio<1]=np.nan
V[radio<1]=np.nan


fig = plt.figure(figsize=(10,10))

ax0 = fig.add_subplot()
ax1 = fig.add_subplot()
#ax0.streamplot(X, Y, U, V, density=[2.5, 2.5])
ax1.streamplot(X, Y, U, V, color=radio, density=[3, 3], cmap='winter')
c=plt.Circle((0,0),1,color="black",alpha=0.5)
plt.gca().add_artist(c)

#for i in range(-n, n):
#    print(i)
#    for j in range(-n,n):
#        x=5*float(i)/n
#        y=5*float(j)/n
#        r=np.sqrt(x**2+y**2)
#        if (r>=1 and y!=0):
#            ax0.quiver(x,y,vx(x,y,u),vy(x,y,u), headwidth=1.5, headlength=1)
#probar con streamplot

ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
plt.show()
