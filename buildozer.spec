[app]

# (Nome do aplicativo que será exibido no dispositivo)
title = ArucoDetectorApp

# (Nome do arquivo principal do seu aplicativo Python)
package.name = opencv_test
package.domain = org.aruco.detector

# (Diretório onde estão localizados os arquivos do seu aplicativo)
source.dir = .

source.include_exts = py,png,jpg,kv,atlas

# (Lista das bibliotecas necessárias para o seu aplicativo separadas por vírgulas)
requirements = python3, kivy, opencv-python, opencv-contrib-python

# (Versão do seu aplicativo)
version = 1.0

# (Permissões do Android necessárias para o seu aplicativo)
android.permissions = CAMERA, INTERNET

# (Configurações adicionais do Android)
android.arch = armeabi-v7a
android.api = 27
android.sdk = 27
android.ndk = 21.1.6352462
android.gradle_dependencies = 'implementation "com.google.firebase:firebase-analytics:17.5.0"'


