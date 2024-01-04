from flask import Flask, request, jsonify
import pika

app = Flask(__name__)

def enviar_mensagem_para_fila(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='fila_exemplo')

    channel.basic_publish(exchange='', routing_key='fila_exemplo', body=message)

    print(f"[x] Mensagem enviada: {message}")
    connection.close()

@app.route('/enviar-mensagem', methods=['POST'])
def enviar_mensagem():
    data = request.get_json()

    if 'mensagem' not in data:
        return jsonify({'error': 'O campo "mensagem" é obrigatório'}), 400

    mensagem = data['mensagem']
    enviar_mensagem_para_fila(mensagem)

    return jsonify({'status': 'Mensagem enviada para a fila'}), 200

if __name__ == '__main__':
    app.run(debug=True)
