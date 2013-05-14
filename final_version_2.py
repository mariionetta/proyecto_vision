import Image, math, cv

def deteccion(im):
    img = Image.open(im)
    pixeles = img.load()
    x = img.size[0]
    y = img.size[1]
    
    filtro(img, pixeles, x, y)
    convolucion(img, pixeles, x, y)
    normaliza(img, pixeles, x, y)
    saca_angulo(img, pixeles, x, y)
    img.show()

def filtro(img, pixeles, x, y):
    pixeles_copy = (img.copy()).load()
    nimg = 'cuadrado1.jpg'
    for i in range(x):
        for j in range(y):
            temporal = []
            for k in range(i-1, i+2):
                for l in range(j-1, j+2):
                    if k >= 0 and l >= 0 and k < x and l < y:
                        temporal.append(pixeles_copy[i,j][0])
            temporal.sort()
            r = g = b = int(temporal[int(len(temporal)/5)])
            pixeles[i,j] = (r, g, b)
    img.save(nimg)

def convolucion(img, pixeles, x, y):
    nimg = 'cuadrado1.jpg'
    tam = dict()
    ancho = x
    largo = y
    gr = gradiente()
    sx = gr.get(0)
    sy = gr.get(1)
    for i in range(x):
        for j in range(y):
            gx = 0
            gy = 0
            for k in range(len(sx[0])):
                for l in range(len(sy[0])):
                    try:
                        gx += (pixeles[k+i, l+j][0] * sx[k][l])
                        gy += (pixeles[k+i, l+j][0] * sy[k][l])
                    except:
                        pass
                    Gradientex = pow(gx, 2)
                    Gradientey = pow(gy, 2)
                    magnitud = int(math.sqrt(Gradientex + Gradientey))
                    angulo = math.atan2(gy, gx)
                    rpo = ((i - ancho / 2) * math.sin(angulo)) + (j - largo / 2) * (math.cos(angulo))
                    tam[i,j] = (angulo, rpo)
            pixeles[i,j] = (magnitud, magnitud, magnitud)
    img.save(nimg)
    return tam


def gradiente():
    d = dict()
    d[0] = [ [-1,0,1], [-2,0,2], [-1,0,1] ]
    d[1] = [ [1,2,1], [0,0,0], [-1,-2,-1] ]
    return d

def saca_angulo(img, pixeles, x, y):
    tam = convolucion(img, pixeles, x, y)
    for i in range(x):
        for j in range(y):
            angulo = tam[i,j][0]

def normaliza(img, pixeles, x, y):
    nimg = 'cuadrado1.jpg'
    img.save(nimg)
             
def main():
    cam=cv.CaptureFromCAM(0)
    while True:
        im =cv.QueryFrame(cam)
        snapshot = im
        image_size = cv.GetSize(snapshot)
        cv.SaveImage("test.png",im)
        imagen = cv.CreateImage(image_size,cv.IPL_DEPTH_8U,3)
        print 'imagen',imagen
        deteccion("test.png")
    #print im
        cv.ShowImage('Camara', snapshot)
        if cv.WaitKey(30)==27:
            break
main()
