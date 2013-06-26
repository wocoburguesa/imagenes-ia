
from extractor import FeatureExtractor
import canny, glcm, histogram

a = FeatureExtractor()

a.dump_features_multiple(histogram.Histogram, 'tramas100/tramas_list.txt','salida/out_histogram_tramas.json')
a.dump_features_multiple(histogram.Histogram, 'irma100/irma_list.txt','salida/out_histogram_irma.json')

a.dump_features_multiple(canny.Canny, 'tramas100/tramas_list.txt','salida/out_canny_tramas1.json')
a.dump_features_multiple(canny.Canny, 'irma100/irma_list.txt','salida/out_canny_irma.json')

a.dump_features_multiple(glcm.Glcm, 'tramas100/tramas_list.txt','salida/out_glcm_tramas.json')
a.dump_features_multiple(glcm.Glcm, 'irma100/irma_list.txt','salida/out_glcm_irma.json')

a.dump_to_pex('salida/out_histogram_tramas.json','salida/pex/out_histogram_tramas')
a.dump_to_pex('salida/out_histogram_irma.json','salida/pex/out_histogram_irma')

a.dump_to_pex('salida/out_canny_tramas1.json','salida/pex/out_canny_tramas')
a.dump_to_pex('salida/out_canny_irma.json','salida/pex/out_canny_irma')

a.dump_to_pex('salida/out_glcm_tramas.json','salida/pex/out_glcm_tramas')
a.dump_to_pex('salida/out_glcm_irma.json','salida/pex/out_glcm_irma')



