"""
AUTHOR:     email
PURPOSE:    text
DATE:       DD Month YYYY
"""
import logging
import coloredlogs


def config_logger(simple=True):
    '''
    simple config for logging,
    if simple is False, then uses a colored logging
      for richer text output.
    '''
    if simple:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.DEBUG)
        coloredlogs.DEFAULT_LEVEL_STYLES = {
            'debug': {'color': 'cyan'},
            'info': {'color': 'white'},
            'warning': {'color': 'yellow', 'bold': True},
            'error': {'color': 'red'},
            'critical': {'color': 'red', 'bold': True}
        }

        coloredlogs.install(
            level='DEBUG',
            fmt="%(asctime)s %(levelname)-8s %(message)s",
            datefmt='%y-%m-%d %H:%M:%S'
        )
    return None


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
    config_logger(simple=False)
    logging.info('hello from main\n' + ('-' * 60))
    
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
