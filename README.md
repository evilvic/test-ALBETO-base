# Proyecto ALBETO base en ONNX - Extracción de Ingredientes de Descripciones de Comida

Este proyecto utiliza el modelo **ALBERT en español** (ALBETO base) para identificar ingredientes en descripciones de comida en lenguaje natural. El modelo ha sido exportado a **ONNX** para hacer inferencias eficientes.

## Requisitos

1. **Python 3.8 o superior**
2. **Entorno virtual** configurado con `venv`
3. Librerías necesarias:
   - `transformers`
   - `torch`
   - `onnx`
   - `onnxruntime`

## 1. Crear el Entorno Virtual e Instalar Dependencias

Para mantener las dependencias del proyecto aisladas, crea y activa un entorno virtual, luego instala las dependencias necesarias.

### Comandos:

```bash
# Crear el entorno virtual
python3 -m venv .env

# Activar el entorno virtual
source .env/bin/activate  # En Linux o macOS
.env\Scripts\activate      # En Windows

# Instalar las dependencias
pip install -r requirements.txt
```

## 2. Descargar y Configurar el Modelo ALBERT en Español

El archivo `setup_model.py` se encargará de descargar el modelo **ALBERT en español** y su tokenizador, guardándolos en la carpeta `albert-base-spanish`.

### Comando para ejecutar:

```bash
python setup_model.py
```

Este script descargará el modelo y el tokenizador desde **Hugging Face** y los guardará localmente.


## 3. Convertir el Modelo a ONNX

El modelo descargado será exportado a formato **ONNX** para realizar inferencias más rápidas. Esto se realiza con el siguiente comando:

### Comando para convertir a ONNX:

```bash
python -m transformers.onnx --model=dccuchile/albert-base-spanish onnx/
```

El modelo será guardado en la carpeta `onnx/` como `model.onnx`.

## 4. Realizar Inferencias con el Modelo ONNX

Para realizar pruebas de inferencia con el modelo ONNX y extraer ingredientes de una descripción de comida, puedes ejecutar el script `run_model.py`.

### Comando para ejecutar:

```bash
python run_model.py
```

Este script procesará una descripción en lenguaje natural de una receta y tratará de identificar ingredientes comunes.

## Resumen

1. **Crear y activar entorno virtual**: `python3 -m venv .env` y activarlo con `source .env/bin/activate`.
2. **Instalar dependencias**: `pip install -r requirements.txt`.
3. **Configurar el modelo**: Ejecutar `python setup_model.py` para descargar el modelo.
4. **Convertir el modelo a ONNX**: Ejecutar `python -m transformers.onnx --model=dccuchile/albert-base-spanish onnx/`.
5. **Probar inferencias**: Ejecutar `python run_model.py` para identificar ingredientes en descripciones de comida.
