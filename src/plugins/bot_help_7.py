# -*- coding: utf-8 -*-

from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event



this_command = "help 娱乐"
bot_help = on_command(this_command, priority=5)

async def create_help():
    return_list = [
        '发病 [发病对象] 向某人发病哈哈哈哈哈哈哈哈哈',
        '舔狗日记 ',
        '投胎',
        '问题 + 翻看答案 很呆慎用',
        '今日人品 获取你的今日人品',
        '本周人品 获取你的本周平均人品',
        '本月人品 获取你的本月平均人品',
        '平均人品 获取你的历史平均人品',
        '二次元化or动漫化or卡通化 + 图片',
        'qq点歌/网易云点歌/酷狗点歌/b站点歌+歌曲名',
        '来点色图 （张数） (r18)括号里的可不填写',
        '群话痨排行榜 看看有史以来（机器人存在以来）群友们发了多少消息！\n回复 help 话痨 查看详细', #8
        '占卜列表 可以查看占卜列表,回复相应功能指令即可使用',
        '/抽签 可以抽签',
        '占卜 启用牌阵进行占卜',
        '塔罗牌 得到单张塔罗牌',
        '签到 回复功能可查看具体功能',
        '娶群友 娶群友做老婆,回复help cp 查看具体功能',#9
        'impact 回复 help imapct 可查看具体功能',#10
        '今天早上吃什么	随机发送食物',	
        '今天早上喝什么	随机发送饮品',	
        '查看全部菜单	查看全部菜单',	
        '查看菜单	   查看指定菜单',
        '资源+动漫名称',


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
