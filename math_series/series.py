
def fibonacci(num):
    '''
     Is a numeric series starting with the integers 0 and 1. In this series, the next integer is 
     determined by summing the previous two. This function takes one required argument.
    num :int
    return: int
    '''
    final=0
    try:
        if int(num)==0:
          return 0
        if int(num)==1:
          return 1
        final=fibonacci(int(num)-1) + fibonacci(int(num)-2)
        return final
    except :
        return("please enter number")   



def lucas(num):
    '''
   Is a numeric series starting with the integers 2 and 1. In this series, the next integer is 
     determined by summing the previous two. This function takes one required argument.
    num :int
    return: int
    '''
    final=0
    try:
        if int(num)==0:
          return 2
        if int(num)==1:
          return 1
        final=lucas(int(num)-1) + lucas(int(num)-2)
        return final
    except :
        return("please enter number")   
     


def  sum_series(num,x=0,y=1):
    '''
Is a numeric series starting with the integers 0 and 1 by default if not spicified. In this series, the next integer is determined by summing the previous two.
This function takes three arguments.
*required num :int
**optional x:int
**optional y: int
return :int
    '''
    try:
  
        final=0
        if int(num)==0:
            return x
        if int(num)==1:
            return y
        final=sum_series(int(num)-1,x,y)+sum_series(int(num)-2,x,y)
        return final
    except:
        return("please enter a number")    
    