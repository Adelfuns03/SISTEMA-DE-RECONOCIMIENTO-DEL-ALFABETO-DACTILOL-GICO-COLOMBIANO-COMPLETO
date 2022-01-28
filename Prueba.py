
from tkinter import *
from PIL import Image
from PIL import ImageTk
import cv2
import HandTrackingModule as htm
import Right as _Right
import Left as _Left
import Images as _Images
import pytesseract
import imutils
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
detector = htm.handDetector(detectionCon=0.75)
HandRight = _Right.Coordinates()
HandLeft = _Left.Coordinates()
Images = _Images.Images()
Hand = 1 # 1- Derecha 0- Izquierda
Contador = 0
Visualizacion = ""

def video_de_entrada():
    global cap
    cap = cv2.VideoCapture(0)
    visualizar()

def RightHand ():
    global Hand
    Hand = 1

def LeftHand ():
    global Hand
    Hand = 0

def Clean ():
    global Visualizacion
    Visualizacion = ""

def visualizar():

    global cap, Bandera, Hand, FolderPath, Contador, Visualizacion

    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    kernel = np.ones((5, 5), np.float32) / 50
    frame = cv2.filter2D(frame, -1, kernel)
    frame = cv2.GaussianBlur(frame, (1, 1), 0)
    frame = cv2.addWeighted(frame, 1, np.zeros(frame.shape, frame.dtype), 0, 0)


    #fingers = detector.fingersUp()

    if Hand == 1 and Contador == 0:
        lblButtonRight.configure(bg='gray68')
        lblButtonLeft.configure(bg='gray94')
        Bandera = HandRight.Right(frame)
        FolderPath, _Vis = Images.Image(Bandera)
        if Bandera >= 1 and Bandera != 33 and Bandera != 32 and Bandera != 31 and Bandera != 9 and Contador == 0:
            Contador = 1
            Visualizacion = Visualizacion + _Vis

    if Hand == 0 and Contador == 0 :
        lblButtonRight.configure(bg='gray94')
        lblButtonLeft.configure(bg='gray68')
        Bandera = HandLeft.Left(frame)
        FolderPath, _Vis = Images.Image(Bandera)
        if Bandera >= 1 and Bandera != 33 and Bandera != 32 and Bandera != 31 and Bandera != 9 and Contador == 0:
            Contador = 1
            Visualizacion = Visualizacion + _Vis


    #frame = detector.findHands(frame)
    if ret == True:

        if Contador >= 1:
            Contador = Contador + 1
        if Contador >= 50:
            Contador = 0
            Bandera = 0
        else:
            pass

        frame = imutils.resize(frame, width=600)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(frame)
        img = ImageTk.PhotoImage(image=im)
        lblVideo.configure(image=img)
        lblVideo.image = img
        lblVideo.after(10, visualizar)

        imgAlfabeto = cv2.imread(f'{FolderPath}')
        imgAlfabeto = cv2.cvtColor(imgAlfabeto, cv2.COLOR_BGR2RGB)
        res2 = cv2.resize(imgAlfabeto, dsize=(170, 210), interpolation=cv2.INTER_CUBIC)
        imAlfabeto = Image.fromarray(res2)
        imAlfabeto = ImageTk.PhotoImage(image=imAlfabeto)
        lblImageAlfabeto.configure(image = imAlfabeto)
        lblImageAlfabeto.image = imAlfabeto

        lblVisualizacion.configure(text=f'{Visualizacion}')

    else:
        lblVideo.image = ""
        selected.set(0)
        cap.release()


cap = None
root = Tk()

imgUD = cv2.imread('logo.jpg')
res = cv2.resize(imgUD, dsize=(105, 100), interpolation=cv2.INTER_CUBIC)
imUD = Image.fromarray(res)
imUD = ImageTk.PhotoImage(image=imUD)

root.title("Sistema de reconocimiento del alfabeto dactilológico Colombiano completo por medio de visión artificial")
root.geometry("805x660")
root.configure(bg='white')


lblVideo = Label(root)
lblVideo.place(x=10, y=135)
lblVideo.configure(bg='white')

lblTitle = Label(root,text="Alfabeto Dactilológico Colombiano", font=("bold",28), borderwidth = 1, relief ="ridge")
lblTitle.place(x=10, y=10, width =785, height = 115 )
lblTitle.configure(bg='white')

lblImageAlfabeto = Label(root, borderwidth = 1, relief ="ridge")
lblImageAlfabeto.place(x=623, y=375)
lblImageAlfabeto.configure(bg='white')

lblLabelV = Label(root,text='Mensaje actual', font=("bold",18))
lblLabelV.place(x=623, y=136, width =172, height = 70 )
lblLabelV.configure(bg='white')

lblVisualizacion = Label(root,borderwidth = 1,relief="sunken", font=("bold",24))
lblVisualizacion.place(x=623, y=216, width =172, height = 130 )
lblVisualizacion.configure(bg='white')

lblImageUD = Label(root, image = imUD)
lblImageUD.place(x=15, y=15)
lblImageUD.configure(bg='white')

lblButtonRight = Button(root, text = "Mano derecha", command=RightHand, font=("bold", 18))
lblButtonRight.place(x=11,y=600,width=188, height=35)

lblButtonLeft = Button(root, text = "Mano izquierda", command=LeftHand, font=("bold", 18))
lblButtonLeft.place(x=209,y=600,width=188, height=35)

lblButtonClean = Button(root, text = "Limpiar", command=Clean, font=("bold", 18))
lblButtonClean.place(x=605,y=600,width=188, height=35)

def Menu():

    VentanaMenu = Toplevel()
    VentanaMenu.title("Alfabeto dactilológico Colombiano ")
    VentanaMenu.geometry("890x610")
    VentanaMenu.resizable(120,939)
    VentanaMenu.configure(bg="white")

    lblTitle = Label(VentanaMenu, text="Alfabeto Dactilológico Colombiano", font=("bold", 16))
    lblTitle.place(x=10, y=0, width=870, height=40)
    lblTitle.configure(bg='white')

    lblImageA = Label(VentanaMenu, borderwidth=1, relief="ridge")
    lblImageA.place(x=10, y=45)
    lblImageA.configure(bg='white')

    lblImageB = Label(VentanaMenu, borderwidth=1, relief="ridge")
    lblImageB.place(x=135, y=45)
    lblImageB.configure(bg='white')

    lblImageC = Label(VentanaMenu, borderwidth=1, relief="ridge")
    lblImageC.place(x=260, y=45)
    lblImageC.configure(bg='white')

    lblImageD = Label(VentanaMenu, borderwidth=1, relief="ridge")
    lblImageD.place(x=385, y=45)
    lblImageD.configure(bg='white')

    lblImageE = Label(VentanaMenu, borderwidth=1, relief="ridge")
    lblImageE.place(x=510, y=45)
    lblImageE.configure(bg='white')

    lblImageF = Label(VentanaMenu, borderwidth=1, relief="ridge")
    lblImageF.place(x=635, y=45)
    lblImageF.configure(bg='white')

    lblImageG = Label(VentanaMenu, borderwidth=1, relief="ridge")
    lblImageG.place(x=760, y=45)
    lblImageG.configure(bg='white')
##
    lblImageH = Label(VentanaMenu, borderwidth=1, relief="ridge")
    lblImageH.place(x=10, y=185)
    lblImageH.configure(bg='white')

    lblImageI = Label(VentanaMenu, borderwidth=1, relief="ridge")
    lblImageI.place(x=135, y=185)
    lblImageI.configure(bg='white')

    lblImageJ = Label(VentanaMenu, borderwidth=1, relief="ridge")
    lblImageJ.place(x=260, y=185)
    lblImageJ.configure(bg='white')

    lblImageK = Label(VentanaMenu, borderwidth=1, relief="ridge")
    lblImageK.place(x=385, y=185)
    lblImageK.configure(bg='white')

    lblImageL = Label(VentanaMenu, borderwidth=1, relief="ridge")
    lblImageL.place(x=510, y=185)
    lblImageL.configure(bg='white')

    lblImageM = Label(VentanaMenu, borderwidth=1, relief="ridge")
    lblImageM.place(x=635, y=185)
    lblImageM.configure(bg='white')

    lblImageN = Label(VentanaMenu, borderwidth=1, relief="ridge")
    lblImageN.place(x=760, y=185)
    lblImageN.configure(bg='white')
##

    lblImageNN = Label(VentanaMenu, borderwidth=1, relief="ridge")
    lblImageNN.place(x=10, y=325)
    lblImageNN.configure(bg='white')

    lblImageO = Label(VentanaMenu, borderwidth=1, relief="ridge")
    lblImageO.place(x=135, y=325)
    lblImageO.configure(bg='white')

    lblImageP = Label(VentanaMenu, borderwidth=1, relief="ridge")
    lblImageP.place(x=260, y=325)
    lblImageP.configure(bg='white')

    lblImageQ = Label(VentanaMenu, borderwidth=1, relief="ridge")
    lblImageQ.place(x=385, y=325)
    lblImageQ.configure(bg='white')

    lblImageR = Label(VentanaMenu, borderwidth=1, relief="ridge")
    lblImageR.place(x=510, y=325)
    lblImageR.configure(bg='white')

    lblImageS = Label(VentanaMenu, borderwidth=1, relief="ridge")
    lblImageS.place(x=635, y=325)
    lblImageS.configure(bg='white')

    lblImageT = Label(VentanaMenu, borderwidth=1, relief="ridge")
    lblImageT.place(x=760, y=325)
    lblImageT.configure(bg='white')

##

    lblImageU = Label(VentanaMenu, borderwidth=1, relief="ridge")
    lblImageU.place(x=10, y=465)
    lblImageU.configure(bg='white')

    lblImageV = Label(VentanaMenu, borderwidth=1, relief="ridge")
    lblImageV.place(x=135, y=465)
    lblImageV.configure(bg='white')

    lblImageW = Label(VentanaMenu, borderwidth=1, relief="ridge")
    lblImageW.place(x=260, y=465)
    lblImageW.configure(bg='white')

    lblImageX = Label(VentanaMenu, borderwidth=1, relief="ridge")
    lblImageX.place(x=385, y=465)
    lblImageX.configure(bg='white')

    lblImageY = Label(VentanaMenu, borderwidth=1, relief="ridge")
    lblImageY.place(x=510, y=465)
    lblImageY.configure(bg='white')

    lblImageZ = Label(VentanaMenu, borderwidth=1, relief="ridge")
    lblImageZ.place(x=635, y=465)
    lblImageZ.configure(bg='white')

    imgA = cv2.imread('Figuras/a.JPG')
    imgA = cv2.cvtColor(imgA, cv2.COLOR_BGR2RGB)
    resA = cv2.resize(imgA, dsize=(120, 130), interpolation=cv2.INTER_CUBIC)
    imA = Image.fromarray(resA)
    imA = ImageTk.PhotoImage(image=imA)
    lblImageA.configure(image=imA)
    lblImageA.image = imA

    imgB = cv2.imread('Figuras/b.JPG')
    imgB = cv2.cvtColor(imgB, cv2.COLOR_BGR2RGB)
    resB = cv2.resize(imgB, dsize=(120, 130), interpolation=cv2.INTER_CUBIC)
    imB = Image.fromarray(resB)
    imB = ImageTk.PhotoImage(image=imB)
    lblImageB.configure(image=imB)
    lblImageB.image = imB

    imgC = cv2.imread('Figuras/c.JPG')
    imgC = cv2.cvtColor(imgC, cv2.COLOR_BGR2RGB)
    resC = cv2.resize(imgC, dsize=(120, 130), interpolation=cv2.INTER_CUBIC)
    imC = Image.fromarray(resC)
    imC = ImageTk.PhotoImage(image=imC)
    lblImageC.configure(image=imC)
    lblImageC.image = imC

    imgD = cv2.imread('Figuras/d.JPG')
    imgD = cv2.cvtColor(imgD, cv2.COLOR_BGR2RGB)
    resD = cv2.resize(imgD, dsize=(120, 130), interpolation=cv2.INTER_CUBIC)
    imD = Image.fromarray(resD)
    imD = ImageTk.PhotoImage(image=imD)
    lblImageD.configure(image=imD)
    lblImageD.image = imD

    imgE = cv2.imread('Figuras/e.JPG')
    imgE = cv2.cvtColor(imgE, cv2.COLOR_BGR2RGB)
    resE = cv2.resize(imgE, dsize=(120, 130), interpolation=cv2.INTER_CUBIC)
    imE = Image.fromarray(resE)
    imE = ImageTk.PhotoImage(image=imE)
    lblImageE.configure(image=imE)
    lblImageE.image = imE

    imgF = cv2.imread('Figuras/f.JPG')
    imgF = cv2.cvtColor(imgF, cv2.COLOR_BGR2RGB)
    resF = cv2.resize(imgF, dsize=(120, 130), interpolation=cv2.INTER_CUBIC)
    imF = Image.fromarray(resF)
    imF = ImageTk.PhotoImage(image=imF)
    lblImageF.configure(image=imF)
    lblImageF.image = imF

    imgG = cv2.imread('Figuras/g.JPG')
    imgG = cv2.cvtColor(imgG, cv2.COLOR_BGR2RGB)
    resG = cv2.resize(imgG, dsize=(120, 130), interpolation=cv2.INTER_CUBIC)
    imG = Image.fromarray(resG)
    imG = ImageTk.PhotoImage(image=imG)
    lblImageG.configure(image=imG)
    lblImageG.image = imG

    imgH = cv2.imread('Figuras/h.JPG')
    imgH = cv2.cvtColor(imgH, cv2.COLOR_BGR2RGB)
    resH = cv2.resize(imgH, dsize=(120, 130), interpolation=cv2.INTER_CUBIC)
    imH = Image.fromarray(resH)
    imH = ImageTk.PhotoImage(image=imH)
    lblImageH.configure(image=imH)
    lblImageH.image = imH

    imgI = cv2.imread('Figuras/i.JPG')
    imgI = cv2.cvtColor(imgI, cv2.COLOR_BGR2RGB)
    resI = cv2.resize(imgI, dsize=(120, 130), interpolation=cv2.INTER_CUBIC)
    imI = Image.fromarray(resI)
    imI = ImageTk.PhotoImage(image=imI)
    lblImageI.configure(image=imI)
    lblImageI.image = imI

    imgJ = cv2.imread('Figuras/j.JPG')
    imgJ = cv2.cvtColor(imgJ, cv2.COLOR_BGR2RGB)
    resJ = cv2.resize(imgJ, dsize=(120, 130), interpolation=cv2.INTER_CUBIC)
    imJ = Image.fromarray(resJ)
    imJ = ImageTk.PhotoImage(image=imJ)
    lblImageJ.configure(image=imJ)
    lblImageJ.image = imJ

    imgK = cv2.imread('Figuras/k.JPG')
    imgK = cv2.cvtColor(imgK, cv2.COLOR_BGR2RGB)
    resK = cv2.resize(imgK, dsize=(120, 130), interpolation=cv2.INTER_CUBIC)
    imK = Image.fromarray(resK)
    imK = ImageTk.PhotoImage(image=imK)
    lblImageK.configure(image=imK)
    lblImageK.image = imK

    imgL = cv2.imread('Figuras/l.JPG')
    imgL = cv2.cvtColor(imgL, cv2.COLOR_BGR2RGB)
    resL = cv2.resize(imgL, dsize=(120, 130), interpolation=cv2.INTER_CUBIC)
    imL = Image.fromarray(resL)
    imL = ImageTk.PhotoImage(image=imL)
    lblImageL.configure(image=imL)
    lblImageL.image = imL

    imgM = cv2.imread('Figuras/m.JPG')
    imgM = cv2.cvtColor(imgM, cv2.COLOR_BGR2RGB)
    resM = cv2.resize(imgM, dsize=(120, 130), interpolation=cv2.INTER_CUBIC)
    imM = Image.fromarray(resM)
    imM = ImageTk.PhotoImage(image=imM)
    lblImageM.configure(image=imM)
    lblImageM.image = imM

    imgN = cv2.imread('Figuras/n.JPG')
    imgN = cv2.cvtColor(imgN, cv2.COLOR_BGR2RGB)
    resN = cv2.resize(imgN, dsize=(120, 130), interpolation=cv2.INTER_CUBIC)
    imN = Image.fromarray(resN)
    imN = ImageTk.PhotoImage(image=imN)
    lblImageN.configure(image=imN)
    lblImageN.image = imN

    imgNN = cv2.imread('Figuras/nn.JPG')
    imgNN = cv2.cvtColor(imgNN, cv2.COLOR_BGR2RGB)
    resNN = cv2.resize(imgNN, dsize=(120, 130), interpolation=cv2.INTER_CUBIC)
    imNN = Image.fromarray(resNN)
    imNN = ImageTk.PhotoImage(image=imNN)
    lblImageNN.configure(image=imNN)
    lblImageNN.image = imNN

    imgO = cv2.imread('Figuras/o.jpg')
    imgO = cv2.cvtColor(imgO, cv2.COLOR_BGR2RGB)
    resO = cv2.resize(imgO, dsize=(120, 130), interpolation=cv2.INTER_CUBIC)
    imO = Image.fromarray(resO)
    imO = ImageTk.PhotoImage(image=imO)
    lblImageO.configure(image=imO)
    lblImageO.image = imO

    imgP = cv2.imread('Figuras/p.jpg')
    imgP = cv2.cvtColor(imgP, cv2.COLOR_BGR2RGB)
    resP = cv2.resize(imgP, dsize=(120, 130), interpolation=cv2.INTER_CUBIC)
    imP = Image.fromarray(resP)
    imP = ImageTk.PhotoImage(image=imP)
    lblImageP.configure(image=imP)
    lblImageP.image = imP

    imgQ = cv2.imread('Figuras/q.jpg')
    imgQ = cv2.cvtColor(imgQ, cv2.COLOR_BGR2RGB)
    resQ = cv2.resize(imgQ, dsize=(120, 130), interpolation=cv2.INTER_CUBIC)
    imQ = Image.fromarray(resQ)
    imQ = ImageTk.PhotoImage(image=imQ)
    lblImageQ.configure(image=imQ)
    lblImageQ.image = imQ

    imgR = cv2.imread('Figuras/r.jpg')
    imgR = cv2.cvtColor(imgR, cv2.COLOR_BGR2RGB)
    resR = cv2.resize(imgR, dsize=(120, 130), interpolation=cv2.INTER_CUBIC)
    imR = Image.fromarray(resR)
    imR = ImageTk.PhotoImage(image=imR)
    lblImageR.configure(image=imR)
    lblImageR.image = imR

    imgS = cv2.imread('Figuras/s.jpg')
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    resS = cv2.resize(imgS, dsize=(120, 130), interpolation=cv2.INTER_CUBIC)
    imS = Image.fromarray(resS)
    imS = ImageTk.PhotoImage(image=imS)
    lblImageS.configure(image=imS)
    lblImageS.image = imS

    imgT = cv2.imread('Figuras/t.jpg')
    imgT = cv2.cvtColor(imgT, cv2.COLOR_BGR2RGB)
    resT = cv2.resize(imgT, dsize=(120, 130), interpolation=cv2.INTER_CUBIC)
    imT = Image.fromarray(resT)
    imT = ImageTk.PhotoImage(image=imT)
    lblImageT.configure(image=imT)
    lblImageT.image = imT

    imgU = cv2.imread('Figuras/u.jpg')
    imgU = cv2.cvtColor(imgU, cv2.COLOR_BGR2RGB)
    resU = cv2.resize(imgU, dsize=(120, 130), interpolation=cv2.INTER_CUBIC)
    imU = Image.fromarray(resU)
    imU = ImageTk.PhotoImage(image=imU)
    lblImageU.configure(image=imU)
    lblImageU.image = imU

    imgV = cv2.imread('Figuras/v.jpg')
    imgV = cv2.cvtColor(imgV, cv2.COLOR_BGR2RGB)
    resV = cv2.resize(imgV, dsize=(120, 130), interpolation=cv2.INTER_CUBIC)
    imV = Image.fromarray(resV)
    imV = ImageTk.PhotoImage(image=imV)
    lblImageV.configure(image=imV)
    lblImageV.image = imV

    imgW = cv2.imread('Figuras/w.JPG')
    imgW = cv2.cvtColor(imgW, cv2.COLOR_BGR2RGB)
    resW = cv2.resize(imgW, dsize=(120, 130), interpolation=cv2.INTER_CUBIC)
    imW = Image.fromarray(resW)
    imW = ImageTk.PhotoImage(image=imW)
    lblImageW.configure(image=imW)
    lblImageW.image = imW

    imgX = cv2.imread('Figuras/x.JPG')
    imgX = cv2.cvtColor(imgX, cv2.COLOR_BGR2RGB)
    resX = cv2.resize(imgX, dsize=(120, 130), interpolation=cv2.INTER_CUBIC)
    imX = Image.fromarray(resX)
    imX = ImageTk.PhotoImage(image=imX)
    lblImageX.configure(image=imX)
    lblImageX.image = imX

    imgY = cv2.imread('Figuras/y.jpg')
    imgY = cv2.cvtColor(imgY, cv2.COLOR_BGR2RGB)
    resY = cv2.resize(imgY, dsize=(120, 130), interpolation=cv2.INTER_CUBIC)
    imY = Image.fromarray(resY)
    imY = ImageTk.PhotoImage(image=imY)
    lblImageY.configure(image=imY)
    lblImageY.image = imY

    imgZ = cv2.imread('Figuras/z.jpg')
    imgZ = cv2.cvtColor(imgZ, cv2.COLOR_BGR2RGB)
    resZ = cv2.resize(imgZ, dsize=(120, 130), interpolation=cv2.INTER_CUBIC)
    imZ = Image.fromarray(resZ)
    imZ = ImageTk.PhotoImage(image=imZ)
    lblImageZ.configure(image=imZ)
    lblImageZ.image = imZ

lblButtonMenu = Button(root, text = "Alfabeto", font=("bold", 18), command=Menu)
lblButtonMenu.place(x=407,y=600,width=188, height=35)


selected = IntVar()
video_de_entrada()
root.mainloop()
