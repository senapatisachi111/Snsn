class script(object):
    START_TXT = """đˇđ´đťo {},
đ˝đ°đźđ´ is <a href=https://t.me/{}>{}</a> Iam A Simple Auto Filter ++ Manual Filter + Extra Features Bot. I Can Provide Movies In Telegram Groups.I Can Also Add Filters In Telegram Groups.  Just Add Me To Your Group And Enjoy"""
    HELP_TXT = """đˇđ´đ {}
đˇđ´đđ´ đ¸đ đđˇđ´ đˇđ´đťđż đľđžđ đźđ đ˛đžđźđźđ°đ˝đłđ."""
    ABOUT_TXT = """âŽ đźđ đ˝đ°đźđ´: {}
âŽ đ˛đđ´đ°đđžđ: <a href=https://t.me/SNSNS01>Đ˝ÎąŃĐźÎąĐ¸</a>
âŽ đťđ¸đąđđ°đđ: đżđđđžđśđđ°đź
âŽ đťđ°đ˝đśđđ°đśđ´: đżđđđˇđžđ˝ đš
âŽ đłđ°đđ° đąđ°đđ´: đźđžđ˝đśđž đłđą
âŽ đąđžđ đđ´đđđ´đ: đˇđ´đđžđşđ
âŽ đąđđ¸đťđł đđđ°đđđ: v1.0.2 [ đąđ´đđ° ]"""

    PRIVATEBOT_TXT = """<b>đżđđ¸đđ°đđ´ đąđžđ đľđžđ đđžđ</b>
<b>âşâş đłđž đđžđ đđ°đ˝đ đ° đąđžđ đđ°đźđ´ đťđ¸đşđ´ đđˇđ¸đ</b>
<b>âşâş đđ¸đđˇ đ°đťđť đđžđđ đ˛đđ´đłđ¸đđ</b>
<b>âşâş đđ¸đđˇ đđžđđ đžđđ˝đ´đđđˇđ¸đż</b>
<b>âşâş đ˛đžđ˝đđ°đ˛đ đźđ´ <a href=https://t.me/SNSNS01>Đ˝ÎąŃĐźÎąĐ¸</a></b>"""

    SOURCE_TXT = """<b>Donation</b>

âŞź <b>đđ¨đŽ đđđ§ đđ¨đ§đđ­đ đđ§đ˛ đđŚđ¨đŽđ§đ­ đđ¨đŽ đđđŻđ đł. 

<b>âââââââââá Payment Methods áâââââââââ

âŽ đđźđźđ´đšđ˛đŁđŽđ
âŽ đŁđŽđđđş
âŽ đŁđľđźđťđ˛đŁđ˛
âŽ đŁđŽđđŁđŽđš

_đđ¨đ§đ­đđđ­ đđ đđ¨đŤ đđ§đ¨đ° đđđ¨đŽđ­ đđĄđ đđđ˛đŚđđ§đ­ đđ§đđ¨_
ââââââââââââá <a href=https://t.me/SNSNS01><b>Đ˝ÎąŃĐźÎąĐ¸</b></a> áââââââââââââ"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>  

- Filter is the feature were users can set automated replies for a particular keyword and Zsearcher will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Zsá´á´Ęá´Ęá´Ę should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
âž /filter - <code>add a filter in chat</code>
âž /filters - <code>list all the filters of a chat</code>
âž /del - <code>delete a specific filter in chat</code>
âž /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Zsearcher Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Zsá´á´Ęá´Ęá´Ę supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Cynitebots)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
âž /connect  - <code>connect a particular chat to your PM</code>
âž /disconnect  - <code>disconnect from a chat</code>
âž /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
These are the extra features of Zsá´á´Ęá´Ęá´Ę

<b>Commands and Usage:</b>
âž /id - <code>get id of a specifed user.</code>
âž /info  - <code>get information about a user.</code>
âž /imdb  - <code>get the film information from IMDb source.</code>
âž /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my OáŻáEáâĄ

<b>Commands and Usage:</b>
âž /logs - <code>to get the rescent errors</code>
âž /stats - <code>to get status of files in db.</code>
âž /delete - <code>to delete a specific file from db.</code>
âž /users - <code>to get list of my users and ids.</code>
âž /chats - <code>to get list of the my chats and ids </code>
âž /leave  - <code>to leave from a chat.</code>
âž /disable  -  <code>do disable a chat.</code>
âž /ban  - <code>to ban a user.</code>
âž /unban  - <code>to unban a user.</code>
âž /channel - <code>to get list of total connected channels</code>
âž /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """âŽ đđžđđ°đť đľđ¸đťđ´đ: <code>{}</code>
âŽ đđžđđ°đť đđđ´đđ: <code>{}</code>
âŽ đđžđđ°đť đ˛đˇđ°đđ: <code>{}</code>
âŽ đđđ´đł đđđžđđ°đśđ´: <code>{}</code> đźđđą
âŽ đľđđ´đ´ đđđžđđ°đśđ´: <code>{}</code> đźđđą"""
    LOG_TEXT_G = """#đđđ°đđŤđ¨đŽđŠ
âŽ đđŤđ¨đŽđŠ âşâş {}(<code>{}</code>)
âŽ đđ¨đ­đđĽ đđđŚđđđŤđŹ âşâş <code>{}</code>
âŽ đđđđđ đđ˛ âşâş {}
"""
    LOG_TEXT_P = """#đđđ°đđŹđđŤ
âŽ đđ âşâş <code>{}</code>
âŽ đđđŚđ âşâş {}
"""
    CARBON_TXT = """ <b>đ˛đ°đđąđžđ˝ đźđžđłđđťđ´</b>

<b>đđžđ đ˛đ°đ˝ đąđ´đ°đđđ¸đľđ đđžđđ đ˛đžđłđ´đ đąđ đđđ¸đ˝đś đđˇđ đľđ´đ°đđđđ´...</b>

<b>đ˛đžđźđźđ°đ˝đł.!</b>
<b>/carbon âşâş đđ´đżđťđ đđž đ°đ˝đ đđ´đđ đźđ´đđđ°đśđ´</b>

<b>đđžđđşđ đžđ˝ đąđžđđˇ đśđđžđđż đ°đ˝đł đżđź</b>
<b>đ˛đđ´đłđ¸đđ âşâş</b> <a href=https://youtube.com/channel/UCiaz-J50QhtJ73XEEjP_aLQ>á´á´á´ĘÉ´ÉŞá´á´Ę-á´ĘÉ´ÉŞá´á´</a></b>"""
