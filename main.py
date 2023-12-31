import os
import itertools

import hikari
import lightbulb
from lightbulb.ext import tasks

from dotenv import load_dotenv

load_dotenv()
bot = lightbulb.BotApp(
    token=os.getenv("TOKEN"),
    prefix="!",
    intents=hikari.Intents.ALL_UNPRIVILEGED | hikari.Intents.MESSAGE_CONTENT,
)

statuses = itertools.cycle(
    [
        "https://github.com/hewol/OpenBot",
        "https://github.com/hewol/aerOS",
    ]
)


@bot.listen(hikari.StartedEvent)
async def on_ready(event: hikari.StartedEvent):
    print(f"Logged in as {str(bot.get_me())}!")
    bot.load_extensions_from("./commands", must_exist=True)
    cycle_status.start()


@tasks.task(s=30)
async def cycle_status():
    # Cycling Statuses Task
    await bot.update_presence(
        status=hikari.Status("dnd"),
        activity=hikari.Activity(
            type=hikari.ActivityType.CUSTOM,
            name=next(statuses),  # noqa
        ),
    )


bot.run()
