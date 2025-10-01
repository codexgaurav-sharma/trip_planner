class Calculator:
    @staticmethod
    def multiply(a: float, b: float) -> float:
        """
        Multiply two numbers.
        
        Args:
            a (float): The first number.
            b (float): The second number.
        
        Returns:
            float: The product of a and b.
        """
        return float(a) * float(b)
    
    @staticmethod
    def calculate_total(*x: float) -> float:
        """
        Calculate sum of the given list of numbers
        
        Args:
            x (list): List of floating numbers
            
        Returns:
            float: The sum of numbers in the list x.
        """
        return sum(x)
    
    
    @staticmethod
    def calculate_daily_budget(total: float, days: int) -> float:
        """
        Calculate daily budget 
        
        Args:
            total (float): Total cost.
            days (int): Number of days.
            
        Returns:
            float: Expense for a single Day.
        """
        
        return total / days if days > 0 else 0
    