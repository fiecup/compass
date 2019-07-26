import cv2
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    height, width = frame.shape[:2]

    size_border_x = int(width * 0.20)
    size_border_y = int(height * 0.20)

    color_border = (246,12,95)
    size_border = 2

    cv2.line(frame,(size_border_x, 0), (size_border_x, height), color_border, size_border)
    cv2.line(frame,(width-size_border_x, 0), (width-size_border_x,height), color_border, size_border)

    cv2.line(frame,(0, size_border_y), (width, size_border_y), color_border, size_border)
    cv2.line(frame,(0, height-size_border_y), (width,height-size_border_y), color_border, size_border)
    for code in decode(frame):
        rect = code.rect

        cv2.rectangle(frame, (rect.left, rect.top),
        (rect.left + rect.width, rect.top + rect.height),
        (0,255,0), 3)

        center_qr = (int(rect.left + rect.width/2), int(rect.top + rect.height/2))
        print('Punto Centro QR:: ',center_qr)
        cv2.circle(frame, center_qr, 10, (0,0,255), -1)
        donde_estoy = ''

        if center_qr[0] < size_border_x and center_qr[1] < size_border_y:
            # NorOeste
            donde_estoy = 'NorOeste'
            print('Estoy en el NorOeste! -------------------------------------------- ')
        elif center_qr[0] > (width-size_border_x) and center_qr[1] < size_border_y:
            # NorEste
            donde_estoy = 'NorEste'
            print('Estoy en el NorEste! -------------------------------------------- ')
        elif center_qr[0] > (width-size_border_x)  and center_qr[1] > (height-size_border_y):
            # SurEste
            donde_estoy = 'SurEste'
            print('Estoy en el SurEste! -------------------------------------------- ')
        elif center_qr[0] < size_border_x and center_qr[1] > (height-size_border_y):
            # SurOeste
            donde_estoy = 'SurOeste'
            print('Estoy en el SurOeste! -------------------------------------------- ')
        elif center_qr[1] < size_border_y :
            # Norte
            donde_estoy = 'Norte'
            print('Estoy en el NORTE! -------------------------------------------- ')
        elif center_qr[0] > (width-size_border_x):
            # Este
            donde_estoy = 'Este'
            print('Estoy en el ESTE! -------------------------------------------- ')
        elif center_qr[1] > (height-size_border_y):
            # Sur
            donde_estoy = 'Sur'
            print('Estoy en el SUR! -------------------------------------------- ')
        elif center_qr[0] < size_border_x:
            # Oeste
            donde_estoy = 'Oeste'
            print('Estoy en el OESTE! -------------------------------------------- ')
        else :
            donde_estoy = 'Centro'
            print(' ------------------ ¡ CENTRO ! -------------------------- ')

        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(frame,donde_estoy ,center_qr, font, 2,(235, 12, 249), 2, cv2.LINE_AA)

    if ret:
        cv2.imshow('video', frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()