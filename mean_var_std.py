import numpy as np  

def calculate(number):
    # Verifica se a lista contém exatamente 9 números. Caso contrário, lança um erro.
    if len(number) != 9:
        raise ValueError("List must contain nine numbers.")

    # Converte a lista de 9 números em uma matriz 3x3.
    matrix = np.array(number).reshape(3,3)

    # Cria um dicionário para armazenar os cálculos solicitados (média, variância, etc.)
    # Cada cálculo é feito ao longo dos eixos 0 (colunas), 1 (linhas) e para a matriz inteira.
    calculations = {
        "mean": [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean()],
        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var()],
        'standart deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std()],
        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max()],
        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min()],
        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum()]
    }
    return calculations
