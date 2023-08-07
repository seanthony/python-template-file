"""
AUTHOR:     email
PURPOSE:    text
DATE:       DD Month YYYY
"""
import logging


def new_function():
    """
    var -> var
    
    returns...
    
    description:
      text
    """ 
    logging.info('hello from function')
    return None
    

def main():
    '''
    
    '''
    logging.basicConfig(level=logging.DEBUG)
    logging.info('hello from main')
    
    new_function()
    return None

    
if __name__=='__main__':
    '''
    why use __name__=='__main__'?
    
    code inside this if statement is run when the script is being
     executed directly by the python interpreter.
     
    code inside the if statement will not be executed if the file's
      code is imported as a module.
    '''
    main()
