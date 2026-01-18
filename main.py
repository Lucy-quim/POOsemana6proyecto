#importamos datos de carpeta y archivo modelo y servicio
from Modelos.modelo import Usuario
from Servicios.servicio import validar_mayoria_edad

if __name__ == "__main__":
    #datos de usuario
    nuevo_usuario = Usuario("Jaime", 20,"jaime@gmail.com")
    es_mayor = validar_mayoria_edad(nuevo_usuario)
    #correo = Usuario("jaime@gmail.com")
    #imprime datos 
    print(f"{nuevo_usuario.nombre} es mayor de edad: {es_mayor} correo:{nuevo_usuario.correo}")