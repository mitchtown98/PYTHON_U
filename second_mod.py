import custom_logger

second_logger = custom_logger.getLogger('second_logger', loglevel='DEBUG')
second_logger.debug("Test From Second logger")

def gen_matrix(rows, cols, default_value):
    return [[default_value for i in range(cols)] for j in range(rows)]
  
robot_matrx = gen_matrix(1,3,1)

second_logger.info(robot_matrx)
  