#Mirka Monzon 18139
#Lab1 Filling any polygon 

from gl import Bitmap

bmp = Bitmap(600, 800)

def glInit():
    return bmp


if __name__ == '__main__':

    #Inicializa el .bmp
    bmp = glInit()

    #Todos los pixeles del mismo color
    bmp.glClear()

    #Indica el color a la estrella
    bmp.glColor(1, 0.93, 0.2)
    #Poligono 1 - estrella
    polygon_1 = ((165, 380), (185, 360), (180, 330), (207, 345), (233, 330), (230, 360), (250, 380), (220, 385), (205, 410), (193, 383))
    #Rellena la figura indicada
    bmp.glFillPolygon(polygon_1)

    #Indica el color al cuadrado
    bmp.glColor(0.2, 1, 0.87)
    #poligono 2 - cuadrado
    polygon_2 = ((321, 335), (288, 286), (339, 251), (374, 302))
    #Rellena la figura indicada
    bmp.glFillPolygon(polygon_2)

    #Indica el color al triangulo 
    bmp.glColor(0.2, 1, 0.26)
    #Poligono 3 - triangulo
    polygon_3 = ((377, 249), (411, 197), (436, 249))
    #Rellena la figura indicada
    bmp.glFillPolygon(polygon_3)

    #Indica el color a la tetera
    bmp.glColor(0, 0, 1)
    #Poligono 4 - tetera
    polygon_4 = ((413, 177), (448, 159), (502, 88), (553, 53), (535, 36), (676, 37), (660, 52), (750, 145), (761, 179), (672, 192), (659, 214), (615, 214), (632, 230), (580, 230), (597, 215), (552, 214), (517, 144), (466, 180))
    #Rellena la figura indicada
    bmp.glFillPolygon(polygon_4)

    #Indica el color al hoyo de la tetera
    bmp.glColor(0, 0, 0)
    #Poligono 5 - hoyo tetera
    polygon_5 = ((682, 175), (708, 120), (735, 148), (739, 170))
    #Rellena la figura indicada
    bmp.glFillPolygon(polygon_5)

    #Output BMP
    bmp.glWrite("out.bmp")