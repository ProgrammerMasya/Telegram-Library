from BotHandler.BotHandler import Handler
from Config.config import token

bot = Handler(token)
hello = ('привет')
nastya = ('настя шлюха')
yulia = ('как ты относишься к недашковской?')
kolja = ('ты знаешь пташица?')

def main():

    new_offset = None
    while True:
        bot.get_updates(new_offset)
        last_update = bot.get_last_update()
        if last_update != None:
            last_update_id = last_update['update_id']
            last_chat_text = last_update['message']['text']
            last_chat_id = last_update['message']['chat']['id']
            last_chat_name = last_update['message']['chat']['first_name']

            if last_chat_text.lower() in hello:
                bot.send_message(last_chat_id, 'Здравствуйте, {}'.format(last_chat_name))

            elif last_chat_text.lower() in nastya:
                bot.send_message(last_chat_id, 'Полность с вами согласен! Даже я ее ебал')

            elif last_chat_text.lower() in yulia:
                bot.send_message(last_chat_id, 'Я хочу ее отпиздить!!!')
                
            elif last_chat_text.lower() in kolja:
                bot.send_message(last_chat_id, 'Да, он ахуенный!!!')

            else:
                bot.send_message(last_chat_id, 'Вы далбаеб? Я вас не понимаю')

            new_offset =last_update_id + 1

if __name__ == '__main__':
    main()
