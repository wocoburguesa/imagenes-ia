Archivos de salida:

    -NORMAL_irma100_hist.txt:
    Salida de 100 imagenes de la carpeta irma100 Normalizada utilizando Histograma
    -NORMAL_tramas100_hist.txt
    Salida de 100 imagenes de la carpeta tramas100 Normalizada utilizando Histograma
    
    -irma_glcm_features.txt:
    Salida de 100 imagenes de la carpeta irma100 Normalizada utilizando GLCM
    -tramas_glcm_features.txt:
    Salida de 100 imagenes de la carpeta tramas100 Normalizada utilizando CLCM
    
    *Los demas archivos son necesarios para la generacion de estos archivos

Para ejeutar el codigo:

    -Ejecutar $python main.py
    
    *Solo se necesita instalar OpnenCV para Python (En la parte inferior las instrucciones para MAc o Ubuntu)

Para instalar OpenCV en Ubuntu:

$sudo apt-get update
$sudo apt-get install opencv python-opencv

Para instalar OpenCV en Mac con virtualenv:

- Comprobar las instalaciones de Python:
  * La que viene por defecto con mac está en /System/Library/etcetera
  * La que se instala con macports está en /opt/local/Library/etcetera
- Comprobar el ejecutable de python que esté utilizando el env generado
- Descargar el codigo fuente mas actual de OpenCV en su repo en github
- Extraer con tar -zxvf

Hacer lo siguiente:
$cd opencv //entrar al root del repo clonado
$mkdir release
$cd release
$sudo cmake 
      -D CMAKE_BUILD_TYPE=RELEASE
      -D CMAKE_INSTALL_PREFIX=/usr/local/
      -D PYTHON_EXECUTABLE={ UBICACION_DEL_ENV }/bin/python
      -D PYTHON_PACKAGES_PATH={ UBICACION_DEL_ENV }/lib/python2.7/site-packages/
      -D BUILD_NEW_PYTHON_SUPPORT=ON
      -D PYTHON_INCLUDE_DIR={ UBICACION_DEL_ENV }/include/python2.7/
      -D PYTHON_LIBRARY={ INSTALACION DE PYTHON }/Versions/2.7/lib/libpython2.7.dylib
      ..

- Asegurar que { INSTALACION DE PYTHON } sea el mismo que el que se comprobó a la hroa de crear el env

