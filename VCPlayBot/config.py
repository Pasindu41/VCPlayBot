import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQGjHhMAkkBnN3j4RoGHDr1c6bOFnLQV_swESeh0iz2jBNpYv1crA7mzKaDiLoYYYJSYxDLcnOaW6ILspRx_5qXEtF1lyUAqP3AyCja8kjfKrasG9bxtWOtYtButAr2l6yPyyO-xvW0aAI4SJnEfYpy6o7qy9BgUzVriLAfwOYmxxtrX_4i42eI7s_m4U1Oj4_Af60Ob897y0xoleOIR8-4jPaJDeaBlJ7qx7XV7_Uh9fUH5F4gxTbGzTvgfWKgmDCGP6o91IIEnhaHrRLjYG-63fe_K0OHD-GQGgr7qG0VaRJX7kP3XSSrQysx5xGMYit3Eol4IuS0nR9TNcyjLOXzVmZZu-gAAAAFsYo9RAA")
BOT_TOKEN = getenv("6130736120:AAGMFRD8EF7Ku85RCtoVwkVxZmnhVMZkr0M")
BOT_NAME = getenv("ᴘꜱ - ᴍᴜꜱɪᴄ🌻")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Psalpha_2002")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/601d4196f2b964ce74479.jpg")
admins = {}
API_ID = int(getenv("27467283"))
API_HASH = getenv("33b272caee9a0d79537cad6b6f33b3f7")
BOT_USERNAME = getenv("Ps_alpha_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "ᴘꜱ - ᴀꜱꜱɪꜱᴛᴀɴᴛ🌻")
OWNER_NAME = getenv("OWNER_NAME", "ᴘᴀꜱɪɪ🌻")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "sri_lankan_dark_Angels_2023")
PROJECT_NAME = getenv("PROJECT_NAME", "Ps-ALphav2")
SOURCE_CODE = getenv("SOURCE_CODE", "https://telegra.ph/file/3faeaff6d1bcc38f243db.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("HMPGSW-HPEHWH-ICCDAO-HFZJHX-ARQ", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", "sri_lankan_dark_Angels_2023")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5975259062").split()))
