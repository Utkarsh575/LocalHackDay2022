x=str(input("enter a string:- "))
string=""
for y in range(len(x)-1,-1,-1):
    string=string+x[y]
print(string) 
