from ..mocks import mock_estudiantes

def listar_estudiantes():
    
    for estudiantes in mock_estudiantes:
        
        nombre = estudiantes["nombre"]
        
        print(f"Nombre: {nombre}")
        
    return

