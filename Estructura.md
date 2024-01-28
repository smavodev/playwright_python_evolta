# Estructura del Proyecto POM en Playwright (Intermedia/Avanzada):
```
proyecto/
├── config/
│   ├── config.py
│   └── data_context.py
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── search_results_page.py
│   └── login_page.py
├── tests/
│   ├── conftest.py
│   ├── test_search.py
│   └── test_login.py
├── data/
│   ├── data_users.xlsx
│   ├── data_users.csv
│   └── data_users.txt
├── .env
└── playwright_config/
    └── playwright_config.yaml
```
## Descripción de la Estructura:
### config/ (Configuraciones):
- config.py: Contiene configuraciones globales, como la configuración de Playwright y manejo de opciones.
- data_context.py: Maneja la obtención de datos desde diferentes fuentes (Excel, CSV, TXT).

### pages/ (Páginas):
- base_page.py: Clase BasePage que contiene métodos comunes para todas las páginas.
- home_page.py: Representa la página de inicio.
- search_results_page.py: Representa la página de resultados de búsqueda.
- login_page.py: Representa la página de inicio de sesión.

### tests/ (Pruebas):
- conftest.py: Configuraciones comunes utilizadas por varias pruebas.
- test_search.py: Pruebas específicas de la funcionalidad de búsqueda.
- test_login.py: Pruebas específicas de la funcionalidad de inicio de sesión.

### data/ (Datos):
- Archivos de datos como data_users.xlsx, data_users.csv, y data_users.txt.

### .env:
- Archivo de entorno que contiene variables como URL_BASE, USER_VALID, PASS_VALID, etc.

### playwright_config/ (Configuración de Playwright):
- playwright_config.yaml: Archivo de configuración específico de Playwright que puede contener configuraciones adicionales.

## Observaciones:
- Las configuraciones globales y la gestión de datos se han separado en sus propios módulos (config/ y data/) para mejorar la modularidad y la mantenibilidad del código.
- Cada página (por ejemplo, home_page.py, search_results_page.py, login_page.py) contiene elementos de la interfaz de usuario y acciones específicas de esa página.
- Las pruebas (por ejemplo, test_search.py, test_login.py) utilizan las páginas y las configuraciones desde sus respectivos módulos.
- Esta estructura más avanzada proporciona una mayor modularidad y escalabilidad, lo que facilita la expansión del proyecto a medida que crece en complejidad.


============================================================================

## Estructura del Proyecto POM en Playwright (Avanzada):
```
proyecto/
├── config/
│   ├── config.py
│   └── data_context.py
├── core/
│   ├── base_page.py
│   └── base_test.py
├── pages/
│   ├── home/
│   │   ├── home_page.py
│   │   ├── home_elements.py
│   │   └── home_actions.py
│   ├── search_results/
│   │   ├── search_results_page.py
│   │   ├── search_results_elements.py
│   │   └── search_results_actions.py
│   └── login/
│       ├── login_page.py
│       ├── login_elements.py
│       └── login_actions.py
├── tests/
│   ├── conftest.py
│   ├── test_search.py
│   └── test_login.py
├── data/
│   ├── data_users.xlsx
│   ├── data_users.csv
│   └── data_users.txt
├── .env
└── playwright_config/
    └── playwright_config.yaml
```

## Descripción de la Estructura:
### config/ (Configuraciones):
- config.py: Contiene configuraciones globales, como la configuración de Playwright y manejo de opciones.
- data_context.py: Maneja la obtención de datos desde diferentes fuentes (Excel, CSV, TXT).

### core/ (Núcleo):
- base_page.py: Clase BasePage que contiene métodos comunes para todas las páginas.
- base_test.py: Clase BaseTest que contiene configuraciones y funciones comunes para todas las pruebas.

### pages/ (Páginas):
- home/: Módulo para la página de inicio.
- search_results/: Módulo para la página de resultados de búsqueda.
- login/: Módulo para la página de inicio de sesión.

### tests/ (Pruebas):
- conftest.py: Configuraciones comunes utilizadas por varias pruebas.
- test_search.py: Pruebas específicas de la funcionalidad de búsqueda.
- test_login.py: Pruebas específicas de la funcionalidad de inicio de sesión.

### data/ (Datos):
- Archivos de datos como data_users.xlsx, data_users.csv, y data_users.txt.

### .env:
- Archivo de entorno que contiene variables como URL_BASE, USER_VALID, PASS_VALID, etc.

###  playwright_config/ (Configuración de Playwright):
- playwright_config.yaml: Archivo de configuración específico de Playwright que puede contener configuraciones adicionales.

## Observaciones:
- Se ha creado una estructura modular dentro de la carpeta pages/, dividiéndola en submódulos para cada página (home/, search_results/, login/). Cada submódulo contiene archivos específicos para los elementos y acciones de esa página.
- Se ha introducido un módulo core/ para clases fundamentales (base_page.py, base_test.py) que contienen funciones y configuraciones comunes utilizadas por otras partes del proyecto.
- La estructura modularizada mejora la mantenibilidad y la escalabilidad del proyecto, facilitando la incorporación de nuevas funcionalidades y la gestión de cambios.