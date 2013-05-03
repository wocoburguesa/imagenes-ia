import json

import constants

class GLCMFeatureExtractor(object):
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
        """
        Dissimilarity
        """
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

    def homogeinity_all(self):
        """
        Homogeinity
        """
        self.homogeinity_data = {}

        for image in self.glcm_data.keys():
            self.homogeinity_data[image] = \
                self.homogeinity_single(self.glcm_data[image])

    def homogeinity_single(self, glcm):
        homogeinity = 0
        row_total = 0
        i = 0
        j = 0
        for row in glcm:
            for a in row:
                row_total += a
                homogeinity += row_total/(1 + (i - j)**2)
                j += 1
            i += 1

        return homogeinity

    def idm_norm_all(self):
        """
        Inverse Difference Moment - Normalized
        """
        self.idm_norm_data = {}

        for image in self.glcm_data.keys():
            self.idm_norm_data[image] = \
                self.idm_norm_single(self.glcm_data[image])

    def idm_norm_single(self, glcm):
        idm_norm = 0
        i = 0
        j = 0
        for row in glcm:
            for a in row:
                idm_norm += a/(1 + (i-j)**2/constants.GRAY_LEVELS**2)
                j += 1
            i += 1

        return idm_norm

    def id_norm_all(self):
        """
        Inverse Difference - Normalized
        """
        self.id_norm_data = {}

        for image in self.glcm_data.keys():
            self.id_norm_data[image] = \
                self.id_norm_single(self.glcm_data[image])

    def id_norm_single(self, glcm):
        id_norm = 0
        i = 0
        j = 0
        for row in glcm:
            for a in row:
                id_norm += a/(1 + abs(i-j)/constants.GRAY_LEVELS)
                j += 1
            i += 1

        return id_norm

    def asm_all(self):
        """
        Angular Second Moment
        """
        self.asm_data = {}

        for image in self.glcm_data.keys():
            self.asm_data[image] = \
                self.asm_single(self.glcm_data[image])

    def asm_single(self, glcm):
        asm = 0
        i = 0
        j = 0
        for row in glcm:
            for a in row:
                asm += a**2
                j += 1
            i += 1

        return asm

    def set_p_x(self, glcm):
        self.p_x = [0 for row in glcm]
        idx = 0
        for row in glcm:
            for a in row:
                p_x[idx] += a
            idx += 1

    def set_p_y(self, glcm):
        self.p_y = [0 for row in glcm]
        for row in glcm:
            for i in range(len(row)):
                p_y[i] += row[i]

    def sa_all(self):
        """
        Sum Average
        """
        self.sa_data = {}

        for image in self.glcm_data.keys():
            self.sa_data[image] = \
                self.sa_single(self.glcm_data[image])

    def sa_single(self, glcm):
        sa = 0
        i = 0
        j = 0
        for idx in range(len(glcm)*2):
            pxy = 0
            i = 0
            j = 0
            for row in glcm:
                for a in row:
                    if i + j == idx:
                        pxy += a
                    j += 1
                i +=1

            sa += idx * pxy

        return sa

    def sv_all(self):
        """
        Sum Variance
        """
        self.sv_data = {}

        for image in self.glcm_data.keys():
            self.sv_data[image] = \
                self.sv_single(self.glcm_data[image])

    def sv_single(self, glcm):
        sv = 0
        i = 0
        j = 0
        for idx in range(len(glcm)*2):
            pxy = 0
            i = 0
            j = 0
            for row in glcm:
                for a in row:
                    if i + j == idx:
                        pxy += a
                    j += 1
                i +=1

            sv += ((idx - self.id_norm_single(glcm))**2) * pxy

        return sv

    @staticmethod
    def normalize_data(data):
        maxi = max(data.values())
        print maxi
        for key in data.keys():
            data[key] /= float(maxi)

    def normalize_all(self):
        self.normalize_data(self.idm_data)
        self.normalize_data(self.dissimilarity_data)
        self.normalize_data(self.homogeinity_data)
        self.normalize_data(self.idm_norm_data)
        self.normalize_data(self.id_norm_data)
        self.normalize_data(self.asm_data)
        self.normalize_data(self.sa_data)
        self.normalize_data(self.sv_data)

    def make_feature_vectors(self):
        self.features_all = { key:{} for key in self.glcm_data.keys()}
        for key in self.glcm_data.keys():
            self.features_all[key]['idm'] = self.idm_data[key]
            self.features_all[key]['dissimilarity'] = self.dissimilarity_data[key]
            self.features_all[key]['homogeinity'] = self.homogeinity_data[key]
            self.features_all[key]['idm_norm'] = self.idm_norm_data[key]
            self.features_all[key]['id_norm'] = self.id_norm_data[key]
            self.features_all[key]['asm'] = self.asm_data[key]
            self.features_all[key]['sa'] = self.sa_data[key]
            self.features_all[key]['sv'] = self.sv_data[key]

    def dump(self, filename):
        out = open(filename, 'w')
        flag = False

        for key in self.features_all.keys():
            out.write('%s: '% key)
            for feature in self.features_all[key].values():
                if flag:
                    out.write(', %s' % feature)
                else:
                    out.write('%s' % feature)
                    flag = True
            out.write(';\n')
            flag = False

        out.close()

    def __repr__(self):
        return json.dumps(self.glcm_data)


if __name__ == '__main__':
    a = GLCMFeatureExtractor('final_salida_tramas100_glcm.txt')
    print a.glcm_data
