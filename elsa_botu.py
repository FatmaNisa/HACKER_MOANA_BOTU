from http import client
from logging import info
import discord
import random
import os
import requests
from discord.ext import commands
import komutlu_konuşma
from flask import Flask, jsonify
from flask_restful import Resource, Api
import elsayapay_z
intents = discord.Intents.default()
intents.message_content = True
import arama_motoru
bot = commands.Bot(command_prefix='-', intents=intents)




@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
   
@bot.command()
async def merhaba(ctx):
    await ctx.send(f'selam! Ben {bot.user}, bir Discord sohbet botuyum!Ve yeteneklerim şunlar 1.istediğin şeyi çarpar,böler,toplar veya çıkarta bilirim bunun için sohbete -topla -çarpı -eksi veya -bölü yaz ve işlem yapmak istediğin iki sayıyı yaz 2.eğer sohbete -bunu_cevapla yaz ve yanına bir sorunu yazarsan sana cevabını anında söylerim 3.eğer sohbete -duck yazarsan sana raskele bir ördek gönderirim ve bu her seferinde değişir 4.eğer sohbete -tilki yazarsan sana raskele bir tilki gönderirim ve bu her seferinde değişir 5.eğer sohbete -Pokemon yazarsan sana raskele bir pokemon gönderirim ve bu her seferinde değişir 6.eğer sohbete -resmi_tanimla yazarsan ve bir kuş resmi gönderirsen sana onun hangi sınıfa ait olduğunu söylerim(bilmediğim resimlere diger derim) 7.eğer sohbete -resim yazarsan sana raskelele bir resim gönderirim 8.eğer sohbete -resim yazıp dibine 1 den 3 e kadar bir sayı yazarsan sana bir resim gönderirim 9.eğer sohbete -ses yazarsan sana şimdi konuşabilirsin mesajını gönderirim bu mesajı gönderdikten sonra konuşursan ve selemlaşma cümleleri,duck,pokemon,tilki veya resim seçeneklerinden birinini söylersen sana cevabını söylerim 10.eğer sohbete -haber yazarsan sana günün sabah haberlerini atarım ')

@bot.command()
async def görüşürüz(ctx):
    await ctx.send(f'gülegüle {bot.user}, sana iyi günler diler')

@bot.command()
async def nasılsın(ctx):
    await ctx.send(f'iyiyim sen nasılsın')

@bot.command()
async def bunu_cevapla(ctx,*,soru):
    arama_motoru.geminiai(soru)
    with open("output.txt","r",encoding="utf-8") as file:
            x=file.read()
    await ctx.send(f'{x}')
@bot.command()
async def haber(ctx): 
    toplam_karakter=0
    sonuc=arama_motoru.haberler()  
    for i in sonuc: 
        await ctx.send (i.text)
    for i in sonuc:

        if toplam_karakter + len(i.text) + 1 > 2000:  # Mesajın 2000 karakteri aşmamasını kontrol ediyoruz
            await ctx.send(mesaj)  # Mesaj sınırını aşmadan gönderiyoruz
            mesaj = ""  # Mesajı sıfırlıyoruz
            toplam_karakter = 0  # Karakter sayacını sıfırlıyoruz
            
        mesaj += i.text + "\n"  # Haberi biriktiriyoruz
        toplam_karakter += len(i.text) + 1  # Karakter uzunluğunu güncelliyoruz
    
    if mesaj:  # Eğer hala gönderilmemiş bir mesaj varsa, onu da gönderiyoruz
        await ctx.send(mesaj)

@bot.command()
async def iyiyim(ctx):
    await ctx.send(f'harika')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def topla(ctx, s1:int,s2:int):
    await ctx.send(f"toplam: {s1+s2}")
@bot.command()
async def çarpı(ctx, s1:int,s2:int):
    await ctx.send(f"çarpım: {s1*s2}")

@bot.command()
async def eksi(ctx, s1:int,s2:int):
    await ctx.send(f"eksilim: {s1-s2}")

@bot.command()
async def bölü(ctx, s1:int,s2:int):
    await ctx.send(f"bölüm: {s1/s2}")
  
@bot.command()
async def resim(ctx):
    a=random.choice(os.listdir("resimler"))
    with open(f"resimler/{a}","rb")as r:
        fatma=discord.File(r)
    await ctx.send(file=fatma)

@bot.command()
async def resimler(ctx):
    ihtimal=[0.10,0.30,0.60]
    n=random.choices(os.listdir("resimler"),weights=ihtimal,k=1) [0]
    with open(f"resimler/{n}","rb")as r:
        fatma=discord.File(r)
    await ctx.send(file=fatma)


@bot.command()
async def resim1(ctx):
    with open(f"resimler/resim1.png","rb")as r:
        fatma=discord.File(r)
    await ctx.send(file=fatma)

@bot.command()
async def ses(ctx):
    await ctx.send ("şimdi konuşabilirsin")
    konuş_t= komutlu_konuşma.konuş_tr().lower()
    await ctx.send  (konuş_t)  
    if "merhaba" in konuş_t:
        await merhaba (ctx)
    elif "resim" in konuş_t:
        if "bir" in konuş_t  or "1" in konuş_t:
            await resim1 (ctx)
        elif "iki" in konuş_t or "2" in konuş_t:
            await resim2 (ctx)
        elif "üç" in konuş_t or "3" in konuş_t:
            await resim3 (ctx)
        else:
            await resim (ctx)
    elif "görüşürüz" in konuş_t:
        await görüşürüz (ctx)
    elif "nasılsın" in konuş_t:
        await nasılsın (ctx)
    elif "iyiyim" in konuş_t:
        await iyiyim (ctx)
    elif "duck" in konuş_t:
        await duck (ctx)
    elif "tilki" in konuş_t:
        await tilki (ctx)
    elif "pokemon" in konuş_t:
        await pokemon (ctx)
    else:
        await ctx.send ("söylediğin şeyi ben bilmiyorum")
@bot.command()
async def resim2(ctx):
    with open(f"resimler/resim2.png","rb")as r:
        fatma=discord.File(r)
    await ctx.send(file=fatma)

@bot.command()
async def resim3(ctx):
    with open(f"resimler/resim3.png","rb")as r:
        fatma=discord.File(r)
    await ctx.send(file=fatma)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def tlk():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']


@bot.command('tilki')
async def tilki(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = tlk()
    await ctx.send(image_url)


@bot.command('Pokemon')
async def pokemon (ctx):
  ranpoke = random.randint(1, 905)
  url = "https://pokeapi.co/api/v2/pokemon/"
  secs = 5

  try:
    r = requests.get(f"{url}{ranpoke}")
    packages_json = r.json()
    packages_json.keys

    napo = packages_json["name"]

    embed = discord.Embed(title = "Bu olur mu ?", color = discord.Color.random())
    embed.set_image(url = f"https://play.pokemonshowdown.com/sprites/ani/{napo}.gif")
    await ctx.send(embed = embed)

    

    def check(msg):
      return msg.author == ctx.author and msg.channel == ctx.channel

    user_ans = await client.wait_for("message", check=check)


    if user_ans == napo:
      await ctx.send("You are correct! :)")
    elif user_ans != napo:
      await ctx.send(f"You are incorrect :v\nThe answer is {napo}")

  except:pass 
@bot.command()
async def resmi_tanimla(ctx):
    if ctx.message.attachments:
        for resim in ctx.message.attachments:
            await resim.save(f'./resimler/{resim.filename}')
            await ctx.send("Mesaj gönderildi")
            moana,elsa=elsayapay_z.discort(f'./resimler/{resim.filename}')
            await ctx.send(f"bu bir {moana}.{elsa} ihtimalle eminim")
            if moana=="Guvercin":
                await ctx.send("Bulgur ve pirinci bolca tüketen güvercinler oldukça sıcakkanlı canlılardır. Güvercinler aynı zamanda çeşitli sebzeleri de beraberinde tüketmektedir. Lahana, bezelye, karnabahar ve marul gibi yiyecekleri dilimleyerek güvercine verebilirsiniz. Dilerseniz petshoplarda yer alan güvercin yemlerini de tercih edebilirsiniz")
            elif moana=="Serce":
                await ctx.send("Genellikle meyve, tohum, böcek ve larva gibi besinler tüketirler. Göçmen değildirler. Çekirdek ve ekmek artıkları da yerler.")
            elif moana=="Karga":
                await ctx.send("Beslenme. Omnivor bir beslenme şekline sahiptirler, hemen hemen her şeyi yerler. Meyve, sebze, tahıl, kuruyemiş, besin çöpleri, leş, her türlü et çeşidi, böcekler, omurgasızlar, tohum, yavru kuşlar, kuş yumurtaları, yavru hayvanlar (kendinden boyut olarak küçük olan, yavru veya sakat olan canlıları avlayıp yerler)")
            elif moana=="Diger":
                await ctx.send("ben bunu tanımıyorum")
            else:
                await ctx.send("kod hatalı")
    else:
        await ctx.send("Herhangi bir resim göndermedin")


bot.run("")




