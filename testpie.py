
import custom_logger 
import second_mod

# 0 = logging.NOTSET
# 10 = logging.DEBUG
# 20 = logging.INFO
# 30 = logging.WARNING
# 40 = logging.ERROR
# 50 = logging.CRITICAL

# log_level = input('Input Log Level: ')

# logging.basicConfig(
#   level = int(log_level),
#   format = "%(asctime)s %(levelname)s %(message)s",
#   datefmt = "%Y-%m-%d %H:%M:%S",
#   filename = ".\LOG\simpleLog.log"
# )

m_logger = custom_logger.getLogger('m_logger', loglevel='DEBUG')
m_logger.debug("Test From Main")
