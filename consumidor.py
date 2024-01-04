import pika

def callback(ch, method, properties, body):
    print(f"[x] Mensagem recebida: {body}")

def consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='fila_exemplo')

    channel.basic_consume(queue='fila_exemplo', on_message_callback=callback, auto_ack=True)

    print('[*] Aguardando mensagens. Para sair pressione CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    consumer()
