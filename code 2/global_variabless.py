
a = 45
print("when 45" ,a)
def anas() :
    a = 6
    def ayan () :
        global a
        a = 88
        print("ayan", a)
        def func_1 () :
            global a 
            a = 1
        func_1()
        print("func_1",a)  
    ayan()            
    print("anas", a)
                                           
anas()        
print(a)