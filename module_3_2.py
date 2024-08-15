
def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if (('@' in recipient and '@' in sender)
            and ('com' in recipient or 'ru' in recipient or 'net' in recipient)
            and ('com' in sender or 'ru' in sender or 'net' in sender)):
        if recipient == sender:
            print('Нельзя отправить письмо самому себе!')
        elif sender == 'university.help@gmail.com':
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
        else:
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'Невозможно отправить пиьсмо с адреса {sender} на адрес {recipient}')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.ru')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

