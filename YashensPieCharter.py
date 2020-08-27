from matplotlib import pyplot as plt

#Pie chart, where the slices will be ordered and plotted counter-clockwise:
Players = 'C#','Python','NodeJS','Ruby'
Score = [10,30,45,15]
explode = (0.1,0,0,0) # it 'explode' the 1st Slice

fig1, ax1 = plt.subplots()
ax1.pie(Score, explode=explode, labels=Players, autoct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal') # Equal aspect ratio ensure that pie is drawn as a circle

plt.show()
