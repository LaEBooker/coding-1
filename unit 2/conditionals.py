# conditional if/else logic- these are keywords that instruct your program
# to do specific instructions based on specific data
# or conditions

# conditional syntax (how its written)
bill_amount = int(input("please type in a bill tender (1s,5s,10s,):"))
# if indicates that something is a possible option

if bill_amount == 1:
    print("here are 4 quaters")
# else is ALWAYS your last input
elif bill_amount ==5:
    print("here are 20 quaters")
elif bill_amount ==10:
    print("here are 40 quaters")
elif bill_amount ==20:
    print("this is not an accepted amount")
elif bill_amount ==50:
    print("this is not an accepted amount")
elif bill_amount ==100:
    print("this is not an accepted amount")

else:
    print("sorry that type of bill is not accepted.")

# elif allows us to indicate that there are more possible options
# you can have as many elif as you want
