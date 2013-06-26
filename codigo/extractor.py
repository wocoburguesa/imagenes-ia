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

    def dump_to_pex(self, data_json, out_pex):
        f = open(data_json, 'r')
        json_dict = json.loads(f.read().strip())
        f.close()

        n_features = len(json_dict.values()[0]) + 1

        target_file = open(out_pex + '.data', 'w')
        target_file.write('DY\n')
        target_file.write('100\n')
        target_file.write('%s\n' % n_features)
        for i in range(n_features):
            target_file.write('c%s;' % i)
        target_file.write('\n')

        for key in json_dict.keys():
            target_file.write('%s; ' % key)
            for i in range(n_features - 1):
                target_file.write('%s; ' % json_dict[key][i])
            target_file.write('%s\n' % int(key[1:3]))

