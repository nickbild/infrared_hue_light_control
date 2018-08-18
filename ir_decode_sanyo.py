# Sanyo DVD player (NC095) remote control.

def decode(timings):
	# Sanity check - did we get a good signal to decode?
	if timings[0][0] < 0.0012 or timings[0][0] > 0.0016:
		return -1

	# Just focus on the unique pulse(s) needed to differentiate
	# buttons of interest.
	if timings[18][0] >= 0.0001 and timings[18][0] <= 0.0003 and timings[20][0] >= 0.0001 and timings[20][0] <= 0.0003:
		return 4
	elif timings[17][0] >= 0.0001 and timings[17][0] <= 0.0003:
		return 2
	elif timings[26][0] >= 0.0004 and timings[26][0] <= 0.0006:
		return 3
	elif timings[25][0] >= 0.0001 and timings[25][0] <= 0.0003 and timings[26][0] >= 0.0001 and timings[26][0] <= 0.0003:
		return 1

	return -1

