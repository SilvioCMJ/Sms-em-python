import boto3

mensagem = 'msg de exemplo'
numero = '+551111111111'
client = boto3.client(service_name='sns', region_name='regiao example', aws_access_key_id='key de acesso',
                      aws_secret_access_key='key secreta')
# enviando sms
client.publish(PhoneNumb=numero, Message=mensagem)
