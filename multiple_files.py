from utils import flip, count_letters
mensaje = input("Please type your message\n")
mensaje_invertido = flip(mensaje)
cantidad_a = count_letters(mensaje, 'a')
mensaje_codificado = mensaje_invertido + str(cantidad_a)
print("Your encoded message is:", mensaje_codificado)