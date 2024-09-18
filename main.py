import smtplib
import os
from dotenv import load_dotenv
load_dotenv()


from_mail = "devmanorg@yandex.ru"
to_mail = "yusupov0904@yandex.ru"
subject = "Приглашение"
letter = """From: {0}
To: {1}
Subject: {2}
Content-Type: text/plain; charset="UTF-8";""".format(from_mail, to_mail, subject)



shablon = """
Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""

shablon = shablon.replace("%website%!", "https://dvmn.org/referrals/6EbJp301UMi0cMD8dF8aVgBhgtJxDvgGL10WenCS/")
shablon = shablon.replace("%website%","dvmn.org")
shablon = shablon.replace("%friend_name%", "Андрей")
shablon = shablon.replace( "%my_name%", "Тимур")
letter_mail = letter + shablon
letter_mail = letter_mail.encode("UTF-8")

login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
msg = server.login(login, password)
server.sendmail(from_mail, to_mail, letter_mail)
server.quit()

