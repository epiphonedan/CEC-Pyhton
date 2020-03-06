# Create a list of the BRICS countries
country = [ 
            "Brazil", 
            "Russia", 
            "India", 
            "China", 
            "South Africa"
          ]

"""Create a dictionary of BRICS capitals.
Note that South Africa has 3 capitals. Therefore, we embed a list inside
the dictionary.
"""

capitals = {
    "Brazil": "Brasilia",
    "Russia": "Moscow",
    "India": "New Delhi",
    "China": "Beijing",
    "South Africa": [
                        "Pretoria",
                        "Cape Town",
                        "Bloemfontein"
                    ]
           }

# Print the list and dictionary
print( country ) 
print( capitals )
"""
What response did you get?
Why did the list and dictionary contents not print?
Fix the code and run the script again.
"""

print( capitals["South Africa"][0] )
"""
Why did you get an error for the 2nd capital of South Africa?
Hint: Check the syntax for the index value.
"""
type(capitals)

nativeVLAN=1
dataVLAN=100
if nativeVLAN==dataVLAN:
   print("The native VLAN and the data VLAN are the same.")
else:
    print("This native VLAN and the data VLAN are different.")

aclNum=int(input("What is the IPv4 ACL number?"))
if aclNum>=1 and aclNum <=99:
    print("this is a standard IPv4 ACL.")
elif aclNum >=100 and aclNum <=199:
    else: print("this is not a standard or extend IPv4 ACL.")

for item in devices:
    if "R" in item:
        print(item)

switches=[]
for item in devices:
    if "S" in item:
        switches.append(item)
switches
['S1','S2']

x=input("Enter a number to count to: ")
x=int(x)
y=1
while y<=x:
    print(y)
    y=y+1
    if y>x:
        break
    
    

    
