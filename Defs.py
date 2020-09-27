import csv
lista_prin = []
def opcion_menu ():
    print("\nAcciones disponibles")
    print("  1. Ver Importaciones y Exportaciones")
    print("  2. Ver Rutas")
    print("  3. Ver por medio de transporte")
    print("  4. Ver todas las transacciones")
    print("  0. Salir")
    opcion = int(input("Selecciona una opción del menu"))
    while opcion < 0 or opcion > 5:
        print("Respuesta invalida. Intenta de nuevo")
        opcion = int(input("Selecciona una opcion del menu"))
    return opcion

def submenu():
  print("1.- Ver información de Importación")
  print("2.- Ver información de Exportación")

def transacciones():
      with open("synergy_logistics_database.csv", "r") as archivo_csv:
        lector = csv.reader(archivo_csv)
        for line in lector:
          lista_prin.append(line)
          print(line)

def rutas(transaccion):
  with open("synergy_logistics_database.csv", "r") as archivo_csv:
    lector = csv.reader(archivo_csv)
    for line in lector:
      lista_prin.append(line)
  contador = 0
  rutas_count = []
  counted = []
  suma = []
  for operacion in lista_prin:
    if operacion[1] == transaccion:
      ruta = [operacion[2], operacion[3]]
      if ruta not in rutas_count:
        for entrada in lista_prin:
          if ruta == [entrada[2], entrada[3]]:
            contador += 1
        rutas_count.append(ruta)
        counted.append([operacion[2], operacion[3], contador])
        suma.append(contador)
        contador = 0
        
  counted.sort(key = lambda x:x [2], reverse = True)
  print(counted)
  print("\nN° de rutas: ", len(counted))
  print("\nTotal de transacciones: ", sum(suma))

  vermenos = input("Presiona '+' para ver sólo las 10 rutas más transitadas o '-' para las diez con menos tránsito")
  if vermenos == '+':
    print(counted[0:9])
  elif vermenos == '-':
    counted.sort(key = lambda x:x[2])
    print(counted[0:9])
  
def dinero2(transaccion):
  with open("synergy_logistics_database.csv", "r") as archivo_csv:
    lector = csv.reader(archivo_csv)
    for line in lector:
      lista_prin.append(line)
  contador = 0
  pais_count = []
  counted = []
  suma = []
  for operacion in lista_prin:
    if operacion[1] == transaccion:
      contador += 1
      if transaccion == "Imports":
        pais =  operacion[3]
      if transaccion == "Exports":
        pais = operacion[2]
      pais_count.append(pais)
      pais_set = set(pais_count)
      valor = int(operacion[9])
      suma.append(valor)
      counted.append(contador)
  contador = 0
        
  print("\n N° de paises", transaccion, ": ", len(pais_set))
  print("\nN° de", transaccion, ": ", len(counted))
  print("\n$ total de transacciones: ", "$",sum(suma))
  print("\n 1.- Ver",transaccion, "por paises \n 2.- Regresar al menu")
  vermas = int(input("Selecciona una opcion"))
  if vermas == 1:
    cuenta=dict(zip(list(pais_count),[list(pais_count).count(i) for i in list(pais_count)]))
    sortcuenta = sorted(cuenta.items(), key = lambda x:x[1], reverse = True)
    print(sortcuenta)
    print("\n \n 1.- Ver ingreso por país \n 2.- Volver al menú")
    nopcion = int(input("Selecciona una opción"))
    if nopcion == 1:
      contador = 0
      countmoney = []
      for operacion in lista_prin:
        if operacion[1] == transaccion:
          money = int(operacion[9])
          if transaccion == "Imports":
            pais =  operacion[3]
          if transaccion == "Exports":
            pais = operacion[2]
          freq = [pais, money]
          countmoney.append(freq)
      contador = 0
      final = [] 

      contador = 0
      for pais in pais_set:
        for accion in countmoney:
          if pais == accion[0]:
            contador += accion[1]      
        nf = [pais, "$",contador, round((contador*100)/sum(suma)),"%"]
        final.append(nf)
        contador = 0
      final.sort(key = lambda x:x[2], reverse = True)
      print(final)
    
def transporte(transaccion):
  with open("synergy_logistics_database.csv", "r") as archivo_csv:
    lector = csv.reader(archivo_csv)   
    for line in lector:
      lista_prin.append(line)
  contador = 0
  transcount = []
  ingreso = []
  suma = []
  for operacion in lista_prin:
    if operacion[1] == transaccion:
      contador += 1
      money = int(operacion[9])
      if transaccion == "Imports":
        m_de_t =  operacion[-3]
      if transaccion == "Exports":
        m_de_t = operacion[-3]
      valor = int(operacion[9])
      suma.append(valor)
      freq = [m_de_t, money]
      transcount.append(m_de_t)
      ingreso.append(freq)
  print("\nTotal de ",transaccion,": ",len(transcount))
  cuenta=dict(zip(list(transcount),[list(transcount).count(i) for i in list(transcount)]))
  sortcuenta = sorted(cuenta.items(), key = lambda x:x[1], reverse = True)
  print("\n",sortcuenta)
  dets = input("\n Presiona + para ver detalles de ingreso por medio de transporte\n")
  if dets == "+":
    final = []
    contador = 0
    transporte_set = set(transcount)
    for i in transporte_set:
      for a in ingreso:
        if i == a[0]:
         contador += a[1]
      nf = [i, "$",contador, round((contador*100)/sum(suma)),"%"] 
      final.append(nf)
      contador = 0
    final.sort(key=lambda x:x[2], reverse = True)
    print("\n",final)
