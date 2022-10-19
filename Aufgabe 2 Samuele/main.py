from PIL import Image
import numpy as np


#rows = int(input("Enter rows: "))
#colums = int(input("Enter colums: "))
rows, colums = 1920, 1080
a= np.array([[255]*rows]*colums)






im = Image.fromarray(a.astype('uint8'))
im.save("./result.png")