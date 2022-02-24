class Animal:
    def breathe(self):
        print("breathing")
class Fish(Animal):
    def breathe(self):
        super().breathe()
        print("underwater")

nemo = Fish()
nemo.breathe()