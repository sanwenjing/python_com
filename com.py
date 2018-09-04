#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os,sys,time;
import datetime as dt;
import platform as pf;
class log:
      fd="";
      def __init__(self,fileaddr=""):
            if(fileaddr):
                  self.fd=fileaddr;
            else:
                  self.fd=getAddrStr(os.getcwd()+"\\"+ getFileName()+".log");
      def getFd(self):
            return(self.fd);
      def w(self,text):
            of=open(self.fd,'a');
            of.write(getTime()+"  "+text+"\r\n");
            of.close();
            return;
def getAddrStr(address):
      if getSystemClass()=="Windows":
            return address.replace("/","\\");
      else:
            return address.replace("\\","/");
def getTime():
      return getTimeFormat('%Y-%m-%d %H:%M:%S');
def getTimeFormat(format):
      now=dt.datetime.now();
      return now.strftime(format);
def sleep(seconds):#延时程序
      time.sleep(seconds);
def getFileName():
    fn=sys.argv[0][sys.argv[0].rfind(os.sep) + 1:];
    return fn.split(".")[0];

def getSystemClass():
      return pf.system();

def killByKw(keyword):#命令行关键字终结程序
      os.system("ps -ef|grep "+keyword+" |awk '{print $2}'|xargs kill -9");
def getHtml(url):#取HTML代码,利用CURL
    html=os.popen("curl "+url)
    htmltxt=""
    while 1:
        line=html.readline()
        if line:
            htmltxt+=line
        else:
            break
    return htmltxt
if __name__=="__main__":
         print(getFileName());
         log1=log();
         print("//\\".replace("/","\\"));
         #log1.w("test");
         print getHtml("www.baidu.com")         
