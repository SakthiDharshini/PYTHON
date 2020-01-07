Month = str(input())
if Month in("January","March","May","July","August","October","December"):
    print("31 days")
elif Month in("April","June","September","November"):
    print("30 days")
elif Month == "February":
    print("28/29 days")
else:
    print("Invalid Input")
