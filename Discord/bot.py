import discord 
from discord.ext import commands
import time
import os

DirLink = 'c:/Users/zen11/Desktop/Python/Mrk_bsuir_parser/'

client = commands.Bot(command_prefix = ']')

@client.event
async def on_ready():
    print('Online!')
    
@client.command()
async def ping(ctx):
    await ctx.send("Pong!")



@client.command()
async def sub(ctx, page=1, sleep=3):  #  ]sub 3
    global work
    work = 1
    while work == 1:
        disLogs = open(DirLink + "disLogs.txt", 'r')
        status = disLogs.read()
        disLogs.close()
        if status == "0":
            print("Нового расписания пока нет " + str(work))
            time.sleep(sleep)
            
        else: 
            await ctx.send("Вышло новое рассписание!")
            await ctx.send(file=discord.File('../Images/page' + str(page) + '.jpg'))
            #discord part
            disLogs = open(DirLink + "disLogs.txt", 'w')
            disLogs.write("0")
            disLogs.close()
            time.sleep(sleep)

@client.command()
async def unsub(ctx):
    global work
    work = 0
    print(work)

@client.command()
async def page(ctx, amount=1):
    await ctx.send("Проверяю рассписание")
    await ctx.send(file=discord.File('../Images/page' + str(amount) + '.jpg'))

client.run('NDg3MjQ0ODk2MTMwODI2MjQz.XoCBWw.U3mZm0bppmrM6Tdu6yIg1S_HJd4')