from modelo import Usuario

class TiendaService:
    def saludar_usuario(self, usuario: Usuario):
        return f"Bienvenido al sistema, {usuario.nombre}"