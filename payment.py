def calcularCuota(compra,tasa,plazo):
     if tasa == 0:
          i = 0
          return compra / plazo
     
     elif plazo == 1:
          i = 1
          return compra / plazo

     else:     
         i= tasa / 100
     return (compra * i) / (1 - (1 + i) ** (-plazo))