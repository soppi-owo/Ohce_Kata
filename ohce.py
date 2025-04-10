from datetime import datetime

class Ohce:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        hour = datetime.now().hour
        if 6 <= hour < 12:
            return f"¡Buenos días {self.name}!"
        elif 12 <= hour < 20:
            return f"¡Buenas tardes {self.name}!"