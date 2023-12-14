# creating a dictionary  
college={'name': "QIS", 'code': "INDIA",'pincode': 560050 }  
print(college)
#adding items to dictionary  
college["location"] = "IBP"
print(college)
#changing values of a key  
college["location"] = "vijayawada"  
print(college)  
#know the length using len()  
print("length of college is:",len(college))  
#Acess items  
print("college['name']:",college['name'])  
# use get ()  
x=college.get('pincode')
print(x)  
#to copy the same dictionary use copy()  
mycollege= college.copy()  
print(mycollege)

