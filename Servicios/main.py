from Modelos import Usuario
from servicios import TiendaServicio

def main():
    nuevo_usuario = Usuario("Jaime", "jaime@gmail.com")
    servicio = TiendaServicio()

    print(servicio.saludar_usuario(nuevo_usuario))

if __name__ == "__main__":
    main()