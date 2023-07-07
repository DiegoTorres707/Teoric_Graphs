import numpy as np
import matplotlib.pyplot as plt

n = 10000
p_values = [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1]

def func(x, n, p):
    return p * ((1 - p) ** x) * x * n

# Valores de x
x = np.arange(1, 8001)

# Graficar la función para cada valor de p
for p in p_values:
    y = func(x, n, p)
    plt.plot(x, y, label=f"h={p}")

plt.xlabel('No. de Stas')
plt.ylabel('Σ Recepcion 1 NACK correctamente')
plt.title(f'Gráfico de la Σ Recepcion 1 NAck/Ack correctamente para diferentes valores de h, frames={n}')
plt.legend()
plt.grid(True)
plt.xscale('log')
plt.show()
