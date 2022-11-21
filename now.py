import matplotlib.pyplot as pyplot

labels = ('Python', 'scala', 'c#', 'java', 'php')
index = (1,2,3,4,5)
sizes = (45, 10, 15, 30, 22)
pyplot.bar(index, sizes, tick_label= labels)

pyplot.ylabel('usage')
pyplot.xlabel('Proramming languages')

pyplot.show()


