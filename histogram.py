import cv, cv2, numpy, json, math

class histogram (object):

    def __init__ (self,path,arch,out,prex):
        imagenes = open (arch, 'r')
        salida = open (out, 'w')
        salida = open (out, 'a')
        linea = imagenes.readline().strip()

        self.features = {}

        while linea != "":

            img = cv2.imread(path+linea,cv.CV_LOAD_IMAGE_GRAYSCALE)
            i_histograma, i_tamano = self.f_histogram(img)
            caracteristica = self.get_caracteristicas(i_histograma,i_tamano)
            print linea
            salida.write(prex+linea+": "+
                str(caracteristica[0])+", "+
                str(caracteristica[1])+", "+
                str(caracteristica[2])+", "+
                str(caracteristica[3])+", "+
                str(caracteristica[4])+", "+
                str(caracteristica[5])+", "+
                str(caracteristica[6])+';\n')

            linea = imagenes.readline().strip()
        imagenes.close()

    def get_caracteristicas (self, histograma, tamano):
        vector_P = self.f_P(histograma, tamano)
        mean = self.f_mean(histograma, vector_P)
        stddev = self.f_stddev(histograma, vector_P, mean)
        skew = self.f_skew(histograma, vector_P, mean, stddev)
        kurtosis = self.f_kurtosis(histograma, vector_P, mean, stddev)
        energy = self.f_energy(histograma,vector_P)
        entropy = self.f_entropy(histograma,vector_P)
        sm = self.f_sm(histograma,stddev)
        return [mean,stddev,skew,kurtosis,energy,entropy,sm]

    def f_histogram (self, imagen):
        histograma = [0]*256
        matriz = cv.fromarray(imagen)
        ancho, largo = cv.GetSize(matriz)

        for i in range(largo) :
            for j in range(ancho) :
                histograma[imagen[i][j]]+=1
        return histograma, ancho*largo

    def f_P (self, histograma, total_pixeles):

        vector_P = [0]*len(histograma)
        for i in range (len(histograma)):
            vector_P[i] = float(histograma[i])/float(total_pixeles)
        return vector_P

    def f_mean (self, histograma, vector_P):
        mean = 0
        for i in range(len(histograma)):
            mean+=histograma[i]*vector_P[i]
        return mean

    def f_stddev (self, histograma, vector_P, mean):
        stddev = 0
        for i in range(len(histograma)):
            stddev+= pow (histograma[i]-mean, 2) * vector_P[i]
        return math.sqrt(stddev)

    def f_skew (self, histograma, vector_P, mean, stddev):
        skew = 0
        for i in range(len(histograma)):
            skew += pow (histograma[i]-mean,3) * vector_P[i]
        return (1/(pow(stddev,3)))*skew

    def f_kurtosis (self, histograma, vector_P, mean, stddev):
        kurtosis = 0
        for i in range(len(histograma)):
            kurtosis+= pow (histograma[i]-mean,4) * vector_P[i]
        return (1/pow(stddev,4))*kurtosis
        
    def f_energy (self, histograma, vector_P):
        energy = 0
        for i in range(len(histograma)):
            energy += pow(vector_P[i],2)
        return energy

    def f_entropy (self, histograma, vector_P):
        entropy = 0
        for i in range(len(histograma)):
            if (vector_P[i]!=0):
                entropy += (vector_P[i] * math.log(vector_P[i],2))
        return -entropy

    def f_sm (self, histograma, stddev):
        return 1-(1/(1+pow(stddev,2)))

histogram('irma100/','irma100.txt','salida_irma_hist100.txt',"")
histogram('tramas100/','tramas100.txt','salida_tramas_hist100.txt',"")



