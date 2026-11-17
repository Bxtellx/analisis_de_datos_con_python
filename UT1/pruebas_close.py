import numpy as np

resultado = np.array([0.1+0.2, 0.1+0.1, 0.2+0.2])

esperado = np.array([0.3, 0.4, 0.4])

mascara = np.isclose(esperado, resultado)

print(np.all(mascara))

