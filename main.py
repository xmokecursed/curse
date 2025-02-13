import os
os.system("pip install -U nextcord")
os.system("pip install akinator.py")
os.system("pip install -U animec")
os.system("pip install -U craiyon.py")
os.system("pip install youtube-dl")
os.system("pip install PyNaCl")
os.system("pip install youtube-search-python")
os.system("pip install nextcord[voice]")
os.system("pip install pillow")
os.system('pip install googletrans==4.0.0-rc1')
os.system('pip install google-api-python-client')
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from nextcord.ui import Button, View
from nextcord import Interaction, SlashOption, ChannelType
from craiyon import Craiyon
from nextcord.ext import commands
from aiohttp import request
from nextcord.ui import View, button
from googletrans import Translator
from io import BytesIO
from datetime import datetime
from datetime import timezone
import requests
import base64
import animec
import giphy_client
import nextcord
import json
import humanfriendly
import urllib
import urllib.parse
import urllib.request
import re
import time
import random
import asyncio
import qrcode
import difflib
from difflib import get_close_matches
from keep_alive import keep_alive

intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True
intents.voice_states = True

