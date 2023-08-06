# MailRobot
Made by Guilherme Romano in 2023

English:
   MailRobot.py - In development
    A Python script that sends a WhatsApp message whenever an email arrives in Outlook.

    Description:
        Using Selenium and webdriver_manager, the program opens a valid instance in Google Chrome and accesses the WhatsApp Web URL. Then, it moves to a second monitor and maximizes the window, waiting for the user to press the keys "ctrl+alt". This avoids potential delays due to internet access that could cause bugs and ensures the WhatsApp update message is displayed. After the user input, the cursor is moved, and a click updates WhatsApp. The program then waits for the user input again. After the update and the message to enable browser notifications, the cursor moves and closes the message, moves to click on the pinned group, clicks on the text box, writes and sends the message "AnonDesk Online!" signaling that everything is ready for notification monitoring.

    Functions:
        notification_action:
            Responsible for sending the message, receiving the content to be written, moving the cursor to the text box, clicking, typing the message, and sending it.

        Wait_for_key_combination:
            Receives a key press or a combination of keys, and performs a specific action or none, making the program continue only after pressing the specified keys.

    Uncompleted Challenges:
        1. Access to Windows notifications:
            Due to the fact that my Operating System is Windows 11, I couldn't find a solution to utilize Windows notifications. I tried using the win11toast and winsdk libraries to access Windows 11 notifications, which would have allowed me to expand the idea to receive notifications on WhatsApp whenever any notification occurred.

    Libraries:
        Selenium, webdriver_manager, time, pyautogui, and keyboard.

Português:
    
    MailRobot.py - Em desenvolvimento
        Um script em python que manda uma menssagem no whatsapp sempre que um chegar um email no outlook.

        Descrição:
            Utilizando o selenium e o webdriver_manager, o programa abre uma instância valida no Google Chrome e acessa a URL do Whatsapp Web
            em seguida move para uma segundo monitor e faz com que a janela seja maximizada, aguarda o input de pressionar as teclas ctrl+alt,
            evitando que possiveis demoras devido ao aceso à internet não gerem bugs e para que a mensagem para atualizar o whatsapp seja exibida,
            após o input, o cursor é movido e ocorre o clique para que whatsapp seja atualizado e novamente aguarda o input do usuario,
            após a atualização e a mensagem para abilitar a notificação no navegador, o cursor se move e fecha a mensagem, se move e clica no grupo fixado,
            se move e clica na caixa de texto e escreve e envia a mensagem "AnonDesk Online!", sinalizando que está tudo de acordo e que pode-se começar o monitoramento de notificações.

        Funções:
            notification_action
                Responsavel pelo envio da mensagem, recebendo como variavel o conteudo que será escrito, movendo o cursor para a caixa de texto, clicando, digitando a mensagem e enviando.

            Wait_for_key_combination
                Recebe como variavel o precionar de uma tecla ou como nessa aplicação, uma combinação de teclas, e executa uma determinada ação ou nehuma, fazendo com que o programa só continue após o precionar das teclas determinadas.
            

        Desafios não concluidos:
            1. Acesso a notifação do Windows
                Devido ao fato de meu Sistema Operacional ser o Windows 11, näo achei uma solução para utilizar as notificações do Windows, tentei com a biblioteca win11toast e a winsdk,
                utilizando as notifcações do win11, seria possivel expandir a ideia para todas as notificações, fazendo com que eu fosse notificado no whatsapp sempre que uma notificação ocorresse. 
        
        Bibliotecas:
            Selenium, webdriver_menager, time, pyautogui e keyboard.