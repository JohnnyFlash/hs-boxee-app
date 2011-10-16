from operator import itemgetter
import mc

def updateLiveList():
	#mc.ShowDialogNotification("clickedLiveList")
	items = mc.GetDirectory('rss://www4.hockeystreams.com/rss/roku_live.php')
	mc.GetWindow(14000).GetList(120).SetItems(items)
	
def updateOnDemand(date):
	items = mc.GetDirectory('rss://www4.hockeystreams.com/rss/roku_demand.php?date=' + date)
	mc.GetWindow(14000).GetList(120).SetItems(items)

def updateDateList():
	#mc.ShowDialogNotification("clickedSetDate")
	items = mc.GetDirectory('rss://www4.hockeystreams.com/rss/roku_dates.php')
	newItems = mc.ListItems()
	while len(items) > 0:
		item = items.pop()
		newItems.append(item)
	mc.GetWindow(14000).GetList(120).SetItems(newItems)
