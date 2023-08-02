from WPP_Whatsapp import Create # importando o create da biblioteca

# start client with your session name
your_session_name = "test"
creator = Create(session=your_session_name) # Criando uma nova sessão do whatsapp
client = creator.start()
# Now scan Whatsapp Qrcode in browser

# check state of login
if creator.state != 'CONNECTED':
    raise Exception(creator.state) # Retorno sobre a leitura do qrcode


def new_message(message): # definindo uma função
    global client
    # Escreva seu Codigo aqui

    print(message)

    # Essa variavel é o texto que sera enviada para o usuario
    msg = ('_Ola sou um Atendente do whatsapp:_'
           '\n\n'
           'O que posso fazer por você? *Escolha uma Opção* \n\n'
           '0 - Sair \n'
           '1 - Fazer Pedido\n'
           '2 - Status do pedido \n'
           '3 - Cadastro\n\n'
           '_Obrigado por ser nosso cliente')

    if message and not message.get("isGroupMsg"): # codição que ve se é grupo ou não
        chat_id = message.get("from") # pega o id do usuario para encaminhar a resposta
        message_id = message.get("id") # Pega o id da message
        if "start" in message.get("body").lower(): # se a mensagem do usuario for start ele responde

            client.reply(chat_id, f"{msg}", message_id)
        else:
            client.reply(chat_id, f"{msg}", message_id)



# aqui ficara ouvindo todas as mensagens novas
creator.client.onMessage(new_message) #fica ouvindo as novas mensagens
