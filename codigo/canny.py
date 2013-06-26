import canny_feature

class Canny(object):
    def __init__(object):
        pass

    def get_features_single(self, img):
        return canny_feature.edge_histogram(canny_feature.canny(img))

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
            buff = self.get_features_single(image).values()
            features_dict[image_name] = buff
            counter +=1

        return features_dict
        

