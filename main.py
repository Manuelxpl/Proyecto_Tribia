print("\n---------BIENVENIDOS A MI TRIVIA SOBRE AL MUNDO DE LA ELECTRICIDAD---------")
print("============================================================================")
print("\n Acepta el desafío y pon a prueba tus conocimientos, acerca de lo que sabes de la historia de la electricidad.")
print("-----------------------------------------------------------------------------------------------------------------")
nombre = (input("Cual es tu nombre participante \n"))
print("Muy bien", nombre, "Empezemos con el juego,  Ahora cuentas con 0 puntos \n "
      "Cada preguntas que respondas bien se te aumentaran 10 puntos, en una escala de 60\n ")
puntaje = 0;
print("-----------------------------------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------------------------------")
print("INSTRUCCIONES:\n")
print("A continuación, le aparecerá pregunta por pregunta con alternativas múltiples en la que usted tendrá que ingresar \n"
"la alternativa que crea correcta y presionar ‘enter’, es importante mencionar que la letra de la alternativa se debe\n"
"ingresar en minúscula, si llega a ingresar mal la respuesta la pregunta volverá aparecer. MUCHA SUERTE\n")
print("-----------------------------------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------------------------------")
print(" LISTADO DE PREGUNTAS\n")
print("-----------------------------\n")
print("1)- ¿Quién fue el creador de la bombilla incandescente?\n ")
print("a) Alessandro Volta")
print("b) Michael Faraday")
print("c) Thomas Alba Edison")
print("d)James Watt")
respuesta1 = (input("Ingresa tu Repuesta: "))
while respuesta1 not in("a", "b", "c", "d"):
    respuesta1 = input("Debes Ingresar de nuevo tu respuesta: ")
if respuesta1 == "a":
    print("Incorrecto", nombre,",Volta invento la Pila")
elif respuesta1=="b":
    print("Incorrecto", nombre, ",Faraday invento el generador electrico ")
elif respuesta1 == "c":
    puntaje +=10
    print("Correcto", nombre, ",Alba Edison invento la bombilla ")
else:
    print("Incorrecto", nombre, ",Whatt invento la maquina a vapor")

print("\n-----------------------------------------------------------------------------------------------------------------\n")
print("2)- ¿Quién diseño el primer sistema para generar y trasmitir corriente alterna ? \n ")
print("a) Michael Faraday")
print("b) Nikola Tesla")
print("c) Thomas Alba Edison")
print("d) Alessandro Volta")
respuesta2 = (input("Ingresa tu Repuesta: "))
while respuesta2 not in("a", "b", "c", "d"):
    respuesta2 = input("Debes Ingresar de nuevo tu respuesta: ")
if respuesta2 == "a":
    print("Incorrecto", nombre,",Faraday invento el generador electrico")
elif respuesta2=="b":
    puntaje += 10
    print("Correcto", nombre, ",Tesla genero la corriente alterna ")
elif respuesta2 == "c":
    print("Incorrecto", nombre, ",Alba Edison invento la bombilla ")
else:
    print("Incorrecto", nombre, ",Volta invento la Pila")

print("\n-----------------------------------------------------------------------------------------------------------------\n")
print("3)- ¿Quién descubrió que una corriente eléctrica produce un campo magnético? \n ")
print("a) Luigi Galvani")
print("b) André Ampere")
print("c) Nikola Tesla")
print("d) Michael Faraday")
respuesta3 = (input("Ingresa tu Repuesta: "))
while respuesta3 not in("a", "b", "c", "d"):
    respuesta3 = input("Debes Ingresar de nuevo tu respuesta: ")
if respuesta3 == "a":
    print("Incorrecto", nombre,",Galvani descubrio la bioelectricidad")
elif respuesta3=="b":
    print("Incorrecto", nombre, ",Ampere contribuyo la desarrollo del electromagnetismo ")
elif respuesta3 == "c":
    print("Incorrecto", nombre, ",Tesla genero la corriente alterna")
else:
    puntaje += 10
    print("Correcto", nombre, ",Faraday descubrio la corriente en un campo magnetico")

print("\n-----------------------------------------------------------------------------------------------------------------\n")
print("4)- ¿Quién invento la pila eléctrica, y en su honor la medida de electricidad se denominó Voltio?  \n ")
print("a) James Watt")
print("b) Alessando Volta")
print("c) André Ampère")
print("d) Michael Faraday")
respuesta4 = (input("Ingresa tu Repuesta: "))
while respuesta4 not in("a", "b", "c", "d"):
    respuesta4 = input("Debes Ingresar de nuevo tu respuesta: ")
if respuesta4 == "a":
    print("Incorrecto", nombre,",Galvani descubrio la bioelectricidad")
elif respuesta4=="b":
    puntaje += 10
    print("Correcto", nombre, ",Volta invento la Pila")
elif respuesta4 == "c":
    print("Incorrecto", nombre, ",Ampere contribuyo la desarrollo del electromagnetismo")
else:
    print("InCorrecto", nombre, ",,Whatt invento la maquina a vapor")

print("\n-----------------------------------------------------------------------------------------------------------------\n")
print("5)- ¿Quién creo la batería más grande del mundo, la cual consistía en más de 800 pilas entre sí?   \n ")
print("a) André Ampère")
print("b) James Watt")
print("c) Humphry Davy")
print("d) Thomas Alba Edison")
respuesta5 = (input("Ingresa tu Repuesta: "))
while respuesta5 not in ("a", "b", "c", "d"):
    respuesta5 = input("Debes Ingresar de nuevo tu respuesta: ")
if respuesta5 == "a":
    print("Incorrecto", nombre, ",Ampere contribuyo la desarrollo del electromagnetismo")
elif respuesta5 == "b":
    print("Incorrecto", nombre, ",Whatt invento la maquina a vapor")
elif respuesta5 == "c":
    puntaje += 10
    print("Correcto", nombre, ",Davy creo la bateria mas grande del mundo")
else:
    print("InCorrecto", nombre, ",Alba Edison invento la bombilla")

print("\n-----------------------------------------------------------------------------------------------------------------\n")
print("6)- ¿Quién diseño el primer sistema para generar y trasmitir corriente continua ? \n ")
print("a) Michael Faraday")
print("b) Nikola Tesla")
print("c) Thomas Alba Edison")
print("d) Alessandro Volta")
respuesta6 = (input("Ingresa tu Repuesta: "))
while respuesta6 not in("a", "b", "c", "d"):
    respuesta6 = input("Debes Ingresar de nuevo tu respuesta: ")
if respuesta6 == "a":
    print("Incorrecto", nombre,",Faraday invento el generador electrico")
elif respuesta6=="b":
    print("Incorrecto", nombre, ",Tesla genero la corriente alterna ")
elif respuesta6 == "c":
    puntaje += 10
    print("Correcto", nombre, ",Alba Edison genero corriente continua ")
else:
    print("Incorrecto", nombre, ",Volta invento la Pila")
print("\n-----------------------------------------------------------------------------------------------------------------\n")
print("FIN DEL CUESTIONARIO",nombre, "Muchas Gracias por Participar ")
print("\n-----------------------------------------------------------------------------------------------------------------\n")
print("TU PUNTAJE OBTENIDO ES DE: ", puntaje)
if puntaje <=20:
    print(nombre,"Tu puntaje es bajo, Puedes intentarlo de nuevo ")
elif puntaje >=40:
    print(nombre, "Tu puntaje es medio, esta muy bien ")
else:
    print(nombre, "Felicidades Obtuviste la mayor puntuación ")