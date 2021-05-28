import json
import datetime



def checkDate(eventDate):
  x = datetime.datetime.now()
  eventMonth = int(eventDate[0:2])
  eventDay = int(eventDate[3:5])
  eventYear = int(eventDate[6:])

  if eventDay == x.day and eventMonth == x.month and eventYear == x.year: return True
  elif eventMonth > x.month and eventYear >= x.year:
    return True
  elif eventDay > x.day and eventMonth >= x.month and eventYear >= x.year:
    return True
  else: 
    return False

def addEventData(eventData):
  with open("Events.json", "r+") as fp:
    events = json.load(fp)
    events.append(eventData)
    fp.seek(0)
    json.dump(events, fp)
  
def removeEventData(eventName):
  with open('Events.json', 'r') as fp:
    events = json.load(fp)

  for event in events:
    if event["Event Name"] == eventName:
        events.remove(event)

  with open('Events.json', 'w') as fp:
    events = json.dump(events, fp) 
  

    



def getPastEventData():
  with open('Events.json') as fp:
    events = json.load(fp)

  num_events = len(events)  
  event_list = ""
  eventNumber = 0

  for index in range(num_events):
    event = events[index]
    event_string = ""
    if checkDate(event["Date"]) == False:
      eventNumber += 1
      event_string += "***" + str(eventNumber) + ". " + "*** "
      for item in event:
        if item == "Links":
          event_string += "**" + item + ": " + "**" + "<" + event[item] + ">" + "\n \t"
        else:
          event_string += "**" + item + ": " + "**" + event[item] + "\n \t"
      event_string += "\n"

    event_list += event_string 
    
  return event_list

def getEventData():
  with open('Events.json') as fp:
    events = json.load(fp)

  num_events = len(events)
  event_list = ""
  eventNumber = 0

  for index in range(num_events):
    event = events[index]
    event_string = ""
    if checkDate(event["Date"]):
      eventNumber += 1
      event_string += "***" + str(eventNumber) + ". " + "*** "
      for item in event:
        if item == "Links":
          event_string += "**" + item + ": " + "**" + "<" + event[item] + ">" + "\n \t"
        else:
          event_string += "**" + item + ": " + "**" + event[item] + "\n \t"
      event_string += "\n"

    event_list += event_string 
    
  return event_list


