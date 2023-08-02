from WPP_Whatsapp import Create

# start client with your session name
your_session_name = "test"
creator = Create(session=your_session_name)
client = creator.start()
# Now scan Whatsapp Qrcode in browser

# check state of login
if creator.state != 'CONNECTED':
    raise Exception(creator.state)


def new_message(message):
    global client
    # Escreva seu Codigo aqui

    print(message)
    msg = ('_Ola sou um Atendente do whatsapp:_'
           '\n\n'
           'O que posso fazer por você? *Escolha uma Opção* \n\n'
           '0 - Sair \n'
           '1 - Fazer Pedido\n'
           '2 - Status do pedido \n'
           '3 - Cadastro\n\n'
           '_Obrigado por ser nosso cliente')

    if message and not message.get("isGroupMsg"):
        chat_id = message.get("from")
        message_id = message.get("id")
        if "start" in message.get("body").lower():

            client.reply(chat_id, f"{msg}", message_id)
        else:
            client.reply(chat_id, f"{msg}", message_id)


# aqui ficara ouvindo todas as mensagens novas
creator.client.onMessage(new_message)
