import cv2
import pydicom
from matplotlib import pyplot as plt


# Cargar la imagen DICOM
ds = pydicom.dcmread('0012.DCM')

# Convertir la imagen DICOM en una matriz numpy
img = ds.pixel_array[0]

# Aplicar el algoritmo de Canny para detección de bordes
edges = cv2.Canny(img, 50, 100)

# Mostrar la imagen resultante con los bordes detectados
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Imagen original'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Bordes en la imagen'), plt.xticks([]), plt.yticks([])
plt.show()
