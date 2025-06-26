import sys
import logging

def error_message_detail(error: Exception, error_detail: sys) -> str:
    """
    Extracts detailed error information including file name, line number, and the error message.

    params
        error : The exception that occurred.
        error_detail : The sys module to access traceback details.
    
    return
        A formatted error message string.
    """

    # Extract traceback details (exception information)
    _, _, exc_tb = error_detail.exc_info()

    # file name where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Create a formatted error message string with file name, line number, and the actual error
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in python script: [{file_name}] at line number [{line_number}]: {str(error)}"
    
    # Log the error for better tracking
    logging.error(error_message)
    
    return error_message

class CustomException(Exception):
    """
    Custom exception class for handling errors
    """
    
    def __init__(self, error: Exception, error_detail: sys):
        """
        Initializes the Exception with a detailed error message.

        params
            error : The exception that occurred.
            error_detail : The sys module to access traceback details.
        """
        # Call the base class constructor with the error message
        super().__init__(str(error))

        # Format the detailed error message using the error_message_detail function
        self.error_message = error_message_detail(error, error_detail)

    def __str__(self) -> str:
        """
        Returns the string representation of the error message.
        """
        return self.error_message