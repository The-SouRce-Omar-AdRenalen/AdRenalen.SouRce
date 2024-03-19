from AdRenalen.core.bot import Omar
from AdRenalen.core.dir import dirr
from AdRenalen.core.git import git
from AdRenalen.core.userbot import Userbot
from AdRenalen.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Omar()
userbot = Userbot()

global BOT_ID, BOT_NAME, BOT_USERNAME, BOT_MENTION, fallendb 
global ASS_ID, ASS_NAME, ASS_USERNAME, ASS_MENTION, SUDOERS

BOT_ID = getme.id
BOT_NAME = getme.first_name
BOT_USERNAME = getme.username
BOT_MENTION = getme.mention

await app2.start()
LOGGER.info(  
    "[•] \x42\x6f\x6f\x74\x69\x6e\x67\x20\x46\x61\x6c\x6c\x65\x6e\x20\x4d\x75\x73\x69\x63\x20\x41\x73\x73\x69\x73\x74\x61\x6e\x74\x2e\x2e\x2e"
    )

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
