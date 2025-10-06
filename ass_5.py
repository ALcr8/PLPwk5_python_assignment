class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery   
    def call(self, number):
        return f"Calling {number} from {self.brand} {self.model}..."
    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        return f"Battery charged to {self.battery}%."

# Inheritance Example (Smartphone → GamingPhone)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery, gpu_power):
        super().__init__(brand, model, battery)
        self.gpu_power = gpu_power
    
    def play_game(self, game):
        if self.battery > 10:
            self.battery -= 10
            return f"Playing {game} on {self.brand} {self.model} 🎮 (GPU: {self.gpu_power})"
        else:
            return "Battery too low to play!"

# Example usage
phone1 = Smartphone("Samsung", "Galaxy S23", 80)
print(phone1.call("08012345678"))
print(phone1.charge(15))

gaming_phone = GamingPhone("Asus", "ROG Phone 7", 50, "High-end GPU")
print(gaming_phone.play_game("Call of Duty"))
print(gaming_phone.charge(30))
