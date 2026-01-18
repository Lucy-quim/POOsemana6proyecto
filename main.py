from Modelos.modelo import Usuario
from Servicios.servicio import validar_mayoria_edad

if __name__ == "__main__":
    nuevo_usuario = Usuario("Jaime", 20, "jaime@gmail.com")
    es_mayor = validar_mayoria_edad(nuevo_usuario)
    print(f"{nuevo_usuario.nombre} es mayor de edad: {es_mayor}")