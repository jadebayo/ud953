import math
from decimal import Decimal, getcontext

getcontext().prec = 30


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates
    
    def magnitude(self):
        coord_squared = [x**2 for x in self.coordinates]
        return sum(coord_squared).sqrt()

    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.mult_scalar(Decimal('1.0')/magnitude)   
        except ZeroDivisionError:
            raise Exception('cannot normalized the zero vector') 
    
    def plus(self, v):
        result = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(result)

    def minus(self, v):
        result = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(result)

    def mult_scalar(self, scale):
        result = [Decimal(scale) * x for x in self.coordinates]
        return Vector(result)    

    def dot(self, v):
        return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])
    
    def angle_with(self, v, in_degrees=False):
        self_norm = self.normalized()
        angle = math.acos(self_norm.dot(v.normalized()))
        if(in_degrees):
            return math.degrees(angle)
        else:
            return angle

    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance

    def is_orthogonal_to(self, v, tolerance=1e-10):
        return abs(self.dot(v)) < tolerance

    def is_parallel_to(self, v):
        angle = self.angle_with(v)
        return (self.is_zero() or v.is_zero() or angle == 0 or angle == math.pi)
        



