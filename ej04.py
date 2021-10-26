#algoritmo para obtener la clasificación en la liga


#PSEUDOCÓDIGO

''' en este caso, se nos pide la puntuación de un cierto equipo en la liga. Para ello, es necesario que que usuario nos pase
por consola el número de partidos ganados, perdidos y empatados. COmo siempre, se trnasforma la cadena de texto introducida
por el usuario a una varibale de tipo int para posteriormente poder calcular la casificación final con las ponderaciones
de cada partido. Finalmente, imprimiremos por pantalla la clasificación final de la liga de este equipo con la
ayuda de la función print'''


partidos_ganados=input("Introduzca el número de partidos ganados por ABC club: ")
partidos_ganados=int(partidos_ganados)

partidos_perdidos=input("Introduzca el número de partidos perdidos por ABC club:: ")
partidos_perdidos=int(partidos_perdidos)

partidos_empatados=input("Introduzca el número de rpartidos empatados por ABC club:: ")
partidos_empatados=int(partidos_empatados)

clasificacion=(partidos_ganados*3)+(partidos_empatados*1)+(partidos_perdidos*0)

clasificacion=str(clasificacion)

print("la clasificación en la liga del ABC club es de: "+ clasificacion+" puntos")