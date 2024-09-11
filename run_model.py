import onnxruntime as ort
from transformers import AutoTokenizer
import numpy as np

# Ruta al modelo ONNX
onnx_model_path = "onnx/model.onnx"

# Cargar el tokenizador
tokenizer = AutoTokenizer.from_pretrained("dccuchile/albert-base-spanish")

# Descripción de comida
input_text = "Para preparar un buen guacamole necesitas aguacate, tomate, cebolla, y limón."

print(input_text)

# Tokenizar el texto de entrada
inputs = tokenizer(input_text, return_tensors="np")

# Crear la sesión ONNX
ort_session = ort.InferenceSession(onnx_model_path)

# Ejecutar el modelo
onnx_inputs = {
    "input_ids": inputs["input_ids"],
    "attention_mask": inputs["attention_mask"],
    "token_type_ids": inputs["token_type_ids"]
}
outputs = ort_session.run(None, onnx_inputs)

# Obtener los tokens de entrada
tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])

# Lista extendida de ingredientes comunes
possible_ingredients = ["aguacate", "tomate", "cebolla", "limón", "ajo", "sal", "aceite", "pimienta", "pollo", "queso"]

# Verificar si los tokens predichos contienen posibles ingredientes
predicted_tokens = [token for token in tokens if token in possible_ingredients]

# Mostrar las palabras identificadas
print("Ingredientes identificados:", predicted_tokens)