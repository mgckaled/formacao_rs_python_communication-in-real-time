from repository.database import db


class Payment(db.Model):
    """
    Represents a payment with the following attributes:
    - id: Integer, primary key
    - value: Float
    - paid: Boolean, default is False
    - bank_payment_id: Integer, nullable
    - qr_code: String, nullable
    - expiration_date: DateTime

    Methods:
    - to_dict(): Returns a dictionary representation of the Payment object.
    """

    __tablename__ = 'payment'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float)
    paid = db.Column(db.Boolean, default=False)
    bank_payment_id = db.Column(db.String(200), nullable=True)
    qr_code = db.Column(db.String(100), nullable=True)
    expiration_date = db.Column(db.DateTime)

    def __init__(self, value, expiration_date):
        self.value = value
        self.expiration_date = expiration_date

    def to_dict(self):
        """
    Converts the Payment object into a dictionary representation.

    Returns:
        dict: A dictionary containing the following attributes of the Payment object:
            - id (int): The primary key of the payment.
            - value (float): The value of the payment.
            - paid (bool): Indicates whether the payment is paid or not.
            - bank_payment_id (int or None): The ID of the bank payment (if available).
            - qr_code (str or None): The QR code associated with the payment (if available).
            - expiration_date (datetime.datetime or None): The expiration date of the payment.
    """
        return {
            "id": self.id,
            "value": self.value,
            "paid": self.paid,
            "bank_payment_id": self.bank_payment_id,
            "qr_code": self.qr_code,
            "expiration_date": self.expiration_date,
        }
