date = int(input("Enter Day of the Date :"))
month = int(input("Enter month no. :"))
day = 0
if month == 1:
    day = date 
elif month == 2:
    day = date + 31    
elif month == 3:
    day = date + 31+28
elif month == 4:
    day = date + 31+28+31        
elif month == 5:
    day = date + 31+28+31+30
elif month == 6:
    day = date + 31+28+31+30+31
elif month == 7:
    day = date + 31+28+31+30+31+30
elif month == 8:
    day = date + 31+28+31+30+31+30+31   
elif month == 9:
    day = date + 31+28+31+30+31+30+31+30  
elif month == 10:
    day = date + 31+28+31+30+31+30+31+30+31
elif month == 11:
    day = date + 31+28+31+30+31+30+31+30+31+30
elif month == 12:
    day = date +31+28+31+30+31+30+31+30+31+30+31 
print (day)        