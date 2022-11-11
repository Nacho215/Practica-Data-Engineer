# app.py
import logging

# Logging básico
logging.basicConfig(
    level=logging.INFO,
    filename='./results.log',
    filemode='w',
    encoding='utf-8',
    datefmt='%Y-%m-%d %H:%M:%S',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Lista de frutas
fruits = ['Frutilla', 'Melón', 'PERA', 99.6, 'NaranJA', 'mORa', 'NisPERo', 99]

# Itera sobre la lista de frutas
for idx, fruit in enumerate(fruits):
    # Si el elemento es una string, lo convierte a minúscula y logging imprime un mensaje de tipo INFO
    try:
        fruits[idx] = fruits[idx].lower()
        logging.info(f"Conversión exitosa: {fruit} ---> {fruit.lower()}")
    # Si el elemento no es una string, logging imprime un mensaje de ERROR
    except Exception:
        logging.error("Conversión fallida: " + str(fruit))
