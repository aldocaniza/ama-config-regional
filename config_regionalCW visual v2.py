import pyautogui
import time
import os
import locale


def main():
    ##if not verificarconfig():
    locale.setlocale(locale.LC_ALL, '')
    verificarconfig()
    

def verificarconfig():
      # Obtiene la configuración regional actual
    conv = locale.localeconv()
    ##print(conv)
    
    # Verifica los separadores de decimales y miles
    decimal_sep = conv['decimal_point']
    
    if decimal_sep == '.':
        print("Cambiando a Contawin.")
        config_regional(',', '.')
        return True
    else:
        print("Cambiando a Nodum.")
        config_regional('.', ',')
        return False


def config_regional(decimal, miles):
        
    # Abre la Configuración Regional de Windows
    os.system("control.exe /name Microsoft.RegionAndLanguage")

    # Espera un momento para que la ventana de Configuración Regional de Windows aparezca
    time.sleep(2)

    # Cambia a la pestaña "Adicionales"
    pyautogui.press('tab', presses=8, interval=0.2)
    pyautogui.press('enter')
    time.sleep(1)

    # Cambia el separador de decimales a ","
    pyautogui.write(decimal)
    pyautogui.press('tab', presses=2, interval=0.2)

    # Cambia el separador de miles a "."
    pyautogui.write(miles)

    # Guarda los cambios y cierra la Configuración Regional de Windows
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('tab', presses=1, interval=0.2)
    pyautogui.press('enter')
    pyautogui.hotkey('alt', 'f4')

if __name__ == "__main__":
    main()