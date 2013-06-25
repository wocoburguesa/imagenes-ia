import scipy.ndimage as ndi
import scipy
import numpy
import Image
import math
import constants
import cv, cv2
from math import pi

def canny(imgfile):

    sigma = 4

    f = imgfile
    img = Image.open(f).convert('L')                                          #grayscale
    img = img.resize((constants.CANNY_RESIZE_WIDTH, constants.CANNY_RESIZE_HEIGHT), Image.NEAREST)     #resize para evitar errores
    imgdata = numpy.array(img, dtype = float)
    G = ndi.filters.gaussian_filter(imgdata, sigma)                           #gaussian low pass filter

    sobelout = Image.new('L', img.size)                                       #empty image
    gradx = numpy.array(sobelout, dtype = float)
    grady = numpy.array(sobelout, dtype = float)

    sobel_x = [[-1,0,1],
               [-2,0,2],
               [-1,0,1]]
    sobel_y = [[-1,-2,-1],
               [0,0,0],
               [1,2,1]]

    width = img.size[1]
    height = img.size[0]

#calculate |G| and dir(G)

    for x in range(1, width-1):
        for y in range(1, height-1):
            px = (sobel_x[0][0] * G[x-1][y-1]) + (sobel_x[0][1] * G[x][y-1]) + \
                (sobel_x[0][2] * G[x+1][y-1]) + (sobel_x[1][0] * G[x-1][y]) + \
                (sobel_x[1][1] * G[x][y]) + (sobel_x[1][2] * G[x+1][y]) + \
                (sobel_x[2][0] * G[x-1][y+1]) + (sobel_x[2][1] * G[x][y+1]) + \
                (sobel_x[2][2] * G[x+1][y+1])

            py = (sobel_y[0][0] * G[x-1][y-1]) + (sobel_y[0][1] * G[x][y-1]) + \
                (sobel_y[0][2] * G[x+1][y-1]) + (sobel_y[1][0] * G[x-1][y]) + \
                (sobel_y[1][1] * G[x][y]) + (sobel_y[1][2] * G[x+1][y]) + \
                (sobel_y[2][0] * G[x-1][y+1]) + (sobel_y[2][1] * G[x][y+1]) + \
                (sobel_y[2][2] * G[x+1][y+1])
            gradx[x][y] = px
            grady[x][y] = py

    sobeloutmag = scipy.hypot(gradx, grady)
    sobeloutdir = scipy.arctan2(grady, gradx)

    for x in range(width):
        for y in range(height):
            if (sobeloutdir[x][y]<22.5 and sobeloutdir[x][y]>=0) or \
                    (sobeloutdir[x][y]>=157.5 and sobeloutdir[x][y]<202.5) or \
                    (sobeloutdir[x][y]>=337.5 and sobeloutdir[x][y]<=360):
                sobeloutdir[x][y]=0
            elif (sobeloutdir[x][y]>=22.5 and sobeloutdir[x][y]<67.5) or \
                    (sobeloutdir[x][y]>=202.5 and sobeloutdir[x][y]<247.5):
                sobeloutdir[x][y]=45
            elif (sobeloutdir[x][y]>=67.5 and sobeloutdir[x][y]<112.5)or \
                    (sobeloutdir[x][y]>=247.5 and sobeloutdir[x][y]<292.5):
                sobeloutdir[x][y]=90
            else:
                sobeloutdir[x][y]=135

    mag_sup = sobeloutmag.copy()

    for x in range(1, width-1):
        for y in range(1, height-1):
            if sobeloutdir[x][y]==0:
                if (sobeloutmag[x][y]<=sobeloutmag[x][y+1]) or \
                        (sobeloutmag[x][y]<=sobeloutmag[x][y-1]):
                    mag_sup[x][y]=0
                elif sobeloutdir[x][y]==45:
                    if (sobeloutmag[x][y]<=sobeloutmag[x-1][y+1]) or \
                            (sobeloutmag[x][y]<=sobeloutmag[x+1][y-1]):
                        mag_sup[x][y]=0
                    elif sobeloutdir[x][y]==90:
                        if (sobeloutmag[x][y]<=sobeloutmag[x+1][y]) or \
                                (sobeloutmag[x][y]<=sobeloutmag[x-1][y]):
                            mag_sup[x][y]=0
            else:
                if (sobeloutmag[x][y]<=sobeloutmag[x+1][y+1]) or \
                        (sobeloutmag[x][y]<=sobeloutmag[x-1][y-1]):
                    mag_sup[x][y]=0

    m = numpy.max(mag_sup)
    th = 0.2*m
    tl = 0.1*m


    gnh = numpy.zeros((width, height))
    gnl = numpy.zeros((width, height))

    for x in range(width):
        for y in range(height):
            if mag_sup[x][y]>=th:
                gnh[x][y]=mag_sup[x][y]
            if mag_sup[x][y]>=tl:
                gnl[x][y]=mag_sup[x][y]

    gnl = gnl-gnh


    def traverse(i, j):
        x = [-1, 0, 1, -1, 1, -1, 0, 1]
        y = [-1, -1, -1, 0, 0, 1, 1, 1]
        for k in range(8):
            if gnh[i+x[k]][j+y[k]]==0 and gnl[i+x[k]][j+y[k]]!=0:
                gnh[i+x[k]][j+y[k]]=1
                traverse(i+x[k], j+y[k])

    for i in range(1, width-1):
        for j in range(1, height-1):
            if gnh[i][j]:
                gnh[i][j]=1
                traverse(i, j)

    gnh = gnh[:100,:64]

    return gnh
    
#matriz blanco y negro

def edge_histogram(canny):
    matrix = canny

    factor = 2
    r_rows = 100/factor
    r_cols = 64/factor

    coeffs = {
        'v': [1.0, -1.0, 1.0, -1.0],
        'h': [1.0, 1.0, -1.0, -1.0],
        'd45': [1.0, 0.0, 0.0, 1.0],
        'd135': [0.0, 1.0, 1.0, 0.0],
        }

    histogram = {
        'v': 0,
        'h': 0,
        'd45': 0,
        'd135': 0,
        'black': 0,
        'white': 0
        }

    for i in range(r_rows):
        for j in range(r_cols):
            for key in coeffs:
                levels = [
                    matrix[i*factor, j*factor],
                    matrix[i*factor, (j*factor)+1],
                    matrix[(i*factor)+1, j*factor],
                    matrix[(i*factor)+1, (j*factor)+1]
                    ]
                total = sum(levels)
                if total == 0:
                    histogram['black'] += 1
                elif total == 4:
                    histogram['white'] += 1
                else:
                    coeff_v = abs(sum(([coeffs['v'][i]*levels[i] for i in range(4)])))
                    if coeff_v == 2:
                        histogram['v'] += 1

                    coeff_h = abs(sum(([coeffs['h'][i]*levels[i] for i in range(4)])))
                    if coeff_h == 2:
                        histogram['h']

                    coeff_d_45 = abs(sum(([coeffs['d45'][i]*levels[i] for i in range(4)])))
                    if coeff_d_45 == 2:
                        histogram['d45'] += 1

                    coeff_d_135 = abs(sum(([coeffs['d135'][i]*levels[i] for i in range(4)])))
                    if coeff_d_135 == 2:
                        histogram['d135'] += 1

    return histogram
#caracteristicas, dicc

if __name__ == '__main__':
    print edge_histogram(canny('irma100/COX_1891.jpg'))


