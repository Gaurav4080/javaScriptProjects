#Write a program to verify whether the phone no. is in given format or not. 
#ex.017-555-1212 is the correct format

st=input("Enter the phone no.:")
v=True

#check conditions where the number is not true
#first when it is not a 12 char
#second when - are missing at places
#third when anything else is entered at the place of numbers

if len(st)!=12:
    print("Please enter the right number")
for i in range(12):
    for i in [3, 7]:
        if(st[i] == '-'):
            continue
        elif(not(st[i].isdigit())):
            print("Please enter the right number")
print("You have entered the right number")