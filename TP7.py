# 1) Escribir una clase llamada Rectángulo que contenga una base y una altura, y que contenga un método que devuelva el área
# del rectángulo.


class Rectangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
        return
    def area(self):
        print(f"El área del rectángulo es {self.area * self.base}")
        return
    pass    













# 2) Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina. La clase debe contener
# como miembros:
# o Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número).
# o Un atributo para el estado (lleno o vacío).
# o Un atributo n, que indica la cantidad máxima de cebadas.
# o Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se debe lanzar una
# excepción que imprima el mensaje ¡Cuidado! ¡Te quemaste!
# o Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta beber un mate vacío, se
# debe lanzar una excepción que imprima el mensaje: ¡El mate está vacío!
# o Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibles. En ese caso la cantidad
# de cebadas restantes se mantendrá en 0, y cada vez que se intente beber se debe imprimir un mensaje de aviso:
# “Advertencia: el mate está lavado.” pero no se debe lanzar una excepción.

class Mate:
    def __init__ (self,cebadas_maximas=int):
        self.cebadas_maximas = cebadas_maximas
        self.estado = False
        self.cebadas_restantes = cebadas_maximas
        return
    def cebar(self):
         try:
            if self.estado:
                raise NameError("Mate ya sebado")
            else:
                print("Mate cebado")
                self.estado = True
                return
         except Exception as e:
                    print(f"Cuidado!! te quemaste!! {e}")
         return
    def tomar(self):
         try:
              if self.cebadas_restantes == 0:
                   print("Advertencia: el mate está lavado.")
                   self.estado = False
                   return
              if not self.estado:
                raise NameError ("¡El mate está vacío!")
              else:
                   self.estado = False
                   self.cebadas_restantes -= 1
                   print("-ruido de mate-")
         except Exception as e:
              print(e)
         return
    
    pass


# prueba = Mate(3)
# prueba.cebar()
# prueba.tomar()
# prueba.cebar()
# prueba.cebar()
# prueba.tomar()
# prueba.tomar()
# prueba.cebar()
# prueba.tomar()
# prueba.cebar()
# prueba.tomar()





# 3) Botella y Sacacorchos
#  Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega).
#  Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho que la tapa, o None si está
# destapada.
#  Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella, le saque el corcho y se guarde
# una referencia al corcho sacado. Debe lanzar una excepción en el caso en que la botella ya esté destapada, o si el
# sacacorchos ya contiene un corcho.
#  Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción en el caso en el que no haya
# un corcho.

class Sacachorchos_con_corcho(Exception):
     def __init__(self):
          self.descripcion = "El sacacorchos ya tiene un corcho"
          pass
     pass

class Botella_destapada(Exception):
     def __init__(self):
          self.descripcion = "La botella no tiene corcho"
          pass
     pass


class Corcho:
     def __init__(self,bodega="Cafayate"):
          self.bodega = bodega
          pass
     pass

class Botella:
     def __init__(self,bodega=str):
          self.corcho = Corcho(bodega)
          self.tapado = True
          pass
     pass

class Sacacorcho:
     def __init__(self):
          self.limpio = True
          pass
     
     def destapar(self,botella=Botella):
          try:
               if not self.limpio:
                    raise Sacachorchos_con_corcho
               if botella.tapado:
                    botella.tapado = False
                    self.limpio = False
                    print(f"Botella destapada, una excelente eleccion de la bodega {botella.corcho.bodega}")
                    return
               else:
                    raise Botella_destapada
          except Sacachorchos_con_corcho as e:
               print (e.descripcion)
          except Botella_destapada as e:
               print (e.descripcion)
          return
     def limpiar(self):
         try:
            if not self.limpio:
                self.limpio = True
                print("El sacacorchos está vacío")
            else:
                raise NameError("El Sacacorchos ya está limpio")
         except NameError as e:
              print(e)
        
     pass




# vinito = Botella("Termidor")

# sacacorcho1 = Sacacorcho()
# sacacorcho1.destapar(botella=vinito)
# sacacorcho1.destapar(botella=vinito)
# sacacorcho1.limpiar()
# sacacorcho1.limpiar()
# sacacorcho1.destapar(vinito)



# 4) Una heladería es un tipo especial de restaurante. Cree una clase Restaurante, cuyo método __init__() guarde dos atributos:
# restaurante_nombre y tipo_comida. Cree un método describir_restaurante() que muestre estas piezas de información, y un
# método abrir_restaurante() que muestre un mensaje indicando que el restaurante ahora está abierto. Luego cree una clase
# Heladeria que herede de Restaurante, y agregue a los existentes un atributo llamado sabores que almacene una lista de los
# sabores de helado disponibles. Escriba también un método que muestre estos valores, cree una instancia de la clase y llame
# al método.


class Restaurante:
     def __init__(self,nombre,comida):
          self.restaurante_nombre = nombre
          self.tipo_comida = comida
          self.abierto = False
          pass
     def describir_restaurante(self):
          print(f"Bienvenido a {self.restaurante_nombre} aquí servimos {self.tipo_comida}")
          pass
     def abrir_restaurante(self):
          try:
               if self.abierto:
                    raise NameError("El restaurante ya está abierto")
               self.abierto = True
               print("Se ha abierto el restaurante")
          except NameError as e:
               print(e)
     pass

class Heladeria(Restaurante):
     def __init__(self, nombre, comida = "Helado", sabores = list):
          super().__init__(nombre, comida)
          self.tipo_comida = comida
          self.sabores = sabores
          pass
     def listado_sabores(self):
          for sabor in self.sabores:
               print(sabor)
          return
     pass


# grido = Heladeria("Grido helado",sabores=["Vainilla","Chocolate","Dulce de leche"])
# grido.abrir_restaurante()
# grido.abrir_restaurante()
# # grido.listado_sabores()
     










# 5) Escribir una clase Personaje que contenga los atributos vida, posicion y velocidad, y los métodos recibir_ataque, que
# reduzca la vida según una cantidad recibida y lance una excepción si la vida pasa a ser menor o igual que cero, y mover
# que reciba una dirección y se mueva en esa dirección la cantidad indicada por velocidad.
#  Escribir una clase Soldado que herede de Personaje, y agregue el atributo ataque y el método atacar, que reciba otro
# personaje, al que le debe hacer el daño indicado por el atributo ataque.
#  Escribir una clase Campesino que herede de Personaje, y agregue el atributo cosecha y el método cosechar, que
# devuelva la cantidad cosechada



class Personaje:
     def __init__(self,posicion = list):
          self.vida = 100
          self.posicion = posicion
          self.velocidad = 100
     def recibir_ataque(self,daño=int):
          try:
            if self.vida==0:
                 raise NameError("Personaje sin vida")
            self.vida -= daño
          except NameError as e:
               print(e)
          pass
     def mover(self,direccion):
          if direccion == "der":
               self.posicion[0] += self.velocidad
          elif direccion == "iz":
               self.posicion[0] -= self.velocidad
          elif direccion == "arriba":
               self.posicion[1] += self.velocidad
          elif direccion == "abajo":
               self.posicion[1] -= self.velocidad
          return

     pass

class Soldado(Personaje):
     def __init__(self,ataque,posicion,vida,velocidad):
          super().__init__(posicion,vida,velocidad)
          self.ataque = ataque
          pass
     def atacar(self,personaje=Personaje):
          personaje.recibir_ataque(self.ataque)
          pass
     pass

import random

class Campesino(Personaje):
     def __init__(self,cosecha=random.randint(5,15)):
          self.cosecha = cosecha
          pass
     def cosechar(self):
          print(f"Se cosecharon {self.cosecha} trigos")
          return self.cosecha
     pass

          
          
          





# 6) Usuarios: Cree una clase Usuario. Cree también dos atributos nombre y apellido, así como otros atributos que típicamente
# se guardan en un perfil de usuario. Escriba un método describir_usuario() que muestre un resumen de la información del
# usuario. Escriba otro método saludar_usuario() que muestre un saludo personalizado al usuario.
# Cree varias instancias que representen distintos usuarios y llame ambos métodos para cada uno.





class Usuario:
     def __init__(self,nombre,apellido,nombre_usuario,contrasenia):
          self.nombre = nombre
          self.apellido = apellido
          self.nombre_usuario = nombre_usuario
          self.contrasenia = contrasenia
          pass
     def describir_usuario(self):
          print(f"Usuario: {self.nombre_usuario} \n Nombre: {self.nombre} {self.apellido}")
          pass
     def saludar_usuario(self):
          print(f"Hola {self.nombre}!!!")
          pass
     pass

usuario1 = Usuario("Pablo","Hearne","pablo_hearne","1234")
usuario2 = Usuario("Pablo1","Hearne","pablo_hearne","12345")
usuario3 = Usuario("Pablo2","Hearne","pablo_hearne","123456")
usuario4 = Usuario("Pablo3","Hearne","pablo_hearne","1234567")


# usuario1.saludar_usuario()
# usuario2.saludar_usuario()
# usuario3.saludar_usuario()
# usuario4.saludar_usuario()






# 8) Privilegios: Escriba una clase Privilegios. La clase debería tener un atributo, privilegios, que almacene una lista de strings
# con los privilegios de manera similar a la del ejercicio 7. Mueva el método mostrar_privilegios() de ese ejercicio a esta
# clase, y haga que una instancia de esta clase sea un atributo de la clase Admin. Cree una nueva instancia de Admin y use
# el método para mostrar privilegios.




class Privilegios:
     def __init__(self,privilegios):
          self.privilegios = privilegios
          pass
     def mostrar_privilegios(self):
         for privilegio in self.privilegios:
            print(privilegio)
         pass
     pass









# 7) Admin: Un administrador es un tipo de usuario con privilegios especiales. Cree una clase Admin que herede de la clase
# Usuario del ejercicio anterior y agréguele un atributo privilegios que almacene una lista de strings tales como “puede
# postear en el foro”, “puede borrar un post”, “puede banear usuario”, etc. Escriba un método mostrar_privilegios() que
# muestre el conjunto de privilegios del administrador, cree una instancia de la clase y llame al método.

privilegios = [ "puede postear en el foro", "puede borrar un post", "puede banear usuario", "puede cambiar la disposición del foro"]

class Admin(Usuario):
     def __init__(self, nombre, apellido, nombre_usuario, contrasenia,privilegios = list):
          super().__init__(nombre, apellido, nombre_usuario, contrasenia)
        #   self.privilegios = privilegios
          self.privilegios = Privilegios(privilegios)
          pass
    #  def mostrar_privilegios(self):
    #       for privilegio in self.privilegios:
    #            print(privilegio)
    #       pass
     pass

admin1 = Admin(usuario1.nombre,usuario1.apellido,usuario1.nombre_usuario,usuario1.contrasenia,privilegios)


# admin1.privilegios.mostrar_privilegios()










# 9) Restaurante importado: Escriba un programa que esté en otro archivo que la clase Restaurante del ejercicio 4, e impórtela
# al módulo actual. Cree una instancia de Restaurante y llame a alguno de sus métodos para asegurarse que la importación
# funcionó.















# 10) (Opcional): Repita el ejercicio anterior pero esta vez importando la clase Heladeria. ¿Qué se necesita para que funcione la
# importación?



