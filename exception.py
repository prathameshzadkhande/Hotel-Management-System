class room_exist_err(Exception):
    def __init__(self,rid):
        self.rid = rid

    def __str__(self) :
        data = f"Room {self.rid} is already exist"
        return data