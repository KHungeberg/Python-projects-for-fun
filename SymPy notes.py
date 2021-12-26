#!/usr/bin/env python
# coding: utf-8

# Notes on sympy

# Sympy is a package in python that is used for symbolic calculations often mathematically related. Sympy is for example excellent for differentiation and defining mathematical functions. Let us first import our favorite packages. 

# In[27]:


from sympy import *
import math as ma
import numpy as np
import matplotlib.pyplot as plt


# $\textbf{Defining a mathematical function by symbols:}$ To define a function we use the command "symbol('x')" where x is just an example of a symbol we could use. We can then define a function f, as we like, using our newly defined symbol variable. To get the value of our function we use (function name).subs((symbol),number). This can be done as such. Let us define the function: $\newline$ $$f(x)=5x+5$$

# In[20]:


x = symbols('x')

f = 5*x+5


# In[22]:


print(f.subs(x,5))


# $\textbf{Basic operators:}$ Let us say that we want to use the square root of something, but we don't necessarily want it to be evaluated at its value. There we can just use the command "sqrt" or any other symbolic equation. To evaluate the equation at its numerical value, we use command N(equation). It can be done as such:

# In[24]:


sqrt(3)+5+pi


# In[25]:


N(sqrt(3)+5+pi)


# $\textbf{Functions and plotting}$: Let us say that we want to define and plot a function. Here we can simply define a function (let us choose something a bit more complicated than the one above) and use the command $\texttt{lambdify(symbol,function_name,modules=['numpy'])}$ which tells python to evaluate our function at all points of a given vector (often the interval we plot it). This is done as such: 

# In[33]:


f = sin(x)

fx = lambdify(x,f,modules=['numpy'])

xvals = np.linspace(-10,10,100)


# In[35]:


plt.plot(xvals,fx(xvals))
plt.ylabel('sin(x)')
plt.title('Sine boi')


# We can also plot multiple functions and have a good time.

# In[36]:


f = cosh(x)
g = sinh(x)

fx = lambdify(x,f,modules=['numpy'])
gx = lambdify(x,g,modules=['numpy'])

xvals = np.linspace(-2*ma.pi,2*ma.pi,100)


# In[42]:


plt.plot(xvals,fx(xvals),label='hyperbolic cosine')
plt.plot(xvals,gx(xvals),label='hyperbolic sine')
plt.title('Hyperbolic bois')
plt.legend()
plt.show


# # Printing and pretty printing

# Ofcourse the equations we get out here is written in beautiful latex. We can use this nicely. Here are a few ways you can make use of this. 
# 
# 1: If you use the command $\texttt{latex(equation)}$ u get the latex code for your expression. This can be very useful if you want to save some time writing in latex

# # Simplifying mathematical expressions

# To simplify functions we can use the command $\texttt{equation.simplify()}$. 

# In[57]:


f = sin(x)**2+cos(x)**2


# In[62]:


print(f,'  ',f.simplify())


# We can see above that this has simplified idiotformlen. We can also expand functions with the appropriately named command 'expand'.

# In[67]:


f = (x-5)**2+3*(5-x)**4
print(f)


# In[68]:


f.expand()


# We cab also facotrise a given polynomial by the command 'factor'. Dette unne man umiddelbart også tro at simplify ville gøre, men det er faktisk ikke tilfældet.

# In[74]:


print(factor(x**3-x**2+x-1),'    ',simplify(x**3-x**2+x-1))


# Another great function is 'collect' which factorises your expression wiht respect to a given variable. So the input is collect(variable, function). Same goes for the command 'cancel'. If we specifically want to simplify trigonometric functions, then 'trigsimp' is our command of choice. 

# For expanding trigonometric functions, we use 'expand_trig'. For expamle we can get the additive formulars as such

# In[77]:


y = symbols('y')
expand_trig(sin(x+y))


# In the same way have 'expand_power_exp()'. Likewise with simplify we have 'powsimp' where we input the expression and then note force=TRUE if we want to use a power rule and false if not.

# In[82]:


expand_power_exp((x*y)**3)


# We also have a factorial command, just named 'factorial', which gives us the facotorial of the given input. Then we have commnand 'binomial(n,k)' understood as "n choose k". Lad os fx sige at vi gerne ville udregne 5 vælg 3. 

# In[85]:


n = symbols('n')
k = symbols('k')
f = binomial(n,k)
f.subs(n,5).subs(k,3)


# # Calculus

# This is where sympy really shines in terms of programming maths in python. For these introductory notes on symPy, we will divide this section into 5 subsections: derivatives, integration, limits, taylor series, equation solving.

# ### Derivatives

# To take the derivative of a function f, we use 'diff(function_name,variable,derivativetimes)'. So we input the function and the variable that we want to take the derivate with respect to. 

# In[97]:


f = 5*x**5

print(diff(f,x),diff(f,x,2),diff(f,x,3),diff(f,x,4),diff(f,x,5))


# ### Integration

# To integrate we se the appropriately named command 'integrate'. Let us integrate the function: $$\int_a^be^{(-x)}dx$$

# In[98]:


f = exp(-x)

integrate(f,x)


# If we want to integrate over an inteval from a to b we to as such: let a=0 og b=infinity ($\textbf{noted 'oo'}$) 

# In[100]:


integrate(f,(x,0,oo))


# To integrate several times we can do as such. Let us do this integration: $$\int_\infty^{-\infty}\int_\infty^{\infty}e^{-x^2-y^2}dxdy$$

# In[101]:


y = symbols('y')

f = exp(-x**2-y**2)

integrate(f,(x,-oo,oo),(y,-oo,oo))


# So we see that the arguments of the integrate command is in the order of integration. To not evaluate the integral, we simply just write integrate(f,x,y)

# In[102]:


integrate(f,x,y)


# ### Limits

# To compute limits, symPy uses the taylor expantion of a function. We use the command 'limit'(f,x,a)' which is understood as "The limit of f as x goes to a". If we want to specify which way we are approaching a, we specify '+' og '-' as and argument i.e limit(f,x,a,'+') gives us $$\lim_{x \to a^+}f(x)$$

# Two examples. Let us look what happens to these as x approaches 0. $$f(x)=\frac{1}{x} \qquad g(x)=\frac{x^5}{e^x}$$

# In[104]:


f = 1/x 

g = x**5/exp(x)

print(limit(f,x,0,'-'),limit(f,x,0,'+'),limit(g,x,0))


# ### Taylor series

# If we want to get the taylor expansion of a function f up to af certain order. Then we use 'f.series(x,a,k)'. Where this is understood as "the taylor expansion of f with respect to x with origin point a up to termn of order k"

# In[105]:


f = exp(x)

f.series(x,0,5)


# ## Equation solvers

# ### f(x)=0

# To solve equations of the form A=B where A and B are expressions. We first declare that this is an equation with 'eq(A,B)' which means "This is equation A=B". Then we use command 'solveset(eq(A,B),x)' which mean "solve for x in equation A=B"

# In[108]:


m = Eq(x**3-10,0)

solveset(m,x)


# ### System of linear equations

# If we want to solve several linear equations we can use two methods (There might be more). First we can use linsolve which is used like 'linsolve([eq1,eq2,eq3,...],(x,y,z,...))'. This command basically tells python "Solve eq 1,2, 3 and so on with respect to variables x,y,z and so on".
# Let us then solve the system
# $$x+y+z-1=0$$
# $$x+y+2z-3=0$$
# $$2x+y-z-5=0$$

# In[110]:


z = symbols('z')
linsolve([x+y+z-1,x+y+2*z-3,2*x+y-z-5],(x,y,z))


# The other method is to solve it as $Ax=b$, where we define matrix a and vector b to get our answer. Herewe simply use the matrix((R1,R2,R3,...)) where 'RN' is a tuble with values corresponding to row N. Then we can define the system of equations as A,b. It is done as such: 

# In[124]:


A = Matrix(((1,1,1),(1,1,2),(2,1,-1)))
A


# In[126]:


b = Matrix(((1),(3),(5)))

b


# In[127]:


system = A,b


# In[128]:


linsolve(system)


# Which gives us the same solution

# ### systems of nonlinear equations

# For this, we just use command 'nonlinsolve([eq1,eq2,..],[x,y,z,...])'. So it's basically the same as linsolve, but her e only use square brackets. 

# ### Differential equations

# To solve differential equations, we need to define our function as a a variable for our equation. This can be done with the 'symbols' command, since it has another input named 'cls' (class). Her we define the class as function. Then we can have our function as the good old f(x). We take the derivative by 'f(x).diff(x,n)' (take n'th derivative of f(x) with respect to x) . Then we can define our differential equation as such. 
# 
# $$f^{''}(x)-2f^{'}(x)+f(x)=\sin x $$

# In[130]:


f = symbols('f',cls=Function)


# In[133]:


f(x).diff(x,2)


# In[137]:


difeq = Eq(f(x).diff(x,2)-f(x).diff(x)*2+f(x),sin(x))


# In[139]:


dsolve(difeq,f(x))


# In[ ]:




