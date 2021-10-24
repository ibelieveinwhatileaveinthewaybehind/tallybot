# TallyBot v0.1

import discord, asyncio, random, os
from dotenv import load_dotenv

load_dotenv()
bot = discord.Bot()

def albumOrAlbum(allAlbums):
    album1 = random.choice(allAlbums)
    album2 = random.choice(allAlbums)
    if album1 == album2:
        albumOrAlbum()
    else:
        return f"**{album1}** or **{album2}**?"

def songFromAlbum(allAlbums):
    album = random.choice(allAlbums)
    if album == "Songs About Girls":
        songsAboutGirls = ["Passing", "Effort and Apathy", "Almost Raining", "Yearbook"]
        song1 = random.choice(songsAboutGirls)
        song2 = random.choice(songsAboutGirls)
        if song1 == song2:
            songFromAlbum(allAlbums)
        else:
            return f"Which song from **{album}** do you prefer?\n**{song1}** or **{song2}**?"
    elif album == "Complete Demos":
        completeDemos = ["Good Day", "Greener", "Welcome to Tally Hall", "Just Apathy", "Two Wuv", "Stationary Love", "Banana Man", "(I Know) It's Just the Same", "Ruler of Everything", "Hidden in the Sand"]
        song1 = random.choice(completeDemos)
        song2 = random.choice(completeDemos)
        if song1 == song2:
            songFromAlbum(allAlbums)
        else:
            return f"Which song from **{album}** do you prefer?\n**{song1}** or **{song2}**?"
    elif album == "The Pingry EP":
        pingryEP = ["The Bidding", "Taken for a Ride", "Be Born", "The Whole World and You", "All of my Friends", "Good Day", "Yearbook", "Just a Friend", "Cell Phone Call"]
        song1 = random.choice(pingryEP)
        song2 = random.choice(pingryEP)
        if song1 == song2:
            songFromAlbum(allAlbums)
        else:
            return f"Which song from **{album}** do you prefer?\n**{song1}** or **{song2}**?"
    elif album == "Marvin's Marvelous Mechanical Museum":
        mmmm = ["Good Day", "Greener", "Welcome to Tally Hall", "Taken for a Ride", "The Bidding", "Be Born", "Banana Man", "Just Apathy", "Spring and a Storm", "Two Wuv", "Haiku", "The Whole World and You", "13", "Ruler of Everything", "Hidden in the Sand"]
        song1 = random.choice(mmmm)
        song2 = random.choice(mmmm)
        if song1 == song2:
            songFromAlbum(allAlbums)
        else:
            return f"Which song from **{album}** do you prefer?\n**{song1}** or **{song2}**?"
    elif album == "Good & Evil":
        gAndE = ["Never Meant to Know", "&", "You & Me", "Cannibal", "Who You Are", "Sacred Beast", "Hymn for a Scarecrow", "A Lady", "The Trap", "Turn the Lights Off", "Misery Fell", "Out in the Twilight", "You", "Fate of the Stars"]
        song1 = random.choice(gAndE)
        song2 = random.choice(gAndE)
        if song1 == song2:
            songFromAlbum(allAlbums)
        else:
            return f"Which song from **{album}** do you prefer?\n**{song1}** or **{song2}**?"
    elif album == "Hawaii: Part II":
        hpii = ["Introduction to the Snow", "Isle Unto Thyself", "White Ball", "Murders", "Space Station Level 7", "The Mind Electric", "Labyrinth", "Time Machine", "Stranded Lullaby", "Dream Sweet in Sea Major"]
        song1 = random.choice(hpii)
        song2 = random.choice(hpii)
        if song1 == song2:
            songFromAlbum(allAlbums)
        else:
            return f"Which song from **{album}** do you prefer?\n**{song1}** or **{song2}**?"
    elif album == "Sketches":
        sketches = ["Miss Melody", "HEY YOU!", "Hummingbird", "Daisy Fingers", "Have a Nice Day (Interludinal)", "Lemons & Pears", "At the End", "Nowhere Else", "The Rainbow Connection"]
        song1 = random.choice(sketches)
        song2 = random.choice(sketches)
        if song1 == song2:
            songFromAlbum(allAlbums)
        else:
            return f"Which song from **{album}** do you prefer?\n**{song1}** or **{song2}**?"
    elif album == "Etudes":
        etudes = ["Etude in 2nds", "Blues Etude", "Fast Etude", "12-Tones Etude", "Pop Etude", "Applause Etude"]
        song1 = random.choice(etudes)
        song2 = random.choice(etudes)
        if song1 == song2:
            songFromAlbum(allAlbums)
        else:
            return f"Which song from **{album}** do you prefer?\n**{song1}** or **{song2}**?"
    elif album == "Etudes II":
        etudesii = ["Where We Left Off Etude", "Indie-Rock (Two Finger) Etude", "Triad Etude", "Crash-and-Burn Etude", "A Little Funk-Ay Etude", "Vamp Etude"]
        song1 = random.choice(etudesii)
        song2 = random.choice(etudesii)
        if song1 == song2:
            songFromAlbum(allAlbums)
        else:
            return f"Which song from **{album}** do you prefer?\n**{song1}** or **{song2}**?"
    elif album == "Cojum Dip":
        cojumDip = ["Cell", "4-LOM", "Reverse Mullet", "M54", "Jabberwocky", '"Waltz in E-major, Op. 15 "Moon Waltz"', "Tap Tap Tap", "Puzzle Dust", "134340 Pluto"]
        song1 = random.choice(cojumDip)
        song2 = random.choice(cojumDip)
        if song1 == song2:
            songFromAlbum(allAlbums)
        else:
            return f"Which song from **{album}** do you prefer?\n**{song1}** or **{song2}**?"
    elif album == "Not A Trampoline":
        notATrampoline = ["Ghost", "Old Bike", "Garden of Eden", "The Rendezvous", "I'm Gonna Win", "All I Need Is You", "Flamingo", "La Telenovela", "In Memoriam", "Let Your Mother Know", "Perfect", "Lonely (But Not Alone)"]
        song1 = random.choice(notATrampoline)
        song2 = random.choice(notATrampoline)
        if song1 == song2:
            songFromAlbum(allAlbums)
        else:
            return f"Which song from **{album}** do you prefer?\n**{song1}** or **{song2}**?"
    elif album == "Joe Hawley Joe Hawley":
        jhjh = ["Joe Hawley Attacks", "Black People White People", "Bring Her Along", "Crazy Food", "Rotary Park", "Your Mother is a Basketball", "Hoodz 'n the Woodz", "The Apologue of Hot Rod Duncan", "Aristotle's Denial", "Bahamian Rap City", "We Are in Space", "Go to Bed", "White Rabbit"]
        song1 = random.choice(jhjh)
        song2 = random.choice(jhjh)
        if song1 == song2:
            songFromAlbum(allAlbums)
        else:
            return f"Which song from **{album}** do you prefer?\n**{song1}** or **{song2}**?"
    elif album == "Asteroid Musical":
        asteroidMusical = ["Overture", "At the Club", "Passing", "At the Club (Reprise)"]
        song1 = random.choice(asteroidMusical)
        song2 = random.choice(asteroidMusical)
        if song1 == song2:
            songFromAlbum(allAlbums)
        else:
            return f"Which song from **{album}** do you prefer?\n**{song1}** or **{song2}**?"

@bot.event
async def on_ready():
    print("Logged in! :D")

@bot.slash_command()
async def tallypls(ctx):
    # Variables
    # "album or album", "what song do you prefer from album", "fav member", "thoughts on track", "consider album"
    options = ["album or album", "thoughts on track", "thoughts on album", "fav member", "what song do you prefer from album", "fav unreleased", "consider album", "fav music video", "fav this episode", "longer song", "too long", "essential songs", "essential albums", "solo career", "first song", "oh five oh six oh eight", "remastered album", "fav part", "fav song", "fav song in album", "best rep", "fav lyrics", "fav sketch", "least fav", "how find th", "what new genre"]
    allSongs = ["&", "(I Know) It's Just the Same", "12-Tones Etude", "13", "134340 Pluto", "4-LOM", "A Lady", "All I Need Is You", "All of My Friends", "Almost Raining", "Another Minute", "Applause Etude", "Aristotle's Denial", "At Least a Day", "At the Club", "At the Club (Reprise)", "At the End", "Bahamian Rap City", "Banana Man", "Be Born", "Black People White People", "Black Rainbows", "Blues Etude", "Break it Down", "Bring Her Along", "Candle on the Water", "Cannibal", "Cell", "Cell Phone Call", "Christian Bale is at Your Party", "Club Can't Handle Me", "Color Be Gone (Demo)", "Country Good", "Crash-and-Burn Etude", "Crazy Food", "Cuckoo", "Daisy Fingers", "Dream", "Dream Sweet in Sea Major", "Effort and Apathy", "Etude in 2nds", "Etude in 5ths", "Everything Means Nothing to Me", "Fast Etude", "Fate of the Stars", "Flamingo", "Garden of Eden", "Ghost", "Go (Demo)", "Go to Bed", "Going Purple", "Good Day", "Grandpa is Hiding", "Greener", "Haiku", "Have a Nice Day (Interludinal)", "HEY YOU!", "Hidden in the Sand", "Hoodz 'n the Woodz", "Hummingbird", "Hymn for a Scarecrow", "I'm Gonna Win", "In Memoriam", "Indie-Rock (Two-Finger) Etude", "Inside the Mind of Simon (Demo)", "Introduction to the Snow", "Isle Unto Thyself", "Jabberwocky", "Joe Hawley Attacks", "Just a Friend", "Just Apathy", "Kazoo Song", "L'Frou Jibet", "La Telenovela", "Labyrinth", "Lemons and Pears", "Let Your Mother Know", "Light & Night", "Lonely (But Not Alone)", "M54", "Maybe in the Night", "Misery Fell", "Miss Melody", "Mucka Blucka", "Murders", "Nathan Naimark", "Never Meant to Know", "Nobody Else Quite Like You", "Nowhere Else", "Old Bike", "Out in the Twilight", "Overture", "Passing", "Perfect", "Pop Etude", "Puzzle Dust", "Reverse Mullet", "Rotary Park", "Ruler of Everything", "Sacred Beast", "Sea Cucumber (Demo)", "Shia LaBeouf (Demo)", "Shia LaBeouf Live", "Since I Don't Have You", "Sleigh Ride Invincibility Star", "Smile Like You Mean It", "Space Station Level 7", "Special", "Spiced Rum Commercial (Demo)", "Spring and a Storm", "Stationary Love", "Stranded Lullaby", "Taken for a Ride", "Tap Tap Tap", "The Apologue of Hot Rod Duncan", "The Bidding", "The Gobble Chicken Song", "The Mind Electric", "The Ministrel Boy", "The Rainbow Connection", "The Rendezvous", "The Trap", "The Whole World and You", "Time Machine", "Tomorrow and Today", "Triad Etude", "Turn the Lights Off", "Two Wuv", "Vamp Etude", "Variations on a Cloud", "Waiting", "Waltz in E-major, Op. 15 - Moon Waltz", "We are in Space", "Weird Bed &/or Yes Please", "Welcome to Tally Hall", "Where We Left Off Etude", "White Ball", "White Rabbit", "Who You Are", "Why Bother?", "Yearbook", "Yes Please &/or Weird Bed", "You", "You and Me", "Your Mother is a Basketball"]
    allAlbums = ["Songs About Girls", "Complete Demos", "The Pingry EP", "Marvin's Marvelous Mechanical Museum", "Good & Evil", "Hawaii: Part II", "Sketches", "Etudes", "Etudes II", "Cojum Dip", "Not A Trampoline", "Joe Hawley Joe Hawley", "Asteroid Musical"]
    unTallyAlbums = ["Songs About Girls", "Hawaii: Part II", "Sketches", "Etudes", "Etudes II", "Not A Trampoline", "Joe Hawley Joe Hawley", "Asteroid Musical"]
    # End of Variables
    option = random.choice(options)
    if option == "album or album":
        await ctx.respond(albumOrAlbum(allAlbums))
    elif option == "thoughts on track":
        song = random.choice(allSongs)
        await ctx.respond(f"Thoughts on **{song}**?")
    elif option == "thoughts on album":
        album = random.choice(allAlbums)
        await ctx.respond(f"Thoughts on **{album}**?")
    elif option == "fav member":
        await ctx.respond("Who's your favorite member of Tally Hall?")
    elif option == "what song do you prefer from album":
        await ctx.respond(songFromAlbum(allAlbums))
    elif option == "fav unreleased":
        await ctx.respond("What's your favorite song that didn't make it on an album?")
    elif option == "consider album":
        album = random.choice(unTallyAlbums)
        await ctx.respond(f"Do you consider **{album}** to be a Tally Hall Album?")
    elif option == "fav music video":
        await ctx.respond("What's your favorite Tally Hall music video?")
    elif option == "fav this episode":
        await ctx.respond("What's your favorite THIS episode?")
    elif option == "longer song":
        await ctx.respond("What Tally Hall song do you wish was longer?")
    elif option == "too long":
        await ctx.respond("What Tally Hall song is too long?")
    elif option == "essential songs":
        await ctx.respond("What are the essential Tally Hall songs?")
    elif option == "essential albums":
        await ctx.respond("What are the essential Tally Hall albums?")
    elif option == "solo career":
        await ctx.respond("Which Tally Hall member has the best solo career?")
    elif option == "first song":
        await ctx.respond("What was the first Tally Hall song you listened to?")
    elif option == "oh five oh six oh eight":
        await ctx.respond("What version of Marvin's Marvelous Mechanical Museum do you like most?\n**2005**, **2006**, or **2008**?")
    elif option == "remastered album":
        await ctx.respond("What Tally Hall album would you want remastered?")
    elif option == "fav part":
        song = random.choice(allSongs)
        await ctx.respond(f"What's your favorite part in **{song}**?")
    elif option == "fav song":
        await ctx.respond("What's your favorite Tally Hall song?")
    elif option == "fav song in album":
        album = random.choice(allSongs)
        await ctx.respond(f"What's your favorite song from **{album}**?")
    elif option == "best rep":
        await ctx.respond("What song from **Marvin's Marvelous Mechanical Museum** is the best representation of Tally Hall?")
    elif option == "fav lyrics":
        await ctx.respond("What are your favorite Tally Hall lyrics?")
    elif option == "fav sketch":
        await ctx.respond("What's your favorite Tally Hall sketch?")
    elif option == "least fav":
        album = random.choice(allAlbums)
        await ctx.respond(f"What's your least favorite song from **{album}**?")
    elif option == "how find th":
        await ctx.respond("How did you find Tally Hall?")
    elif option == "what new genre":
        await ctx.respond("What genre would you like Tally Hall to explore in a new album?")

@bot.slash_command()
async def clear(ctx, amount):
    if amount > "0":
        await ctx.channel.purge(limit = int(amount))
        await ctx.respond(f"Deleted {amount} messages.")
        await asyncio.sleep(1)
        await ctx.channel.purge(limit = 1)
    else:
        await ctx.respond("Specify the amount of messages to delete.")

bot.run(os.getenv("TOKEN"))