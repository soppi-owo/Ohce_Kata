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
        if text == "Stop!":
            return f"Adios {self.name}"
        reversed_text = text[::-1]
        if text == reversed_text:
            return f"{reversed_text}\n¡Bonita palabra!"
        return reversed_text
    
    def run(self):
        print(self.greet())
        while True:
            text = input("$ ")
            result = self.process_input(text)
            print(result)
            if text == "Stop!":
                break

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Uso: python ohce.py <nombre>")
    else:
        ohce = Ohce(sys.argv[1])
        ohce.run()