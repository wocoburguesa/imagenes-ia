import json

import constants

class Pexifier(object):
    def __init__(self):
        pass

    def pexify(self, json_file, target, irma=False):
        f = open(json_file, 'r')
        json_dict = json.loads(f.read().strip())
        f.close()

        n_features = len(json_dict.values()[0]) + 1

        target_file = open(target + '.data', 'w')
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
            if irma:
                target_file.write('%s\n' % constants.IRMA_CATS[key.split('_')[0]])
            else
                target_file.write('%s\n' % int(key[1:3]))
