from logica_negocio.prestamo_service import PrestamoDeLibros


from domain.socio import Socio
from domain.libro import Libro

# --- main.py (Esquema de Flujo) ---
if __name__ == "__main__":
    
    
    socio_laura = Socio(dni="123456", nombre="Laura Perez", email="laura@mail.com")
    libro_cien_años = Libro(isbn="978-0061120084", titulo="Cien Años de Soledad", autor="G. García Márquez", disponible=True)
    libro_codigo = Libro(isbn="978-0385537856", titulo="El Código Da Vinci", autor="Dan Brown", disponible=False)
    

    servicio_prestamo = PrestamoDeLibros()
    

     ## PRÉSTAMO EXITOSO (Libro disponible)
    
    print("=========================================================")
    print(f"PETICIÓN DE USUARIO: Laura pide '{libro_cien_años.titulo}'")
    
    
    resultado_exito = servicio_prestamo.procesar_prestamo(socio_laura, libro_cien_años)
    print(resultado_exito)
    
    
    print(f"\n[DEMOSTRACIÓN] Estado final de '{libro_cien_años.titulo}': {'DISPONIBLE' if libro_cien_años.disponible else 'PRESTADO'}")
    
    
    ## PRÉSTAMO FALLIDO (Libro no disponible)
  
    print("\n=========================================================")
    print(f"PETICIÓN DE USUARIO: Laura pide '{libro_codigo.titulo}' (Ya prestado)")
    
   
    resultado_fallido = servicio_prestamo.procesar_prestamo(socio_laura, libro_codigo)
    print(resultado_fallido)
    print("=========================================================")