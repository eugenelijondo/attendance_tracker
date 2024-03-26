class Shape:
    def __init__(self, color_entered, added_by_entered):
        self.color = color_entered
        self.added_by = added_by_entered
    def area(self):
        return f"The area of the shape is: "
    def report(self):
        return (f"The color of the shape reported is of color: {self.color}")
    def report_author(self):
        return (f"The shape was reported by: {self.added_by}")

shape1 = Shape(color_entered="red", added_by_entered="Mercy")
print(shape1.area())