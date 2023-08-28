# -*- coding: utf-8 -*-

from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

from src.plugins.item import item_help
from src.plugins.lottery import lottery_help
from src.plugins.market import market_help
from src.plugins.nuannuan import nuannuan_help
from src.plugins.precious import precious_help
from src.plugins.ff_weibo import ff_weibo_help
from src.plugins.item_new import item_new_help
from src.plugins.market_new import market_new_help
from src.plugins.house import house_help
from src.plugins.logs_dps import logs_dps_help


this_command = "help"
bot_help = on_command(this_command, priority=5)

async def create_help():
    return_list = [
        '机器人Ver 2.0',
        '已支持游戏 FF14 游戏王 LOL apex bf1 bf5 r6s 雀魂',
        '辱骂机器人的会被拉入黑名单',
        'help 回复现有功能',
        'help other 回复其它功能',#回复其它功能
        '.send+内容 可以反馈建议和bug'

    ]
    help_list=['出现问题请联系机器人的妈咪']
    creator_list=['by Nuaris[1830873642]']

    return_list.append(await nuannuan_help())
    return_list.append(await precious_help())
    return_list.append(await lottery_help())
    return_list.append(await ff_weibo_help())
    return_list.append(await item_help())
    return_list.append(await item_new_help())
    return_list.append(await market_help())
    return_list.append(await market_new_help())
    return_list.append(await house_help())
    return_list.append(await logs_dps_help())
    return_list.append('出现问题请联系机器人的妈咪')
    return_list.append('by Nuaris[1830873642]')
    return "【莫拉莫莫拉现有的功能】\n" + "\n\n".join(return_list)


@bot_help.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    if args == this_command:
        return_str = await create_help()
        await bot_help.finish(return_str)
    else:
        return
