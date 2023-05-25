# Imports
"""
Bulk-imports

Used for importing in main while contaning readbility
"""
import asyncio
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils.executor import start_webhook

import envars as env
from db import BaseModel, User, proceed_schemas
from db.session import async_engine
from handlers import callback, commands
from handlers.commands.tools import set_cmd
