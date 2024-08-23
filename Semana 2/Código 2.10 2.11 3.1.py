# 2.10

class Modista:
    def __init__(self, metros):
        self.metros  = metros
        
        # constantes
        self.PULGADA = 0.0254
        self.METRO = 39.37
        
    def determinarPulgadasNecesarias(self):
        pulgadasNecesarias = 0
        pulgadasNecesarias = self.metros / self.PULGADA
        return pulgadasNecesarias

    # metodo extra, pasa de pulgadas a metros    
    def pasarPulgadasA_metros(self, nPulgadas):
        nMetros = 0
        nMetros = nPulgadas / self.METRO
        return nMetros
    
test = Modista(45)
print(test.determinarPulgadasNecesarias())
print(test.pasarPulgadasA_metros(1771.6535433070867))

# 2.11

def calcularMetrosCubicosAlberca(ancho, largo, profundidad):
    precioPorMetroCubico = 5600
    
    volumenAlberca = ancho * largo * profundidad
    precioTotalPagar = volumenAlberca * precioPorMetroCubico
    return precioTotalPagar

print(calcularMetrosCubicosAlberca(4, 7, 2))

# 3.1

def cualEsMayor(valorA, valorB):
    if valorA > valorB:
        return valorA
    elif valorB > valorA:
        return valorB
    else:
        return "Los valores son iguales"
    
print(cualEsMayor(5, 6))
print(cualEsMayor(7, 6))
print(cualEsMayor(5, 5))
    