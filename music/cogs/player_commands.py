import discord
import logging
from discord.ext import commands

logger = logging.getLogger(__name__)

class PlayerCommands(commands.Cog):

    def __init__(self, context):
        self.context = context

    @commands.command()
    async def pause(self, ctx):

        vc = ctx.voice_client

        if vc and vc.is_playing():

            vc.pause()

            await ctx.send(
                embed=discord.Embed(
                    description="⏸️ Canción pausada",
                    color=discord.Color.orange(),
                )
            )

        else:

            await ctx.send(
                "No hay audio reproduciéndose."
            )

    @commands.command()
    async def resume(self, ctx):

        vc = ctx.voice_client

        if vc and vc.is_paused():

            vc.resume()

            await ctx.send(
                "▶️ Reanudado"
            )

        else:

            await ctx.send(
                "No está en pausa."
            )

    @commands.command(name="vol")
    async def volume_cmd(self, ctx, vol: int):

        if 0 <= vol <= 100:

            self.context.player.volume = vol / 100

            vc = ctx.voice_client

            if vc and vc.source:
                vc.source.volume = self.context.player.volume

            await ctx.send(
                f"🔊 Volumen ajustado a **{vol}%**"
            )

        else:

            await ctx.send(
                "El volumen debe estar entre **0** y **100**."
            )

    @commands.command()
    async def skip(self, ctx):

        vc = ctx.voice_client

        if vc:

            logger.info(f"is_playing={vc.is_playing()}")

            logger.info(f"is_paused={vc.is_paused()}")

            self.context.player.stopping = True

            vc.stop()

            logger.info("vc.stop ejecutado")

    @commands.command()
    async def stop(self, ctx):

        vc = ctx.voice_client

        if vc:

            self.context.player.stopping = True

            self.context.player.queue.clear()

            self.context.player.cache.clear()

            vc.stop()

            await ctx.send(
                "⏹️ Detenido y cola vaciada."
            )

    @commands.command()
    async def leave(self, ctx):

        vc = ctx.voice_client

        if vc:

            self.context.player.queue.clear()

            self.context.player.cache.clear()

            self.context.player.stopping = True

            vc.stop()

            await vc.disconnect()