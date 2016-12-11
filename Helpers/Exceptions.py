import functools

class Exception:
	def exceptionDeco(self, function):

		@functools.wraps(function)
		def wrapper(*args, **kwargs):
			try:
				return function(*args, **kwargs)
			except:
				err = "There was an exception in  "
				err += function.__name__
				print(err)
				raise
		return wrapper