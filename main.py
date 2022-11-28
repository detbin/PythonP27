class vehiculo ():
    marca=''
    modelo=''
    color=''
    def __init__(self,marca,modelo,color):
        self.marca=marca
        self.modelo=modelo
        self.color=color

def main():
    f=open('vehiculo.txt','w')
    vehiculo1 = vehiculo('toyota','prius','blanco')
    f.write(vehiculo1.marca)
    f.write(' ')
    f.write(vehiculo1.modelo)
    f.write(' ')
    f.write(vehiculo1.color)
    f.write(' ')
    f.close()
    f=open('vehiculo.txt','r')
    datos=f.read()
    print (datos)
if __name__ == '__main__':
    main()