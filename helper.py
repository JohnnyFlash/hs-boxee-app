import mc

def updateLiveList():
	#mc.ShowDialogNotification("clicked2")
	items = mc.GetDirectory('rss://www4.hockeystreams.com/rss/roku_live.php')
	mc.GetWindow(14000).GetList(120).SetItems(items)
	
def updateOnDemand(date):
	items = mc.GetDirectory('rss://www4.hockeystreams.com/rss/roku_demand.php?date=' + date)
	mc.GetWindow(14000).GetList(120).SetItems(items)