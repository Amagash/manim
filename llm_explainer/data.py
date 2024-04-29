import gensim.downloader
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt


model = gensim.downloader.load('glove-wiki-gigaword-50')
cat = model["cat"][0:3]
dog = model["dog"][0:3]
flower = model["flower"][0:3]

# fig = plt.figure(figsize = (10,10))
# ax = plt.axes(projection='3d')
# ax.scatter3D(cat[0], cat[1], cat[2], color = 'red')
# ax.scatter3D(dog[0], dog[1], dog[2], color = 'blue')
# ax.scatter3D(flower[0], flower[1], flower[2], color = 'green')
# plt.show()