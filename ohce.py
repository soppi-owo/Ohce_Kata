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
        else:  # 20-6
            return f"¡Buenas noches {self.name}!"
        
    def process_input(self, text):
        reversed_text = text[::-1]
        if text == reversed_text:
            return f"{reversed_text}\n¡Bonita palabra!"
        return reversed_text