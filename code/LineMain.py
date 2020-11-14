import configparser
from posix import SCHED_RESET_ON_FORK
from line_notiry_bot import LINENotiryBot
import Oura_get
import Message_create

def main():
    config_ini = configparser.ConfigParser()
    config_ini.read('config.ini', encoding='utf-8')

    today_score,week_score = Oura_get.get_oura_data()
    bot = LINENotiryBot(access_token=config_ini['LINE']['Token'])
    message = Message_create.score_create(today_score,week_score)
    message += Message_create.blurred_create(today_score)

    bot.send(
        message= message,
    #     #image='test.jpeg,
    #     #sticker_package_id=1,
    #     #sticker_id=13
    )


if __name__=='__main__':
    main()