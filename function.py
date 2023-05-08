"""
there are three types of function in pytho lang
are 
in built 
modules 
userdefid 
and then we have actual arguments and formal argumeuts  
actual arguments are when we call the function and pass some arguments and formal arguments are when we make a function and the args in parentheses 
are formal args 
there are 5 types of arguments in pytho 
1)positional
2)keyword
3)variable lnght 
4)deafault 
5)keyword variable lenght 
"""
def add(c,d): #this is a formal args
    print(c+d)

add(10,30) #this is an actual argument \
#positional  argument is when we pass actual args whrn calling a function it is catched by function through formal args 
def pie( value,pie=3.14):#this is a deafault args
    print(value,pie)

"""pie(pie=3.14,value=2000)""" #this is the keyword args 
pie(2000)
def total_cost(x, *y):
   sum=0
   for i in y:
       sum+=i
   print(x + sum)
#calling function
total_cost(100, 200,4000,8000) #valid #this a variable lenght args 
def details(**dict):
    for i in dict.items():
        print(i)

details(id=100, name="Subbalaxmi")#this a keword variable lenght 

    