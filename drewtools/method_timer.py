from time import time
from . import config

def mtimer(func):
	def wrapper(*args, **kwargs):
		repeat = kwargs.get('mt_repeat', config.mt_repeat)
		iterations = kwargs.get('mt_iterations', config.mt_iterations)
		try:
			del kwargs['mt_repeat']
		except:
			pass

		try:
			del kwargs['mt_iterations']
		except:
			pass

		results = []
		main_start_time = time()
		for x in range(0, repeat):
			start_time = time()
			for x in range(0, iterations):
				retval = func(*args, **kwargs)
			results.append(time() - start_time)
		if repeat > 1:
			print ' %-25s: %4.6f sec. (%4.6f total)' % (func.func_name, min(results), time()-main_start_time)
		else:
			print ' %-25s: %4.6f sec.' % (func.func_name, min(results))
		return retval
	return wrapper
