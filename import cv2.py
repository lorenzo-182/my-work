import cv2


cap = cv2.VideoCapture(0)

ret, frame = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    # NIVEL 1: Todo esto está dentro del while
    gray1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    diff = cv2.absdiff(gray1, gray2)
    _, threshold = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(threshold, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # NIVEL 2: Dentro del for
        if cv2.contourArea(contour) < 500:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Frame", frame)

    frame = frame2
    ret, frame2 = cap.read()

    # NIVEL 1: El IF está alineado con gray1, gray2, etc.
    if cv2.waitKey(10) & 0xFF == ord('q'):
        # NIVEL 2: El break está dentro del IF
        break

# NIVEL 0: Fuera del while (se ejecuta al presionar 'q')
cap.release()
cv2.destroyAllWindows()
