import matplotlib.pyplot as plt
x = [1, 1, 6, 4]

e =(0.24, 0, 0, 0)
plt.pie(x, explode = e)
plt.title("Pie chart")
plt.show()