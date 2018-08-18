# Sanyo DVD player (NC095) remote control.

tolerance = 0.0001

def decode(timings):
	# Sanity check - did we get a good signal to decode?
	if timings[0][0] < 0.0012 or timings[0][0] > 0.0016:
		return -1

	for code in codes:
		match = 0
		for i in range(30):
			if codes[code][i][0] + tolerance >= timings[i][0] and codes[code][i][0] - tolerance <= timings[i][0]:
				match += 1
		if match == 30:
			return code

	return -1

codes = {}
# "AUDIO" button
codes[1] = []
codes[1].append([0.0014, 0.0002])
codes[1].append([0.0005, 0.0002])
codes[1].append([0.0005, 0.0002])
codes[1].append([0.0005, 0.0002])
codes[1].append([0.0002, 0.0002])
codes[1].append([0.0002, 0.0002])
codes[1].append([0.0002, 0.0002])
codes[1].append([0.0002, 0.0002])
codes[1].append([0.0005, 0.0002])
codes[1].append([0.0002, 0.0002])
codes[1].append([0.0005, 0.0002])
codes[1].append([0.0002, 0.0002])
codes[1].append([0.0002, 0.0002])
codes[1].append([0.0002, 0.0002])
codes[1].append([0.0005, 0.0002])
codes[1].append([0.0002, 0.0002])
codes[1].append([0.0002, 0.0002])
codes[1].append([0.0005, 0.0002])
codes[1].append([0.0005, 0.0002])
codes[1].append([0.0002, 0.0002])
codes[1].append([0.0005, 0.0002])
codes[1].append([0.0005, 0.0002])
codes[1].append([0.0005, 0.0002])
codes[1].append([0.0005, 0.0002])
codes[1].append([0.0002, 0.0002])
codes[1].append([0.0002, 0.0002])
codes[1].append([0.0002, 0.0002])
codes[1].append([0.0005, 0.0002])
codes[1].append([0.0002, 0.0002])
codes[1].append([0.0002, 0.0002])
# "SUBTITLE" button
codes[2] = []
codes[2].append([0.0014, 0.0002])
codes[2].append([0.0005, 0.0002])
codes[2].append([0.0005, 0.0002])
codes[2].append([0.0005, 0.0002])
codes[2].append([0.0002, 0.0002])
codes[2].append([0.0002, 0.0002])
codes[2].append([0.0002, 0.0002])
codes[2].append([0.0002, 0.0002])
codes[2].append([0.0005, 0.0002])
codes[2].append([0.0002, 0.0002])
codes[2].append([0.0005, 0.0002])
codes[2].append([0.0002, 0.0002])
codes[2].append([0.0002, 0.0002])
codes[2].append([0.0002, 0.0002])
codes[2].append([0.0005, 0.0002])
codes[2].append([0.0002, 0.0002])
codes[2].append([0.0002, 0.0002])
codes[2].append([0.0002, 0.0002])
codes[2].append([0.0005, 0.0002])
codes[2].append([0.0002, 0.0002])
codes[2].append([0.0005, 0.0002])
codes[2].append([0.0005, 0.0002])
codes[2].append([0.0005, 0.0002])
codes[2].append([0.0005, 0.0002])
codes[2].append([0.0002, 0.0002])
codes[2].append([0.0005, 0.0002])
codes[2].append([0.0002, 0.0002])
codes[2].append([0.0005, 0.0002])
codes[2].append([0.0002, 0.0002])
codes[2].append([0.0002, 0.0002])
# "ANGLE" button
codes[3] = []
codes[3].append([0.0014, 0.0002])
codes[3].append([0.0005, 0.0002])
codes[3].append([0.0005, 0.0002])
codes[3].append([0.0005, 0.0002])
codes[3].append([0.0001, 0.0002])
codes[3].append([0.0002, 0.0002])
codes[3].append([0.0002, 0.0002])
codes[3].append([0.0002, 0.0002])
codes[3].append([0.0005, 0.0002])
codes[3].append([0.0002, 0.0002])
codes[3].append([0.0005, 0.0002])
codes[3].append([0.0002, 0.0002])
codes[3].append([0.0002, 0.0002])
codes[3].append([0.0002, 0.0002])
codes[3].append([0.0005, 0.0002])
codes[3].append([0.0002, 0.0002])
codes[3].append([0.0002, 0.0002])
codes[3].append([0.0005, 0.0002])
codes[3].append([0.0002, 0.0002])
codes[3].append([0.0002, 0.0002])
codes[3].append([0.0005, 0.0002])
codes[3].append([0.0005, 0.0002])
codes[3].append([0.0005, 0.0002])
codes[3].append([0.0005, 0.0002])
codes[3].append([0.0002, 0.0002])
codes[3].append([0.0002, 0.0002])
codes[3].append([0.0005, 0.0002])
codes[3].append([0.0005, 0.0002])
codes[3].append([0.0002, 0.0002])
codes[3].append([0.0002, 0.0002])
# "ZOOM" button
codes[4] = []
codes[4].append([0.0014, 0.0002])
codes[4].append([0.0005, 0.0002])
codes[4].append([0.0005, 0.0002])
codes[4].append([0.0005, 0.0002])
codes[4].append([0.0002, 0.0002])
codes[4].append([0.0002, 0.0002])
codes[4].append([0.0002, 0.0002])
codes[4].append([0.0002, 0.0002])
codes[4].append([0.0005, 0.0002])
codes[4].append([0.0002, 0.0002])
codes[4].append([0.0006, 0.0002])
codes[4].append([0.0002, 0.0002])
codes[4].append([0.0002, 0.0002])
codes[4].append([0.0002, 0.0002])
codes[4].append([0.0005, 0.0002])
codes[4].append([0.0002, 0.0002])
codes[4].append([0.0002, 0.0002])
codes[4].append([0.0005, 0.0002])
codes[4].append([0.0002, 0.0002])
codes[4].append([0.0002, 0.0002])
codes[4].append([0.0002, 0.0002])
codes[4].append([0.0002, 0.0002])
codes[4].append([0.0002, 0.0002])
codes[4].append([0.0002, 0.0002])
codes[4].append([0.0005, 0.0002])
codes[4].append([0.0002, 0.0002])
codes[4].append([0.0005, 0.0002])
codes[4].append([0.0005, 0.0002])
codes[4].append([0.0005, 0.0002])
codes[4].append([0.0005, 0.0002])

