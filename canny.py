import canny_feature

class Canny(object):
    def __init__(object):
        pass

    def get_features(self, img):
        return canny_feature.edge_histogram(canny_feature.canny(img))
