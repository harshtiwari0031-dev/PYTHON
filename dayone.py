print("Today is day one")
print("Hello, World!")

#LOOPS

for i in range(5):
    print(i)        #output: 0 1 2 3 4   

for i in range(1,6):
    print(i)        #output: 1 2 3 4 5 

#array
flower=[]
for i in range(1,1001):
    flower.append(i)
for i in range(1000):
    print(flower[i])

#M-2
flower=[]
for i in range(1,1001):
    flower.append(i)
    print(flower[i-1])
