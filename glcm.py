import cv,cv2,numpy
import json

class Glcm:



	def __init__ (self,path,arch,out):
		imgs = open (arch, 'r')	
		sal = open (out, 'w')
		sal = open (out, 'a')
		f=0
		linea = imgs.readline().strip()
		sal.write('{')
		while linea != "":		
			img_r=self.reducir(
				cv2.imread(path+linea, 
				cv.CV_LOAD_IMAGE_GRAYSCALE))
			print 'Reducida: ' + path+linea
			if f==1 : sal.write(',\n')
			array = [
				['nombre',linea],
				['glcm',self.toString(self.glcm(img_r,3,1))]
				]						
			json.dump(array,sal)
			
			print 'Glcm: ' + path+linea + " OK"
			linea = imgs.readline().strip()	
			f=1
		sal.write('}')
				
		imgs.close()

	def toString(self, img):
		st = "["
		mat = cv.fromarray(img)
		ancho, largo = cv.GetSize(mat)
		for i in range(largo) :
			st +="["			
			for j in range(ancho) :
				st +=str(img[i,j])
				if j != ancho-1 : 
					st += ","
			st+="]"
			if i != largo-1 : st += ","
		st+="]"
		return st
			
	def glcm(self, r_img, right, down):
		mat =  cv.CreateMat(8,8,cv.CV_16U)
		cv.Set(mat,0)
		m = numpy.asarray(mat)
		ancho, largo = cv.GetSize(cv.fromarray(r_img))
		for i in range(largo) :
			for j in range(ancho) :
				m[
					r_img[i,j],
					r_img[
						(i+down)%largo,
						(j+right)%ancho
					]
				]+=1	
		return m

	def reducir(self,img):
		mat = cv.fromarray(img)
		ancho, largo = cv.GetSize(mat)
		for i in range(largo) :
			for j in range(ancho) :
				if img[i,j] != 0 :
					img[i,j] = img[i,j]/32
		
		return img


x = Glcm('irma/','irma.txt','salida_irma.txt')
y = Glcm('tramas/','tramas.txt','salida_tramas.txt')

