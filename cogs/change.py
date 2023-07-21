import datetime

from discord.ext import commands
from discord.ext import tasks
from PIL import Image, ImageDraw, ImageFont

class Bannerch(commands.Cog):

    def __init__ (self, bot):
        self.bot = bot

    @commands.slash_command(name = 'banner_start', description = 'starting a loop')
    async def activate_banner(self, ctx):
        @tasks.loop(minutes = 10)
        async def banner_changer(self):

                guild = self.bot.get_guild(891345145713270854)
                channel1 = self.bot.get_channel(891367331727564821) #общий чат
                channel2 = self.bot.get_channel(966744691372597248) #флудилка
                channel3 = self.bot.get_channel(1038011786105995275) #команды
                channel4 = self.bot.get_channel(1038011856108929094) #казино
                
                print('start counting...', datetime.datetime.now())
                print(f'Количество участников на {datetime.datetime.now()} {guild.member_count}')

                image = Image.open('cogs/banner.png')
                draw = ImageDraw.Draw(image)

                print('Point 1 passed')

                one_month = datetime.datetime.utcnow() - datetime.timedelta(days = 1)

                message_count_channel1 = 0
                message_count_channel2 = 0
                message_count_channel3 = 0
                message_count_channel4 = 0

                async for _ in channel1.history(after = one_month, limit = None): #подсчет сообщений в общем чате за последие 15 дней
                    message_count_channel1 += 1

                print('...')

                async for _ in channel2.history(after = one_month, limit = None): #подсчет сообщений во флудилке за последние 15 дней
                    message_count_channel2 += 1

                print('...')

                async for _ in channel3.history(after = one_month, limit = None): #подсчет сообщений в командах за последние 15 дней
                    message_count_channel3 += 1

                print('...')

                async for _ in channel4.history(after = one_month, limit = None): #подсчет сообщений в казино за последние 15 дней
                    message_count_channel4 += 1

                print('...')

                message_count = message_count_channel1 + message_count_channel2 + message_count_channel3 + message_count_channel4

                print('Point 2 passed')
                            
                font = ImageFont.truetype('cogs/DynaPuff-Medium.ttf', size = 150)
                draw.text((527, 705), f' {guild.member_count}', fill='#8D17BA', font=font)

                font = ImageFont.truetype('cogs/DynaPuff-Medium.ttf', size = 150)
                draw.text((1250, 705), f' {message_count}', fill='#8D17BA', font=font) 

                image.save('cogs/stats_banner.png')
                print('Point 3 passed')

                with open('cogs/stats_banner.png', 'rb') as f:
                    new_banner = f.read()
                    
                await guild.edit(banner = new_banner)
                print('Баннер обновлен', datetime.datetime.now())
        
        banner_changer.start(self)
        await ctx.respond('Has been activated')

def setup(bot):
    bot.add_cog(Bannerch(bot))