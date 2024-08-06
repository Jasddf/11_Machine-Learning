import matplotlib.pyplot as plt

categories = ['Apple','Banana','Orange','Strawberry','Grape']
values = [25,38,15,20,35]

plt.clf()
plt.bar(categories,values,color = 'skyblue')
plt.title('Fruit Sales')
plt.xlabel('Fruit')
plt.ylabel('Sales')

plt.show()