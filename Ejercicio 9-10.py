# 9) Restaurante importado: Escriba un programa que esté en otro archivo que la clase Restaurante del ejercicio 4, e impórtela
# al módulo actual. Cree una instancia de Restaurante y llame a alguno de sus métodos para asegurarse que la importación
# funcionó.


from TP7 import Heladeria


# charcaz_vacca = Restaurante("Charcaz Vacca","Buffet")

# charcaz_vacca.describir_restaurante()
# charcaz_vacca.abrir_restaurante()
# charcaz_vacca.abrir_restaurante()

# 10) (Opcional): Repita el ejercicio anterior pero esta vez importando la clase Heladeria. ¿Qué se necesita para que funcione la
# importación?


"""Supongo que necesito importar ambas clases"""
grido = Heladeria("Grido Helados",sabores=["Vainilla","Sambayón","Oreo"])

grido.listado_sabores()
grido.abrir_restaurante()