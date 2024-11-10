from aiogram.client.default import DefaultBotProperties
from aiogram import Bot, Dispatcher, html
from aiogram.filters import CommandStart
from html import escape as html_escape
from aiogram.enums import ParseMode
from aiogram.types import Message
from config.def_config import *
from handlers.defaults import *
import asyncio
import logging
import os
import sys
