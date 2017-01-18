import matplotlib.pyplot as plt
import numpy as np

def plot(data, ndim):
    """Erzeuge eine zweidimensionale Grafik auf einem
       Raster von ndim×ndim Punkten. Die in der Liste data
       übergebenen Daten bestimmen die Farbe an dem
       jeweiligen Gitterpunkt und müssen zwischen 0 und
       1 liegen. Die Daten aus der Liste werden in Zeilen
       von Farbpunkten umgesetzt, die von unten nach oben
       in der Abbildung dargestellt werden.

    """
    Farbschema = "hot"
    plt.imshow(np.array(data).reshape((ndim, ndim)),
               cmap = Farbschema, origin="lower")
    plt.show()

# Initialisierung der benötigten Variablen
zoom = 0.5
xmin = -1/zoom
xmax = 1/zoom
ymin = -1/zoom
ymax = 1/zoom
Schwellwert  = 2
Max_Iteration = 75
seitenlaenge = 500
Schrittweite = (xmax-xmin)/seitenlaenge
# diese Liste soll die erzeugten Daten enthalten 
mandelbrot_data = []

# Schleifen über die Startwerte und Abarbeitung der
# Iterationsvorschrift
for ny in range(seitenlaenge):
    y = ymin+ny*Schrittweite
    for nx in range(seitenlaenge):
        x = xmin+nx*Schrittweite
        c = complex(x,y)
        z=0
        for n in range(Max_Iteration):
            z = z**2+c
            if abs(z) > Schwellwert:
                break
        farbe = n/Max_Iteration
        
   # Anhängen des neuen Farbwerts an die Liste
        mandelbrot_data.append(farbe)
# Erstellung der Grafik
plot(mandelbrot_data, seitenlaenge)
#print(julia_daten)