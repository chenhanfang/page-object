import logging
import logging.handlers
class Logger():
    LOG_FILE = 'tst.log'
    handler = logging.handlers.RotatingFileHandler(LOG_FILE,maxBytes=1024*1024,backupCount=5)
    fmt = '%(asctime)s -%(filename)s:%(lineno)s-%(name)s-%(message)s'
    formatter = logging.Formatter(fmt)
    handler.setFormatter(formatter)
    logger=logging.getLogger('tst')
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    def loginfo(self,message):
        self.logger.info(message)
    def logdebug(self,message):
        self.logger.debug(message)

