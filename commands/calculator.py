import hikari
import lightbulb

plugin = lightbulb.Plugin(name="Hello")


@plugin.command()
@lightbulb.option("expression", "Enter the Expression in the format 26*3 and 345/5", type=str)
@lightbulb.command("calculator", "Calculate the given expression")
@lightbulb.implements(lightbulb.SlashCommand)
async def calculator(ctx: lightbulb.Context):
    try:
        if ctx.options.expression in ["0/0", "0 / 0"]:
            return await ctx.respond("Imagine that you have zero cookies and you split them evenly among zero friends. "
                                     "How many cookies does each person get? See? It doesn't make sense. "
                                     "And Cookie Monster is sad that there are no cookies, "
                                     "and you are sad that you have no friends.")
        result = eval(ctx.options.expression)
    except ZeroDivisionError:
        return await ctx.respond("Not Approved")
    except (SyntaxError, NameError):
        return await ctx.respond("Please enter a valid expression like `/calc 3*23` or `/calc 34+35`")
    await ctx.respond(result)


def load(bot):
    bot.add_plugin(plugin)


def unload(bot):
    bot.remove_plugin(plugin)