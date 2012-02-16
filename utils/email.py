#coding=utf-8
from threading import Thread

from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.models import User

FROM_EMAIL = 'admin@pylogs.cn'
#append this message to mail content bottom
MAIL_BOTTOM_MESSAGE = u'''<br/><br/><br/>
This is a mail send by the pylogs system automaticaly, Please do not reply this mail.<br/>
<a href="http://gentoogle.com" style="color:#f0f;font-weight:bold;">Pydiary</a> mail system.'''

def new_comment_mail(post_title,comment_content):
    '''send a mail to admin when a new comment posted'''

    #get the first user mailaddress
    try:

        firstuser = User.objects.get(id__exact = 1)
        if User is not None:
            subject = u'Pydiary有新评论等待审核'
            message = u'Pydiary中的文章<b>%s</b>有一条新评等待您的审核.内容为:<br/>%s' % (post_title,comment_content)
            recipient_list= [firstuser.email]    
            th = Thread(target=send_html_mail,args=(subject,message,recipient_list))
            th.start()
            #send_html_mail(subject,message,recipient_list)
    except:pass
    
def send_html_mail(subject,html_content,recipient_list):
    html_content += MAIL_BOTTOM_MESSAGE
    msg = EmailMessage(subject,html_content,FROM_EMAIL, recipient_list)
    msg.content_subtype = 'html'
    msg.send(fail_silently=True)     
