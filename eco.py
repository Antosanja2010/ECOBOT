import discord
import random
import os
from discord.ext import commands




intents = discord.Intents.default()
intents.message_content = True



bot = commands.Bot(command_prefix='%', intents=intents)


@bot.event
async def on_member_join(member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Приветсвую чтобы начать изучать как очистить свою окружающию среду впиши:%start, {0.mention}.'.format(member))


@bot.command()
async def start(ctx):
    await ctx.send(f'Привет я бот ECO-BOT я тебе помогу улучшить окружающию среду вокруг тебя !')
    await ctx.send(f'Для начала ты должен понять куда какой мусор ложить есть 3 вида мусорных баков')
    await ctx.send(f'Первый мусорный бак это пластик ')
    await ctx.send(f'Второй стекло')
    await ctx.send(f'Трейтий метал')
    await ctx.send(f'Четвертый бумага')
    images = os.listdir('images')
    img_name = random.choice(images)
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

    images1 = os.listdir('images1')
    img_name = random.choice(images1)
    with open(f'images1/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send(f'Как уменшить загрезнение природы от себя?')
    await ctx.send(f'1:выкидывать все неорганическое в урну')
    await ctx.send(f'2:использовать меньше пластиковых пакетов')
    await ctx.send(f'3:по возможности ложит мусор в перерабатывающие контейнеры')
    await ctx.send(f'4:не выкидывать батарейки на землю')
    images2 = os.listdir('images2')
    img_name = random.choice(images2)
    with open(f'images2/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send(f'Что батарейки очень плохо воздействуют на почву радиацией?')
    await ctx.send(f'Что ты хочешь узнать?!:как гниет разные продукции? (gnil) или где самое грязное мето на земле?(mesto)')
@bot.command()
async def gnil(ctx):
    images3 = os.listdir('images3')
    img_name = random.choice(images3)
    with open(f'images3/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send(f'Ну вроде все все я тебе показал до встречи! И выбрасывай за собой мусор!!!')

@bot.command()
async def mesto(ctx):
    images4 = os.listdir('images4')
    img_name = random.choice(images4)
    with open(f'images4/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send(f'Вот самое грязное место в мире:Сарно, Италия')
    images5 = os.listdir('images5')
    img_name = random.choice(images5)
    with open(f'images5/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

    await ctx.send(f'Ну вроде все все я тебе показал до встречи! И выбрасывай за собой мусор!!!')





bot.run("Свой токен")
