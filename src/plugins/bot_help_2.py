# -*- coding: utf-8 -*-

from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event



this_command = "help lol"
bot_help = on_command(this_command, priority=5)

async def create_help():
    return_list = [
        'lol 查看今日比赛信息',
        'lol 本周 查看本周比赛信息'
        'lol 本周 查看本周比赛信息',
        'lol 详情 [matchID] 查询指定比赛详细信息',
        'lol 订阅 [tournamentID] 订阅联赛 每晚检查当日结果和第二天赛程',
        'lol 查看订阅 查看已订阅的所有联赛',
        'lol 联赛 查看所有即将进行或正在进行的联赛和tournamentID',
        'lol 联赛详情 [tournamentID] 查看所选联赛近期已完成的赛事获取 [matchID]'
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
