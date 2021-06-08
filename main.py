import os
import discord
import events
import meetings
import Commands
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
      
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
    elif message.content.startswith('!help'):
        await message.channel.send(Commands.commandList)
    elif message.content.startswith("!get"):
      if message.content.startswith('!get CAD'):
          await message.channel.send('Here is the link to the CAD: https://ftc8404-ultimate-goal-robot-360.netlify.app/')
      elif message.content.startswith('!get PALS'):
          await message.channel.send('Here is the link to the PALS homepage: https://pals.quixilver8404.org/')
      elif message.content.startswith('!get match scouting'):
          await message.channel.send('Here is the link to the PALS match scouting page: https://pals.quixilver8404.org/match-scouting')
      elif message.content.startswith('!get pregame scouting'):
          await message.channel.send('Here is the link to the PALS pregame scouting page: https://pals.quixilver8404.org/pre-game-scouting')
      elif message.content.startswith('!get competition overview'):
          await message.channel.send('Here is the link to the PALS competition overview: https://pals.quixilver8404.org/competition-overview')
      elif message.content.startswith('!get team info'):
          await message.channel.send('Here is the link to the PALS team info: https://pals.quixilver8404.org/team-info')
      elif message.content.startswith('!get events'):
          data_string = events.getEventData()
          string = "The next team events are .... \n \n" + data_string
          await message.channel.send(string)
      elif message.content.startswith('!get past events'):
          data_string = events.getPastEventData()
          string = "The past team events are .... \n \n" + data_string
          await message.channel.send(string)
      elif message.content.startswith('!get meetings'):
          data_string = meetings.getMeetingData()
          string = "The next team meetings are .... \n \n" + data_string
          await message.channel.send(string)
      elif message.content.startswith('!get past meetings'):
          data_string = meetings.getPastMeetingData()
          string = "The past team meetings are .... \n \n" + data_string
          await message.channel.send(string)
    elif message.content.startswith('!add event'):
        await message.channel.send('Please enter the Event Name:')
        eventName = await client.wait_for("message")
        await message.channel.send('Please enter the Event Date (mm/dd/yyyy):')
        eventDate = await client.wait_for("message")
        await message.channel.send('Please enter the Event Time:')
        eventTime = await client.wait_for("message")
        await message.channel.send('Please enter the Event Description:')
        eventDescription = await client.wait_for("message")
        await message.channel.send('Please enter any associated link:')
        eventLinks = await client.wait_for("message")
        eventData = {"Event Name": str(eventName.content), "Date": str(eventDate.content), "Time": str(eventTime.content), "Description": str(eventDescription.content), "Links": str(eventLinks.content)}
        events.addEventData(eventData)
        await message.channel.send("Your event has been added!")
    elif message.content.startswith('!remove event'):
        await message.channel.send('Please enter the Event Name:')
        eventName = await client.wait_for("message")
        await message.channel.send('Are you sure you would like to delete this event? ' + str(eventName.content))
        confirmation = await client.wait_for("message")
        if confirmation.content.lower() == "yes":
          events.removeEventData(eventName.content)
          await message.channel.send('Your event has been deleted.')
        else:
          await message.channel.send('No events were deleted.')
    elif message.content.startswith('!edit event'):
        await message.channel.send('Please enter the Event Name:')
        eventName = await client.wait_for("message")
        await message.channel.send('What would you like to change about this event? (i.e. Event Name, Date, Time, Description, Links')
        edit = await client.wait_for("message")
        if edit.content == "Event Name" or edit.content == "Date" or edit.content == "Time" or edit.content == "Description" or edit.content == "Links":
          await message.channel.send('What would you like to change it to?')
          editData = await client.wait_for("message")
          events.editEventData(eventName.content, edit.content, editData.content)
          await message.channel.send('Your event has been edited.')
        else: await message.channel.send('Invalid edit')
    elif message.content.startswith('!add meeting'):
        await message.channel.send('Please enter the Meeting Name:')
        meetingName = await client.wait_for("message")
        await message.channel.send('Please enter the Meeting Date (mm/dd/yyyy):')
        meetingDate = await client.wait_for("message")
        await message.channel.send('Please enter the Meeting Time:')
        meetingTime = await client.wait_for("message")
        await message.channel.send('Please enter the first item on the Meeting Agenda:')
        meetingAgendaItem = await client.wait_for("message")
        meetingAgenda = {"Item 1": str(meetingAgendaItem.content)}
        await message.channel.send('Please enter any associated links:')
        meetingLinks = await client.wait_for("message")
        meetingData = {"Meeting Name": str(meetingName.content), "Date": str(meetingDate.content), "Time": str(meetingTime.content), "Agenda": meetingAgenda, "Links": str(meetingLinks.content), "Attendees": "", "Meeting ID": ""}
        meetings.addMeetingData(meetingData)
        await message.channel.send("Your meeting has been added!")
    elif message.content.startswith('!remove meeting'):
        await message.channel.send('Please enter the Meeting Name:')
        meetingName = await client.wait_for("message")
        await message.channel.send('Are you sure you would like to delete this event? ' + str(meetingName.content))
        confirmation = await client.wait_for("message")
        if confirmation.content.lower() == "yes":
          meetings.removeMeetingData(eventName.content)
          await message.channel.send('Your meeting has been deleted.')
        else:
          await message.channel.send('No meetings were deleted.')
    elif message.content.startswith('!edit meeting'):
        await message.channel.send('Please enter the Meeting Name:')
        meetingName = await client.wait_for("message")
        await message.channel.send('What would you like to change about this meeting? (i.e. Meeting Name, Date, Time, Links')
        edit = await client.wait_for("message")
        if edit.content == "Meeting Name" or edit.content == "Date" or edit.content == "Time" or edit.content == "Links":
          await message.channel.send('What would you like to change it to?')
          editData = await client.wait_for("message")
          meetings.editMeetingData(meetingName.content, edit.content, editData.content)
          await message.channel.send('Your meeting has been edited.')
        else: await message.channel.send('Invalid edit')
    elif message.content.startswith('!start meeting'):
        await message.channel.send('Which meeting would you like to start?')
        meetingName = await client.wait_for("message")
        message = await message.channel.send(meetings.startMeeting(meetingName.content))
        meetings.addMeetingID(meetingName.content, message.id)
        await message.add_reaction('\N{THUMBS UP SIGN}')

        
    elif message.content.startswith('!end meeting'):
        await message.channel.send('Which meeting would you like to end?')
        meetingName = await client.wait_for("message")
        channel = message.channel
        users = ""
        async for message in channel.history(limit=200):
            if message.id == meetings.getMeetingID(meetingName.content):
              for reaction in message.reactions:
                async for user in reaction.users():
                    users += str(user) + ", "
        
        #print(str(users))
        
        #meetings.editMeetingData(meetingName.content, "Attendance", users)

        await message.channel.send('Your meeting has ended.')
        #await message.channel.send(meetings.endMeeting(meetingName.content))
        



keep_alive()
client.run(os.environ['TOKEN'])





