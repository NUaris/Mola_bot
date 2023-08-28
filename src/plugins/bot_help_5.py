# -*- coding: utf-8 -*-

from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event



this_command = "help r6s"
bot_help = on_command(this_command, priority=5)

async def create_help():
    return_list = [
        'r6s 昵称	查询玩家基本信息',
        'r6spro	昵称	查询玩家进阶信息',
        'r6sops	昵称	查询玩家干员信息',
        'r6sp 昵称	查询玩家 近期对战 历史段位信息',
        'r6sset	昵称	设置玩家昵称，设置后其余指令可以不带昵称即查询已设置昵称信息',
        '群聊查询不好使的话可以私聊查询'

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
