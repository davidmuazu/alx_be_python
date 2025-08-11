class Calculator:
    # Class attribute shared by all instances
    calculation_type = "Arithmetic Operations"

    # Static Method
    @staticmethod
    def add(a, b):
        """
        note
        This method doesn't need access to the class (cls)
        or instance (self). It simply performs an addition.
        """
        return a + b

    # Class Method
    @classmethod
    def multiply(cls, a, b):
        """
        This method needs access to the class itself (cls)
        so it can use the class attribute 'calculation_type'.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
