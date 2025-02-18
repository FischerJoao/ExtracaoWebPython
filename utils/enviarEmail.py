import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os

def enviar_email():
    corpo_email = """
    <p>Olá, aqui está o seu relatório dos notebooks extraídos da Magazine Luiza.</p>
    <p>Atenciosamente,</p>
    <p>Robô</p>
    """

    arquivo = os.path.join("E:\\ExtracaoMagalu\\Output", "Notebooks.xlsx")

    msg = MIMEMultipart()
    msg['Subject'] = "Relatório Notebooks"
    msg['From'] = ''  #INSIRA  SEU EMAIL AQUI 
    msg['To'] = '' #INSERA PARA QUEM IRA ENVIAR O EMAIl


# converte o aquivo em binário e adiciona o conteúdo ao email

    msg.attach(MIMEText(corpo_email, 'html'))

    with open(arquivo, 'rb') as anexo:
        att = MIMEBase('application', 'vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        att.set_payload(anexo.read())
        encoders.encode_base64(att)
        att.add_header('Content-Disposition', 'attachment', filename='Notebooks.xlsx')
        msg.attach(att)

    #Padroes de envio de email
    #protocolo SMTP

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    password = ''    #SENHA TEMPORARIA!!
    s.login(msg['From'], password)
    s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
    s.quit()
    print('Email enviado com sucesso!')
