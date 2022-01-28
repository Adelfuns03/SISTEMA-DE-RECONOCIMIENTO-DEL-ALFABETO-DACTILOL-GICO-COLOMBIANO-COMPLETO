import HandTrackingModule as htm

detector = htm.handDetector(detectionCon=0.75)

Bandera2 = 0, 0
Bandera3 = 0, 0
Bandera4 = 0, 0
Bandera5 = 0, 0
xx8, xx12, yy12, yy8 = 0, 0, 0, 0
class Coordinates():

    def Left (self, frame):
        global Bandera2, Bandera3, Bandera4, Bandera5,xx8, xx12, yy12,yy8
        frame = detector.findHands(frame)
        lmList = detector.findPosition(frame, draw=False)
        Bandera = 0
        if len(lmList) != 0:

            x0, y0 = lmList[0][1:]
            x1, y1 = lmList[1][1:]
            x2, y2 = lmList[2][1:]
            x3, y3 = lmList[3][1:]
            x4, y4 = lmList[4][1:]
            x5, y5 = lmList[5][1:]
            x6, y6 = lmList[6][1:]
            x7, y7 = lmList[7][1:]
            x8, y8 = lmList[8][1:]
            x9, y9 = lmList[9][1:]
            x10, y10 = lmList[10][1:]
            x11, y11 = lmList[11][1:]
            x12, y12 = lmList[12][1:]
            x13, y13 = lmList[13][1:]
            x14, y14 = lmList[14][1:]
            x15, y15 = lmList[15][1:]
            x16, y16 = lmList[16][1:]
            x17, y17 = lmList[17][1:]
            x18, y18 = lmList[18][1:]
            x19, y19 = lmList[19][1:]
            x20, y20 = lmList[20][1:]

            fingers = detector.fingersUp()

            # Letra A-a - Izquierda
            if fingers[0] == 1 and fingers[1] == 0 and x8 < x4 and x12 < x8 and x16 < x12 and x20 < x16 and y6 < y8 and y10 < y12 and y14 < y16 and y18 < y20 and y4 < y6 and y4 < y10 and y4 < y14 and y4 < y18 and y0 > y1 and x20 < x0:
                print("A")
                Bandera = 1
            # Letra B-b  - Izquierda
            elif  y8 < y6 and y12 < y10 and y16 < y14 and y20 < y18 and y4 > y9 and y5 < y17 and x5 > x4:
                print("B")
                Bandera = 2
            # Letra C-c Izquierda
            elif x17 < x5 and x0 < x17 and y8 < y6 and y12 < y10 and y16 < y14 and y20 < y18:
                print("C")
                Bandera = 3
            # Letra D-d - Izquierda
            elif y8 < y6 and y5 < y3 and y11 < y12 and x5 > x17 and y15 < y16 and y4 > y5 and y20 > y19 and x20 < x1 and x4 < x5 and y18 < y17 and y11 < y9:
                print("D")
                Bandera = 4
            # Letra E-e - Izquierda
            elif y7 > y6 and y11 > y10 and y15 > y14 and y20 > y18 and y5 < y4 and y11 < y9 and y12 > y11 and y9 < y4 and y13 < y4 and y17 < y4 and y20 < y5 and x4 < x5:
                print("E")
                Bandera = 5
            # Letra F-f - Izquierda
            elif fingers[0] == 1 and fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0 and y8 < y6 and y8 < y7 and y5 < y3 and y11 < y12 and x5 > x17 and y15 < y16 and y4 < y5 and y20 > y19 and (x3 - x6) > 10:
                print("F")
                Bandera = 6
            # Letra G-g - Izquierda
            elif fingers[0] == 0 and fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0 and y8 < y6 and y12 > y11 and y16 > y15 and y20 > y19 and x5 < x17 and y16 < y17:
                Bandera = 7
                print("Bandera g")
            if Bandera == 7 and x20 < x0 and y5 < y0 and y8 < y20:
                Bandera = 8
                print("G")
            # Letra H-h - Izquierda
            elif x5 < x17 and y8 < y6 and y12 < y10 and y16 > y5 and y20 > y5 and Bandera != 8:
                Bandera2 = 9
                print("Bandera h")
            if Bandera2 == 9 and x8 > x0 and x12 > x0 and x8 > x6 and x12 > x10 and x8 > x14 and x8 > x18 and x12 > x14 and x12 > x18:
                Bandera = 10
                Bandera2 = 0
                print("H")
            # Letra I-i - #Izquierda
            elif fingers[4] == 1 and fingers[0] == 0 and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0 and y20 < y19 and x5 > x17  and y16 > y14 and y12 > y10 and y8 > y6  and (x20 - x17) < 10 and y4 > y9 and x4 < x5 and (x4 - x5) > 20:
                print("I")
                Bandera = 11
            # Letra J-j #Izquierda
            elif y20 < y19 and x5 > x17 and y16 > y14 and y12 > y10 and y8 > y6  and (x20 - x17) < 10 and y4 > y9:
                Bandera = 12
                print("Bandera J")
            if Bandera == 12 and x0 > x16 :
                Bandera = 13
                print("J")
            # Letra K-k #Izquierda
            elif y8 < y6 and y8 < y12 and y4 < y12 and y4 < y11 and y4 < y10 and x12 > x8 and x0 < x4 and x1 < x17:
                print("K")
                Bandera = 14
            # Letra L-l #Izquierda
            elif y8 < y6 and y8 < y7 and x3 > x5 and y12 > y10 and y12 > y11 and y16 > y14 and y16 > y15 and y20 > y18 and y20 > y19 and (x17 - x5) > 25 and (x5 - x4) > 80 and (x8 - x4) > 10:
                print("L", x4, x8)
                Bandera = 15
            # Letra M-m Izquierda
            elif y6 > y5 and y10 > y9 and y15 > y20 and y0 < y12 and y16 > y11 and y14 > y13 and y16 > y14 and y12 > y8 and x12 < x5:
                print("M")
                Bandera = 16
            # Letra N-n Izquierda
            elif y6 > y5 and y10 > y9 and y15 > y20 and y0 < y12 and y11 > y16 and Bandera != 18 and x5 < x17 and y12 > y8 and y4 < y12 and y4 < y8 and x4 < x11:
                print("N")
                Bandera = 17
            # Letra Ñ-ñ #Recalibracion
            elif y12 > y0 and y8 > y0 and y8 > y16 and y8 > y20 and y8 > y4 and x4 < x11:
                Bandera = 18
                print("Bandera ñ")
                Bandera = 19
            # print("Ñ")
            # Letra O-o Izquierda
            elif x17 < x5 and x0 < x17 and y8 > y6 and y12 > y10 and y16 > y14 and y20 > y18 and y4 < y9:
                print("O")
                Bandera = 20
            # Letra P-p #Izquierda
            elif x0 < x4 and y4 > y0 and x6 > x4 and x10 > x4 and x20 < x4:
                print("P")
                Bandera = 21
            # Letra Q-q #Izquierda
            elif y4 < y10 and y5 > y3 and y20 < y4 and (x4 - x5) > 10 and x5 < x17:
                print("Q")
                Bandera = 22
            # Letra R-r #Izquierda
            elif y4 < y17 and y20 > y4 and y8 > y12 and y16 > y14 and y5 < y14 and x5 > x17 and x8 < x12:
                print("R")
                Bandera = 27
            # Letra S-s # Izquierda
            elif Bandera4 != 35 and Bandera4 != 36 and Bandera4 != 37 and Bandera4 != 24 and Bandera != 31 and x5 < x17 and y8 < y6 and y8 < y4 and y8 < y16 and y8 < y20 and y5 < y4 and x8 < x5:
                xx8 = x8
                yy8 = y8
                Bandera4 = 35
                print("Bandera 1 s", x8)
            if Bandera4 == 35 and Bandera4 != 36 and xx8 < x8 and (x8 - xx8) < 30 and (
                    yy8 - y8) < 5 and x5 < x17 and y8 < y6 and y8 < y4 and y8 < y16 and y8 < y20 and y5 < y4 and x8 < x5:
                xx8 = x8
                yy8 = y8
                Bandera4 = 36
                print("Bandera 2 s")
            if Bandera4 == 36 and Bandera4 != 37 and xx8 > x8 and (x8 - xx8) < 40 and (
                    y8 - yy8) > 15 and x5 < x17 and y8 < y6 and y8 < y4 and y8 < y16 and y8 < y20 and y5 < y4 and x8 < x5:
                xx8 = x8
                yy8 = y8
                Bandera4 = 37
                print("Bandera 3 s")
            if Bandera4 == 37 and xx8 > x8 and (x8 - xx8) > 30 and (
                    yy8 - y8) < 5 and x5 < x17 and y8 < y6 and y8 < y4 and y8 < y16 and y8 < y20 and y5 < y4 and x8 < x5:
                xx8 = x8
                yy8 = y8
                #Bandera = 24
                Bandera4 = 0
                print("S")
            # Letra T-t #Izquierda
            elif fingers[0] == 0 and fingers[1] == 0 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1 and y12 < y11 and y16 < y15 and y20 < y19 and y8 > y11 and x5 > x17:
                print("T")
                Bandera = 25
            # Letra U-u #Izquierda
            elif   y8 < y6 and y20 < y18 and y12 > y10 and y16 > y14 and x5 > x17:
                print("U")
                Bandera = 26
            # Letra V-v #Izquierda
            elif y12 < y10 and y8 < y6 and y14 < y16 and y18 < y20 and y9 < y4 and y5 > y14 and x8 > x6 and x5 > x17:
                print("V", x12, x8)
                Bandera = 23
            # Letra W-w #Izquierda
            elif y4 < y17 and y20 > y4 and y8 > y12 and y16 < y14 and y18 < y20 and x5 > x17:
                print("W")
                Bandera = 28
            # Letra X-x #Izquierda
            elif y8 > y6 and x0 < x4 and x0 < x17 and y7 < y12 and y7 < y16 and y7 < y20 and x1 > x17 and y4 > y5 and y16 > y5 and y20 > y5 and y0 > y5 and y4 > y8 and y0 > y1 and y20 < y1 and y20 > y13 and y20 > y17:
                print("X")
                Bandera = 29
            # Letra Y-y #Izquierda
            elif x5 > x17 and y8 > y6 and y12 > y10 and y12 > y9 and y16 > y14 and y16 > y15 and y20 < y18 and y4 < y5 and y4 < y9 and x4 > x5 and y0 > y1 and x17 > x20 and x4 > x3:
                print("Y")
                Bandera = 30
            # Letra Z-z #Izquierda
            elif Bandera2 != 31 and Bandera2 != 32 and Bandera2 != 33 and Bandera2 != 34 and x5 < x17 and y8 < y6 and y8 < y4 and y8 < y16 and y8 < y20 and y12 < y10 and y12 < y4 and y12 < y16 and y12 < y20 and ( x12 - x8) < 15:
                xx8 = x8
                xx12 = x12
                yy8 = y8
                yy12 = y12
                Bandera2 = 31
                print("Bandera 1 z", x12, x8)
            if Bandera2 == 31 and Bandera2 != 32 and xx8 < x8 and xx12 < x12 and (x8 - xx8) > 30 and (x12 - xx12) > 30 and (yy12 - y12) < 5 and (yy8 - y8) < 5 and x5 < x17 and y8 < y6 and y8 < y4 and y8 < y16 and y8 < y20 and y12 < y10 and y12 < y4 and y12 < y16 and y12 < y20:
                xx8 = x8
                xx12 = x12
                yy8 = y8
                yy12 = y12
                Bandera2 = 32
                print("Bandera 2 z")
            if Bandera2 == 32 and Bandera2 != 33 and xx8 > x8 and xx12 > x12 and (x8 - xx8) < 40 and (x12 - xx12) < 40 and (y12 - yy12) > 15 and (y8 - yy8) > 15 and x5 < x17 and y8 < y6 and y8 < y4 and y8 < y16 and y8 < y20 and y12 < y10 and y12 < y4 and y12 < y16 and y12 < y20:
                xx8 = x8
                xx12 = x12
                yy8 = y8
                yy12 = y12
                Bandera2 = 33
                print("Bandera 3 z")
            if Bandera2 == 33 and xx8 < x8 and xx12 < x12 and (x8 - xx8) > 30 and (x12 - xx12) > 30 and (yy12 - y12) < 5 and (yy8 - y8) < 5 and x5 < x17 and y8 < y6 and y8 < y4 and y8 < y16 and y8 < y20 and y12 < y10 and y12 < y4 and y12 < y16 and y12 < y20:
                xx8 = x8
                xx12 = x12
                yy8 = y8
                yy12 = y12
                Bandera = 34
                Bandera2 = 0

                print('Z')
            else:
                if Bandera == 24:
                    pass

        return Bandera

def main():

    _Left = Coordinates()


if __name__ == "__main__":
    main()
