#!/usr/bin/python
# -*- coding: UTF-8 -*-
#sakura_frp反向代理守护脚本
import os,sys;
import com;
#def checkOL():


if __name__=="__main__":
# com.bgrun("./frpc_linux_arm -c frpc.ini")
#  print com.isrun("frpc_linux_arm")
            progName="frpc_linux_arm"
            cmdline="/usr/program/sshproxy/frp/frpc_linux_arm -c /usr/program/sshproxy/frp/frpc.ini"
            if(len(sys.argv)>=2):
                cmd=com.getArgs(1);
                if(cmd=="stop"):
                    com.killByKw(progName);
                elif(cmd=="restart"):
                    print("killlinks:");
                    com.killByKw(progName);
                    com.sleep(1);
                    com.bgrun(cmdline)
                elif(cmd=="start"):
                    if not com.isrun(progName):
                      com.bgrun(cmdline)



