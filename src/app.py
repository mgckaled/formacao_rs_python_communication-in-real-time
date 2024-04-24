import os
from datetime import datetime, timedelta

from flask import Flask, jsonify, request

from db_models.payment import Payment
from repository.database import db

app = Flask(__name__)

# Obtendo o caminho absoluto para a pasta src
src_dir = os.path.abspath(os.path.dirname(__file__))

# Definindo o caminho para o banco de dados dentro da pasta src
database_file = os.path.join(src_dir, "instance", "database.db")

# Configurando o URI do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{database_file}"
app.config['SECRET_KEY'] = 'SECRET_KEY_WEBSOCKET'

db.init_app(app)


@app.route('/payments/pix', methods=['POST'])
def create_payment_pix():
    data = request.get_json()

    if 'value' not in data:
        return jsonify({"message": "invalid value"}), 400

    expiration_date = datetime.now() + timedelta(minutes=30)

    new_payment = Payment(value=data['value'], expiration_date=expiration_date)

    db.session.add(new_payment)
    db.session.commit()

    return jsonify({
        "message": "The payment has been created",
        "payment": new_payment.to_dict(),
    })


@app.route('/payments/pix/confirmation', methods=['POST'])
def confirmation_pix():
    return jsonify({"message": "The payment has been confirmed"})


@app.route('/payments/pix/<int:payment_id>', methods=['GET'])
def payment_pix_page(payment_id):
    return 'pagamento pix'


if __name__ == '__main__':
    app.run(debug=True)
