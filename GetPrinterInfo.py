# -*- coding: UTF-8 -*-
import socket
import sys
import time


def connect_Printer(HOST, self):
    try:
        self.settimeout(2)
        self.connect((HOST, 9100))
    except Exception as e:
        err = str(e)
        print("Connect fail, Reason:\n")
        print(err)

def get_ID(self):   #打印机型号信息
    try:
        self.settimeout(2)
        self.send("@PJL INFO ID\r\n")
        time.sleep(1)   #Delay
        rec = self.recv(256)
        print(rec)
        sys.stdout.flush()
    except Exception as e:
        err = str(e)
        print("Get ID information fail,Reason:\n")
        print(err)

def get_ENV(self):  #打印机变量信息
    try:
        self.settimeout(10)
        self.send("@PJL INFO VARIABLES\r\n")
        time.sleep(2)   #Delay
        rec = self.recv(40960)
        print(rec)
        sys.stdout.flush()
    except Exception as e:
        err = str(e)
        print("Get variable information fail,Reason:\n")
        print(err)

def get_CONFIG(self):   #打印机初始化信息
    try:
        self.settimeout(3)
        self.send("@PJL INFO CONFIG\r\n")
        time.sleep(2)   #Delay
        rec = self.recv(40960)
        print(rec)
        sys.stdout.flush()
    except Exception as e:
        err = str(e)
        print("Get config information fail,Reason:\n")
        print(err)

def get_MEM(self):  #打印机内存信息
    try:
        self.settimeout(3)
        self.send("@PJL INFO MEMORY\r\n")
        time.sleep(2)   #Delay
        rec = self.recv(1024)
        print(rec)
        sys.stdout.flush()
    except Exception as e:
        err = str(e)
        print("Get memory information fail,Reason:\n")
        print(err)

def get_PAGECOUNT(self):  #打印计数
    try:
        self.settimeout(3)
        self.send("@PJL INFO PAGECOUNT\r\n")
        time.sleep(2)   #Delay
        rec = self.recv(1024)
        print(rec)
        sys.stdout.flush()
    except Exception as e:
        err = str(e)
        print("Get pagecount information fail,Reason:\n")
        print(err)

def get_STATUS(self):  #打印机状态
    try:
        self.settimeout(3)
        self.send("@PJL INFO STATUS\r\n")
        time.sleep(2)   #Delay
        rec = self.recv(1024)
        print(rec)
        sys.stdout.flush()
    except Exception as e:
        err = str(e)
        print("Get status information fail,Reason:\n")
        print(err)

def main():
    HOST = sys.argv[1]
    self = socket.socket()
    connect_Printer(HOST, self)
    get_ID(self)
    get_ENV(self)
    get_CONFIG(self)
    get_MEM(self)
    get_PAGECOUNT(self)
    get_STATUS(self)

    self.close()

if __name__ == '__main__':
    try:
        main()
    # catch CTRL-C
    except (KeyboardInterrupt):
        pass
    finally:
        print("")

#self = socket.socket()
#rec = ""
#self.connect(("10.255.88.75",9100))
#self.send("%-12345X@PJL INFO ID\r\n %-12345X")
#self.send("@PJL INFO ID\r\n")
#self.settimeout(2)
#self.close()
#print(rec)
#self.send("@PJL INFO VARIABLES\r\n")
#rec = self.recv(4096)
#print(rec)
#self.close()

