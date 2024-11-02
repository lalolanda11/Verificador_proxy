#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import os
from io import open
import time
import sys
import time
print(sys.platform)
print('ESpera un momento ......')
time.sleep(2)

#sitio='https://free-proxy-list.net/'

sitio='http://free-proxy.cz/en/proxylist/country/all/all/ping/all'
def respuesta():
	res=requests.get(sitio)
	sp=BeautifulSoup(res.content,'html.parser')
	fd=sp.find_all('script',{"type":'text/javascript'})
	for i in fd:
		et=i.get_text()[30:46]
		print(et)
	#for x in et:
		#for i in x:
			#print(i)

def rasp():
	res=requests.get(sitio)
	sp=BeautifulSoup(res.content,'html.parser')
	fd=sp.find_all("div",{'class':"modal-body"})
	print(fd)
	for y in fd:
		variable=y.find('textarea')
		#print(y)
		num=str(variable)
		abrir=open('proxies.txt','w')
		abrir.write(num)
		abrir.close()
		dato=open("proxies.txt","r").readlines()
		abrir=open("proxies.txt","w")
		for i in dato[3:299]:
			
			abrir.write('socks4'+"	"+str(i).replace(":",'	'))
			abrir.flush()
		#abrir.write(str(dato[3:299]))
		abrir.close()

		#dato=open("proxies.txt","r").readlines()
		#abrir=open("proxies.txt","w")
		

		print('Se han guardado los proxies')
if __name__=='__main__':
	print('[a] para checar los proxys mas recientes\n[b] para guardarlos')
	opcion=input('introduce la opcion :')
	if opcion == 'a':
		respuesta()
	elif opcion =='b':
		rasp()
	elif opcion =='':
		print('finalizo el programa')
