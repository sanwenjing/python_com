#!/usr/bin/python
# -*- coding: UTF-8 -*-
#SSH反向代理守护脚本,命令存储在tasklist文件中
import os,sys;
import com;
def online():
    rt=0
    #cmd=os.popen("netstat -anpt|grep ssh|grep :22");
    cmd=os.popen("ps -ef|grep -v grep|grep qngfCNTR");
    print("online:");
    while 1:
            rusult=cmd.readline()
            if(rusult):
                print rusult.replace("\n","");
                rt=1;
            else:
                break;
    if rt:
	return 1;
    else:
	return 0;
def connect():
    log=com.log();
    log.w("Executed!!!");
    tl=open(com.getRunPath()+"/tasklist");
    print("Connecting:");
    while 1:
        line=tl.readline();
        if line:
            line.replace("\n","");
            if line.find("#")<0:
                os.system(line);
                print line;
        else:
            tl.close();
            online();
            break;
	
if __name__=="__main__":
#        print online();
            if(not online()):
                   connect();
            if(len(sys.argv)>=2):
                cmd=sys.argv[1];
                if(cmd=="stop"):
                    com.killByKw("qngfCNTR");
                elif(cmd=="restart"):
                    print("killlinks:");
                    com.killByKw("qngfCNTR");
                    com.sleep(1);
                    connect();
                elif(cmd=="start"):
                    connect();
