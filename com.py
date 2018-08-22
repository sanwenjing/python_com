#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os,sys;
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
	
def getFileName():
    fn=sys.argv[0][sys.argv[0].rfind(os.sep) + 1:];
    return fn.split(".")[0];

def getSystemClass():
      return pf.system();
if __name__=="__main__":
         print(getFileName());
         log1=log();
         print("//\\".replace("/","\\"));
         #log1.w("test");
