Para instalar OpenCV en mac con virtualenv:

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