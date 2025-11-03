class person : 
    def __init__(self , name , age , branch):
        self.name = name
        self.age = age
        self.branch = branch
    def intro(self):
     print(f"my name is {self.name} i am {self.age} old and my branch is {self.branch}")    

a = person('sufi' , 18 , 'biotechnology')
b = person('radhika' , 45 , 'fashion technology')
# SELF CALLS THE OBJECT THE METHOD TO THE VARIABLE WE ARE CALLING IT ON 
print(a.intro())
print(b.intro())