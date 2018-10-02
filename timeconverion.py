#
#This is just the function defination.
#Copy the code from below and below the function defination
#

def timeConversion(s):
    s1=s;
    if(s[8:]=="AM" and s[0:2]=="12"):
        s1="00"+s[2:8];
        return(s1);
    elif(s[8:]=="AM"):
        return(s[:8]);
    elif(s[8:]=="PM" and s[0:2]=="12"):
        return(s[:8]);
    else:
        s1=str(int(s[:2])+12)+s[2:8];
        return(s1);
    
#
#To check whether code is working you can use following function calls
#

a=timeConversion("07:05:45PM");
print(a);
b=timeConversion("09:25:32AM");
print(b)

