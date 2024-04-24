import uuid

import qrcode


class Pix:

    def __init__(self) -> None:
        pass

    def create_payment(self):
        # criar pagamento na instituição financeira
        bank_payment_id = str(uuid.uuid4())

        # copia e cola
        hash_payment = f'hash_payment_{bank_payment_id}'

        # qr code
        img = qrcode.make(hash_payment)

        # definir caminho das imagens e sua extensão
        img.save(f"src/static/img/qr_code_payment_{bank_payment_id}.png")

        return {
            "bank_payment_id":  bank_payment_id,
            "qr_code_path": f"qr_code_payment_{bank_payment_id}",
        }
