import glcm, extractor

def test1():
    a = glcm.Glcm()
    a.get_features_multiple('texture_list.txt')

if __name__ == '__main__':
    test1()
