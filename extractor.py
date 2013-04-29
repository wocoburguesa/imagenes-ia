import json

class Extractor(object):
    def __init__(self, filename):
        glcm_file = open(filename, 'r')
        glcm_json = glcm_file.read()
        glcm_file.close()

        glcm_raw = json.loads(glcm_json)
        self.glcm_data = {}
        for pair in glcm_raw:
            self.glcm_data[pair[0][1]] = json.loads(pair[1][1])

    def idm_all(self):
        """
        Inverse difference moment
        """
        self.idm_data = {}

        for image in self.glcm_data.keys():
            self.idm_data[image] = \
                self.idm_single(self.glcm_data[image])

    def idm_single(self, glcm):
        idm = 0
        i = 0
        j = 0
        for row in glcm:
            for a in row:
                idm += a / float(1 + (i - j) ** 2)
                j += 1
            i += 1

        return idm

    def dissimilarity_all(self):
        self.dissimilarity_data = {}

        for image in self.glcm_data.keys():
            self.dissimilarity_data[image] = \
                self.dissimilarity_single(self.glcm_data[image])

    def dissimilarity_single(self, glcm):
        dissimilarity = 0
        i = 0
        j = 0
        for row in glcm:
            for a in row:
                dissimilarity += abs(i-j) * a
                j += 1
            i += 1

        return dissimilarity

    def __repr__(self):
        return json.dumps(self.glcm_data)


if __name__ == '__main__':
    a = Extractor('salida_tramas.txt')
    a.dissimilarity_all()
    a.idm_all()
    print a.idm_data
