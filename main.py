import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

ret, frame = cap.read()
#frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
kernel = np.ones((5, 5), np.float32) / 25
frame2 = cv2.filter2D(frame, -1, kernel)
#frame = cv2.GaussianBlur(frame, (1, 1), 0)
frame3 = cv2.addWeighted(frame2, 1, np.zeros(frame2.shape, frame2.dtype), 0, 0)

#frame2 = cv2.addWeighted(frame, 0.7, np.zeros(frame.shape, frame.dtype), 0, 0)
frame4 = cv2.flip(frame3, 1)


plt.subplot(221),plt.imshow(frame),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(frame2),plt.title('Filtro 2d')
plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(frame3),plt.title('Filtro add')
plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(frame4),plt.title('Ajuste flip')
plt.xticks([]), plt.yticks([])
plt.show()
