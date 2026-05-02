from datetime import datetime

class GreetingAgent:
    def greet(self, name: str = "User"):
        hour = datetime.now().hour
        
        if hour < 12:
            return f"Good morning, {name}!"
        elif hour < 18:
            return f"Good afternoon, {name}!"
        else:
            return f"Good night, {name}!"