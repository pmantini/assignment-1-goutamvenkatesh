import numpy
import math
from resize.interpolation import interpolation
interpolate=interpolation()


class resample:

    def resize(self, image, fx = None, fy = None, interpolation = None):
        """calls the appropriate funciton to resample an image based on the interpolation method
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        interpolation: method used for interpolation ('either bilinear or nearest_neighbor)
        returns a resized image based on the interpolation method
        """

        if interpolation == 'bilinear':
            return self.bilinear_interpolation(image, fx, fy)

        elif interpolation == 'nearest_neighbor':
            return self.nearest_neighbor(image, fx, fy)

    def nearest_neighbor(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the nearest neighbor interpolation method
        """

        #Write your code for nearest neighbor interpolation here
        
        row,column=image.shape
        new_row=row*float(fx)
        new_column=column*float(fy)
        output_image = numpy.zeros((int(new_row), int(new_column), 3),numpy.uint8)
        for i in range(int(new_row)-1):
            for j in range(int(new_column)-1):
                row_value=math.floor(float(i)/float(fx))
                col_value=math.floor(float(j)/float(fy))
                output_image[i,j]=image[row_value,col_value]

        
        
        return output_image


    def bilinear_interpolation(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the bilinear interpolation method
        """

        # Write your code for bilinear interpolation here
        
        row, column = image.shape
        new_row = row * float(fx)
        new_column = column * float(fy)
        output_image = numpy.zeros((int(new_row), int(new_column), 3), numpy.uint8)

        for i in range(int(new_row) - 1):
            x1 = math.floor(float(i) / float(fx))
            x2 = math.ceil(float(i) / float(fx))
            if x2 >=254:
                x2 = 254-x2
            if x1>=254:
                x1=254-x1
            for j in range(int(new_column) - 1):
                y1 = math.floor(float(j) / float(fy))
                y2 = math.ceil(float(j) / float(fy))
                if y2==254:
                    y2=254-y2
                if y1>=254:
                    y1=254-y1

                p1 = (x1, y1, image[x1, y1])
                p2 = (x1, y1, image[x2, y1])
                p3 = (x1, y2, image[x1, y2])
                p4 = (x2, y2, image[x2, y2])
                unknown = (float(i/float(fx)), float(j/float(fy)))
               
                output_image[i, j] = interpolate.bilinear_interpolation(p1, p2, p3, p4, unknown)

        return output_image

