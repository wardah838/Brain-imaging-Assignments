#activate image processing 
conda activate image_process

#navigate to the folder which has the image
cd /mnt/c/Users/warda/Downloads
ls          #check for the file


#activate python
python


#import matplotlib.pyplot 
import matplotlib.pyplot as plt
from scipy import misc, ndimage

#reading the image of the brain
brain_image=plt.imread("Brain_image.jpg")
plt.imshow(brain_image)
plt.show()


#dimensions of the image
brain_image.shape


#greyscale image
plt.imshow(brain_image, cmap='Greys_r')
plt.show()


#histogram
plt.hist(brain_image, bins=10)
plt.show()
