from code_executor import CodeExecutor
        
codeExecutor = CodeExecutor()

def add(a, b):
        """Adds two numbers and prints the result.

        This method dynamically generates and executes code to add two numbers.
        If an exception occurs during the addition, it catches the exception and 
        prints an error message.

        Parameters:
            a (int or float): The first number to add.
            b (int or float): The second number to add.

        Returns:
            The printable result of the addition operation.
        """
        
        code = f"""
try:
    result = {a} + {b}
except Exception as e:
    result = f'ERROR: {{e}}'
"""
        codeExecutor.execute(code)
        return codeExecutor.print_var('result')
        
def subtract(a, b):
    """Subtracts the second number from the first and prints the result.
    
    This method dynamically generates and executes code to subtract the second number
    from the first number. If an exception occurs during the subtraction, it catches
    the exception and prints an error message.
        
    Parameters:
        a (int or float): The first number.
        b (int or float): The second number.
        
    Returns:
        The printable result of the subtraction operation.
    """
        
    code = f"""
try:
    result = {a} - {b}
except Exception as e:
    result = f'ERROR: {{e}}'
"""
    codeExecutor.execute(code)
    return codeExecutor.print_var('result')
    
def multiply(a, b): 
    """Multiplies two numbers and prints the result.
    
    This method dynamically generates and executes code to multiply two numbers.
    If an exception occurs during the multiplication, it catches the exception and
    prints an error message.
    
    Parameters:
        a (int or float): The first number.
        b (int or float): The second number.
        
    Returns:
        The printable result of the multiplication operation.
    """
    
    code = f"""
try:
    result = {a} * {b}
except Exception as e:
    result = f'ERROR: {{e}}'
"""
    codeExecutor.execute(code)
    return codeExecutor.print_var('result') 
    
def divide(a, b):
    """Divides the first number by the second and prints the result.
    
    This method dynamically generates and executes code to divide the first number
    by the second number. If an exception occurs during the division, it catches
    the exception and prints an error message.
    
    Parameters:
        a (int or float): The numerator.
        b (int or float): The denominator.
        
    Returns:
        The printable result of the division operation.
    """
    
    code = f"""
try:
    result = {a} / {b}
except Exception as e:
    result = f'ERROR: {{e}}'
"""
    codeExecutor.execute(code)
    return codeExecutor.print_var('result')
    
def power(a, b):
    """Calculate the power of a number.

    This method calculates the result of raising `a` to the power of `b`.
    If an exception occurs during the calculation, it captures the exception
    and stores an error message in the result.

    Parameters:
        a (int or float): The base number.
        b (int or float): The exponent.

    Returns:
        The printable result of the power operation.
    """
    
    code = f"""
try:
    result = {a} ** {b}
except Exception as e:
    result = f'ERROR: {{e}}'
"""
    codeExecutor.execute(code)
    return codeExecutor.print_var('result')
        
def run_code(code):
    """Execute the given code in the calculator environment.
    
    This method must be used ONLY for different operations that are not covered by the existing methods.
    
    Parameters:
        code (str): The Python code to execute.
    """
    codeExecutor.execute(code)
        
def get_calculator_locals():
    """Get the local variables in the calculator environment.

    Returns:
        dict: A dictionary containing the local variables in the calculator environment.
    """
    return codeExecutor.get_locals()
    
def get_calculator_globals():
    """Get the global variables in the calculator environment.
        
    Returns:
        dict: A dictionary containing the global variables in the calculator environment
    """
    return codeExecutor.get_globals()
    
def get_calculator_all():
    """Get all local and global variables in the calculator environment.
        
    Returns:
        tuple: A tuple containing two dictionaries:
            - locals (dict): Local variables in the calculator environment.
            - globals (dict): Global variables in the calculator environment.
    """
        
    return codeExecutor.get_all()