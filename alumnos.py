class alumnos:
  def __init__(self,nombre,apellido,edad,nota,nacionalidad):
    self.nombre = nombre
    self.apellido =apellido
    self.edad = edad
    self.nacionalidad = nacionalidad
    self.nota = nota
  def leerNota(self):
    return self.nota
  def registrarNota(self,notaAlumno):
    self.nota = notaAlumno