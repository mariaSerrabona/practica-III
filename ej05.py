#algoritmo que haga em cambio de galones a litros


#PSEUDOCÓDIGO

''' EN este ejercicio, se nos pide transformar cierta cantidad de galones a litros para poder calcular el coste total
de gasolina del cleinte. Para ello, definimos una variable que almacenará la canridad de galones a convertir.
Después, clacularemos los litros correspondientes mediante una multiplicación. EL números obtenido, de litros
se transformará a una cadena de texto String para poder unirla a más cadenas de texto.
Al final, obtendremos por pantalla, el número total de litros que se ha de cobrar al cliente '''

num_galones=9

#conversión de galones a litros
num_litros=num_galones*3,78541

num_litros=str(num_litros)

print("El total de litros que hay que cobrarle al cliente es de: "+num_litros+" litros")
