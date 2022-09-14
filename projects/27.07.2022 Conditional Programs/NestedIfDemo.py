#boolean values gives 
#us either true or false
isLaptopHere=False
IsItCharged=True

# NestedIf works when first 
# condition is true
if isLaptopHere==True:
    if IsItCharged==True:
        print("Use Laptop")
    else:
        print("Please charge it before use")
else:
    print("use iMac")




