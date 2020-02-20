import logging
from api import PixabayAPI
import concatenacion
import archivos

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

#api.listaDeImagenes()
#carpeta_imagenes = './imagenes'
carpeta_imagenes = '/home/concurrente/Documentos/AEOtero/python-manipulando-imagenes-aeotero/imagenes'
query = 'vehiculo militar'
api = PixabayAPI('15310851-8beba4d80305d85650c9c7cc2', carpeta_imagenes)





logging.info(f'Buscando imagenes de {query}')
urls = api.buscar_imagenes(query, 6)

for u in urls:
  logging.info(f'Descargando {u}')
  api.descargar_imagen(u)

for u in range (0,6,6): #"""len(api.listaDeImagenes)"""
  imagen1 = archivos.leer_imagen(api.listaDeImagenes[u])
  imagen2 = archivos.leer_imagen(api.listaDeImagenes[u+1])
  imagen3 = archivos.leer_imagen(api.listaDeImagenes[u+2])
  imagen4 = archivos.leer_imagen(api.listaDeImagenes[u+3])
  imagen5 = archivos.leer_imagen(api.listaDeImagenes[u+4])
  imagen6 = archivos.leer_imagen(api.listaDeImagenes[u+5])
  archivos.escribir_imagen('concatenada-vertical.jpg', concatenacion.concatenar_vertical([imagen1, imagen2, imagen3]))    
  archivos.escribir_imagen('concatenada-horizontal.jpg', concatenacion.concatenar_horizontal([imagen4, imagen5, imagen6]))    