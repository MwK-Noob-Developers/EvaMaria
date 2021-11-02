class script(object):
    START_TXT = """𝙷𝙴𝙻𝙾 {},
𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href=https://t.me/{}>{}</a>, 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈 😍"""

    HELP_TXT = """<b>Here is the Usual commands:</b>
/start - check whether im online
/help - get this help message
/about - about me"""

    ABOUT_TXT = """<b>Hello 🙌</b>
<b>○ My Name :</b> <code>Autofilter v1</code>
<b>○ Creator :</b> <a href='t.me/shamilnelli'>𝕊𝕞𝕃</a>
<b>○ Credits :</b> <a href='https://t.me/shamilnelli/78'>Everyone in this journey</a>
<b>○ Language :</b> <a href='t.me/python'>Python3</a>
<b>○ Library :</b> <a href='https://docs.pyrogram.org'>Pyrogram asyncio 0.17.1</a>
<b>○ Source Code :</b> 👉 <a href='http://github.com/shamilhabeebnelli/source-code'>Click Here</a>
<b>○ Server :</b> <a href='contabo.com'>Contabo</a>
<b>○ Database :</b> <code>MongoDB Free Tier</code>
<b>○ Build Status :</b> <code>V9.7 [ALPHA]</code>"""

    SOURCE_TXT = """<b>NOTE:</b>
- Eva Maria is a open source project. 
- Source - https://github.com/EvamariaTG/EvaMaria  

<b>DEVS:</b>
- <a href=https://t.me/TeamEvamaria>Team Eva Maria</a>"""
    MANUELFILTER_TXT = """<b>Filters:</b>
Filter is the feature were users can set automated replies for a particular keyword and the bot will respond whenever a keyword is found the message
<b>NOTE:</b>
1. bot should have admin privillage in order to reply filters in a chat.
2. only admins can add filters in a chat.
3. filters does support all the telegram markdowns, medias and buttons.
4. alert buttons are also supported with a limit of 64 characters.
5. there are some easter eggs, try to find it out.
<b>Commands and Usage:</b>
/filter  or /add - add a filter
/filters or /viewfilters - list all the filters of a chat
/stop or /del - delete a specific filter (separate keywords with spaces for deleting multiple filters at a time)
/stopall or /delall - delete the whole filters in a chat (chat owner only)"""
    BUTTON_TXT = """<b>Buttons:</b>
<i>@mwk_autofilterbot supports both url and alert inline buttons, now lets see how to implement it.</i>
<b>NB:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. This bot supports buttons with any telegram media type.
3. Buttons should be properly formatted as below or else result will be malformed.
<b>URL buttons:</b>
- single button
<code>[Button](buttonurl://t.me/redbullFED)</code>
- Double button
<code>[Button1](buttonurl://t.me/redbullfed)
[Button2](buttonurl://t.me/shamilhabeeb)</code>
- Double buttons in Same Raw
<code>[Button1](buttonurl://t.me/redbullfed)
[Button2](buttonurl://t.me/shamilnelli:same)</code>
<b>Alert buttons:</b>
<code>[Button](buttonalert:Ahoy, this is an alert!)</code>"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>
<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains cam rip, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""

    CONNECTION_TXT = """<b>Connections:</b>
Used to connect bot to PM which let will you to execute both normal filter related commands and some other sensitive commands right from the PM that will
reflect in the group which helps you to keep the filter additions and other stuffs private and helps to prevent flooding.
<b>NOTE:</b>
1. Only admins can add a connection.
2. In a chat you can simply use the /connect for starting a connection 
3. In PM you must specify chat id right after the command.
<b>Commands and Usage:</b>
/connect  - connect a particular chat to your PM
/disconnect  - disconnect from a chat
/connections - list all your connections"""

    EXTRAMOD_TXT = """Help: <b>🐶 Show Commands</b>
<b>NOTE:</b>
these are the extra features of tessa
<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>
<b>NOTE:</b>
This module only works for my admins
<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /index  - <code>to add files from a channel</code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all tssa users</code>"""

    STATUS_TXT = """• Saved Files: <code>{}</code>
• Users : <code>{}</code>
• Groups : <code>{}</code>
• DB Usage: <code>{}</code>"""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - <code>{}</code>
"""
