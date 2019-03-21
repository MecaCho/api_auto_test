# -*-coding=UTF-8-*-
import os
import threading
import logging
import requests
import ssl

from exchangelib import Account, Credentials, Configuration, EWSTimeZone, EWSDateTime, Message, Mailbox, HTMLBody

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s - %(name)s - %(message)s")
LOG = logging.getLogger(__name__)


def send_msg(body):
    requests.urllib3.disable_warnings()

    ssl._create_default_https_context = ssl._create_unverified_context

    from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter
    BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter

    sender = '@.com'

    user = 'C'
    import sys
    mail_pass = sys.argv[1]
    print user, mail_pass

    credentials = Credentials(
            username=user,  # Or myusername@example.com for O365
            password=mail_pass
    )

    mail_host = ".."
    config = Configuration(credentials, server=mail_host)
    account = Account(
            primary_smtp_address=sender,
            config=config, access_type='delegate'
    )

    addr = "@.com"
    subject = u""
    m = Message(
            account=account,
            subject=subject,
            body=HTMLBody("".join(body)),
            to_recipients=[
                Mailbox(email_address=addr),
            ],
    )
    m.send()
    logger.info("Sended subject: %s to %s", subject, addr)


def check_wiki():
    print "Checking wiki ..."
    os.system("cd /root/Python/ief.wiki/ && git log > /root/Python/auto_wiki/log.txt")
    bak_file = "/root/Python/auto_wiki/log_bak.txt"
    bak_fp = open(bak_file, "r")
    old_lines = bak_fp.readlines()

    new_file = "/root/Python/auto_wiki/log.txt"
    new_fp = open(new_file, "r")
    new_lines = new_fp.readlines()

    print len(old_lines), len(new_lines)
    try:
        print ""
    except Exception:
        pass

    if len(old_lines) < len(new_lines):
        print "Wiki changed!"
        body = [u"：http://n\n"]
        body.extend(new_lines[:5])
        os.system("cd /root/Python/ief.wiki/ && git log -p -1 > /root/Python/auto_wiki/log_last.txt")
        fp = open("log_last.txt", "r")
        log_lines = fp.readlines()
        body.extend(log_lines)
        send_msg(body)
        os.system("cp /root/Python/auto_wiki/log.txt /root/Python/auto_wiki/log_bak.txt")
    else:
        print "check finished and no changed."


def Run():
    t = threading.Timer(10, Run, ())
    check_wiki()
    t.start()


if __name__ == "__main__":
    Run()
