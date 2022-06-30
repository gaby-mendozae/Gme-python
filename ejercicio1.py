from pygame import GL_CONTEXT_PROFILE_COMPATIBILITY


nombre=input("Ingresa tu nombre: ")
num_tel=int(input("Ingresa numero de telefono: "))
direc=input("Ingresa direccion: ")
edad=int(input("Ingresa edad: "))
na=input("Ingresa nacionalidad: ")
f_naci= input("Ingresa fecha de nacimiento: ")
alt1=int(input("Ingresa altura: "))
peso=int(input("Ingresa peso: "))

print("\nLos datos de", nombre,"son los siguientes", type(nombre))
print("Telefono: ", num_tel, type(num_tel))
print("Direccion: ", direc, type(direc))
print("Edad: ", edad, type(edad))
print("Nacionalidad: ", na, type(na))
print("Fecha de nacimiento: ", f_naci, type(f_naci))
print("Altura: ", alt1, type(alt1))
print("Peso: ", peso, type(peso))

