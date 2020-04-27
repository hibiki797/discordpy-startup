# インストールした discord.py を読み込む
import discord
from googletrans import Translator

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NzAzOTgyNDQ2NzE4NDg0NTYw.XqWnvQ.HjoHlresLWBLU17T253pecyKh1o'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

@client.event
async def on_reaction_add(reaction, user):
    print("emoji-id")
    print(reaction.emoji.id)
    if reaction.count == 1:
        # 日本語訳
        if reaction.emoji.id == 704020784724836432:
            translator = Translator()
            trans_en = translator.translate(reaction.message.content, dest='ja')
            await reaction.message.channel.send(trans_en.text)
            
        
        
        # 英語訳
        if reaction.emoji.id == 704020826634321991:
            translator = Translator()
            trans_en = translator.translate(reaction.message.content, dest='en')
            await reaction.message.channel.send(trans_en.text)

        # 英語訳
        if reaction.emoji.id == 704358392130568222:
            translator = Translator()
            trans_en = translator.translate(reaction.message.content, dest='es')
            await reaction.message.channel.send(trans_en.text)

        # 英語訳
        if reaction.emoji.id == 704358570904518686:
            translator = Translator()
            trans_en = translator.translate(reaction.message.content, dest='ko')
            await reaction.message.channel.send(trans_en.text)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)