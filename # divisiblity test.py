# divisiblity test 
divisibleno = []
nondivisible = []
for i in range(100):
    if i%7 == 0 :
         divisibleno.append(i)
    else :
         nondivisible.append(i)
         
print(divisibleno)
# gives list 

for i in range(100):
     if i%7 != 0:
          continue 
     else :
          print(i)  

# gives each no one by one