def outer():  
    x = 1  
    def inner():  
        print x # 1  
    inner() # 2  
  
outer()  
