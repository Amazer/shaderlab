import logging
import logging.handlers

class Debug:
    logger=None
    levels={"n":logging.NOTSET,
            "d":logging.DEBUG,
            "i":logging.INFO,
            "w":logging.WARN,
            "e":logging.ERROR,
            "c":logging.CRITICAL
           }
    log_level="d"
    log_file="debug.log"
    log_max_byte=10*1024*1024
    log_backup_count=5

    @staticmethod
    def GetLogger():
        if Debug.logger is not None:
            return Debug.logger
        Debug.logger=logging.Logger('cyc.Debug')
        log_handler=logging.handlers.RotatingFileHandler(filename=Debug.log_file,\
                                                         maxBytes=Debug.log_max_byte,\
                                                         backupCount=Debug.log_backup_count)
        log_fmt=logging.Formatter("[%(levelname)s][%(funcName)s][%(asctime)s]%(message)s")
        log_handler.setFormatter(log_fmt)
        Debug.logger.addHandler(log_handler)
        Debug.logger.setLevel(Debug.levels.get(Debug.log_level))
        return Debug.logger

if __name__=='__main__':
    logger=Debug.GetLogger()
    logger.debug("this debug msg")
    logger.info('info msg')
    logger.warn('warn msg')
    logger.error('error')
    logger.critical('critical msg')


