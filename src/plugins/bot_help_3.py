# -*- coding: utf-8 -*-

from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event



this_command = "help apex"
bot_help = on_command(this_command, priority=5)

async def create_help():
    return_list = [
        '玩家 [玩家名称]	  根据玩家名称查询信息 (暂仅支持查询 PC 平台玩家信息)',
        'UID [玩家UID]	 根据玩家 UID 查询信息 (暂仅支持查询 PC 平台玩家信息)',
        '自查	根据玩家已绑定的 UID 自动查询玩家信息',
        '地图	查询地图轮换',
        '猎杀	查询各平台顶尖猎杀者信息',
        '制造	查询复制器轮换',
        '服务	查询服务器状态',
        '订阅地图	每整点查询地图轮换',
        '取消订阅地图	取消每整点查询地图轮换',
        '订阅制造	每日 2 时查询复制器轮换',
        '取消订阅制造	取消每日 2 时查询复制器轮换',
        '绑定 [玩家 UID]	将 UID 与 QQ 账号绑定 (群聊 与 频道 信息不互通)',
        '解绑	将 UID 与 QQ 账号解除绑定 (群聊 与 频道 信息不互通)',
        '.pd/.猎杀 查询全平台大逃杀、竞技场猎杀最低分和大师段位以上的人数。',
        '.crafting/.复制器 查询当前复制器轮换物品。',
        '.stat/.查询 origin_id (平台) 根据origin_id查询玩家信息,可查询多平台(PC、PS4、X1),不添加默认PC',
        '.map/.地图 查看当前大逃杀、竞技场模式轮换地图，以及地图剩余时间。'

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
