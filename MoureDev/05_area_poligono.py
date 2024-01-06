def calculateArea(polygon):
  if polygon.type == 'square' or polygon.type == 'rectangle':
    return polygon.width * polygon.hight
  else:
    return (polygon.width * polygon.hight) / 2


class Polygon:
  def __init__(self, width, hight, type):
    self.width = int(width)
    self.hight = int(hight)
    self.type = type
  

if __name__ == '__main__':

  print('Bienvenido \n')
  opc = input('Poligono \n1. Cuadrado, \n2. Rectangulo \n3. Triangulo \n')
  typeP = 'square' if opc == '1' else 'rectangle' if opc == '2' else 'triangle' 
  hight = input('Altura: ')
  if typeP != 'square':
    width = input('Anchura: ')
  else:
    width = hight
  print('El área del ',typeP,' es: ',calculateArea(Polygon(width, hight,typeP)))

