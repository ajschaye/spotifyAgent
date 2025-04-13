import logging
import datetime

class LogLevel:
    _levels = [logging.DEBUG, logging.INFO, logging.ERROR]
    _currentLvl = logging.DEBUG

    @staticmethod
    def initLogger(lvl=logging.DEBUG):
        LOGGER.setLevel(lvl)
        
    def setLevel(this, l):
        if l not in this._levels:
            raise Exception('unknown log level. input: {} not in [{}]'.format(l, ','.join(this._levels)))
        this._currentLvl = l
    
    @staticmethod
    def _log(l, m):
        now = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        outM = '{} {} | {}'.format(now, l, m)
        print(outM)

LOGGER = LogLevel()

def debug(message):
    if LOGGER._currentLvl <= logging.DEBUG:
        LOGGER._log('DEBUG', message)

def info(message):
    if LOGGER._currentLvl <= logging.INFO:
        LOGGER._log('INFO', message)

def error(message):
    if LOGGER._currentLvl <= logging.ERROR:
        LOGGER._log('ERROR', message)

