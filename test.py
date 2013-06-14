import glcm, glcm2, extractor

def test1():
    a = glcm.Glcm('tramas100/T11_20.jpg')
    b = a.get_features()
    for row in b:
        print row

def test2():
    a = glcm2.Glcm('tramas100/T11_20.jpg')

def test3():
    a = extractor.FeatureExtractor()
    b = a.get_features_multiple(glcm.Glcm, 'texture_list.txt')
    a.dump_to_file(a.files_features, 'texture_output.json')

def test4():
    a = glcm.Glcm()
    a.get_features_single('tramas100/T01_10.jpg')

def test5():
    a = glcm.Glcm()
    a.get_features_multiple('texture_list.txt')

if __name__ == '__main__':
    test5()
