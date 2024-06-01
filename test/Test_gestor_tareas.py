import unittest
from src.logica.gestor_tareas import GestorTareas


class TestGestorTareas(unittest.TestCase):
 def setUp(self):
  self.gestor = GestorTareas()

  def test_agregar_tarea(self):
   self.gestor.agregar_tarea("Tarea 1", "Descripción de la tarea 1")

  self.assertEqual(len(self.gestor.tareas), 1)
  self.assertEqual(self.gestor.tareas[0].titulo, "Tarea 1")
  self.assertEqual(self.gestor.tareas[0].descripcion, "Descripción de la tarea 1")

  def test_agregar_tarea_sin_titulo(self):
   with self.assertRaises(ValueError):
    self.gestor.agregar_tarea("", "Descripción")

  def test_ver_tarea(self):
   self.gestor.ver_tarea("Tarea 1", "Descripción de la tarea 1")

  self.assertEqual(len(self.gestor.tareas), 1)
  self.assertEqual(self.gestor.tareas[0].titulo, "Tarea 1")
  self.assertEqual(self.gestor.tareas[0].descripcion, "Descripción de la tarea 1")

  def test_ver_tarea_sin_titulo(self):
   with self.assertRaises(ValueError):
    self.gestor.ver_tarea("", "Descripción")


  def test_marcar_tarea(self):
   self.gestor.marcar_tarea("Tarea en ejecucion", "Descripción de la tarea ")

  self.assertEqual(len(self.gestor.tareas), 1)
  self.assertEqual(self.gestor.tareas[0].titulo, "Tarea Completada")
  self.assertEqual(self.gestor.tareas[0].descripcion, "Descripción de la tarea ")

  def test_marcar_tarea_sin_titulo(self):
   with self.assertRaises(ValueError):
    self.gestor.marcar_tarea("", "Tarea completa")

      def test_eliminar_tarea(self):
     self.gestor.eliminar_tarea("Tarea en ejecucion", "Descripción de la tarea ")

    self.assertEqual(len(self.gestor.tareas), 1)
    self.assertEqual(self.gestor.tareas[0].titulo, "Tarea eliminada")
    self.assertEqual(self.gestor.tareas[0].descripcion, "Descripción de la tarea ")

    def test_eliminar_tarea_sin_titulo(self):
     with self.assertRaises(ValueError):
      self.gestor.eliminar_tarea("", "Tarea eliminada")


