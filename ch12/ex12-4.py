# 12.9 에러 메시지 로깅

import logging
logging.debug("Looks like rain")
logging.info("And hail")
logging.warn("Did I hear thunder?")
# WARNING:root:Did I hear thunder?
logging.error("Was that lightning?")
# ERROR:root:Was that lightning?
logging.critical("Stop fencing and get inside!")
# CRITICAL:root:Stop fencing and get inside!


import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug("It's raining again")
# DEBUG:root:It's raining again
logging.info("With hail the size of hailstones")
# INFO:root:With hail the size of hailstones


import logging
logging.basicConfig(level='DEBUG')
logger = logging.getLogger('bunyan')
logger.debug('Timber!')
# DEBUG:bunyan:Timber!


import logging
logging.basicConfig(level='DEBUG', filename='blue_ox.log')
logger = logging.getLogger('bunyan')
logger.debug("Where's my axe?")
logger.warn("I need my axe")


import logging
fmt = '%(asctime)s %(levelname)s %(lineno)s %(message)s'
logging.basicConfig(level='DEBUG', format=fmt)
logger = logging.getLogger('bunyan')
logger.error("Where's my other plaid shirt?")
