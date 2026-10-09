import csv
from pathlib import Path
import joblib
from .contracts import Entrada, Salida


def leer_csv(ruta: Path) -> list[Entrada]:
    csv = csv.DictReader(ruta)
    entradas = []

    for i, row in csv:
        entrada = Entrada(**row.to_dict())
        entradas.append(entrada)

    return entradas



def preprocesar(entrada: Entrada) -> list[float]:
    peso_kg = entrada.peso_kg
    peso = round(peso_kg, 1)

    return [
        peso,
        entrada.distancia_km
    ]



def cargar_modelo(ruta: Path):
    modelo = joblib.load(ruta)
    return modelo


def predecir(entrada: Entrada, modelo) -> Salida:
    diccionario = entrada.model_dump()

    matriz = list(zip(*diccionario.values()))

    prediccion1 = modelo.predict_proba(matriz)[0][0]
    prediccion2 = modelo.predict_proba(matriz)[0][1]

    if (prediccion1 > prediccion2):
        probabilidad = prediccion1
    else:
        probabilidad = prediccion2

    categoria = modelo.predict(matriz)[0]
    id_paquete= entrada.id_paquete

    return Salida(
        id_paquete=id_paquete,
        categoria=categoria,
        confianza=probabilidad
    )


def guardar_csv(resultados: list[Salida], ruta: Path) -> None:
    with open(ruta, mode='w', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["id_paquete", "categoria", "confianza"])
        escritor.writeheader()

        for i in resultados:
            escritor.writerows([i.dump()])
    
        


def ejecutar(entrada: Path, modelo: Path, salida: Path) -> None:
    # TODO
    raise NotImplementedError


if __name__ == "__main__":
    ejecutar(
        Path("data/raw/paquetes.csv"),
        Path("models/modelo.joblib"),
        Path("resultados.csv"),
    )
