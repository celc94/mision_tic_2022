from pydoc import doc


class Datos:
    #Método Constructor vacío
    def __init__(self, doc, nom, cla, rol):
        self.__documento=doc #Encapsulamiento
        self.__nombre=nom
        self.clave=cla
        self.rol=rol
    #Método Getter
    def obtdocumento(self):
        return self.__documento

    def obtnombre(self):
        return self.__nombre

da=Datos(123,'César','209','Cliente')
#da.__documento=200
print(da.obtdocumento())#Se obtiene el documento a través del método getter
print(da.obtnombre())
