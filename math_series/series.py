
def fibonacci(num):
    '''
list= [0, 1, 2, 3, 4, 5, 6, 7]
fib()=[0, 1, 1, 2, 3, 5, 8, 13]

#  '''
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

#     if num ==0:
#        return 0
#     if num==1:
#         return 1
#     if num ==2:
#       return fibonacci(num-2)+fibonacci(num-1)
#     if num==3:
#       return fibonacci(num-2)+fibonacci(num-1)
#     if num==4:
#       return fibonacci(num-2)+fibonacci(num-1)
#     if num==5:
#       return fibonacci(num-2)+fibonacci(num-1)
#     if num==6:
#       return fibonacci(num-2)+fibonacci(num-1)

def lucas(num):
    '''
list= [0, 1, 2, 3, 4, 5, 6, 7]
luc()=[2, 1, 3, 4, 7, 11, 18, 29]

#  '''
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
    