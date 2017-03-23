import logging


class Logger:

	_handler = None
	_logger = None
	_formatter = None
	def __init__(self):
		self._logger = logging.getLogger(__name__)
		self._formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		self._handler = logging.FileHandler('hello.log')
		self._handler.setLevel(logging.DEBUG)
		self._handler.setFormatter(self._formatter)
		self._logger.addHandler(self._handler)
		self._logger.setLevel(logging.INFO)


	def Log(self, message, loggerLevel):
		options = {
			0 : self._logger.debug,
			1 : self._logger.info
		}
		options[loggerLevel](message)