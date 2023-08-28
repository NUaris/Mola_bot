#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nonebot
from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11Adapter
#from nonebot.adapters.kaiheila import Adapter as KaiheilaAdapter
nonebot.load_plugins("src/plugins/nonebot_plugin_xiuxian_2")
nonebot.init()

# Custom your logger
# 
# from nonebot.log import logger, default_format
# logger.add("error.log",
#            rotation="00:00",
#            diagnose=False,
#            level="ERROR",
#            format=default_format)

# You can pass some keyword args config to init function
nonebot.init(_env_file=".env.dev")
app = nonebot.get_asgi()


#TAROT_PATH="/home/nuaris/MoLa_MoMoLa/data/Taro/"
#CHAIN_REPLY = True
#APEX_API_KEY="b0e848706cf35472be4aa8eaebee5efb"
#apex_api_token="b0e848706cf35472be4aa8eaebee5efb"
driver = nonebot.get_driver()
driver.register_adapter(ONEBOT_V11Adapter)
#driver.register_adapter(KaiheilaAdapter)
#兩個#的是可以正確加載的
##nonebot.load_builtin_plugins("echo")
##nonebot.load_builtin_plugins("single_session")
##nonebot.load_plugin('nonebot_plugin_dialectlist')
##nonebot.load_plugin('nonebot_plugin_songpicker2')
##nonebot.load_plugin('nonebot_plugin_lolmatch')
#nonebot.load_plugin('nonebot_plugin_autohelp')
##nonebot.load_plugin('nonebot_plugin_shindan')
#nonebot.load_plugin('nonebot_plugin_repeater')
##nonebot.load_plugin('nonebot_plugin_picsearcher')
##nonebot.load_plugin('nonebot_plugin_word_bank2')
##nonebot.load_plugin('nonebot_plugin_dailysign')
##nonebot.load_plugin('nonebot_plugin_random_stereotypes')
##nonebot.load_plugin('nonebot_plugin_cartoon')
##nonebot.load_plugin('nonebot_plugin_AutoRepeater')
##nonebot.load_plugin("youth-version-of-setu4")
##nonebot.load_plugin('nonebot_plugin_what2eat')
##nonebot.load_plugin('nonebot_plugin_blacklist')
##nonebot.load_plugin('nonebot_plugin_ygo')
##nonebot.load_plugin('nonebot_plugin_impact')
##nonebot.load_plugin('nonebot_plugin_groupmate_waifu')
##nonebot.load_plugin('nonebot_plugin_learning_chat')
#nonebot.load_plugin('nonebot-plugin-picstatus')
#nonebot.load_plugin('nonebot_plugin_drawer')
#nonebot.load_plugin('nonebot-plugin-reboot')
##nonebot.load_plugin('nonebot_plugin_status')
#nonebot.load_plugin('nonebot_plugin_autohelp')

# Please DO NOT modify this file unless you know what you are doing!
# As an alternative, you should use command `nb` or modify `pyproject.toml` to load plugins

#nonebot.load_from_toml("pyproject.toml")

# Modify some config / config depends on loaded configs
# 
# config = driver.config
# do something...
if __name__ == "__mp_main__": # 仅在子进程运行的代码
    # Please DO NOT modify this file unless you know what you are doing!
    # As an alternative, you should use command `nb` or modify `pyproject.toml` to load plugins
    # 加载插件
    nonebot.load_from_toml("pyproject.toml")
    nonebot.load_builtin_plugins("echo")
    nonebot.load_builtin_plugins("single_session")
    nonebot.load_plugin('nonebot_plugin_dialectlist')
    #nonebot.load_plugin('nonebot_plugin_songpicker2')
    nonebot.load_plugin('nonebot_plugin_lolmatch')
    #nonebot.load_plugin('nonebot_plugin_autohelp')
    nonebot.load_plugin('nonebot_plugin_shindan')
    #nonebot.load_plugin('nonebot_plugin_repeater')
    #nonebot.load_plugin('nonebot_plugin_picsearcher')
    #nonebot.load_plugin('nonebot_plugin_word_bank2')
    #nonebot.load_plugin('nonebot_plugin_dailysign')
    nonebot.load_plugin('nonebot_plugin_cloudsignx')
    nonebot.load_plugin('nonebot_plugin_random_stereotypes')
    nonebot.load_plugin('nonebot_plugin_cartoon')
    nonebot.load_plugin('nonebot_plugin_AutoRepeater')
    nonebot.load_plugin("youth-version-of-setu4")
    #nonebot.load_plugin('nonebot_plugin_what2eat')
    nonebot.load_plugin('nonebot_plugin_blacklist')
    nonebot.load_plugin('nonebot_plugin_ygo')
    nonebot.load_plugin('nonebot_plugin_impact')
    nonebot.load_plugin('nonebot_plugin_groupmate_waifu')
    nonebot.load_plugin('nonebot_plugin_learning_chat')
    nonebot.load_plugin('nonebot_plugin_simplemusic')
    #nonebot.load_plugin('nonebot-plugin-picstatus')
    #nonebot.load_plugin('nonebot_plugin_drawer')
    #nonebot.load_plugin('nonebot-plugin-reboot')
    #nonebot.load_plugin('nonebot_plugin_status')
    #nonebot.load_plugin('nonebot_plugin_autohelp')
    #nonebot.load_plugin('nonebot_plugin_bilibilibot')
    nonebot.load_plugin('nonebot_plugin_animeres')
    nonebot.load_plugin('nonebot_plugin_jrrp2')
    #nonebot.load_plugin('xingzuo_luck')
    nonebot.load_plugin('nonebot_plugin_CyberSensoji')
    #nonebot.load_plugin('nonebot_plugin_send')
    nonebot.load_plugin('nonebot_plugin_answersbook')
    nonebot.load_plugin('nonebot_plugin_whateat_pic') #今天吃什么图文版
    nonebot.load_plugin('nonebot_plugin_majsoul') #雀魂
    nonebot.load_plugin('nonebot_plugin_reborn')
    #nonebot.load_plugin('nonebot_plugin_wolf_kill')
    #nonebot.load_plugin('nonebot_plugin_horserace')
    #nonebot.load_plugin('nonebot_plugin_fortune')#缺资源包
    nonebot.load_plugin('nonebot_plugin_r6s')
    nonebot.load_plugin('nonebot_plugin_dog')
    nonebot.load_plugin('nonebot_plugin_tarot')
    #nonebot.load_plugin('nonebot_plugin_crazy_thursday')
    nonebot.load_plugin('nonebot_plugin_apexranklookup')
    nonebot.load_plugin('nonebot_plugin_bfinfo')
    nonebot.load_plugin('nonebot_plugin_apex_api_query')
    #nonebot.load_plugin('nonebot_plugin_chatgpt_turbo')
    #nonebot.load_plugin('nonebot_plugin_bfchat')
    nonebot.load_plugin('nonebot_plugin_setu_collection')
    nonebot.load_plugin('nonebot_plugin_send')
    nonebot.load_plugin('nonebot_plugin_anime_trace')
    nonebot.load_plugin('nonebot_plugin_megumin')
    nonebot.load_plugin('nonebot_plugin_error_alert')
    nonebot.load_plugin('nonebot_plugin_miao')
    #nonebot.load_plugin('nonebot_plugin_xiuxian_2')
    nonebot.load_plugin('nonebot_plugin_HttpCat')
    nonebot.load_plugin('nonebot_plugin_picmcstat')
    nonebot.load_plugin('nonebot_plugin_searchBiliInfo')
    nonebot.load_plugin('nonebot_plugin_russian_ban')
    nonebot.load_plugin('nonebot_plugin_bottle')
    nonebot.load_plugin('nonebot_plugin_picstatus')
    #nonebot.load_plugin('nonebot_plugin_Imagelabels')
    nonebot.load_plugins("src/plugins/nonebot-plugin-bfchat-master")
    #nonebot.load_plugins("src/plugins_function/PicMenu")

if __name__ == "__main__": # 仅在主进程运行的代码
    # nonebot.logger.warning("Always use `nb run` to start the bot instead of manually running!")
    # 运行 nonebot
    nonebot.load_plugin("nonebot_plugin_reboot") # 加载重启插件
    nonebot.run(app="__mp_main__:app")
#    nonebot.run()

#if __name__ == "__main__":
#    nonebot.logger.warning("Always use `nb run` to start the bot instead of manually running!")
#    nonebot.run(app="__mp_main__:app")
