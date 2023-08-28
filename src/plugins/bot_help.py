# -*- coding: utf-8 -*-

from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

#游戏王 LOL apex bf1&bf5 r6s 雀魂 
#1 2 3 4 5 6 7 8 9

this_command = "help other"
bot_help = on_command(this_command,priority=5)

async def create_help():
    return_list = [
        'help ygo  获取游戏王详细帮助', #1
        'help lol  获取LOL详细帮助',   #2
        'help apex  获取apex详细帮助',  #3
        'help bf  获取战地1和战地5详细帮助',    #4
        'help r6s  获取彩虹六号详细帮助',   #5
        'help 雀魂  获取雀魂详细帮助', # 6
     #   '帮助游戏王  获取详细帮助', #
     #   '帮助游戏王  获取详细帮助', #
     #   '帮助游戏王  获取详细帮助', #
        'help 娱乐 获取娱乐相关帮助', #

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
