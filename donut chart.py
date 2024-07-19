import matplotlib.pyplot as plt



sizes= [15,30, 45,10]
l= ['A','B','C', 'D']

plt.pie(sizes, labels= l, autopct= "%1.f%%")
circle = plt.Circle((0,0), 0.8, color="white")
plt.gca().add_artist(circle)
plt.title("Donut Chart")
plt.show()