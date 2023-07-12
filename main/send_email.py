from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.core import mail

connection = mail.get_connection()

# Manually open the connection
connection.open()

def send_email(email):
    # connection = mail.get_connection()
    #
    # # Manually open the connection
    # connection.open()
    #
    # email1 = mail.EmailMessage(
    #     "Hello",
    #     "Body goes here",
    #     "from@example.com",
    #     ["ni.charikov05@gmail.com"],
    #     connection=connection,
    # )
    # email1.send()  # Send the email
    # connection.close()
    subject = 'Startup Life-Line'
    message = 'Рады, что вас заинтересовал наш проект' \
              'Просим ознакомиться с нашей призентацией https://drive.google.com/file/d/1sr2oqHTrfmOz9SnUQa_VXztVB7Qh365O/view?usp=sharing' \
              'С уважением, команда Life-Line.'
    from_email = 'ni.charikov@gmail.com'

    if email:
        try:
            send_mail(subject, message, from_email, [f"{email}"], fail_silently=False)
        except BadHeaderError:
            return HttpResponse("Invalid header found.")
        return HttpResponseRedirect("/contact/thanks/")
    else:
        return HttpResponse("Make sure all fields are entered and valid.")

