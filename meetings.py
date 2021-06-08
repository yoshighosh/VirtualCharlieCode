import json
import datetime



def checkDate(meetingDate):
  x = datetime.datetime.now()
  meetingMonth = int(meetingDate[0:2])
  meetingDay = int(meetingDate[3:5])
  meetingYear = int(meetingDate[6:])

  if meetingDay == x.day and meetingMonth == x.month and meetingYear == x.year: return True
  elif meetingMonth > x.month and meetingYear >= x.year:
    return True
  elif meetingDay > x.day and meetingMonth >= x.month and meetingYear >= x.year:
    return True
  else: 
    return False

def editMeetingData(meetingName, edit, editData):
  with open('Meetings.json') as fp:
    meetings = json.load(fp)

  for meeting in meetings:
    if meeting["Meeting Name"] == meetingName:
      meeting[edit] = editData

  with open('Meetings.json', 'w') as fp:
    meetings = json.dump(meetings, fp)
  

def addMeetingData(meetingData):
  with open("Meetings.json", "r") as fp:
    print("test 1")
    meetings = json.load(fp)

  meetings.append(meetingData)
  
  with open('Meetings.json', 'w') as fp:
    meetings = json.dump(meetings, fp)
    
  
def removeMeetingData(meetingName):
  with open('Meetings.json', 'r') as fp:
    meetings = json.load(fp)

  for meeting in meetings:
    if meeting["Meeting Name"] == meetingName:
        meetings.remove(meeting)

  with open('Meetings.json', 'w') as fp:
    meetings = json.dump(meetings, fp) 
  
def getPastMeetingData():
  with open('Meetings.json') as fp:
    meetings = json.load(fp)

  num_meetings = len(meetings)  
  meeting_list = ""
  meetingNumber = 0

  for index in range(num_meetings):
    meeting = meetings[index]
    meeting_string = ""
    if checkDate(meeting["Date"]) == False:
      meetingNumber += 1
      meeting_string += "***" + str(meetingNumber) + ". " + "*** "
      for item in meeting:
        if item == "Links":
          meeting_string += "**" + item + ": " + "**" + "<" + meeting[item] + ">" + "\n \t"
        elif item == "Agenda":
          meeting_string += "**" + item + ":**\n \t" 
          item_number = 0
          for thing in meeting[item]:
            meeting_string += "\t*" + thing + ":* " + meeting[item][thing] + "\n \t"
            item_number += 1
        elif item == "Attendees":
          print("nothing to see here")
        else:
          meeting_string += "**" + item + ": " + "**" + meeting[item] + "\n \t"
      meeting_string += "\n"

    meeting_list += meeting_string 
    
  return meeting_list

def getMeetingData():
  with open('Meetings.json') as fp:
    meetings = json.load(fp)

  num_meetings = len(meetings)
  meeting_list = ""
  meetingNumber = 0

  for index in range(num_meetings):
    meeting = meetings[index]
    meeting_string = ""
    if checkDate(meeting["Date"]):
      meetingNumber += 1
      meeting_string += "***" + str(meetingNumber) + ". " + "*** "
      for item in meeting:
        if item == "Links":
          meeting_string += "**" + item + ": " + "**" + "<" + meeting[item] + ">" + "\n \t"
        elif item == "Agenda":
          meeting_string += "**" + item + ":**\n \t" 
          item_number = 0
          for thing in meeting[item]:
            meeting_string += "\t*" + thing + ":* " + meeting[item][thing] + "\n \t"
            item_number += 1
        elif item == "Attendees" or item == "Meeting ID":
          print("nothing to see here")
        else:
          meeting_string += "**" + item + ": " + "**" + meeting[item] + "\n \t"
      meeting_string += "\n"

    meeting_list += meeting_string 
    
  return meeting_list


def startMeeting(meetingName):
  with open('Meetings.json') as fp:
    meetings = json.load(fp)

  meeting_string = meetingName + " is now starting, please react with a 👍 if you are in attendance \n"
  for meeting in meetings:
    if meeting["Meeting Name"] == meetingName:
      for item in meeting:
        if item == "Links":
          meeting_string += "**" + item + ": " + "**" + "<" + meeting[item] + ">" + "\n \t"
        elif item == "Agenda":
          meeting_string += "**" + item + ":**\n \t" 
          item_number = 0
          for thing in meeting[item]:
            meeting_string += "\t*" + thing + ":* " + meeting[item][thing] + "\n \t"
            item_number += 1
        elif item == "Attendees" or item == "Meeting ID":
          print("nothing to see here")
        else:
          meeting_string += "**" + item + ": " + "**" + meeting[item] + "\n \t"
  
  return meeting_string

def addMeetingID(meetingName, meetingID):
  editMeetingData(meetingName, "Meeting ID", meetingID)

def getMeetingID(meetingName):
  with open('Meetings.json') as fp:
    meetings = json.load(fp)
  
  for meeting in meetings:
    if meeting["Meeting Name"] == meetingName:
      return meeting["Meeting ID"]


