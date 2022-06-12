import logging as lg
from src.utils.common import create_directories
from src.utils.configHandler import configHandler
import os
import time

class customLogger:

    def __init__(self,appname='PREDICTION',ipaddress=None,username=None):
        try:            
            cf = configHandler()
            self.appname = appname
            if(ipaddress is not None and username is not None):
                format = '%(asctime)-15s %(name)s %(clientip)s %(user)-8s %(message)s'
                self.extra = True
            else:
                format = '%(asctime)-15s %(name)s %(message)s'
                self.extra = False

            self.log_formatter = lg.Formatter(format)

            self.BASE_LOG_DIR = cf.section('BASE_LOG_DIR')
            self.ENVIRONMENT = cf.section('ENVIRONMENT')
            print(f"Logging for appname= {self.appname}")
            if(self.appname == "TRAINNING"):
                TRAINNING = cf.section("TRAINNING_LOG")
                self.log_dir = TRAINNING['DIRECTORY']
                self.file_base_name = TRAINNING['FILE_NAME']
                self.level = TRAINNING['LEVEL']
            else:
                PREDICTION_LOG = cf.section("PREDICTION_LOG")
                self.log_dir = PREDICTION_LOG['DIRECTORY']
                self.file_base_name = PREDICTION_LOG['FILE_NAME']
                self.level = PREDICTION_LOG['LEVEL']

            full_log_dir = os.path.join(self.BASE_LOG_DIR, self.log_dir)
            print(f"Logging for full_log_dir= {full_log_dir}")

            if(os.path.isdir(full_log_dir) == False):
                create_directories([self.BASE_LOG_DIR,self.log_dir])

            self.file_name = self.get_unique_log_path(full_log_dir,self.file_base_name)
            print(f"Log File Name with full path {self.file_name}")

            self.d = {'clientip': ipaddress, 'user': username}

            # Deleting all the old log files for first time from parent directory
            if self.ENVIRONMENT == "LOCAL":
                self.flushLogFiles(full_log_dir)

            self.logger = lg.getLogger(self.appname)
            self.addFileHandler()
            #Alternate way
            # lg.basicConfig(filename=self.file_name , format=self.log_formatter,filemode="a")

            if self.ENVIRONMENT == "LOCAL":
                self.addConsoleLogger()
            
        except Exception as e:
            print('Logger Failed with exception - {}'.format(e))

    def getLogger(self):
        return self.logger

    def addFileHandler(self):
        """
        To add console stream handler
        """
        try:
            file_handler = lg.FileHandler(filename=self.file_name,mode="a")
            file_handler.setLevel(lg.DEBUG)
            
            if self.level == "DEBUG":
                file_handler.setLevel(lg.DEBUG)
            elif self.level == "ERROR":
                file_handler.setLevel(lg.ERROR)
            elif self.level == "WARNING":
                file_handler.setLevel(lg.WARNING)
            elif self.level == "INFO":
                file_handler.setLevel(lg.INFO)
            
            file_handler.setFormatter(self.log_formatter)
            self.logger.addHandler(file_handler)
        except Exception as e:
            print('FileHandler Logger Failed with exception - {}'.format(e))

    
   
    def addConsoleLogger(self):
        """
        To add console stream handler
        """
        try: 
            console_log = lg.StreamHandler()
            console_log.setLevel(lg.DEBUG)
            console_log.setFormatter(self.log_formatter)
            self.logger.addHandler(console_log)
        except Exception as e:
            print('Console Logger Failed with exception - {}'.format(e))

    
    def flushLogFiles(self,full_log_dir):
        """
        To delete all .log files from the given log directory
        :return:
        """
        try:
            if os.path.isdir(full_log_dir):
                for file in os.listdir(full_log_dir):
                    if not file.endswith(".log") and file.find('.log.') == -1:
                        continue
                    os.remove(os.path.join(full_log_dir, file))
        except Exception as e:
            print('Console Logger Failed with exception - {}'.format(e))
    

    def get_unique_log_path(self,log_dir="logs",base_file_name=""):
        """
        To get unique log file name with its the full path in return 
        unique path is derived using datetime 
        """

        create_directories([log_dir])

        uniqueName = base_file_name + "_" + time.asctime().replace(" ", "_").replace(":", "") + '.log'
        log_path = os.path.join(log_dir, uniqueName)
        return log_path

    def log(self,msg):
        '''
        :param msg: message to log
        :return: nothing
        '''
        try:
            if(self.extra):
                self.logger.info(msg , extra=self.d)
            else:
                self.logger.info(msg)
        except Exception as e:
            print('Log function Failed with exception - {}'.format(e))

    def logWarning(self,msg):
        '''
        :param msg: warning message to log
        :return: nothing
        '''
        try:
            if(self.extra):
                self.logger.warning(msg , extra=self.d)
            else:
               self.logger.warning(msg)
        except Exception as e:
            print('Log function Failed with exception - {}'.format(e))

    def logError(self,msg):
        '''
        :param msg: error message to log 
        :return: nothing
        '''
        try:
            if(self.extra):
                self.logger.error(msg, extra=self.d)
            else:
                self.logger.error(msg)
        except Exception as e:
            print('Log function Failed with exception - {}'.format(e)) 

    def logException(self,msg="Exception occured",e=""):
        self.logger.exception(
            msg + "%s", e)       

# for debugging purpose
if(__name__ == "__main__"):

    clg = customLogger()
    clg.log('Random log msg for test INFO')
    clg.logWarning('Random log msg for test WARNING')
    clg.logError('Random log msg for test ERROR')

    for i in range(0, 1000):
        clg.log('INFO This is a message {}'.format(i))
        if i % 5 == 0:
            clg.logError('ERROR THis is a error {}'.format(i))

    # To create logs with extra info
    # clg2 = customLogger(__name__, '192.168.0.1', 'WebAPP')
    # clg2.log('Random log msg for test2')
    # clg2.log('Random log msg for test2', 'WARNING')
    # clg2.log('Random log msg for test2', 'ERROR')