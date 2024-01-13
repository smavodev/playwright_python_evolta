
# Instalar PLAYWRIGHT: 
### https://playwright.dev/python/docs/intro
```pip install pytest-playwright```

```playwright install```

## Generar lista de paquetes a instalar
```pip freeze > requirements.txt```

## Install dependencies por archivo
```pip install -r requirements.txt```

## Run tests in headed mode
```pytest --headed```

## Run tests on different browsers
```pytest --browser webkit```
```pytest --browser webkit --browser firefox```

## Run specific tests
```pytest test_example.py```

## Run tests in parallel
```pytest --numprocesses 2```

## Running Codegen
```playwright codegen <url>```
