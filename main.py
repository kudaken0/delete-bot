import discord
from discord import app_commands

TOKEN = 'My token'

# 接続に必要なオブジェクトを生成
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="起動中"))  # ステータスメッセージを設定
    print("起動完了")
    await tree.sync()#スラッシュコマンドを同期
    await client.change_presence(activity = discord.Activity(name="/help", type=discord.ActivityType.competing))


@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    

@tree.command(name="delete", description="メッセージを一括削除します")
@app_commands.describe(number="数字を入力(例: 10)")
async def purge(interaction: discord.integrations, number: int):
    channel = interaction.channel
    if channel:
        progress_message = await interaction.response.send_message("メッセージを削除中...")

        # Botが削除する対象のメッセージを取得
        deleted = []
        async for message in channel.history(limit=number + 1):
            deleted.append(message)

        bot = interaction.client  # Botを取得する
        bot_user = await bot.fetch_user(bot.user.id)

        bot_messages = [progress_message]  # 進行状況を示すメッセージを保持

        # 最初のメッセージは無視して、それ以降のメッセージを削除
        ignore_first = True
        for msg in deleted:
            if ignore_first:
                ignore_first = False
                continue

            if msg.author != bot_user:  # Bot自身のメッセージでない場合のみ削除
                await msg.delete()

        # edit_original_responseを使ってオリジナルのレスポンスを編集する
        await interaction.edit_original_response(content=f"{len(deleted) - 1}メッセージを削除しました")
    else:
        await interaction.response.send_message("チャンネルを取得できませんでした")


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)