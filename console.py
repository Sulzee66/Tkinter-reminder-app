import cmd
from base import Reminder
import json
from countdown import count

def parse(arguments):
    return arguments.split(" ")


class ReminderCmd(cmd.Cmd):
    prompt = "(Reminder)"

    def default(self, arg):
        print("**Invalid Syntax**")

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True
    
    def emptyline(self):
        """
        do nothing on empty line
        """
        pass

    

    def do_show(self, arg):
        """
        show: displays all set alarms
            Usage
                show
        """
        # reload data from file
        with open("file.json", "r") as f:
            data = json.load(f)
        
        for key, value in data.items():
            print(f"{key} : {value}")
    
    def do_start(self, arg):
        """
        start: begins countdown for the alarm
            Usage
                start
        """
        count()
        ReminderCmd().cmdloop()

if __name__ == "__main__":
    ReminderCmd().cmdloop()