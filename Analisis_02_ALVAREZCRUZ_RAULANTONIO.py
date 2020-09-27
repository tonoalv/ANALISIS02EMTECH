import Defs as dfs
lista_prin = []
  
print("*****     Bienvenido *****")
print("**     Synergy Logistics  ****")

pase = input("Presiona cualquier tecla para continuar")

opcion = 1
while opcion != 0:
  opcion = dfs.opcion_menu()
  if opcion == 1: #ImprtacionesExportaciones
    dfs.submenu()
    opcion_submenu = int(input("\nSelecciona la opción que deseas ver"))
    if opcion_submenu == 1:
      dfs.dinero2("Imports")
    if opcion_submenu == 2:
      dfs.dinero2("Exports")
  if opcion == 2: #Rutas
    dfs.submenu()
    opcion_menu2 = int(input("\nSelecciona la opción que deseas ver"))
    if opcion_menu2 == 1:
      dfs.rutas("Imports")
    if opcion_menu2 == 2:
      dfs.rutas("Exports")
  if opcion == 3: #Transporte
    dfs.submenu()
    opcion_menu2 = int(input("\nSelecciona la opción que deseas ver"))
    if opcion_menu2 == 1:
      dfs.transporte("Imports")
    if opcion_menu2 == 2:
      dfs.transporte("Exports")

  if opcion == 4: #Transacciones
    dfs.impresion_transacciones()
  if opcion == 0:
    print("Has salido exitosamente")
print("Adiós")


