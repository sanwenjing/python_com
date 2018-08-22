#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os,sys;
import datetime as dt;

class log:
      fd="";
      def __init__(self,fileaddr=""):
            if(fileaddr):
                  self.fd=fileaddr;
            else:
                  self.fd=os.getcwd()+"\\"+ getFileName()+".log";
      def getFd(self):
            return(self.fd);
      def w(self,text):
            of=open(self.fd,'a');
            of.write(getTime()+"  "+text+"\r\n");
            of.close();
            return;
def getTime():
      now=dt.datetime.now();
      return now.strftime('%Y-%m-%d %H:%M:%S');

	
def getFileName():
    fn=sys.argv[0][sys.argv[0].rfind(os.sep) + 1:];
    return fn.split(".")[0];
	
if __name__=="__main__":
         print(getFileName());
         log1=log();
         print(log1.getFd());
         #log1.w("test");
