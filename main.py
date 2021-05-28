import os
import discord
import events
import Commands

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
    elif message.content.startswith('!get CAD'):
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
          

client.run(os.environ['TOKEN'])





