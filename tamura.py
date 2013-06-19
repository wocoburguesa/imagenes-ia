import cv, cv2
import numpy as np
import Image

class Tamura(object):
    """docstring for Tamura"""
    def __init__(self, imgs, k=3):
        super(Tamura, self).__init__()
        self.imgs = imgs
        self.k = k

    def process_coarseness(self,img):
        f = Image.open(img).convert('L')
        mat = np.array(f, dtype = float)
        self.width = f.size[1]
        self.height = f.size[0]
        res = 0.0
        for i in xrange(1,self.width-1):
            for j in xrange(1,self.height-1):
                for kk in xrange(1, self.k):
                    res += 2 ** self.coarseness(mat, i, j, kk)

        return res / (self.width * self.height)

    def coarseness(self, mat, x, y, kk):
        horizontal = self.average_horizontal(mat, x, y, kk)
        vertical = self.average_vertical(mat, x, y, kk)

        if(horizontal >= vertical):
            return horizontal
        return vertical

    def average_horizontal(self, img, x, y, kk):
        return abs(self.average(img, x + 2**(kk-1), y, kk) - self.average(img, 
                                                        x - 2**(kk-1),y, kk))

    def average_vertical(self, img, x, y, kk):
        return abs(self.average(img, x, y+ 2**(kk-1), kk) - self.average(img,
                                                        x, y - 2**(kk-1), kk))

    def average(self, img, x, y, kk):
        acum = 0.0
        for i in xrange(1,2**(2*kk)):
            for j in xrange(1,2**(2*kk)):
                ii = x - 2**(kk-1) + i
                jj = y - 2**(kk-1) + j
                if(ii > 0 and ii < self.width) and (jj > 0 and jj< self.height):
                    acum += img[ii, jj]
        
        return acum/(2**(2*kk))




if __name__ == '__main__':
    tam = Tamura('irma.txt')
    print tam.process_coarseness("irma100/COX_1891.jpg")


