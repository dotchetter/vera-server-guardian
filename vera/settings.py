import os
from pathlib import Path
from dotenv import load_dotenv

"""
    Welcome to the settings module! Please take a minute to read
    this little introduction, if it's your first time here.
    
    If you've used Django before, this is familiar to you and 
    you can stop reading now. If you haven't, thats okay too. 
    
    Everything in this file is available to you in your app 
    through 'pyttman.settings'. You can store things here, but
    be >>> very careful <<< not to push API tokens, 
    passwords or other sensitive details to version control. 
    This is why it's recommended to use .env or another form 
    of storing these sentitive credentials in your app, and 
    then using them here in this file with `os.getenv("my_api_token")` 
    for example.
"""

load_dotenv()

DEBUG = True

# Create a new log file for each time your app starts, or append the most recent one.
APPEND_LOG_FILES = True

# Configure the behavior of the MessageRouter here
MESSAGE_ROUTER = {

    # The MessageRouter routes messages to your app's Feature classes.
    # To see the available classes and choose on that fits your app,
    # check out the documentation on GitHub!
    "ROUTER_CLASS": "pyttman.core.parsing.routing.FirstMatchingRouter",

    # Define a collection of strings to return to the user if no command matched
    # the user's message. One is randomly chosen by the Router and returned to
    # the user.
    "COMMAND_UNKNOWN_RESPONSES": [
        "I'm sorry, I didn't understand. Try again! ",
        "Hmm.. I don't think I follow?"
    ],

    # Define the keyword for Pyttman's auto-generated help pages to be
    # displayed for a user, if they type this word in the beginning of
    # a message. The keyword is case insensitive and has to occur as
    # first string in the command.
    "HELP_KEYWORD": "help",
}

# Define your features here, with path starting from your project directory.
# TIP! If you use PyCharm, you can right-click your feature class name
# and select "Copy / Paste Special" -> "Copy Reference" and paste it below.
# Example:  FEATURES = ["features.myfeature.MyFeatureClass",]
FEATURES = ["vera.features.guardian.feature.GuardianFeature"]

# This text is what will be returned to users if your app runs in to
# a fatal error from which no Reply object could be returned to the client.
# That is - in the worst thinkable scenario, this message should still
# reach your users and hint to them that an error occurred, and your
# app isn't simply ignoring them by keeping quiet.
# The string "Error ID: { uuid here } " will be appended to
# the string defined here, with said UUID, you can spot the error in
# the log file easily.
FATAL_EXCEPTION_AUTO_REPLY = "I'm sorry, something went wrong. Try again in a few moments."

# Define the clients which your Pyttman app uses as its front end here.
# There are clients available to use which Pyttman provides for you,
# and it's easy to develop a custom client for your platform by subclassing
# the BaseClient class, and using it here. Provide the full reference to the
# client class under the 'module' key. Any other data in the dict will be
# passed as kwargs to your client.
# -- Notice --
# Clients can be used concurrently. This means that you can have one app connected
# to multiple clients in parallel, while using the same app memory. Below is an
# example of an app using both the Pyttman CLI - client, used for dev testing,
# and the included Discord client.
CLIENTS = [
    {
        "module": "vera.discordclient.CustomDiscordClient",
        "token":os.getenv("DISCORD_TOKEN_DEV") if DEBUG else os.getenv("DISCORD_TOKEN"),
        "guild": os.getenv("DISCORD_GUILD_DEV") if DEBUG else os.getenv("DISCORD_GUILD")
    },
]

# No need to change this setting
APP_BASE_DIR = Path(os.path.dirname(os.path.realpath(__file__)))

# No need to change this setting
LOG_FILE_DIR = APP_BASE_DIR / Path("logs")

# This setting is set by pyttman-cli when you create your project.
# Do not change it afterwards without also renaming the directory for your app.
APP_NAME = "vera"
