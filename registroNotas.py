from alumnos import alumnos
from os import system, name

def clear():
  # windows
  if name == 'nt':
    _ = system('cls')
  # mac/linux
  else:
    _ = system('clear')

class sistema:
  def __init__(self):
    self.comando = None
    self.comandosValidos = ["R","C","P","S","X"]
    self.alumnos = []
    self.anchoPantalla = 40
    self.estadoActual = True

  def pantallaPrincipal(self):
    print("╔"+"═"*(self.anchoPantalla-2)+"╗")
    print("║"+"Bienvenidos al registro de notas".center(self.anchoPantalla-2)+"║")
    print("╚"+"═"*(self.anchoPantalla-2)+"╝")
    print()
    print("Comandos disponibles:")
    print("> R : Registrar alumnos")
    print("> C : Calificar a los alumnos")
    print("> P : Promedio de los alumnos")
    print("> S : Suma de notas de los alumnos")
    print("> X : Salida")
    print()
    self.comando = input("ingrese Comando Valido:")
    return

  def registrarAlumnos(self):
    print("╔"+"═"*(self.anchoPantalla-2)+"╗")
    print("║"+"Registro de Alumnos".center(self.anchoPantalla-2)+"║")
    print("╚"+"═"*(self.anchoPantalla-2)+"╝")
    print()
    nombre = input("ingrese el nombre del alumno:")
    apellido = input("ingrese el apellido del alumno:")
    edad = input("ingrese la edad del alumno:")
    nacionalidad = input("ingrese la nacionalidad del alumno:")
    self.alumnos.append(alumnos(nombre,apellido,edad,0,nacionalidad))
    clear()
    print("╔"+"═"*(self.anchoPantalla-2)+"╗")
    print("║"+"Registro de Alumnos".center(self.anchoPantalla-2)+"║")
    print("╚"+"═"*(self.anchoPantalla-2)+"╝")
    print()
    print(f"El alumno {nombre}, {apellido} a sido registrado")
    print()
    self.comando = input("ingrese Comando Valido:")
    return
  
  def calificarAlumnos(self):
    print("╔"+"═"*(self.anchoPantalla-2)+"╗")
    print("║"+"Calificacion de Alumnos".center(self.anchoPantalla-2)+"║")
    print("╚"+"═"*(self.anchoPantalla-2)+"╝")
    print()
    if len(self.alumnos) == 0:
      print("no hay alumnos registrados")
    else:
      for alumno in self.alumnos:
        nota = 0
        while True:
          nota = input(f"Alumno {alumno.nombre}, {alumno.apellido} , Ingrese nota:")
          try:
            nota = float(nota)
            if nota >= 0 and nota <= 20:
              break
            else:
              pass
          except:
            pass
        alumno.registrarNota(nota)
    print()
    self.comando = input("ingrese Comando Valido:")
    return
  
  def promedioAlumnos(self):
    print("╔"+"═"*(self.anchoPantalla-2)+"╗")
    print("║"+"Promedio de Alumnos".center(self.anchoPantalla-2)+"║")
    print("╚"+"═"*(self.anchoPantalla-2)+"╝")
    print()
    if len(self.alumnos) == 0:
      print("no hay alumnos registrados")
    else:
      promedio = 0
      numeroAlumnos = len(self.alumnos)
      for alumno in self.alumnos:
        promedio += alumno.leerNota()
      promedio /= numeroAlumnos
      print(f"El promedio de notas para {numeroAlumnos} alumnos es : {promedio}")
    self.comando = input("ingrese Comando Valido:")
    return
  
  def sumaAlumnos(self):
    print("╔"+"═"*(self.anchoPantalla-2)+"╗")
    print("║"+"Suma de notas de Alumnos".center(self.anchoPantalla-2)+"║")
    print("╚"+"═"*(self.anchoPantalla-2)+"╝")
    print()
    if len(self.alumnos) == 0:
      print("no hay alumnos registrados")
    else:
      suma = 0
      numeroAlumnos = len(self.alumnos)
      for alumno in self.alumnos:
        suma += alumno.leerNota()
      print(f"La suma de notas para {numeroAlumnos} alumnos es : {suma}")
    self.comando = input("ingrese Comando Valido:")
    return

  def ejecutarSistema(self):
    self.pantallaPrincipal()
    clear()
    while self.estadoActual:
      if self.comando in self.comandosValidos:
        if self.comando == "R":
          self.registrarAlumnos()
        elif self.comando == "C":
          self.calificarAlumnos()
        elif self.comando == "P":
          self.promedioAlumnos()
        elif self.comando == "S":
          self.sumaAlumnos()
        elif self.comando == "X":
          self.estadoActual = False
        clear()
      else:
        self.pantallaPrincipal()
        clear()
      
if __name__ == '__main__':
  sis = sistema()
  sis.ejecutarSistema()



