import smtplib
import ssl

from django.conf import settings
from email.message import EmailMessage

from businesslogic.models import Feedback


# 


NEW_REQUESTS_ADMIN_URL = settings.SERVER_ORIGIN + "/admin/businesslogic/feedback/?is_completed__exact=0"


# 


# Сохраняет новую заявку в БД и возвращает ее
def save_user_feedback(email: str, name: str, message: str):
    return Feedback.objects.create(
        name = name,
        email = email,
        message = message
    )


# Отправка письма администратору с уведомлением о том, что пользователь оставил сообщение через форму на сайте
def send_notification_email(admin_email: str, user_request: Feedback):

    # Email account details
    sender_email = settings.NOTIFICATIONS_SENDER_EMAIL
    sender_password = settings.NOTIFICATIONS_SENDER_PASSWORD

    # Create the email message
    msg = EmailMessage()
    html_content = """
<html><body>
<p>На сайте <a href="https://кпппк.рф">кпппк.рф</a> получено новое обращение через форму обратной связи.</p>

<p><strong>Данные клиента:</strong></p>
<ul>
<li><strong>Дата и время:</strong> {}</li>
<li><strong>Имя отправителя:</strong> {}</li>
<li><strong>E-mail для ответа:</strong> {}</li>
<li><strong>Номер заявки (ID):</strong> #{}</li>
</ul>

<p><strong>Текст сообщения:</strong></p>
<p>---------------------------------------------------------------------</p>
<p>{}</p>
<p>---------------------------------------------------------------------</p>

<p><strong>Для действий:</strong></p>
<ol>
<li>Ответьте клиенту в течение 1-2 рабочих дней.</li>
<li>При ответе используйте адрес {}</li>
<li>После ответа отметьте заявку как обработанную в админ-панели.</li>
</ol>

<p>Ссылка на админ-панель для просмотра: <a href="{}">{}</a></p>

<p>Хорошего дня!</p>
<p>---</p>
<p>Это письмо создано автоматически. Пожалуйста, не отвечайте на него.</p>
</body></html>""".format(user_request.created_at.strftime("%d.%m.%Y %H:%M:%S"), user_request.name, user_request.email, 
            user_request.id, user_request.message, user_request.email, NEW_REQUESTS_ADMIN_URL, NEW_REQUESTS_ADMIN_URL)

    msg.set_content(html_content, subtype='html')
    msg['Subject'] = "Новое обращение с сайта #{} от {}".format(user_request.id, user_request.created_at.strftime("%d.%m.%Y %H:%M:%S"))
    msg['From'] = sender_email
    msg['To'] = admin_email

    try:
        # Create a secure SSL context
        context = ssl.create_default_context()

        # Connect to the server and send the email
        with smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context) # Secure the connection
            server.ehlo()  # Can be omitted
            server.login(sender_email, sender_password)
            server.send_message(msg)

    except smtplib.SMTPAuthenticationError:
        print("Authentication error: Check your username and app password.")
        raise Exception("Ошибка отправки e-mail")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise Exception("Ошибка отправки e-mail")



# Отправка noreply-письма пользователю, что сообщение успешно дошло администратору
def send_noreply_email(receiver_email: str, receiver_name: str, receiver_msg: str):

    # Email account details
    sender_email = settings.NOREPLY_SENDER_EMAIL
    sender_password = settings.NOREPLY_SENDER_PASSWORD

    # Create the email message
    msg = EmailMessage()
    html_content = """
<html><body>
<p>Здравствуйте, {}!</p>
    
<p>Благодарим вас за обращение в ГБПОУ «Коми-Пермяцкий профессионально-педагогический колледж ордена «Знак Почета»»!</p>

<p>Это автоматическое подтверждение, что ваше сообщение успешно доставлено.</p>
<p>Мы получили следующую информацию:</p>

<ul>
<li><strong>Имя:</strong> {}</li>
<li><strong>E-mail:</strong> {}</li>
<li><strong>Ваше сообщение:</strong> "{}"</li>
</ul>

<p>Наша команда уже ознакомилась с вашим запросом. Мы постараемся дать вам подробный и полезный ответ в кратчайшие сроки.</p>

<p>Обычно мы обрабатываем обращения в течение 1-2 рабочих дней.</p>

<p>Пожалуйста, ожидайте ответа на указанный вами адрес электронной почты.</p>

<p>С уважением и наилучшими пожеланиями,<br/>
ГБПОУ КПППК<br/>
<a href="https://кпппк.рф">кпппк.рф</a><br/>
+7 342 604 11 08</p>
</body></html>""".format(receiver_name, receiver_name, receiver_email, receiver_msg)

    msg.set_content(html_content, subtype='html')
    msg['Subject'] = "Ваше сообщение получено — ГБПОУ КПППК"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        # Create a secure SSL context
        context = ssl.create_default_context()

        # Connect to the server and send the email
        with smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context) # Secure the connection
            server.ehlo()  # Can be omitted
            server.login(sender_email, sender_password)
            server.send_message(msg)

    except smtplib.SMTPAuthenticationError:
        print("Authentication error: Check your username and app password.")
        raise Exception("Ошибка отправки e-mail")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise Exception("Ошибка отправки e-mail")



def send_feedback_email(receiver_email: str, receiver_name: str, receiver_msg: str):

    # Сохраняем данные заявки в БД:

    try:
        user_request = save_user_feedback(receiver_email, receiver_name, receiver_msg)
    except Exception as e:
        raise Exception("Ошибка сохранения заявки в БД")

    # Отправка емейлов:

    # ПРОДАКШЕН-ВЕРСИЯ: send_noreply_email(receiver_email, receiver_name, receiver_msg)
    # РАЗРАБОТКА-ВЕРСИЯ: send_noreply_email("sweetqiwi@gmail.com", "Alisa K.", "Stupid canadian wolf bird")
    send_noreply_email("sweetqiwi@gmail.com", receiver_name, receiver_msg)

    # ПРОДАКШЕН-ВЕРСИЯ: send_notification_email(settings.KPPPK_ADMIN_EMAIL, user_request)
    # РАЗРАБОТКА-ВЕРСИЯ: send_notification_email("sweetqiwi@gmail.com", user_request)
    send_notification_email("sweetqiwi@gmail.com", user_request)
