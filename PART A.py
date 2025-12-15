
#Task1
print("Swimming Pool membership System")

#task2
User = {
    "Name": "Rae An" , "Age": 20, "Membership": "Standart",
}

name = (input("Enter Name:"))
age = int(input("Enter Age:"))

#check age member ship
if age <12:{
    print("Not eligible for membership"),
    exit()#exit if user under 10
}   
elif age <=60:{
    print("standart Membership granted"),#give standart Membership
}   
elif age >60:
    print("senior membership is Granted")#old foks membership


#how many session
sessionBooked = (input("how many session:"))
print("Sesstion Is booked", sessionBooked)



