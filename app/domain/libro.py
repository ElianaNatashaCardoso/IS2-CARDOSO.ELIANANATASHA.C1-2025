class Libro:
    """
    Modelo de la entidad Libro.
    (Basado en el diagrama UML)
    """
    def __init__(self, isbn, titulo, autor, disponible=True):
        # Atributos: -isbn, -titulo, -autor, -disponible
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    
    def cambiar_estado_disponibilidad(self, estado: bool):
        """Cambia el estado de disponibilidad del libro."""
        self.disponible = estado
        return f"Libro '{self.titulo}' ahora disponible: {estado}."