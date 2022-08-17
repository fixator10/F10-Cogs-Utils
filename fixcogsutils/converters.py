import emoji
from discord.ext.commands.converter import Converter, EmojiNotFound
from discord.ext.commands.errors import BadArgument

CURRENT_UNICODE_EMOJI_VERSION = 13.1


class DiscordUnicodeEmoji(Converter):
    """Checks if unicode emoji is, in fact, an emoji and from version supported by discord"""

    async def convert(self, ctx, argument):
        if not emoji.is_emoji(argument):
            raise EmojiNotFound
        if emoji.version(argument) > CURRENT_UNICODE_EMOJI_VERSION:
            raise BadArgument("This emoji is not yet supported by Discord")
        return argument
