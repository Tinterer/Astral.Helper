import codecs
import discord

from discord.ext import commands

class Rules(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(name = 'rule', description = 'show server rules')
    async def rule(self, ctx, number: discord.Option(str)):

        g = codecs.open('cogs/rules.txt', encoding = 'utf-8')

            #ЦИКЛЫ ПРАВИЛ

        #1.1
        rule1_1 = ''
        for i in range(9):
            rule1_1 += g.readline()

        emb_rule1_1 = discord.Embed(color = 0xffffff, 
                                title = "**Правило 1.1**", 
                                description = rule1_1)

        #1.2
        rule1_2 = ''
        for i in range(3):
            rule1_2 += g.readline()

        emb_rule1_2 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 1.2**",
                                    description = rule1_2)

        #1.3
        rule1_3 = ''
        for i in range(2):
            rule1_3 += g.readline()

        emb_rule1_3 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 1.3**",
                                    description = rule1_3)

        #1.3.1
        rule1_3_1 = ''
        for i in range(8):
            rule1_3_1 += g.readline()

        emb_rule1_3_1 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 1.3.1**",
                                    description = rule1_3_1)

        #1.4
        rule1_4 = ''
        for i in range(3):
            rule1_4 += g.readline()

        emb_rule1_4 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 1.4**",
                                    description = rule1_4)

        #1.5
        rule1_5 = ''
        for i in range(2):
            rule1_5 += g.readline()

        emb_rule1_5 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 1.5**",
                                    description = rule1_5)

        #1.5.1
        rule1_5_1 = ''
        for i in range(2):
            rule1_5_1 += g.readline()

        emb_rule1_5_1 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 1.5.1**",
                                    description = rule1_5_1)

        #1.6
        rule1_6_1 = ''
        for i in range(2):
            rule1_6_1 += g.readline()

        emb_rule1_6_1 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 1.6.1**",
                                    description = rule1_6_1)

        rule1_6_2 = ''
        for i in range(2):
            rule1_6_2 += g.readline()

        emb_rule1_6_2 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 1.6.2**",
                                    description = rule1_6_2)

        rule1_6_3 = ''
        for i in range(2):
            rule1_6_3 += g.readline()

        emb_rule1_6_3 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 1.6.3**",
                                    description = rule1_6_3)

        rule1_6_4 = ''
        for i in range(2):
            rule1_6_4 += g.readline()

        emb_rule1_6_4 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 1.6.4**",
                                    description = rule1_6_4)

        rule1_6_5 = ''
        for i in range(2):
            rule1_6_5 += g.readline()

        emb_rule1_6_5 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 1.6.5**",
                                    description = rule1_6_5)

        rule1_6_6 = ''
        for i in range(2):
            rule1_6_6 += g.readline()

        emb_rule1_6_6 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 1.6.6**",
                                    description = rule1_6_6)

        #1.7
        rule1_7 = ''
        for i in range(2):
            rule1_7 += g.readline()

        emb_rule1_7 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 1.7**",
                                    description = rule1_7)

        #1.8.1
        rule1_8_1 = ''
        for i in range(2):
            rule1_8_1 += g.readline()

        emb_rule1_8_1 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 1.8.1**",
                                    description = rule1_8_1)

        #1.8.1
        rule1_8_2 = ''
        for i in range(2):
            rule1_8_2 += g.readline()

        emb_rule1_8_2 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 1.8.2**",
                                    description = rule1_8_2)

        #1.9
        rule1_9 = ''
        for i in range(2):
            rule1_9 += g.readline()

        emb_rule1_9 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 1.9**",
                                    description = rule1_9)

        #1.10
        rule1_10 = ''
        for i in range(2):
            rule1_10 += g.readline()

        emb_rule1_10 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 1.10**",
                                    description = rule1_10)

        #1.11
        rule1_11 = ''
        for i in range(1):
            rule1_11 += g.readline()

        emb_rule1_11 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 1.11**",
                                    description = rule1_11)

        #1.11.1
        rule1_11_1 = ''
        for i in range(2):
            rule1_11_1 += g.readline()

        emb_rule1_11_1 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 1.11.1**",
                                    description = rule1_11_1)

        #1.11.2
        rule1_11_2 = ''
        for i in range(3):
            rule1_11_2 += g.readline()

        emb_rule1_11_2 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 1.11.2**",
                                    description = rule1_11_2)

        #1.11.3
        rule1_11_3 = ''
        for i in range(2):
            rule1_11_3 += g.readline()

        emb_rule1_11_3 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 1.11.3**",
                                    description = rule1_11_3)

        #1.12
        rule1_12 = ''
        for i in range(2):
            rule1_12 += g.readline()

        emb_rule1_12 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 1.12**",
                                    description = rule1_12)

        #1.13
        rule1_13 = ''
        for i in range(2):
            rule1_13 += g.readline()

        emb_rule1_13 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 1.13**",
                                    description = rule1_13)

        #1.14
        rule1_14 = ''
        for i in range(2):
            rule1_14 += g.readline()

        emb_rule1_14 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 1.14**",
                                    description = rule1_14)

        #1.15
        rule1_15 = ''
        for i in range(2):
            rule1_15 += g.readline()

        emb_rule1_15 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 1.15**",
                                    description = rule1_15)

        #1.16
        rule1_16 = ''
        for i in range(2):
            rule1_16 += g.readline()

        emb_rule1_16 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 1.16**",
                                    description = rule1_16)

        #1.17
        rule1_17 = ''
        for i in range(9):
            rule1_17 += g.readline()

        emb_rule1_17 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 1.17**",
                                    description = rule1_17)

        #1.18
        rule1_18 = ''
        for i in range(2):
            rule1_18 += g.readline()

        emb_rule1_18 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 1.18**",
                                    description = rule1_18)

        #1.19
        rule1_19 = ''
        for i in range(2):
            rule1_19 += g.readline()

        emb_rule1_19 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 1.19**",
                                    description = rule1_19)

        #2.1
        rule2_1 = ''
        for i in range(2):
            rule2_1 += g.readline()

        emb_rule2_1 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 2.1**",
                                    description = rule2_1)

        #2.2
        rule2_2 = ''
        for i in range(2):
            rule2_2 += g.readline()

        emb_rule2_2 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 2.2**",
                                    description = rule2_2)

        #2.3
        rule2_3 = ''
        for i in range(2):
            rule2_3 += g.readline()

        emb_rule2_3 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 2.3**",
                                    description = rule2_3)

        #2.4
        rule2_4 = ''
        for i in range(3):
            rule2_4 += g.readline()

        emb_rule2_4 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 2.4**",
                                    description = rule2_4)

        #2.5
        rule2_5 = ''
        for i in range(2):
            rule2_5 += g.readline()

        emb_rule2_5 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 2.5**",
                                    description = rule2_5)

        #3.1
        rule3_1 = ''
        for i in range(3):
            rule3_1 += g.readline()

        emb_rule3_1 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 3.1**",
                                    description = rule3_1)

        #3.2
        rule3_2 = ''
        for i in range(2):
            rule3_2 += g.readline()

        emb_rule3_2 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 3.2**",
                                    description = rule3_2)

        #3.3
        rule3_3 = ''
        for i in range(2):
            rule3_3 += g.readline()

        emb_rule3_3 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 3.3**",
                                    description = rule3_3)

        #3.4
        rule3_4 = ''
        for i in range(3):
            rule3_4 += g.readline()

        emb_rule3_4 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 3.4**",
                                    description = rule3_4)

        #3.5
        rule3_5 = ''
        for i in range(2):
            rule3_5 += g.readline()

        emb_rule3_5 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 3.5**",
                                    description = rule3_5)

        #3.6
        rule3_6 = ''
        for i in range(3):
            rule3_6 += g.readline()

        emb_rule3_6 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 3.6**",
                                    description = rule3_6)

        #3.7
        rule3_7 = ''
        for i in range(5):
            rule3_7 += g.readline()

        emb_rule3_7 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 3.7**",
                                    description = rule3_7)

        #3.8
        rule3_8 = ''
        for i in range(1):
            rule3_8 += g.readline()

        emb_rule3_8 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 3.8**",
                                    description = rule3_8)

        #3.9
        rule3_9 = ''
        for i in range(3):
            rule3_9 += g.readline()

        emb_rule3_9 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 3.9**",
                                    description = rule3_9)

        #4
        rule4 = ''
        for i in range(1):
            rule4 += g.readline()

        emb_rule4 = discord.Embed(color = 0xffffff, 
                                    title = "**Правило 4.0**",
                                    description = rule4)

        if number == '1.1':
            await ctx.respond(embed = emb_rule1_1, delete_after = 300)
        if number == '1.2':
            await ctx.respond(embed = emb_rule1_2, delete_after = 300)
        if number == '1.3':
            await ctx.respond(embed = emb_rule1_3, delete_after = 300)
        if number == '1.3.1':
            await ctx.respond(embed = emb_rule1_3_1, delete_after = 300)
        if number == '1.4':
            await ctx.respond(embed = emb_rule1_4, delete_after = 300)
        if number == '1.5':
            await ctx.respond(embed = emb_rule1_5, delete_after = 300)
        if number == '1.5.1':
            await ctx.respond(embed = emb_rule1_5_1, delete_after = 300)
        if number == '1.6.1':
            await ctx.respond(embed = emb_rule1_6_1, delete_after = 300)
        if number == '1.6.2':
            await ctx.respond(embed = emb_rule1_6_2, delete_after = 300)
        if number == '1.6.3':
            await ctx.respond(embed = emb_rule1_6_3, delete_after = 300)
        if number == '1.6.4':
            await ctx.respond(embed = emb_rule1_6_4, delete_after = 300)
        if number == '1.6.5':
            await ctx.respond(embed = emb_rule1_6_5, delete_after = 300)
        if number == '1.6.6':
            await ctx.respond(embed = emb_rule1_6_6, delete_after = 300)
        if number == '1.7':
            await ctx.respond(embed = emb_rule1_7, delete_after = 300)
        if number == '1.8.1':
            await ctx.respond(embed = emb_rule1_8_1, delete_after = 300)
        if number == '1.8.2':
            await ctx.respond(embed = emb_rule1_8_2, delete_after = 300)
        if number == '1.9':
            await ctx.respond(embed = emb_rule1_9, delete_after = 300)
        if number == '1.10':
            await ctx.respond(embed = emb_rule1_10, delete_after = 300)
        if number == '1.11':
            await ctx.respond(embed = emb_rule1_11, delete_after = 300)
        if number == '1.11.1':
            await ctx.respond(embed = emb_rule1_11_1, delete_after = 300)
        if number == '1.11.2':
            await ctx.respond(embed = emb_rule1_11_2, delete_after = 300)
        if number == '1.11.3':
            await ctx.respond(embed = emb_rule1_11_3, delete_after = 300)
        if number == '1.12':
            await ctx.respond(embed = emb_rule1_12, delete_after = 300)
        if number == '1.13':
            await ctx.respond(embed = emb_rule1_13, delete_after = 300)
        if number == '1.14':
            await ctx.respond(embed = emb_rule1_14, delete_after = 300)
        if number == '1.15':
            await ctx.respond(embed = emb_rule1_15, delete_after = 300)
        if number == '1.16':
            await ctx.respond(embed = emb_rule1_16, delete_after = 300)
        if number == '1.17':
            await ctx.respond(embed = emb_rule1_17, delete_after = 300)
        if number == '1.18':
            await ctx.respond(embed = emb_rule1_18, delete_after = 300)
        if number == '1.19':
            await ctx.respond(embed = emb_rule1_19, delete_after = 300)
        if number == '2.1':
            await ctx.respond(embed = emb_rule2_1, delete_after = 300)
        if number == '2.2':
            await ctx.respond(embed = emb_rule2_2, delete_after = 300)
        if number == '2.3':
            await ctx.respond(embed = emb_rule2_3, delete_after = 300)
        if number == '2.4':
            await ctx.respond(embed = emb_rule2_4, delete_after = 300)
        if number == '2.5':
            await ctx.respond(embed = emb_rule2_5, delete_after = 300)
        if number == '3.1':
            await ctx.respond(embed = emb_rule3_1, delete_after = 300)
        if number == '3.2':
            await ctx.respond(embed = emb_rule3_2, delete_after = 300)
        if number == '3.3':
            await ctx.respond(embed = emb_rule3_3, delete_after = 300)
        if number == '3.4':
            await ctx.respond(embed = emb_rule3_4, delete_after = 300)
        if number == '3.5':
            await ctx.respond(embed = emb_rule3_5, delete_after = 300)
        if number == '3.6':
            await ctx.respond(embed = emb_rule3_6, delete_after = 300)
        if number == '3.7':
            await ctx.respond(embed = emb_rule3_7, delete_after = 300)
        if number == '3.8':
            await ctx.respond(embed = emb_rule3_8, delete_after = 300)
        if number == '3.9':
            await ctx.respond(embed = emb_rule3_9, delete_after = 300)
        if number == '4.0':
            await ctx.respond(embed = emb_rule4, delete_after = 300)

def setup(bot):
    bot.add_cog(Rules(bot))