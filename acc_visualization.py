import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import json
import random


def InitializeFirstPoint():
    # Setting the axes properties
    ax.set_xlim3d([min(xs), max(xs)])
    ax.set_xlabel('X')

    ax.set_ylim3d([min(ys), max(ys)])
    ax.set_ylabel('Y')

    ax.set_zlim3d([min(zs), max(zs)])
    ax.set_zlabel('Z')

    ax.set_title('3D Test')
    return line

def GenerateNewPoint():
    i = random.randint(0, len(xs)-1)
    j = random.randint(0, len(xs)-1)
    s = random.randint(0, len(xs)-1)
    print(xs[i], ys[j], zs[s])
    yield xs[i], ys[j], zs[s]
    # cnt = 0
    # while cnt < 1000:
    #     cnt += 1
    #     t += 0.1
    #     yield t, np.sin(2*np.pi*t) * np.exp(-t/10.), t

def UpdateData(data):
    x, y, z = data
    # initialPoint.set_data(data[0:2, :num])
    line.set_data(x, y)

    line.set_3d_properties(z)

    # for line, data in zip(lines, dataLines):
    #     # print(line, data)
    #     # NOTE: there is no .set_data() for 3 dim data...
    #     line.set_data(data[0:2, :num])
    #     line.set_3d_properties(data[2, :num])

    return line


with open('pach-cardiac-LinearAcceleration-export.json') as f:
    JSONdata = json.load(f)

xs = np.array([value['x'] for key, value in JSONdata.items()])
ys = np.array([value['y'] for key, value in JSONdata.items()])
zs = np.array([value['z'] for key, value in JSONdata.items()])

# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig)

data = np.array([xs, ys, zs])
line = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1], 'o-')[0]

# initialPoint = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1], 'o-')[0] for dat in data]

# Creating the Animation object
line_ani = animation.FuncAnimation(fig=fig, 
                                   func=UpdateData, 
                                   frames=GenerateNewPoint, 
                                   interval=10, 
                                   blit=False, 
                                   init_func=InitializeFirstPoint)

plt.show()





