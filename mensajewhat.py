from heyoo import WhatsApp
messenger = WhatsApp('TOKEN',phone_number_id='IDDEL NUMERO DE TELEFONO')
messenger.send_message('mensaje','numero de telefono')
print('Mensaje enviado')