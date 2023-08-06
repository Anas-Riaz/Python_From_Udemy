
def hurricanes(x,*args,**kwargs):
    print (x,"\n")
    for i in args :
        print(i,"\n")
    for d,name in kwargs.items() :
        print(f"{d}':'{name} \n")

a = ["Anas", "Arqam", "Ashir", "Abdur rehman", "Huzaifa"]
b = "Hurricanes"
c = {"Photo grapher,Nakam Ashiq" : "Ashir","Topper" : "Abdur rehman"
     ,"Cr without authorities" : "Huzaifa","Editor" : "Arqam"
     , "Sasta artist":"Anas"}
hurricanes(b,*a,**c )
