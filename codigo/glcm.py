import json, math

import cv, cv2, numpy

import constants

class GLCMFeatureExtractor(object):
    def __init__(self):
        pass

    def contrast(self, glcm):
        contrast = 0
        for i in range(len(glcm)):
            inner_sum = 0
            for j in range(len(glcm)):
                for k in range(len(glcm)):
                    if abs(k-j) == i:
                        inner_sum += glcm[j][k]
            contrast += (i**2) * inner_sum

        return contrast

    def entropy(self, glcm):
        entropy = 0
        for i in range(len(glcm)):
            for j in range(len(glcm)):
                entropy += glcm[i][j] * math.log(glcm[i][j], 2)

        return entropy

    def correlation(self, glcm):
        pass

    def idm(self, glcm):
        idm = 0
        i = 0
        j = 0
        for row in glcm:
            for a in row:
                idm += a / float(1 + (i - j) ** 2)
                j += 1
            i += 1

        return idm

    def dissimilarity(self, glcm):
        dissimilarity = 0
        i = 0
        j = 0
        for row in glcm:
            for a in row:
                dissimilarity += abs(i-j) * a
                j += 1
            i += 1

        return dissimilarity

    def homogeinity(self, glcm):
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

    def idm_norm(self, glcm):
        idm_norm = 0
        i = 0
        j = 0
        for row in glcm:
            for a in row:
                idm_norm += a/(1 + (i-j)**2/constants.GRAY_LEVELS**2)
                j += 1
            i += 1

        return idm_norm

    def id_norm(self, glcm):
        id_norm = 0
        i = 0
        j = 0
        for row in glcm:
            for a in row:
                id_norm += a/(1 + abs(i-j)/constants.GRAY_LEVELS)
                j += 1
            i += 1

        return id_norm

    def asm(self, glcm):
        asm = 0
        i = 0
        j = 0
        for row in glcm:
            for a in row:
                asm += a**2
                j += 1
            i += 1

        return asm

    def sa(self, glcm):
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

    def sv(self, glcm):
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

            sv += ((idx - self.id_norm(glcm))**2) * pxy

        return sv

    @staticmethod
    def normalize_data(data):
        maxi = max(data.values())
        print maxi
        for key in data.keys():
            data[key] /= float(maxi)

    def make_feature_vector(self, glcm):
        features = {}
        features['idm'] = self.idm(glcm)
        features['dissimilarity'] = self.dissimilarity(glcm)
        features['homogeinity'] = self.homogeinity(glcm)
        features['idm_norm'] = self.idm_norm(glcm)
        features['id_norm'] = self.id_norm(glcm)
        features['asm'] = self.asm(glcm)
        features['sa'] = self.sa(glcm)
        features['sv'] = self.sv(glcm)
        return features

    def __repr__(self):
        return json.dumps(self.glcm_data)

class Glcm(object):
    def __init__(self, rows=None, cols=None,
                 down=None, right=None,
                 reduce_factor=None):
        if rows:
            self.rows = rows
        else:
            self.rows = constants.GLCM_DEFAULT_ROWS

        if cols:
            self.cols = cols
        else:
            self.cols = constants.GLCM_DEFAULT_COLS

        if down:
            self.down = down
        else:
            self.down = constants.GLCM_DEFAULT_DOWN

        if right:
            self.right = right
        else:
            self.right = constants.GLCM_DEFAULT_RIGHT

        if reduce_factor:
            self.reduce_factor = reduce_factor
        else:
            self.reduce_factor = constants.GLCM_REDUCE_FACTOR

        self.feature_extractor = GLCMFeatureExtractor()

    def get_features_single(self, img):
        img = cv2.imread(
            img,
            cv.CV_LOAD_IMAGE_GRAYSCALE
            )

        glcm = self.glcm(self.reduce(img))

        return self.feature_extractor.make_feature_vector(glcm)


    def get_features_multiple(self, imglist):
        imglist = open(imglist, 'r')
        imgfiles = [f.strip() for f in imglist.readlines()]
        imglist.close()

        features_dict = {}

        counter = 1
        total = len(imgfiles)

        for image in imgfiles:
            print 'Extracting features for {file}. {current} out of {total}'.format(
                file=image,
                current=counter,
                total=total
                )
            image_name = image.split('/')[1]
            image = cv2.imread(
                image,
                cv.CV_LOAD_IMAGE_GRAYSCALE
                )

            glcm = self.glcm(self.reduce(image))

            features_dict[image_name] = self.feature_extractor.make_feature_vector(glcm).values()
            counter +=1

        return features_dict


    def glcm(self, r_img):
        glcm_mat = [[ 0 for col in range(self.cols)] for row in range(self.rows)]

        total = 0

        for i in range(self.img_rows) :
            for j in range(self.img_cols) :
                row = r_img[i][j]
                column = r_img[(i+self.down)%self.img_rows][(j+self.right)%self.img_cols]
                glcm_mat[row][column] += 1
                total += 1

        for i in range(self.rows) :
            for j in range(self.cols) :
                glcm_mat[i][j] = glcm_mat[i][j]/float(total)

        return glcm_mat

    def reduce(self, img):
        mat = list(img)
        self.img_matrix = [list(row) for row in mat]

        self.img_rows = len(self.img_matrix)
        self.img_cols = len(self.img_matrix[0])

        for i in range(self.img_rows):
            for j in range(self.img_cols):
                mat[i][j] /= constants.GLCM_REDUCE_FACTOR

        return mat
