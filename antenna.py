class antenna:
    def __init__(self, name: str, part_num: int, serial_num: int) -> None:
        self.name = name
        self.part_num = part_num
        self.serial_num = serial_num
    
    def set_name(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name
    
    def set_part_num(self, part_num: int):
        self.part_num = part_num

    def get_part_num(self) -> int:
        return self.part_num

    def set_serial_num(self, serial_num: int):
        self.serial_num = serial_num

    def get_serial_num(self) -> int:
        return self.serial_num
