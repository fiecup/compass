import cv2
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)

def core_compass(imagen, margen_x=0.2, margen_y=0.2, imprimir_posicion=False, ver_delimitacion=False):
    """Detecta un Codigo QR basandose en los Puntos Cardinales.

    Devuelve:

    donde_estoy --> Norte, Este, Sur, Oeste, NorOeste, NorEste, SurEste, SurOeste.
    
    imagen --> imagen

    Parámetros:

    imagen <-- es la instancia de la imagen, o frame de un video.
    """
    alto, ancho = imagen.shape[:2]

    size_border_x = int(ancho * margen_x)
    size_border_y = int(alto * margen_y)

    color_border = (246,12,95)
    size_border = 2

    if ver_delimitacion: cv2.line(imagen,(size_border_x, 0), (size_border_x, alto), color_border, size_border)
    if ver_delimitacion: cv2.line(imagen,(ancho-size_border_x, 0), (ancho-size_border_x,alto), color_border, size_border)

    if ver_delimitacion: cv2.line(imagen,(0, size_border_y), (ancho, size_border_y), color_border, size_border)
    if ver_delimitacion: cv2.line(imagen,(0, alto-size_border_y), (ancho,alto-size_border_y), color_border, size_border)
    for code in decode(imagen):
        rect = code.rect

        if ver_delimitacion: cv2.rectangle(imagen, (rect.left, rect.top), (rect.left + rect.width, rect.top + rect.height), (0,255,0), 3)

        center_qr = (int(rect.left + rect.width/2), int(rect.top + rect.height/2))
        if imprimir_posicion: print('Punto Centro QR:: ',center_qr)
        if ver_delimitacion: cv2.circle(imagen, center_qr, 10, (0,0,255), -1)
        donde_estoy = ''

        if center_qr[0] < size_border_x and center_qr[1] < size_border_y:
            # NorOeste
            donde_estoy = 'NorOeste'
            if imprimir_posicion: print('----------- Estoy en el NorOeste! -------------------------------------------- ')
        elif center_qr[0] > (ancho-size_border_x) and center_qr[1] < size_border_y:
            # NorEste
            donde_estoy = 'NorEste'
            if imprimir_posicion: print('----------- Estoy en el NorEste! -------------------------------------------- ')
        elif center_qr[0] > (ancho-size_border_x)  and center_qr[1] > (alto-size_border_y):
            # SurEste
            donde_estoy = 'SurEste'
            if imprimir_posicion: print('----------- Estoy en el SurEste! -------------------------------------------- ')
        elif center_qr[0] < size_border_x and center_qr[1] > (alto-size_border_y):
            # SurOeste
            donde_estoy = 'SurOeste'
            if imprimir_posicion: print('----------- Estoy en el SurOeste! -------------------------------------------- ')
        elif center_qr[1] < size_border_y :
            # Norte
            donde_estoy = 'Norte'
            if imprimir_posicion: print('----------- Estoy en el NORTE! -------------------------------------------- ')
        elif center_qr[0] > (ancho-size_border_x):
            # Este
            donde_estoy = 'Este'
            if imprimir_posicion: print('----------- Estoy en el ESTE! -------------------------------------------- ')
        elif center_qr[1] > (alto-size_border_y):
            # Sur
            donde_estoy = 'Sur'
            if imprimir_posicion: print('----------- Estoy en el SUR! -------------------------------------------- ')
        elif center_qr[0] < size_border_x:
            # Oeste
            donde_estoy = 'Oeste'
            if imprimir_posicion: print('----------- Estoy en el OESTE! -------------------------------------------- ')
        else :
            donde_estoy = 'Centro'
            if imprimir_posicion: print(' ------------------ ¡ CENTRO ! -------------------------- ')

        if ver_delimitacion: cv2.putText(imagen,donde_estoy ,center_qr, cv2.FONT_HERSHEY_COMPLEX, 2,(235, 12, 249), 2, cv2.LINE_AA)
        return donde_estoy, imagen


### ----------------------------------------------------------------
### !Prueba con una imagen¡
imagen = cv2.imread('03.png')
_, imagen = core_compass(imagen, ver_delimitacion=True)
# cv2.imshow('imagen', res_img)
cv2.imwrite('posicion_qr.png', imagen)
cv2.waitKey(0)
### ----------------------------------------------------------------


### ----------------------------------------------------------------
### ¡Prueba con la camara!
# while(True):
#     ret, frame = cap.read()
#     resp, frame = core_compass(frame)
#     if resp:
#         print('resp:: ',resp)

#     if ret:
#         cv2.imshow('video', frame)
    
#     if cv2.waitKey(1) & 0xFF == 27:
#         break

# cap.release()
# cv2.destroyAllWindows()
### ----------------------------------------------------------------
