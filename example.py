#!/usr/bin/env python3
from quesstionnare import Questionnaire
from typing import Final
from telegrambot import TeleBot, filters
import asyncio

BOT_USERNAME: Final = 'Lang_Lear_Sort_Tele_Bot'
token = ''
with open(".keys", "r") as f:
    token = f.read()

app = TeleBot(token)

@app.handle_message(filters.TEXT & ~filters.COMMAND)
async def handle_message(update, context):
    lastmessage = update.message.text
    await update.message.reply_text(f"echo : {lastmessage}")

@app.handle_command("chatid")
async def getchatid(update, context):
    chatid = update.effective_message.chat_id

    print(f"[request] /chatid : {chatid}")

    await update.message.reply_text(f"your chatid is")
    await update.message.reply_text(f"{chatid}")

#app.send_to_user("hello?", "your_chat_id")
#app.send_to_users("hello?", ["your_chat_id", "your_chat_id"])


@app.handle_command("go")
async def getchatid(update, context):
    # Create a questionnaire instance
    questionnaire = Questionnaire()

    # Add questions to the questionnaire
    await update.message.reply_text(f"What is your favorite color?")
    print(update.message)
    questionnaire.add_question("How old are you?")
    questionnaire.add_question("Do you like pizza?")

    # Add branching logic to the questionnaire
    questionnaire.add_branch("What is your favorite color?", "blue", "You like blue.")
    questionnaire.add_branch("How old are you?", "18", "You are 18 years old.")
    questionnaire.add_branch("Do you like pizza?", "yes", "You like pizza.")

    # Run the questionnaire
    questionnaire.run_questionnaire()


    await update.message.reply_text(f"your chatid is")




app.start()