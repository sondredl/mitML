import math as ma

def main():
    row_vector = Vector(VectorType.Row)
    row_vector.set_values(1,2,3)
    print(row_vector)
    
    column_vecor = Vector(VectorType.Column)
    column_vector.set_values(4,5,6)
    pass

class VectorType(Enum):
    row = 1
    column = 2

class Vector:
    def __init__(self, vector_type):
        self.vector_type = vector_type
        self.values = []
    
    def set_values(self, *args):
        if(self.vector_type == VectorType.Row:
            self.values = list(args)
        elif(self.vector_type == VectorType.Column:
            self.values = [args[0] for _ in range(len(args))]

    def __str__(self):
        return f"Type: {self.vecotr_type}
        

if __name__ == "__main__":
    main()
