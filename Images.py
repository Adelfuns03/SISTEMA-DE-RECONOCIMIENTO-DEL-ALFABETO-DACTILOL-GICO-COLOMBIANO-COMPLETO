class Images():

    def Image(self, Bandera):
        folderPath = 'Figuras/blanco.jpg'
        Visualizacion = ''
        if Bandera == 1:  # A-a
            folderPath = 'Figuras/a.jpg'
            Visualizacion = 'a'
        elif Bandera == 2:  # B-b
            folderPath = 'Figuras/b.jpg'
            Visualizacion = 'b'
        elif Bandera == 3:  # C-c
            folderPath = 'Figuras/c.jpg'
            Visualizacion = 'c'
        elif Bandera == 4:  # D-d
            folderPath = 'Figuras/d.jpg'
            Visualizacion = 'd'
        elif Bandera == 5:  # E-e
            folderPath = 'Figuras/e.jpg'
            Visualizacion = 'e'
        elif Bandera == 6:  # F-f
            folderPath = 'Figuras/f.jpg'
            Visualizacion = 'f'
        elif Bandera == 8:  # G-g
            folderPath = 'Figuras/g.jpg'
            Visualizacion = 'g'
        elif Bandera == 10:  # H-h
            folderPath = 'Figuras/h.jpg'
            Visualizacion = 'h'
        elif Bandera == 11:  # I-i
            folderPath = 'Figuras/i.jpg'
            Visualizacion = 'i'
        elif Bandera == 13:  # J-j
            folderPath = 'Figuras/j.jpg'
            Visualizacion = 'j'
        elif Bandera == 14:  # K-k
            folderPath = 'Figuras/k.jpg'
            Visualizacion = 'k'
        elif Bandera == 15:  # L-l
            folderPath = 'Figuras/l.jpg'
            Visualizacion = 'l'
        elif Bandera == 16:  # M-m
            folderPath = 'Figuras/m.jpg'
            Visualizacion = 'm'
        elif Bandera == 17:  # N-n
            folderPath = 'Figuras/n.jpg'
            Visualizacion = 'n'
        elif Bandera == 19:  # Ñ-ñ
            folderPath = 'Figuras/nn.jpg'
            Visualizacion = 'ñ'
        elif Bandera == 20:  # O-o
            folderPath = 'Figuras/o.jpg'
            Visualizacion = 'o'
        elif Bandera == 21:  # P-p
            folderPath = 'Figuras/p.jpg'
            Visualizacion = 'p'
        elif Bandera == 22:  # Q-q
            folderPath = 'Figuras/q.jpg'
            Visualizacion = 'q'
        elif Bandera == 23:  # V-v
            folderPath = 'Figuras/v.jpg'
            Visualizacion = 'v'
        elif Bandera == 24:  # S-s
            folderPath = 'Figuras/s.jpg'
            Visualizacion = 's'
        elif Bandera == 25:  # T-t
            folderPath = 'Figuras/t.jpg'
            Visualizacion = 't'
        elif Bandera == 26:  # U-u
            folderPath = 'Figuras/u.jpg'
            Visualizacion = 'u'
        elif Bandera == 27:  # R-r
            folderPath = 'Figuras/r.jpg'
            Visualizacion = 'r'
        elif Bandera == 28:  # W-w
            folderPath = 'Figuras/w.jpg'
            Visualizacion = 'w'
        elif Bandera == 29:  # X-x
            folderPath = 'Figuras/x.jpg'
            Visualizacion = 'x'
        elif Bandera == 30:  # Y-y
            folderPath = 'Figuras/y.jpg'
            Visualizacion = 'y'
        elif Bandera == 34:  # Z-z
            folderPath = 'Figuras/z.jpg'
            Visualizacion = 'z'
        else:
            pass

        return folderPath, Visualizacion

def main():

    _Images = Images()


if __name__ == "__main__":
    main()
