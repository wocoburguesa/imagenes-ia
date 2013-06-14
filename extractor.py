import json

import constants

class FeatureExtractor(object):
    def __init__(self):
        pass

    def get_features_single(self, method, imagefile):
        extractor = method()
        return extractor.get_features_single(imagefile)

    def get_features_multiple(self, method, imagefiles):
        extractor = method()
        return extractor.get_features_multiple(imagefiles)

    def dump_features_multiple(self, method, imagefiles, dump_name):
        extractor = method()
        dumpfile = open(dump_name, 'w')
        dumpfile.write(json.dumps(extractor.get_features_multiple(imagefiles)))
        dumpfile.close()

    def dump_to_file(self, data, filename):
        f = open(filename, 'w')
        f.write(json.dumps(data))
        f.close()


if __name__ == '__main__':
    a = GLCMFeatureExtractor('final_salida_tramas100_glcm.txt')
    print a.glcm_data
