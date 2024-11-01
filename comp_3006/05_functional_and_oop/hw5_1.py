import math

class Quadratic:
    def __init__(self, a, b, c):
        """Class constructor for Quadratic."""
        self.a = a
        self.b = b
        self.c = c
        self.discriminant()
        
    def __repr__(self):
        """Returns the 'official' string representation or canonical representation of Quadratic class in string form."""
        return f'Quadratic({self.a}, {self.b}, {self.c})'
    
    def __str__(self):
        """Returns the 'unofficial' string representation of Quadratic class"""
        return f'Quadratic(a: {self.a}, b: {self.b}, c: {self.c})'
    
    def discriminant(self):
        """Calculates the class attribute, discriminant, of the quadratic equation, b^2-4ac"""
        self.discriminant = self.b**2 - 4*self.a*self.c
    
    def roots(self):
        """Returns the 2 roots of the quadratic polynomial."""
        try:
            # two real solutions
            if self.discriminant > 0:
                root_1 = (-self.b + math.sqrt(self.discriminant))/(2*self.a)
                root_2 = (-self.b - math.sqrt(self.discriminant))/(2*self.a)
                return root_1, root_2
            # one real solution
            elif self.discriminant == 0:
                root = (-self.b + math.sqrt(self.discriminant))/(2*self.a)
                return root
            # no real solution
            else:
                raise ValueError
        except ZeroDivisionError:
            print(f'Coefficient a cannot be 0.')
        except ValueError:
            print(f'No real solutions to', self)    
        
            
if __name__ == '__main__':
    
    # discriminant > 0 (two real solutions)
    eq = Quadratic(1, -5, 6)
    roots = eq.roots()
    assert roots == (3.0, 2.0)
    print(f"Test Case #1:\n{eq}\nroots:{roots}\n{'--- ' * 15}")
    
    # discriminant == 0 (one real solution)
    eq = Quadratic(1, -4, 4)
    roots = eq.roots()
    assert roots == 2.0
    print(f"Test Case #2:\n{eq}\nroots:{roots}\n{'--- ' * 15}")

    # discriminant < 0 (no real solutions)
    eq = Quadratic(1, 2, 5)
    roots = eq.roots()
    assert roots is None
    print(f"Test Case #3:\n{eq}\nroots:{roots}\n{'--- ' * 15}")

    print("All tests passed!")
