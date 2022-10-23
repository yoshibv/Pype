from random import randint
import discord

def rDANCE():
    # creación de lista vacía 
    gifNumberList = []
    # bucle para randomizar las urls de los 
    # gifs dentro de la carpeta
    for i in range(0,21):
        i+1
        gifNumberList.append(i)
    # asignación de los parámetros a y b que 
    # aleatorizará la url con randint
    a = gifNumberList[0]
    b = gifNumberList[i]
    fileNumber = randint(a,b)
    # variable equivalente a la url construida 
    # con su número aleatoriamente escogido
    url = "./images/animageslib/dance/dance-"+str(fileNumber)+".gif"
    return url

def rHUG():
    # creación de lista vacía 
    gifNumberList = []
    # bucle para randomizar las urls de los 
    # gifs dentro de la carpeta
    for i in range(0,21):
        i+1
        gifNumberList.append(i)
    # asignación de los parámetros a y b que 
    # aleatorizará la url con randint
    a = gifNumberList[0]
    b = gifNumberList[i]
    fileNumber = randint(a,b)
    # variable equivalente a la url construida 
    # con su número aleatoriamente escogido
    url = "./images/animageslib/hug/hug-"+str(fileNumber)+".gif"
    return url

def rKILL():
    # creación de lista vacía 
    gifNumberList = []
    # bucle para randomizar las urls de los 
    # gifs dentro de la carpeta
    for i in range(0,21):
        i+1
        gifNumberList.append(i)
    # asignación de los parámetros a y b que 
    # aleatorizará la url con randint
    a = gifNumberList[0]
    b = gifNumberList[i]
    fileNumber = randint(a,b)
    # variable equivalente a la url construida 
    # con su número aleatoriamente escogido
    url = "./images/animageslib/kill/kill-"+str(fileNumber)+".gif"
    return url

def rKISS():
    # creación de lista vacía 
    gifNumberList = []
    # bucle para randomizar las urls de los 
    # gifs dentro de la carpeta
    for i in range(0,21):
        i+1
        gifNumberList.append(i)
    # asignación de los parámetros a y b que 
    # aleatorizará la url con randint
    a = gifNumberList[0]
    b = gifNumberList[i]
    fileNumber = randint(a,b)
    # variable equivalente a la url construida 
    # con su número aleatoriamente escogido
    url = "./images/animageslib/kiss/kiss-"+str(fileNumber)+".gif"
    return url

def rPAT():
    # creación de lista vacía 
    gifNumberList = []
    # bucle para randomizar las urls de los 
    # gifs dentro de la carpeta
    for i in range(0,21):
        i+1
        gifNumberList.append(i)
    # asignación de los parámetros a y b que 
    # aleatorizará la url con randint
    a = gifNumberList[0]
    b = gifNumberList[i]
    fileNumber = randint(a,b)
    # variable equivalente a la url construida 
    # con su número aleatoriamente escogido
    url = "./images/animageslib/pat/pat-"+str(fileNumber)+".gif"
    return url

def rSLAP():
    # creación de lista vacía 
    gifNumberList = []
    # bucle para randomizar las urls de los 
    # gifs dentro de la carpeta
    for i in range(0,21):
        i+1
        gifNumberList.append(i)
    # asignación de los parámetros a y b que 
    # aleatorizará la url con randint
    a = gifNumberList[0]
    b = gifNumberList[i]
    fileNumber = randint(a,b)
    # variable equivalente a la url construida 
    # con su número aleatoriamente escogido
    url = "./images/animageslib/slap/slap-"+str(fileNumber)+".gif"
    return url

def rSLEEP():
    # creación de lista vacía 
    gifNumberList = []
    # bucle para randomizar las urls de los 
    # gifs dentro de la carpeta
    for i in range(0,21):
        i+1
        gifNumberList.append(i)
    # asignación de los parámetros a y b que 
    # aleatorizará la url con randint
    a = gifNumberList[0]
    b = gifNumberList[i]
    fileNumber = randint(a,b)
    # variable equivalente a la url construida 
    # con su número aleatoriamente escogido
    url = "./images/animageslib/sleep/sleep-"+str(fileNumber)+".gif"
    return url

def rSAD():
    # creación de lista vacía 
    gifNumberList = []
    # bucle para randomizar las urls de los 
    # gifs dentro de la carpeta
    for i in range(0,21):
        i+1
        gifNumberList.append(i)
    # asignación de los parámetros a y b que 
    # aleatorizará la url con randint
    a = gifNumberList[0]
    b = gifNumberList[i]
    fileNumber = randint(a,b)
    # variable equivalente a la url construida 
    # con su número aleatoriamente escogido
    url = "./images/animageslib/sad/sad-"+str(fileNumber)+".gif"
    return url

def rHENTAI():
    # creación de lista vacía 
    gifNumberList = []
    # bucle para randomizar las urls de los 
    # gifs dentro de la carpeta
    for i in range(0,67):
        i+1
        gifNumberList.append(i)
    # asignación de los parámetros a y b que 
    # aleatorizará la url con randint
    a = gifNumberList[0]
    b = gifNumberList[i]
    fileNumber = randint(a,b)
    # variable equivalente a la url construida 
    # con su número aleatoriamente escogido
    url = "./images/hentaimages/hentai ("+str(fileNumber)+").gif"
    return url

def imgpath(archivo):
    return "./images/assets/" + archivo

def ailibind(archivo):
    return "./images/animageslib/" + archivo

def color_parser(color):
    if color == "AMARILLO":
        res = discord.Color.gold()
    elif color == "ROJO":
        res = discord.Color.red()
    elif color == "AZUL":
        res = discord.Color.blue()
    elif color == "DISCORD":
        res = discord.Color.blurple()
    elif color == "NARANJA":
        res = discord.Color.orange()
    elif color == "ROSA":
        res = discord.Color.nitro_pink()
    elif color == "MORADO":
        res = discord.Color.purple()
    else:
        res = discord.Color.og_blurple()
    return res