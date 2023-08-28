# -*- coding: utf-8 -*-

from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event



this_command = "help cp"
bot_help = on_command(this_command, priority=5)

async def create_help():
    return_list = [
        '娶群友 纯爱 双向奔赴版，每天刷新一次，两个人会互相抽到对方。',
        '娶群友@name 有机会娶到at的人。。。',
        '分手 雪花飘飘北风萧萧，天地一片苍茫~',
        '本群cp 查看当前群内的cp',
        '群友卡池 查看当前群可以娶到的群友列表',
        '透群友 ntr 宫吧老哥狂喜版，每次抽到的结果都不一样。',
        '涩涩记录 查看当前群的群友今日透群友次数和被透的次数，记录是跨群的。也就是说群友在别的群挨透也会在记录里显示出来'


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
