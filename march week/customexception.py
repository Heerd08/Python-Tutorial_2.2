import sys
import logging

def error_message_detail(error :Exception,error_detail:sys)-> str:
""" return : a formatted error message string ."""
    
    #Extract traceback details (exception information)
_, _, exc_tb =  error_detail.exc_info()
    