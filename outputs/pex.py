import json, math

class pex (object):

    def __init__ (self,path, out, numero_img , numero_fea):
        imagenes = open(path, 'r')
        salida = open(out, 'w')
        features = json.load(imagenes.read().strip())
        salida.write(features)
        
a = pex('texture_output_glcm.json','salida_glcm.data',100,8)

