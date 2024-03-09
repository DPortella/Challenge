import os.path
import cv2
import texto_em_imagem
import infos_to_file


def imagem(caminho, file, path):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    img = cv2.imread(caminho)  # Lendo a imagem
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Tornando a imagem em P/B
    # img_75 = cv2.resize(img, (1080, 720))
    faces = face_cascade.detectMultiScale(gray_image, 1.1, 5)  # Escala da imagem e detecção de rostos
    for (x, y, w, h) in faces:  # --------------------------------------|
        # cv2.rectangle(img, (x, y), (x + h, y + h), (0, 255, 0), 2)  # |Desenhando os retângulos nos rostos encontrados
        if (faces).all():
            print('Rosto encontrado em: %s' % os.path.join(path, file))
            # json2(image)
            infos_to_file.image_to_file(caminho)
            break
    texto_em_imagem.texto(caminho, file, path)
    # cv2.imshow(image, img_75)