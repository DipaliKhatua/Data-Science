# import sys
# from src.DSProject.logger import logging

# def error_message_detail(error,error_detail:sys):
#     _,_,exc_tb=error_detail.exc_info()
#     file_name=exc_tb.tb_frame.f_code.co_filename
#     error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
#      file_name,exc_tb.tb_lineno,str(error))

#     return error_message


# class CustomException(Exception):
#     def __init__(self,error_message,error_details:sys):
#         super().__init__(error_message)
#         self.error_message=error_message_detail(error_message,error_details)

#     def __str__(self):
#         return self.error_message 

import sys
from src.DSProject.logger import logging

def error_message_detail(error, error_detail: sys):
    """
    Captures detailed error information using sys.exc_info().
    """
    # Use sys.exc_info() to fetch traceback details
    _, _, exc_tb = sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename  # File where the error occurred
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message


class CustomException(Exception):
    """
    Custom Exception for detailed error reporting.
    """
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message