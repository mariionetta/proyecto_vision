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
