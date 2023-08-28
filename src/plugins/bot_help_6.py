# -*- coding: utf-8 -*-

from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event



this_command = "help 雀魂"
bot_help = on_command(this_command, priority=5)

async def create_help():
    return_list = [
        '/雀魂(三麻)信息\t <雀魂账号>\t [<房间类型>]\t [最近<数量>场]\t [最近<数量>{天|周|个月|年}]\t 查询个人数据（可按照时间、按照场数、按照房间类型查询）',

        '/雀魂(三麻)对局\t <雀魂账号>\t [<房间类型>]\t 查询个人最近对局（可按照房间类型查询）',

        '/雀魂(三麻)PT图\t <雀魂账号>\t [最近<数量>场]\t [最近<数量>{天|周|个月|年}] 绘制个人PT推移图'

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
