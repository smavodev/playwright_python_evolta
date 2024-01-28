
# Instalar PLAYWRIGHT: 
### https://playwright.dev/python/docs/intro
```pip install pytest-playwright```

### Instalar navegadores Chrome, Firefox, webkit
```playwright install```

## Generar lista de paquetes a instalar
```pip freeze > requirements.txt```

## Install dependencies por archivo
```pip install -r requirements.txt```

## Run tests in headed mode
```pytest --headed``` <test>
```pytest --headed .\test_example_1.py```

## Run tests on different browsers
```pytest --browser webkit```
```pytest --browser webkit --browser firefox```

## Run specific tests
```pytest test_example.py```

## Run tests in parallel
```pytest --numprocesses 2 .\test_example_1.py```

## Running Codegen
```playwright codegen <url>```
```playwright codegen https://test.evolta.pe/Login/Acceso/Index```

## Ejecutar con 1 marcador
```pytest -m "data_test" .\test_login_data_03.py```
```pytest -k "data_test" .\test_login_data_03.py```

## Ejecutar prueba con marcador + ignorar advertencias
```pytest -m "data_test" -W ignore::UserWarning .\test_login_data_03.py```

## Ejecutar con 2 marcadores o mas
### Ejecutar pruebas que tengan ambos marcadores:
```pytest -k "test_all and data_test" .\test_login_data_03.py```

#### Ejecutar pruebas que tengan al menos uno de los marcadores:
```pytest -k "test_all or data_test" .\test_login_data_03.py```

### Ejecutar pruebas con un marcador y excluir pruebas con otro:
```pytest -k "test_all and not data_test" .\test_login_data_03.py```
