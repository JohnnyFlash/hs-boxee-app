import mc

play_count = 0
declined_count = 0

def updateLabel():
	global play_count, declined_count
	label = mc.GetActiveWindow().GetLabel(110)
	label.SetLabel('Play Count: %s[CR]Declined Count: %s' % (play_count, declined_count))

