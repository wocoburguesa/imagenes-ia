import cv,cv2,numpy
import json

class Glcm(object):

    def __init__ (self,path,arch,out):
        imgs = open (arch, 'r')
        sal = open (out, 'w')
        sal = open (out, 'a')
        linea = imgs.readline().strip()
        glcm_dic = {}

        while linea != "":
            img_r=self.reducir(
                cv2.imread(path+linea,
                cv.CV_LOAD_IMAGE_GRAYSCALE))
            print 'Reducida: ' + path+linea

            glcm_dic.update({linea : self.glcm(img_r,3,1)})

            print 'Glcm: ' + path+linea + " OK"
            
            linea = imgs.readline().strip()

        sal.write(str(glcm_dic))

        imgs.close()

    def glcm(self, r_img, right, down):
        mat =  cv.CreateMat(
            8,
            8,
            cv.CV_16U
            )
        cv.Set(mat,0)

        m = numpy.asarray(mat)
        ancho, largo = cv.GetSize(cv.fromarray(r_img))

        for i in range(largo) :
            for j in range(ancho) :
                fila = r_img[i,j]
                columna = r_img[
                    (i+down)%largo,
                    (j+right)%ancho
                    ]
                m[fila, columna] += 1

        return m

    def reducir(self, img):
        mat = cv.fromarray(img)
        ancho, largo = cv.GetSize(mat)

        for i in range(largo) :
            for j in range(ancho) :
                img[i,j] /= 32

        return img


Glcm('irma100/','irma100.txt','salida_irma100_glcm.txt')
Glcm('tramas100/','tramas100.txt','salida_tramas100_glcm.txt')

