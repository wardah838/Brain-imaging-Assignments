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



#sigma = 5 Gaussian filter and histogram
brain_image_sigma5=ndimage.gaussian_filter(brain_image, sigma=5)
plt.imshow(brain_image_sigma5, cmap='Greys_r')
plt.show()
plt.hist(brain_image_sigma5, bins=10)
plt.show()


#sigma=10 Gaussian filter and histogram
brain_image_sigma10=ndimage.gaussian_filter(brain_image, sigma=10)
plt.imshow(brain_image_sigma10, cmap='Greys_r')
plt.show()
plt.hist(brain_image_sigma10, bins=10)
plt.show()


#sigma=20 Gaussian filter and histogram
brain_image_sigma20=ndimage.gaussian_filter(brain_image, sigma=20)
plt.imshow(brain_image_sigma20, cmap='Greys_r')
plt.show()
plt.hist(brain_image_sigma20, cmap='Greys_r')
plt.show()


#sigma=30 Gaussian filter and histogram
brain_image_sigma30=ndimage.gaussian_filter(brain_image, sigma=30)
plt.imshow(brain_image_sigma30, cmap='Greys_r')
plt.show()
plt.hist(brain_image_sigma30, cmap='Greys_r')
plt.show()


#sigma=40 Gaussian filter and histogram
brain_image_sigma40=ndimage.gaussian_filter(brain_image, sigma=40)
plt.imshow(brain_image_sigma40, cmap='Greys_r')
plt.show()
plt.hist(brain_image_sigma40, cmap='Greys_r')
plt.show()


#sigma=50 Gaussian filter and histogram
brain_image_sigma50=ndimage.gaussian_filter(brain_image, sigma=50)
plt.imshow(brain_image_sigma50, cmap='Greys_r')
plt.show()
plt.hist(brain_image_sigma50, cmap='Greys_r')
plt.show()

