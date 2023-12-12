import requests
import time

print('Esta es una herramienta para verificar qué proxy está funcional')
print(time.ctime(), '==> xela-stone')
print('[x] http\n[y] socks4\n[z] socks5')
proto = input('Ingresa los valores ->: ')

if proto == 'x':
    proto = 'http'
elif proto == 'y':
    proto = 'socks4'
elif proto == 'z':
    proto = 'socks5'

ruta = input('Introduce la ruta de los proxys ->: ')
nombre = input('Introduce el nombre del archivo ->: ')

# Abre el archivo y prueba línea por línea
with open(ruta + nombre) as archivo:
    lineas = archivo.readlines()
    lineas = [x.strip() for x in lineas]

for linea in lineas:
    proxies = {f"http": f"{proto}://{linea}"}
    try:
        res = requests.get("https://canihazip.com/", proxies=proxies, timeout=2)
        if res.status_code == 200:
            print('El proxy está vivo: {}'.format(linea))
            with open('proxys_vivos.txt', 'a') as proxy_vivo:
                proxy_vivo.write(linea + '\n')
        else:
            print('El proxy está muerto: {}'.format(linea))
            with open('proxys_muertos.txt', 'a') as proxy_muerto:
                proxy_muerto.write(linea + '\n')
    except KeyboardInterrupt:
        print('Finalizado por el usuario')
        break
    except Exception as e:
        print(f"Error al verificar el proxy {linea}: {str(e)}")
        pass
