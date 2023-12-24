class Computer:
    def __init__(self):
        self.CPU = None
        self.RAM = None
        self.hardDrive = None
        self.graphicsCard = None
        # Add other components as needed

    def __str__(self):
        return f"CPU: {self.CPU}, RAM: {self.RAM}, Hard Drive: {self.hardDrive}, Graphics Card: {self.graphicsCard}"

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def setCPU(self, cpu):
        self.computer.CPU = cpu
        return self

    def setRAM(self, ram):
        self.computer.RAM = ram
        return self

    def setHardDrive(self, hardDrive):
        self.computer.hardDrive = hardDrive
        return self

    def setGraphicsCard(self, graphicsCard):
        self.computer.graphicsCard = graphicsCard
        return self

    def build(self):
        return self.computer

# Example of using the builder to create a computer
builder = ComputerBuilder()
my_computer = builder.setCPU("Intel i7").setRAM("16GB").setHardDrive("1TB SSD").setGraphicsCard("NVIDIA GTX 3080").build()
print(my_computer)
