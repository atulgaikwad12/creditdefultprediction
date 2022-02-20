import logging as lg
#from logging.handlers import RotatingFileHandler

class customLogger:

    d = {'clientip': '192.168.0.1', 'user': 'ATUL'}

    def __init__(self,appname):
        try:
            #log_formatter = '%(asctime)-15s %(name)s %(clientip)s %(user)-8s %(message)s'
            log_formatter = '%(asctime)-15s %(name)s %(message)s'
            log_name = 'Logs\\crudeapp.log'

            lg.basicConfig(filename=log_name, level=lg.DEBUG, format=log_formatter)

            # To add console stream handler
            console_log = lg.StreamHandler()
            console_log.setLevel(lg.DEBUG)
            formatter = lg.Formatter(log_formatter)
            console_log.setFormatter(formatter)
            lg.getLogger().addHandler(console_log)

            # To add rotating file handler so that new log file will be created after certain file size
            # rotating_handler = lg.handlers.RotatingFileHandler(log_name, mode='a',maxBytes=1024, backupCount=2, encoding=None,delay=False)
            # rotating_handler.setFormatter(log_formatter)
            # rotating_handler.setLevel(lg.DEBUG)
            # lg.getLogger().addHandler(rotating_handler)

            self.logger = lg.getLogger(appname)

        except Exception as e:
            print('Logger Failed with exception - {}'.format(e))

    def log(self,msg,level="INFO",extra=False):
        '''

        :param msg: msg to log
        :param level: default is "INFO" but can provide "WARNING"/"ERROR"
        :return: nothing
        '''
        try:
            if(extra):
                if level == "INFO":
                    self.logger.info(msg , extra=customLogger.d)
                elif level == "WARNING":
                    self.logger.warning(msg , extra=customLogger.d)
                else:
                    self.logger.error(msg, extra=customLogger.d)
            else:
                if level == "INFO":
                    self.logger.info(msg)
                elif level == "WARNING":
                    self.logger.warning(msg)
                else:
                    self.logger.error(msg)
        except Exception as e:
            print('Log function Failed with exception - {}'.format(e))


