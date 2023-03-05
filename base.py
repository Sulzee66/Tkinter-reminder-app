"""
contains the functionality for the reminder app
"""
import json

class Reminder:

    # private instance attributes
    __file_path = "file.json"
    __objects = {}

    def __init__(self, hour, minute, message):
        self.hour = hour
        self.minute = minute
        self.message = message
        self.save()

    def save(self):
        json_obj = {}
        with open(Reminder.__file_path, "w") as f:
            # store dictionary data of reminder
            key = "alarms"
            Reminder.__objects.update(self.__dict__)
           # json_obj[key] = Reminder.__objects
            json.dump(Reminder.__objects, f)