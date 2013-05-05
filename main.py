import glcm, extractor, histogram

if __name__ == '__main__':
    hist_irma = histogram.histogram(
        'irma100/','irma100.txt','NORMAL_irma100_hist.txt',""
        )
    hist_tramas = histogram.histogram(
        'tramas100/','tramas100.txt','NORMAL_tramas100_hist.txt',""
        )

    glcm_irma = glcm.Glcm(
        'irma100/','irma100.txt','final_salida_irma100_glcm.txt'
        )
    glcm_tramas = glcm.Glcm(
        'tramas100/','tramas100.txt','final_salida_tramas100_glcm.txt'
        )

<<<<<<< HEAD
    feature_extractor = extractor.GLCMFeatureExtractor('final_salida_tramas100_glcm.txt')
=======
    a = extractor.GLCMFeatureExtractor('final_salida_tramas100_glcm.txt')
>>>>>>> 53a1a8e8efbeaf1a2cf09f752eb54c99131367c5
    a.idm_all()
    a.dissimilarity_all()
    a.homogeinity_all()
    a.idm_norm_all()
    a.id_norm_all()
    a.asm_all()
    a.sa_all()
    a.sv_all()
    a.normalize_all()
    a.make_feature_vectors()
    a.dump('tramas_glcm_features.txt')

<<<<<<< HEAD
    feature_extractor = extractor.GLCMFeatureExtractor('final_salida_irma100_glcm.txt')
=======
    a = extractor.GLCMFeatureExtractor('final_salida_irma100_glcm.txt')
>>>>>>> 53a1a8e8efbeaf1a2cf09f752eb54c99131367c5
    a.idm_all()
    a.dissimilarity_all()
    a.homogeinity_all()
    a.idm_norm_all()
    a.id_norm_all()
    a.asm_all()
    a.sa_all()
    a.sv_all()
    a.normalize_all()
    a.make_feature_vectors()
    a.dump('irma_glcm_features.txt')
