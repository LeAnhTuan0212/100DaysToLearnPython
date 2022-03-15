# Function with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")
    
greet_with("Jack Bauer", "Nowhere")
greet_with("Nowhere", "Jack Bauer")

greet_with(name="Angela", location="London")
greet_with(location="London", name="Angela")