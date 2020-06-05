from .command_requests import api_get_request, api_delete_request


def start(update, context):
    """function to deal with 'start' command"""

    if context.args:  # checking for referral code parameter
        referral_id = context.args[0]
        refferal_data = api_get_request(referral_id)  # making GET request to our Django REST API
        if refferal_data:
            if api_delete_request(referral_id):  # providing instance deletion
                update.message.reply_text(f'Приветствую {refferal_data["user_name"]}! '
                                          f'Твой уникальный код - {refferal_data["user_id"]}')
        else:
            update.message.reply_text('Случилась ошибка. Попробуйте перейти '
                                      'по пригласительной ссылке позже.')
    else:
        update.message.reply_text('Вы не можете начать использовать бот '
                                  'без реферальной ссылки. Перейдите в бот '
                                  'с помощью реферальной ссылки')
