# 04 - Módulos y Paquetes

Organización del código en módulos reutilizables y paquetes.

## Estructura
```
03-modulos-paquetes/
├── apuntes_modulos.py    # Archivo principal con ejemplos
├── mi_modulo.py          # Módulo de ejemplo
├── otro_modulo.py        # Otro módulo
└── mi_paquete/           # Paquete de ejemplo
    ├── __init__.py
    ├── matematicas.py
    └── utilidades.py
```

## Ejecutar los apuntes
```bash
python apuntes_modulos.py
```

Esto mostrará:
- Diferentes formas de importar
- Funcionamiento de `__name__ == "__main__"`
- Sistema de importación (`sys.path`)
- Uso de paquetes

## Conceptos clave
```python
# Importar módulo completo
import mi_modulo

# Importar elementos específicos
from mi_paquete import suma, resta

# Usar alias
import otro_modulo as om
```

## Recursos
- [PDF: Módulos y Librerías](../recursos/pdfs/Modulos_Librerias.pdf)