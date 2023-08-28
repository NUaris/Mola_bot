# -*- coding: utf-8 -*-

from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event



this_command = "help impact"
bot_help = on_command(this_command, priority=5)

async def create_help():
    return_list = [
    '嗦牛子 (给目标牛牛增加长度, 自己或者他人, 通过艾特选择对象, 没有at时目标是自己)',
    '打胶 | 开导 (给自己牛牛增加长度)',
    'pk | 对决 (普通的pk,单纯的random实现输赢, 胜利方获取败方随机数/2的牛牛长度)',
    '查询 (目标牛牛长度, 自己或者他人, 通过艾特选择对象, 没有at时目标是自己)',
    'jj排行榜 | jj排名 | jj榜单 | jjrank (字面意思, 输出倒数五位和前五位, 以及自己的排名)',
    '开启淫趴|禁止淫趴 (由管理员 | 群主 | SUPERUSERS开启或者关闭淫趴)',
    '日群友|透群友|日群主|透群主|日管理|透管理 (字面意思, 当使用透群友的时候如果at了人那么直接指定)',
    '注入查询 | 摄入查询 (查询目标被透注入的量，后接(历史|全部), 可查看总被摄入的量, 无艾特的时候是自己, 有at的时候是目标)',
    '淫趴介绍 | 淫趴说明| 淫趴帮助 (输出淫趴插件的命令列表)'
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
