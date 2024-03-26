from shape import Shape

class Circle(Shape):
    def __init__(self, color_entered, added_by_entered, radius_entered):
        super().__init__(color_entered, added_by_entered)
        self.radius = radius_entered
    def report(self):
        return f"Reporting for shape of color: {self.color}"
    def area(self):
        super().area()
        return 3.142 * self.radius * self.radius
    
circle1 = Circle("Yellow", "Shukri", 24)
print(circle1.area())