from discord.ext import commands
import random
import discord

class smug:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def smug(self, context):
        author = context.message.author.mention
        
        smug = "**{0} your smug anime girl.**"
        
        choices = ['https://i.imgur.com/sqQlid7.jpg', 'https://i.imgur.com/pqtjBVj.jpg', 'https://i.imgur.com/YQChpfK.png', 'https://i.imgur.com/Gefe560.png', 'https://i.imgur.com/PHBGLgr.jpg', 'https://i.imgur.com/d3eQXfY.jpg', 'https://i.imgur.com/btWVBlP.jpg', 'https://i.imgur.com/CHOFPo7.jpg', 'https://i.imgur.com/GCNg379.png', 'https://i.imgur.com/ZPjDfHq.png', 'https://i.imgur.com/RejV7KV.png', 'https://i.imgur.com/Ioo2Oc0.jpg', 'https://i.imgur.com/FO95uuz.jpg', 'https://i.imgur.com/im9xnhc.jpg', 'https://i.imgur.com/H8xrPUD.png', 'https://i.imgur.com/9wggL5v.jpg', 'https://i.imgur.com/wRkMX5Z.jpg', 'https://i.imgur.com/bh04loy.jpg', 'https://i.imgur.com/niweAfq.png', 'https://i.imgur.com/QiER5UO.jpg', 'https://i.imgur.com/Vx6M6v2.jpg', 'https://i.imgur.com/iWGphzP.jpg', 'https://i.imgur.com/abqg0c3.jpg', 'https://i.imgur.com/bBBtaFM.png', 'https://i.imgur.com/yyB8re1.jpg', 'https://i.imgur.com/WtTI9ci.png', 'https://i.imgur.com/KzWcJZD.png', 'https://i.imgur.com/obbVBmY.png', 'https://i.imgur.com/zPKyhmu.png', 'https://i.imgur.com/I34u1za.jpg', 'https://i.imgur.com/RawIh69.jpg', 'https://i.imgur.com/C5rzm8M.jpg', 'https://i.imgur.com/qSOmXJd.png', 'https://i.imgur.com/9WkHArf.jpg', 'https://i.imgur.com/wKibqOP.jpg', 'https://i.imgur.com/o0ntuR7.jpg', 'https://i.imgur.com/RKceLp9.png', 'https://i.imgur.com/23IMBQI.png', 'https://i.imgur.com/AKe8TJq.jpg', 'https://i.imgur.com/BnZDcah.jpg', 'https://i.imgur.com/UZTtfjY.jpg', 'https://i.imgur.com/8HEzvSW.jpg', 'https://i.imgur.com/H7nKviA.png', 'https://i.imgur.com/Zgwbvdj.png', 'https://i.imgur.com/PWHKhNv.jpg', 'https://i.imgur.com/h2XX55O.png', 'https://i.imgur.com/EkbVTKv.jpg', 'https://i.imgur.com/Vgxp1CW.png', 'https://i.imgur.com/M6ngGah.png', 'https://i.imgur.com/1c0njBO.jpg', 'https://i.imgur.com/PmGreiU.png', 'https://i.imgur.com/4FJ2jhE.png', 'https://i.imgur.com/plPhOhO.jpg', 'https://i.imgur.com/aY2VZB5.png', 'https://i.imgur.com/M6kiRmm.png', 'https://i.imgur.com/6yfW1bh.jpg', 'https://i.imgur.com/z6Dl1cW.jpg', 'https://i.imgur.com/z3QIBss.jpg', 'https://i.imgur.com/B5DXyxi.png', 'https://i.imgur.com/NS1m9Zp.jpg', 'https://i.imgur.com/tCiIYQg.jpg', 'https://i.imgur.com/cCnZveD.jpg', 'https://i.imgur.com/4qN2uI8.jpg', 'https://i.imgur.com/oxoJhjL.jpg', 'https://i.imgur.com/NY2F7Vx.jpg', 'https://i.imgur.com/d0tTkoh.png', 'https://i.imgur.com/H7dLDQ0.jpg', 'https://i.imgur.com/ZiReTwz.jpg', 'https://i.imgur.com/qPgToh9.png', 'https://i.imgur.com/VFyABQ1.png', 'https://i.imgur.com/tAVlk8L.jpg', 'https://i.imgur.com/x3h2jhe.jpg', 'https://i.imgur.com/lOZE5c0.jpg', 'https://i.imgur.com/Ty5Z6MR.jpg', 'https://i.imgur.com/8RK451r.png', 'https://i.imgur.com/ddyHl6L.png', 'https://i.imgur.com/fd9Hf3h.png', 'https://i.imgur.com/nKzZo35.png', 'https://i.imgur.com/xoijBs3.png', 'https://i.imgur.com/Gpi8pd4.jpg', 'https://i.imgur.com/J8vPOex.jpg', 'https://i.imgur.com/UNQTmHs.jpg', 'https://i.imgur.com/USim8Fb.jpg', 'https://i.imgur.com/4i0nIfs.jpg', 'https://i.imgur.com/Ihtg8mf.png', 'https://i.imgur.com/ItSig5b.jpg', 'https://i.imgur.com/OE4wtKT.jpg', 'https://i.imgur.com/HrW5zgR.jpg', 'https://i.imgur.com/qStyNgZ.jpg', 'https://i.imgur.com/y2W5tBG.png', 'https://i.imgur.com/CXojydN.jpg', 'https://i.imgur.com/gQkyWTU.jpg', 'https://i.imgur.com/fLKQMnH.jpg', 'https://i.imgur.com/AdsbQlh.png', 'https://i.imgur.com/WcioBtP.jpg', 'https://i.imgur.com/7tcbusm.png', 'https://i.imgur.com/oTHNfVJ.png', 'https://i.imgur.com/KNycJUR.png', 'https://i.imgur.com/u3tc7nW.jpg', 'https://i.imgur.com/5yDibuV.jpg', 'https://i.imgur.com/bdOv9nM.jpg', 'https://i.imgur.com/BuxtbJQ.jpg', 'https://i.imgur.com/vhgkQPB.png', 'https://i.imgur.com/UjrsUa3.jpg', 'https://i.imgur.com/mOb61tb.jpg', 'https://i.imgur.com/SY6UpYd.png', 'https://i.imgur.com/R01fW9n.png', 'https://i.imgur.com/vT2fN7I.jpg', 'https://i.imgur.com/VIsnAaw.jpg', 'https://i.imgur.com/77lDBNn.jpg', 'https://i.imgur.com/7o5cTsr.jpg', 'https://i.imgur.com/a9mFzPu.jpg', 'https://i.imgur.com/aitpQnP.jpg', 'https://i.imgur.com/GKxJQgk.jpg', 'https://i.imgur.com/QfGfVRf.jpg', 'https://i.imgur.com/2cu58Fx.jpg', 'https://i.imgur.com/w5SCrSm.png', 'https://i.imgur.com/s5HoDfR.jpg', 'https://i.imgur.com/xz4aGiz.jpg', 'https://i.imgur.com/9sOAfNi.png', 'https://i.imgur.com/opCNbIz.jpg', 'https://i.imgur.com/jiYgJg0.jpg', 'https://i.imgur.com/aLBHcIW.jpg', 'https://i.imgur.com/cWqVuey.jpg', 'https://i.imgur.com/9Z6xmoM.jpg', 'https://i.imgur.com/HfKh8Gn.jpg', 'https://i.imgur.com/y7rp8L6.jpg', 'https://i.imgur.com/Dh8PLuP.png', 'https://i.imgur.com/LIOvSmo.jpg', 'https://i.imgur.com/uJqQ4Gj.jpg', 'https://i.imgur.com/3Ob8hvb.jpg', 'https://i.imgur.com/FKC5CGp.jpg', 'https://i.imgur.com/O5a0oJr.jpg', 'https://i.imgur.com/qXB8EBU.jpg']
        
        image = random.choice(choices)
        
        embed = discord.Embed(description=smug.format(author),colour=discord.Colour(0x644aba))
        embed.set_image(url=image)

        await self.bot.say(embed=embed)

def setup(bot):
    n = smug(bot)
    bot.add_cog(n)