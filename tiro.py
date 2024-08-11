import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Constante de gravedad
g = 9.81

def calcular_altura_maxima(v, theta):
    # Convierte el ángulo de grados a radianes
    theta_rad = np.radians(theta)
    # Fórmula de la altura máxima
    h = (v**2 * np.sin(2 * theta_rad)) / g
    return h

def generar_datos(v):
    angulos = np.arange(0, 91, 5)
    alturas = [calcular_altura_maxima(v, theta) for theta in angulos]
    altura_maxima = max(alturas)
    angulo_maximo = angulos[np.argmax(alturas)]
    return angulos, alturas, angulo_maximo, altura_maxima

def graficar_tiro_parabolico(v, color, label, ax):
    angulos, alturas, angulo_maximo, altura_maxima = generar_datos(v)
    ax.plot(angulos, alturas, label=label, color=color)
    ax.scatter([angulo_maximo], [altura_maxima], color=color)
    ax.text(angulo_maximo, altura_maxima, f'({angulo_maximo}°, {altura_maxima:.2f} m)', fontsize=9, ha='right')
    ax.set_xlabel('Ángulo de lanzamiento (°)')
    ax.set_ylabel('Altura máxima (m)')
    ax.grid(True)
    ax.legend()
    ax.set_xticks(np.arange(0, 91, 5))  # Configura los ticks del eje x de 5 en 5

def solicitar_velocidad(mensaje):
    while True:
        try:
            v = float(input(mensaje))
            return v
        except ValueError:
            print("Por favor, ingrese un número válido.")

def preguntar_repetir():
    while True:
        respuesta = input("¿Desea ingresar nuevas velocidades? (s/n): ").strip().lower()
        if respuesta in ['s', 'n']:
            return respuesta
        else:
            print("Respuesta no válida. Por favor, ingrese 's' para sí o 'n' para no.")

def main():
    while True:
        # Solicitar velocidades iniciales al usuario
        v1 = solicitar_velocidad("Ingrese la primera velocidad inicial (m/s): ")
        v2 = solicitar_velocidad("Ingrese la segunda velocidad inicial (m/s): ")

        # Crear figura y ejes con gridspec
        fig = plt.figure(figsize=(12, 10))
        gs = GridSpec(2, 2, height_ratios=[1, 2])

        # Gráfica para la primera velocidad (fila 0, columna 0)
        ax1 = fig.add_subplot(gs[0, 0])
        graficar_tiro_parabolico(v1, 'blue', f'Velocidad {v1} m/s', ax1)
        ax1.set_title(f'Tiro parabólico con velocidad {v1} m/s')

        # Gráfica para la segunda velocidad (fila 0, columna 1)
        ax2 = fig.add_subplot(gs[0, 1])
        graficar_tiro_parabolico(v2, 'green', f'Velocidad {v2} m/s', ax2)
        ax2.set_title(f'Tiro parabólico con velocidad {v2} m/s')

        # Gráfica comparativa (fila 1, columna 0 y 1 combinadas)
        ax3 = fig.add_subplot(gs[1, :])
        graficar_tiro_parabolico(v1, 'blue', f'Velocidad {v1} m/s', ax3)
        graficar_tiro_parabolico(v2, 'green', f'Velocidad {v2} m/s', ax3)
        ax3.set_title('Comparación de tiros parabólicos')

        # Ajustar espaciado entre subplots
        plt.tight_layout()

        # Mostrar las gráficas
        plt.show()

        # Preguntar si el usuario quiere ingresar nuevos datos
        repetir = preguntar_repetir()
        if repetir != 's':
            break

if __name__ == "__main__":
    main()
