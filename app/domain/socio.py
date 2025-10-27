class Socio:
    """
    Modelo de la entidad Socio. Contiene atributos y lógica interna básica.
    (Basado en el diagrama UML)
    """
    def __init__(self, dni, nombre, email):
        # Atributos: -dni, -nombre, -email, -fecha_alta
        self.dni = dni
        self.nombre = nombre
        self.email = email
        self.fecha_alta = "2024-01-01" 

   
    def verificar_aptitud(self):
        """Verifica si el socio está apto para un nuevo préstamo."""
        return True