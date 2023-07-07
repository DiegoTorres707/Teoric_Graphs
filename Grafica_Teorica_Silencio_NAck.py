import numpy as np
import matplotlib.pyplot as plt

p=0.005
def func(x, n):
   #return (p) * ((1 - p) ** x) * x * n
    #return n - (p) * ((1 - p) ** (x - 1)) * x * n - ((1 - p) ** x) * n
  return ((1 - p) ** x) * n

# Valores de x
x = np.arange(1, 8001)

# Valores de n
n_values = np.arange(500, 10001, 500)

# Graficar la función para cada valor de n
for n in n_values:
    y = func(x, n)
    plt.plot(x, y, label=f"#frames={n}")

plt.xlabel('H')
plt.ylabel('Σ Silencio')
plt.title(f'Gráfico de la Σ Silencio NAck/Ack, P({p}), Corte 500 to 10000 frames')
plt.legend()
plt.grid(True)
plt.xscale('log')
plt.show()
