import asyncio
import datetime
import random
import re
import time
import matplotlib.pyplot as plt
import numpy as np
from random import randint
from urllib import parse, request

import discord
from discord.ext import commands, tasks

from modules.anigifs import *
from config import *

bot = commands.Bot(intents=discord.Intents.all(), help_command=None)

 #     #     #     ######   ###  #######   #####  
 #     #    # #    #     #   #   #     #  #     # 
 #     #   #   #   #     #   #   #     #  #       
 #     #  #     #  ######    #   #     #   #####  
  #   #   #######  #   #     #   #     #        # 
   # #    #     #  #    #    #   #     #  #     # 
    #     #     #  #     #  ###  #######   ##### 

@bot.slash_command(name="ping", description="Muestra la latencia del bot.")
async def ping(ctx):
    await ctx.respond(f'Pong! Latency is {bot.latency}')

@bot.slash_command(name="info", description="Muestra información sobre el servidor.")
async def info(ctx):
    embed1 = discord.Embed(title=f"{ctx.guild.name}", description="Información del servidor", timestamp=datetime.datetime.now(), color=discord.Color.gold() )
    embed1.add_field(name="Miembros: ", value=f"{ctx.guild.member_count}")
    embed1.add_field(name="Creador: ",  value=f"{ctx.guild.owner}")
    dislogo = discord.File(imgpath(DISCORD_LOGO), filename="image.png")
    embed1.set_footer(icon_url="attachment://image.png", text=f"pedido por {ctx.author.name}")
    embed1.set_thumbnail(url="attachment://image.png")

    embed2 = discord.Embed(title=BOT_NAME, color=discord.Color.gold())
    embed2.add_field(name="Lenguaje", value=f"Python", inline=False)
    embed2.add_field(name="Tipo", value=f"Multipropósito", inline=False)
    botlogo = discord.File(imgpath(BOT_LOGO), filename="image.png")
    embed2.set_image(url="attachment://image.png")

    await ctx.respond(file=dislogo, embed=embed1)
    await ctx.respond(file=botlogo, embed=embed2)

@bot.slash_command(name='yt', description="Busca algo en YouTube.")
async def yt(ctx, *, búsqueda):
    query_string = parse.urlencode({'search_query': búsqueda})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results=re.findall('watch\?v=(.{11})',html_content.read().decode('utf-8'))
    print(search_results)
    await ctx.respond('https://www.youtube.com/watch?v=' + search_results[0])

@bot.slash_command(name='say', description="Manda un mensaje a través del bot.")
async def say(ctx, *, algo):
    await ctx.respond("Mensaje enviado :)", ephemeral=True)
    await ctx.send(algo)

@bot.slash_command(name='help', description="Muestra todos los comandos del bot en un menú de ayuda.")
async def help(ctx):
    embed = discord.Embed(title="Menú de ayuda", color=discord.Color.gold())
    embed.add_field(name="Varios", value="ping, info, yt, say, help, platano, dado, moneda, avatar, spam", inline=False)
    embed.add_field(name="Interacción", value="amb, dance, fbi, hug, kill, kiss, pat, run, sad, slap, sleep, fusilar, hentai", inline=False)
    embed.add_field(name="Operaciones matemáticas", value="contar, calc", inline=False)
    embed.add_field(name="Gráficas", value="sen, cos, rect, par")
    embed.add_field(name="Música", value="*Próximamente...*", inline=False)
    await ctx.respond(embed=embed)

@bot.slash_command(name='platano', description="Conoce la medida de tu plátano.")
async def platano(ctx):
    a = 2
    b = 21
    if ctx.author.id == OWNER_ID: #id del owner para que la medida siempre salga 21
        banana = 21
    else:
        banana = randint(a,b)
    embed = discord.Embed(title=f"El plátano de **{ctx.author}** mide {banana} cm 😳", color=discord.Color.gold())
    embed.set_image(url="https://cdn.discordapp.com/attachments/755529601333067940/853072892702490624/banana.png")
    await ctx.respond(embed=embed)    

@bot.slash_command(name='dado', description="Tira un dado de 6 caras.")
async def dado(ctx):
    a = 1
    b = 6
    res = randint(a,b)
    embed = discord.Embed(title="🎲 Se ha lanzado un dado", color = discord.Color.gold())
    embed.add_field(name="Resultado: ", value=str(res))
    await ctx.respond(embed=embed)

@bot.slash_command(name='moneda', description="Tira una moneda al aire.")
async def moneda(ctx):
    coinResults = ("Cara 😀", "Cruz ❌")
    res = random.choice(coinResults)
    embed = discord.Embed(title="🪙 Se ha lanzado la moneda", color = discord.Color.gold())
    embed.add_field(name="Resultado: ", value=res)
    await ctx.respond(embed=embed)

@bot.slash_command(name='avatar', description="Renderiza el avatar de alguien.")     
async def avatar(ctx, *, miembro: discord.Member):
    embed = discord.Embed(color=discord.Color.gold())
    embed.add_field(name='Avatar de:', value=miembro.mention)
    pfp = miembro.avatar.with_size(1024)
    embed.set_image(url=pfp)
    await ctx.respond(embed=embed)

@bot.slash_command(name='spam', description="A molestar ùwú.")
async def spam(ctx, *, miembro: discord.Member, mensaje, veces: int):
    if miembro.id != OWNER_ID: # id del owner para que no le puedan spammear
        idl = list(miembro.mention)
        usrid = idl[2:-1]
        spamtoid = int(''.join(str(i) for i in usrid))
        user = await bot.fetch_user(spamtoid)
        await ctx.respond("Spammeando", ephemeral = True)      
        await user.send(f"Fuiste spameado por {ctx.author} 🙂\n================================")
        for r in range(veces):
            await user.send(mensaje)
        await user.send("||`"+DISCORD_INVITE+"`||")
    else:
        await ctx.respond("No puedes spammear a" + OWNER_NAME + "😡", ephemeral = True)


 ###  #     #  #######  #######  ######      #      #####    #####   ###  #######  #     # 
  #   ##    #     #     #        #     #    # #    #     #  #     #   #   #     #  ##    # 
  #   # #   #     #     #        #     #   #   #   #        #         #   #     #  # #   # 
  #   #  #  #     #     #####    ######   #     #  #        #         #   #     #  #  #  # 
  #   #   # #     #     #        #   #    #######  #        #         #   #     #  #   # # 
  #   #    ##     #     #        #    #   #     #  #     #  #     #   #   #     #  #    ## 
 ###  #     #     #     #######  #     #  #     #   #####    #####   ###  #######  #     # 

@bot.slash_command(name='dance', description="Saca los pasos prohibidos.")
async def dance(ctx):
    embed = discord.Embed(description=f"{ctx.author.mention} se puso a bailar", color = discord.Color.gold())
    danceFile = rDANCE();
    file = discord.File(danceFile, filename="imagen.gif")
    embed.set_image(url="attachment://imagen.gif")
    await ctx.respond(file=file, embed=embed)

@bot.slash_command(name='hug', description="Abraza a alguien.")
async def hug(ctx, *, miembro: discord.Member):
    embed = discord.Embed(description=f"{ctx.author.mention} le dio un abrazo a {miembro.mention}", color = discord.Color.gold())
    danceFile = rHUG();
    file = discord.File(danceFile, filename="imagen.gif")
    embed.set_image(url="attachment://imagen.gif")
    await ctx.respond(file=file, embed=embed)

@bot.slash_command(name='kill', description="Arrebátale la vida a alguien.")
async def kill(ctx, *, miembro: discord.Member):
    embed = discord.Embed(description=f"{ctx.author.mention} asesinó a {miembro.mention}", color = discord.Color.gold())
    danceFile = rKILL();
    file = discord.File(danceFile, filename="imagen.gif")
    embed.set_image(url="attachment://imagen.gif")
    await ctx.respond(file=file, embed=embed)

@bot.slash_command(name='kiss', description="Cómele la boca a alguien.")
async def kiss(ctx, *, miembro: discord.Member):
    embed = discord.Embed(description=f"{ctx.author.mention} le dio un beso a {miembro.mention} >.<", color = discord.Color.gold())
    danceFile = rKISS();
    file = discord.File(danceFile, filename="imagen.gif")
    embed.set_image(url="attachment://imagen.gif")
    await ctx.respond(file=file, embed=embed)

@bot.slash_command(name='pat', description="Acaricia a alguien.")
async def pat(ctx, *, miembro: discord.Member):
    embed = discord.Embed(description=f"{ctx.author.mention} acarició a {miembro.mention} UwU", color = discord.Color.gold())
    danceFile = rPAT();
    file = discord.File(danceFile, filename="imagen.gif")
    embed.set_image(url="attachment://imagen.gif")
    await ctx.respond(file=file, embed=embed)

@bot.slash_command(name='slap', description="Abofetea a alguien.")
async def slap(ctx, *, miembro: discord.Member):
    embed = discord.Embed(description=f"{ctx.author.mention} le dio una bofetada a {miembro.mention} >:)", color = discord.Color.gold())
    danceFile = rSLAP();
    file = discord.File(danceFile, filename="imagen.gif")
    embed.set_image(url="attachment://imagen.gif")
    await ctx.respond(file=file, embed=embed)

@bot.slash_command(name='sleep', description="A mimir.")
async def sleep(ctx):
    embed = discord.Embed(description=f"{ctx.author.mention} se fue a mimir", color = discord.Color.gold())
    danceFile = rSLEEP();
    file = discord.File(danceFile, filename="imagen.gif")
    embed.set_image(url="attachment://imagen.gif")
    await ctx.respond(file=file, embed=embed)

@bot.slash_command(name='sad', description="Expresa tu tristeza...")
async def sad(ctx):
    embed = discord.Embed(description=f"{ctx.author.mention} se puso triste :(", color = discord.Color.gold())
    danceFile = rSAD();
    file = discord.File(danceFile, filename="imagen.gif")
    embed.set_image(url="attachment://imagen.gif")
    await ctx.respond(file=file, embed=embed)

@bot.slash_command(name='hentai', description="Go to horny jail.")
async def hentai(ctx):
    if ctx.channel.is_nsfw():
        embed = discord.Embed(description="Disfruta 😳", color = discord.Color.gold())
        hentaiFile = rHENTAI();
        file = discord.File(hentaiFile, filename="imagen.gif")
        embed.set_image(url="attachment://imagen.gif")
        await ctx.respond(file=file, embed=embed)
    else:
        await ctx.respond("*Debes usar el comando en un canal NSFW...*", ephemeral=True)

########################################################################################################################################

@bot.slash_command(name='fusilar', description="Fusila a alguien como tito Franco hacía antiguamente.")
async def fusilar(ctx, *, alguien: discord.Member):
    embed = discord.Embed(description=f"{ctx.author.mention} fusiló a {alguien.mention}", color=discord.Color.gold())
    file = discord.File(ailibind("fusilar.gif"), filename="imagen.gif")
    embed.set_image(url="attachment://imagen.gif")
    await ctx.respond(file=file, embed=embed)

@bot.slash_command(name='run', description="Huye!!!")
async def run(ctx):
    embed = discord.Embed(description=f"{ctx.author.mention} se puso a correr", color = discord.Color.gold())
    file = discord.File(ailibind("run.gif"), filename="imagen.gif")
    embed.set_image(url="attachment://imagen.gif")
    await ctx.respond(file=file, embed=embed)

@bot.slash_command(name='fbi', description="Llama al FBI.")
async def run(ctx, *, miembro: discord.Member):
    embed = discord.Embed(description=f"{ctx.author.mention} ha llamado al FBI. Corre {miembro.mention}!", color = discord.Color.gold())
    file = discord.File(ailibind("fbi.gif"), filename="imagen.gif")
    embed.set_image(url="attachment://imagen.gif")
    await ctx.respond(file=file, embed=embed)

@bot.slash_command(name='amb', description="Llama a la ambulancia.")
async def amb(ctx, *, miembro: discord.Member):
    embed = discord.Embed(description=f"{ctx.author.mention} ha llamado al 061. La ayuda está en camino, {miembro.mention}", color = discord.Color.gold())
    file = discord.File(ailibind("ambulancia.gif"), filename="imagen.gif")
    embed.set_image(url="attachment://imagen.gif")
    await ctx.respond(file=file, embed=embed)

 #######  ######   #######  ######      #      #####   ###  #######  #     #  #######   #####  
 #     #  #     #  #        #     #    # #    #     #   #   #     #  ##    #  #        #     # 
 #     #  #     #  #        #     #   #   #   #         #   #     #  # #   #  #        #       
 #     #  ######   #####    ######   #     #  #         #   #     #  #  #  #  #####     #####  
 #     #  #        #        #   #    #######  #         #   #     #  #   # #  #              # 
 #     #  #        #        #    #   #     #  #     #   #   #     #  #    ##  #        #     # 
 #######  #        #######  #     #  #     #   #####   ###  #######  #     #  #######   #####  

@bot.slash_command(name='contar', description="Cuenta desde a hasta b.")
async def contar(ctx, a: int, b: int):
    await ctx.respond(f"*Contando desde {a} hasta {b}...*", ephemeral=True)
    i = a
    time.sleep(1)
    await ctx.send(a)
    time.sleep(1)
    for i in range(a,b):
        await ctx.send(str(i+1))
        time.sleep(1)

@bot.slash_command(name="calc", description="Resuelve una expresión matemática.")
async def calc(ctx, *, expresion):
    embed = discord.Embed(color=discord.Color.gold())
    embed.add_field(name="**Resultado**", value=f"{expresion} = " + str(eval(expresion)))
    await ctx.respond(embed=embed)

  #####   ######      #     #######  ###   #####      #      #####  
 #     #  #     #    # #    #         #   #     #    # #    #     # 
 #        #     #   #   #   #         #   #         #   #   #       
 #  ####  ######   #     #  #####     #   #        #     #   #####  
 #     #  #   #    #######  #         #   #        #######        # 
 #     #  #    #   #     #  #         #   #     #  #     #  #     # 
  #####   #     #  #     #  #        ###   #####   #     #   #####  
                                                                    
@bot.slash_command(name='sen', description="Grafica una función seno (a, k).")
async def sen(ctx, a: int, k: int):
    x = np.linspace(0, 2*np.pi,400)
    y = a * np.sin(k*x)
    plt.axhline(0, color="black")
    plt.plot(x, y)
    plt.savefig("graf.png")
    await ctx.respond(file=discord.File("graf.png"))
    plt.clf()

@bot.slash_command(name='cos', description="Grafica una función coseno (a, k).")
async def cos(ctx, a: int, k: int):
    x = np.linspace(0, 2*np.pi,400)
    y = a * np.cos(k*x)
    plt.axhline(0, color="black")
    plt.plot(x, y)
    plt.savefig("graf.png")
    await ctx.respond(file=discord.File("graf.png"))
    plt.clf()

@bot.slash_command(name='rect', description="Grafica una función lineal (m, n).")
async def rect(ctx, m: int, n: int):
    def f(x):
        return m*x+n
    x = range(-10000, 10000)
    y = [f(i) for i in x]
    plt.axhline(0, color="black")
    plt.axvline(0, color="black")
    plt.xlim(-10, 10)
    plt.ylim(-20, 20)
    plt.plot(x, y)
    plt.savefig("graf.png")
    await ctx.respond(file=discord.File("graf.png"))
    plt.clf()

@bot.slash_command(name='par', description="Grafica una parábola (a, b, c).")
async def par(ctx, a: int, b: int, c: int):
    def f(x):
        return a*(x*x)+b*x+c
    x = np.linspace(-10, 10, 1000)
    y = [f(i) for i in x]
    plt.axhline(0, color="black")
    plt.axvline(0, color="black")
    plt.xlim(-10, 10)
    plt.ylim(-20, 20)
    plt.plot(x, y)
    plt.savefig("graf.png")
    await ctx.respond(file=discord.File("graf.png"))
    plt.clf()

 #######  #     #  #######  #     #  #######   #####  
 #        #     #  #        ##    #     #     #     # 
 #        #     #  #        # #   #     #     #       
 #####    #     #  #####    #  #  #     #      #####  
 #         #   #   #        #   # #     #           # 
 #          # #    #        #    ##     #     #     # 
 #######     #     #######  #     #     #      #####  

@bot.event
async def on_ready():         
    channel = bot.get_channel(ADMIN_CHANNEL_ID) # canal de admins para anunciar cuando se inicia el bot
    embed = discord.Embed(title = "Pype Console", description = "```✅ | Server has started\n✅ | Bot has run succesfully\n🤖 | Estoy listo pa\n🤖 | _```", color = discord.Color.gold())
    await channel.send(embed=embed)

    print(
        '╔════════════════════════════════════╗\n'
        '║EL BOT SE HA INICIADO CORRECTAMENTE!║\n'
        '╚════════════════════════════════════╝',
        )
    
    with open("./data/grupos.txt", encoding="utf-8") as f:
        grupos = []
        for linea in f:
            grupos.append(linea)
    
    with open("./data/grupos.txt", encoding="utf-8") as f:
        juegos = []
        for linea in f:
            juegos.append(linea)

    with open("./data/grupos.txt", encoding="utf-8") as f:
        shows = []
        for linea in f:
            shows.append(linea)

    botstatus = "ready"
    while botstatus == "ready":
        await bot.change_presence(activity=discord.Game(name=str(random.choice(juegos))))
        await asyncio.sleep(60)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=str(random.choice(shows))))
        await asyncio.sleep(60)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=str(random.choice(grupos))))
        await asyncio.sleep(60)

bot.run(BOT_TOKEN)
