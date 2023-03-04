# Importamos la librería datetime para trabajar con fechas y horas
import datetime

# Creamos una lista vacía para almacenar los datos de las bandas
bandas = []

# Definimos una función para agregar las bandas a la lista
def agregar_banda():
  # Solicitamos los datos de la banda al usuario
  nombre = input("Ingrese el nombre de la banda: ")
  hora_inicio = input("Ingrese la hora de inicio en formato HH:MM AM/PM: ")
  hora_fin = input("Ingrese la hora de fin en formato HH:MM AM/PM: ")
  escenario = input("Ingrese el nombre del escenario: ")
  
  # Convertimos las horas a formato de 24 horas para facilitar la comparación
  hora_inicio_24 = datetime.datetime.strptime(hora_inicio, "%I:%M %p").strftime("%H:%M")
  hora_fin_24 = datetime.datetime.strptime(hora_fin, "%I:%M %p").strftime("%H:%M")
  
  # Agregamos los datos de la banda a la lista
  bandas.append({"nombre": nombre, "hora_inicio": hora_inicio_24, "hora_fin": hora_fin_24, "escenario": escenario})

# Solicitamos al usuario que ingrese los datos de las bandas
while True:
  agregar = input("Desea agregar una banda? (si/no): ")
  if agregar.lower() == "si":
    agregar_banda()
  else:
    break

# Ordenamos las bandas por hora de inicio
bandas.sort(key=lambda x: x["hora_inicio"])

# Creamos un diccionario para almacenar las bandas por escenario
horarios_por_escenario = {}

# Recorremos la lista de bandas y las agrupamos por escenario
for banda in bandas:
  if banda["escenario"] in horarios_por_escenario:
    horarios_por_escenario[banda["escenario"]].append(banda)
  else:
    horarios_por_escenario[banda["escenario"]] = [banda]

# Creamos un archivo .txt para guardar el horario
with open("horarioVL2023.txt", "w") as archivo:
  # Recorremos los horarios por escenario y los escribimos en el archivo
  for escenario, bandas in horarios_por_escenario.items():
    archivo.write(f"{escenario}\n")
    for i, banda in enumerate(bandas):
      archivo.write(f"{banda['hora_inicio']} - {banda['hora_fin']}: {banda['nombre']}\n")
      # Buscamos las bandas que se empalman con la actual
      for j in range(i + 1, len(bandas)):
        if bandas[j]["hora_inicio"] < banda["hora_fin"]:
          archivo.write(f"  Empalma con: {bandas[j]['nombre']} en {bandas[j]['escenario']}\n")
    archivo.write("\n")
