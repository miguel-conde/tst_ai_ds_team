import io
import sys

from langchain_experimental.utilities import PythonREPL

class CodeExecutor():
    """
    A class to execute Python code within a REPL environment and manage its local and global variables.
    
    This class provides a simple interface to execute Python code within a REPL (Read-Eval-Print Loop)
    environment and manage the local and global variables in that environment. It uses the `PythonREPL`
    class from the `utilities` module to create a Python REPL environment and provides methods to execute
    code, print variables, and manage local and global variables.
    
    Attributes:
        repl (PythonREPL): An instance of the PythonREPL class
        
    Methods:
        execute(code): Executes the given code in the REPL environment.
        print_var(var_name): Prints the value of a variable in the REPL environment.
        get_locals(): Retrieve the local variables from the REPL environment.
        set_locals(locals): Sets the local variables for the REPL environment.
        reset_locals(): Resets the local variables in the REPL environment.
        get_globals(): Retrieve the global variables from the REPL environment.
        set_globals(globals): Sets the global variables for the REPL environment.
        reset_globals(): Resets the global variables in the REPL environment.
        get_all(): Retrieve all local and global variables from the REPL environment.
        set_all(locals, globals): Set the local and global variables for the REPL environment.
        reset_all(): Resets the REPL environment by clearing all local and global variables.
    """
    
    def __init__(self):
        """
        Initializes a new instance of the class.

        Attributes:
            repl (PythonREPL): An instance of the PythonREPL class.
        """
        self.repl = PythonREPL()
        
    def execute(self, code):
        """
        Executes the given code in the REPL (Read-Eval-Print Loop) environment.

        Args:
            code (str): The code to be executed.

        Returns:
            The result of executing the code in the REPL environment.
        """
        return self.repl.run(code)
    
    def print_var(self, var_name):
        """Returns the printed output of a variable in the REPL environment.
        
        This method captures the output of the `print` statement for a variable in the REPL
        environment and returns it as a string. If the variable is not found in the local
        namespace, it returns a message indicating that the variable was not found.
        
        Parameters:
            var_name (str): The name of the variable to print.
            
        Returns:
            str: The printed output of the variable in the REPL environment.
        """
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        print(self.repl.locals.get(var_name, f'Variable "{var_name}" not found'))
        sys.stdout = sys.__stdout__
        output_string = output_buffer.getvalue()
        output_buffer.close()
        
        return output_string
    
    def get_locals(self):
        """
        Retrieve the local variables from the REPL (Read-Eval-Print Loop) environment.

        Returns:
            dict: A dictionary containing the local variables in the REPL environment.
        """
        return self.repl.locals
    
    def set_locals(self, locals):
        """
        Sets the local variables for the REPL (Read-Eval-Print Loop) environment.

        Parameters:
        locals (dict): A dictionary containing the local variables to be set in the REPL environment.
        """
        self.repl.locals = locals
    
    def reset_locals(self):
        """
        Resets the local variables in the REPL (Read-Eval-Print Loop) environment.

        This method clears all the local variables stored in the REPL's local
        namespace by setting it to an empty dictionary.
        """
        self.repl.locals = {}
        
    def get_globals(self):
        """
        Retrieve the global variables from the REPL (Read-Eval-Print Loop) environment.

        Returns:
            dict: A dictionary containing the global variables.
        """
        return self.repl.globals
    
    def set_globals(self, globals):
        """
        Sets the global variables for the REPL (Read-Eval-Print Loop) environment.

        Args:
            globals (dict): A dictionary containing global variables to be set in the REPL environment.
        """
        self.repl.globals = globals
        
    def reset_globals(self):
        """
        Resets the global variables in the REPL (Read-Eval-Print Loop) environment.

        This method clears the `globals` dictionary of the `repl` attribute, effectively
        removing all global variables and resetting the environment to its initial state.
        """
        self.repl.globals = {}
        
    def get_all(self):
        """
        Retrieve all local and global variables from the REPL environment.

        Returns:
            tuple: A tuple containing two dictionaries:
                - locals (dict): Local variables in the REPL environment.
                - globals (dict): Global variables in the REPL environment.
        """
        return self.repl.locals, self.repl.globals
    
    def set_all(self, locals, globals):
        """
        Set the local and global variables for the REPL (Read-Eval-Print Loop) environment.

        Parameters:
        locals (dict): A dictionary representing the local variables.
        globals (dict): A dictionary representing the global variables.
        """
        self.repl.locals = locals
        self.repl.globals = globals
        
    def reset_all(self):
        """
        Resets the REPL (Read-Eval-Print Loop) environment by clearing all local and global variables.
        
        This method sets the `locals` and `globals` dictionaries of the REPL to empty dictionaries,
        effectively removing all previously defined variables and functions.
        """
        self.repl.locals = {}
        self.repl.globals = {}
        
        
### Usage
if __name__ == '__main__':
    # Create an instance of the CodeExecutor class
    code_executor = CodeExecutor()
    
    # Execute some code in the REPL environment
    code_executor.execute('x = 42')
    code_executor.execute('y = 3.14')
    code_executor.execute('z = "hello"')
    
    # Print the value of a variable
    print(code_executor.print_var('x'))
    print(code_executor.print_var('y'))
    print(code_executor.print_var('z'))
    
    # Retrieve and print the local variables
    print(code_executor.get_locals())
    
    # Set new local variables
    code_executor.set_locals({'a': 10, 'b': 20})
    print(code_executor.get_locals())
    
    # Reset the local variables
    code_executor.reset_locals()
    print(code_executor.get_locals())
    
    # Retrieve and print the global variables
    print(code_executor.get_globals())
    
    # Set new global variables
    code_executor.set_globals({'name': 'Alice', 'age': 30})
    print(code_executor.get_globals())
    
    # Reset the global variables
    code_executor.reset_globals()
    print(code_executor.get_globals())
    
    # Set new local and global variables
    code_executor.set_all({'a': 100, 'b': 200}, {'name': 'Bob', 'age': 40})
    print(code_executor.get_all())
    
    # Reset all variables
    code_executor.reset_all()
    print(code_executor.get_all())