import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Definir la función modelo sin la constante c
def model(x, a, b):
    return a - b / x

# Datos experimentales
x_data = np.array([5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175,180,185,190,195,200,205,210,215,220,225,230,235,240,245,250,300,350,400,450,500,550,600,650,700])  # Valores de x
y_data = np.array([0.726,0.719,0.755,0.792,0.800,0.808,0.821,0.839,0.849,0.850,0.854,0.854,0.852,0.856,0.858,0.854,0.860,0.858,0.866,0.860,0.860,0.866,0.868,0.862,0.858,0.864,0.862,0.864,0.864,0.866,0.862,0.862,0.862,0.864,0.864,0.866,0.864,0.864,0.860,0.866,0.860,0.858,0.858,0.862,0.862,0.862,0.864,0.864,0.864,0.860,0.862,0.858,0.862,0.862,0.858,0.860,0.860,0.856,0.862])  # Valores de y

# Ajuste de la curva
popt, pcov = curve_fit(model, x_data, y_data, p0=[1, 1])  # p0 son las estimaciones iniciales
a, b = popt  # Valores ajustados

# Generar datos para la curva ajustada
y_fit = model(x_data, *popt)  # Valores ajustados en las mismas posiciones que y_data

# Calcular el coeficiente de correlación
residuals = y_data - y_fit
ss_res = np.sum(residuals**2)  # Suma de los cuadrados de los residuos
ss_tot = np.sum((y_data - np.mean(y_data))**2)  # Suma de los cuadrados totales
r_squared = 1 - (ss_res / ss_tot)  # Coeficiente de determinación

# Generar datos para la curva ajustada para graficar
x_fit = np.linspace(min(x_data), max(x_data), 100)
y_fit_curve = model(x_fit, *popt)

# Graficar los datos experimentales y el ajuste
plt.scatter(x_data, y_data, label="Datos experimentales", color="red")
plt.plot(x_fit, y_fit_curve, label="Ajuste: $f(n) = a - \\frac{b}{n}$", color="blue")
plt.xlabel("Número de ligas")
plt.ylabel("coeficiente de restitución")
plt.legend()
plt.title("Ajuste de curva")

# Agregar los valores ajustados y el R^2 en la gráfica
ajuste_texto = f"$a = {a:.3f}$\n$b = {b:.3f}$\n$R^2 = {r_squared:.3f}$"
plt.text(0.6 * max(x_data), 0.9 * max(y_data), ajuste_texto, fontsize=10, 
         bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))

# Mostrar la gráfica
plt.show()

# Imprimir los valores ajustados y R^2 en la consola
print(f"Valores ajustados: a = {a:.3f}, b = {b:.3f}")
print(f"Coeficiente de determinación (R^2): {r_squared:.3f}")

