"""

"""
from datetime import datetime
import antenna

class Record:
    def __init__(self, record_num: int, title: str, place: str, date_time: datetime,
                operator: str, test_antenna: antenna, unit_under_test: antenna,
                reference_level: float, reference_position: float, scale: float,
                remarks: str, start: int, stop: int, insertion_loss: bool,
                field_notes:str, record_type: int) -> None:
        self.record_num = record_num
        self.title = title
        self.place = place
        self.date_time = date_time
        self.operator = operator
        self.test_antenna = test_antenna
        self.unit_under_test = unit_under_test
        self.reference_level = reference_level
        self.reference_position = reference_position
        self.scale = scale
        self.remarks = remarks
        self.start = start
        self.stop = stop
        self.insertion_loss = insertion_loss
        self.field_notes = field_notes
        self.record_type = record_type