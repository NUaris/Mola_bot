# -*- coding: utf-8 -*-

from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event



this_command = "help 话痨"
bot_help = on_command(this_command, priority=5)

async def create_help():
    return_list = [
        '/群话痨排行榜 ————看看有史以来（机器人存在以来）群友们发了多少消息！',

        '/今日群话痨排行榜 ————看看今天的群友发了多少消息！',

        '/昨日群话痨排行榜 ————看看昨天的群友发了多少消息！',

        '/本周群话痨排行榜 ————看看本周的群友发了多少消息！',

        '/上周群话痨排行榜 ————看看上周的群友发了多少消息！',

        '/本月群话痨排行榜 ————看看这个月的群友发了多少消息！',

        '/年度群话痨排行榜 ————看看今年的群友发了多少消息！',

        '/历史群话痨排行榜 ————看看历史上（机器人存在以来）的群友发了多少消息！'

    ]
    help_list=['出现问题请联系机器人的妈咪']
    creator_list=['by Nuaris[1830873642]']

    return_list.append('出现问题请联系机器人的妈咪')
    return_list.append('by Nuaris[1830873642]')
    return "\n\n".join(return_list)


@bot_help.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    if args == this_command:
        return_str = await create_help()
        await bot_help.finish(return_str)
    else:
        return
