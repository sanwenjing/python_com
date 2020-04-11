#!/usr/bin/python
# -*- coding: UTF-8 -*-
#sakura_frp反向代理守护脚本
import os,sys;
import com;
def checkOL():

if __name__=="__main__":
            if(len(sys.argv)>=2):
                cmd=com.getArgs(1);
                if(cmd=="stop"):
                    com.killByKw("qngfCNTR");
                elif(cmd=="restart"):
                    print("killlinks:");
                    com.killByKw("qngfCNTR");
                    com.sleep(1);
                    checkOL();
                elif(cmd=="start"):
                    checkOL();
