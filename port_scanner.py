import socket
import sys
host = input("Host Giriniz: ")
ıp = socket.gethostbyname(host)

try:
    # -----------------------------------------------------
    s_21 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    sonuç_21 = s_21.connect_ex((ıp,21))
    if s_21 == 0:
        print("Ftp 21 portu Açık ")
    else:
        print("FTP  21 portu Kapalı ")
    s_21.close()
    # -----------------------------------------------------
    s_22 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    sonuç_22 = s_22.connect_ex((ıp,22))
    if sonuç_22 ==0:
        print("22 SSH Portu Açık")
    else:
        print("22 SSH Portu Kapalı")
        s_22.close()
    # -----------------------------------------------------
    s_23 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    sonuç_23 = s_23.connect_ex((ıp , 23))
    if sonuç_23 ==0:
        print("TELNET 23 Portu Açık")
    else:
        print("TELNET 23 Portu Kapalı")
    s_23.close()
    # ------------------------------------------------------
    s_25 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    sonuç_25 = s_25.connect_ex((ıp,25))
    if sonuç_25 == 0 :
        print("SMTP 25 Portu Açık ")
    else:
        print("SMTP 25  Portu Kapalı")
    s_25.close()
    # -----------------------------------------------------
    s_53 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    sonuç_53 = s_53.connect_ex((ıp,53))
    if sonuç_53 == 0 :
        print("DNS 53  Portu Açık ")
    else:
        print("DNS 53 Portu Kapalı")
    s_53.close()
    #------------------------------------------------------
    s_69 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    sonuç_69 = s_69.connect_ex((ıp,69))
    if sonuç_69 == 0 :
        print("TFTP 69 Portu Açık")
    else:
        print("TFTP 69 Portu Kapalı")
    s_69.close()
    # ------------------------------------------------------
    s_80 =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    sonuç_80 = s_80.connect_ex((ıp,80))
    if sonuç_80 == 0 :
        print("HTTP 80 Portu Açık")
    else:
        print("HTTP 80 Portu Kapalı")
    s_80.close()
    # ------------------------------------------------------
    s_110 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    sonuç_110 = s_110.connect_ex((ıp,110))
    if sonuç_110 == 0 :
        print("POP3 110 Portu Açık")
    else:
        print("POP3 110 Portu Kapalı")
    s_110.close()
    # ------------------------------------------------------
    s_123 =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    sonuç_123 = s_123.connect_ex((ıp,123))
    if sonuç_123 ==0:
        print("NTP 123 Portu Açık")
    else:
        print("NTP 123 Portu Kapalı ")
        s_123.close()
    # ------------------------------------------------------
    s_143 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    sonuç_143 = s_143.connect_ex((ıp,143))
    if sonuç_143 == 0 :
        print("IMAP 143 Portu Açık")
    else:
        print("IMAP 143 Portu Kapalı")
    s_143.close()
    # ------------------------------------------------------
    s_443 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    sonuç_443 = s_443.connect_ex((ıp,443))
    if sonuç_443 ==0:
        print("HTTPS 443 Portu Açık")
    else:
        print("HTTPS 443 Portu Kapalı")
    s_443.close()
    # ------------------------------------------------------
except KeyboardInterrupt:
    print("/n Çıkılıyor...")
    sys.exit()

except socket.gaierror:
    print("/n Hostname Geçersiz.")
    sys.exit()
except socket.error:
    print("/n Servere bağlanılamıyor")
    sys.exit()
