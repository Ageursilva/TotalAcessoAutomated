from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import tkinter as tk
from threading import Thread
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://cart.totalacesso.com/saopaulofcxflamengocopabetanodobrasil2023_24_09_23") #Este é o link do jogo, mas pode alterar para outros jogo, se quiser

driver.implicitly_wait(10)

paused = False  
can_refresh = True  
pause_button = None
continue_button = None
cpf_value = "11111111" #Coloque seu CPF sem pontos aqui   

def toggle_pause():
    global paused, can_refresh
    paused = not paused
    if paused:
        pause_button.config(state=tk.DISABLED)
        continue_button.config(state=tk.NORMAL)
    else:
        pause_button.config(state=tk.NORMAL)
        continue_button.config(state=tk.DISABLED)
        can_refresh = True 

intervalo = 20  
tempo_inicial = time.time()  
cliques_no_botao = 0  
limite_de_cliques = 3  

def execute_script():
    global can_refresh, tempo_inicial, cliques_no_botao
    try:
        while True:
            if not paused:
                try:
                    campo = driver.find_element(By.CSS_SELECTOR, 'input[data-cy="promocode-input"]')
                    current_value = campo.get_attribute("value")
                    if current_value != cpf_value:
                        campo.clear()
                        campo.send_keys(cpf_value)
                except Exception as e:
                    pass

                try:
                    botao = driver.find_element(By.CSS_SELECTOR, 'button[data-cy="promocode-button"]')
                    
                    WebDriverWait(driver, 5).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'div.swal2-container')))
                    botao.click()
                    cliques_no_botao += 1
                except Exception as e:
                    pass

                tempo_passado = time.time() - tempo_inicial
                if cliques_no_botao >= limite_de_cliques:
                    cliques_no_botao = 0
                    driver.execute_script("location.reload(true);")  
                    tempo_inicial = time.time()  
                    can_refresh = False
    except KeyboardInterrupt:
        pass

script_thread = Thread(target=execute_script)
script_thread.daemon = True
script_thread.start()


root = tk.Tk()
root.title("Controle do Script")
root.geometry("200x100")

pause_button = tk.Button(root, text="Pausar", state=tk.NORMAL, command=toggle_pause)
continue_button = tk.Button(root, text="Continuar", state=tk.DISABLED, command=toggle_pause)

pause_button.pack(pady=10)
continue_button.pack()

root.mainloop()

driver.quit()