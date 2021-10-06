import uuid
import datetime
from utils.data import generate_random_float, generate_random_int

class SampleData:

    def __init__(self):
        self.id = generate_random_int(1000000)
        self.reference_id = generate_random_int(1000000)
        self.relation_id = str(uuid.uuid4())
        self.created_date = datetime.datetime.today()
        self.amount = generate_random_float(2)
        self.fee_amount = generate_random_float(2)

    @staticmethod
    def get_headers() -> tuple:
        return (
            "Id",
            "Reference Id",
            "Relation Id ",
            "Created Date",
            "Amount",
            "Fee Amount"
        )