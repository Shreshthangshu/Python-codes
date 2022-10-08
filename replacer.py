# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 07:45:41 2022

@author: SHRESHTHANGSHU
"""
def replacer(os,strtorep,newstr):
    #print(os,strtorep,newstr)
    new=[]
    for i in range(len(os)):
        new.append(os[i])
    flag=True
    if (len(strtorep)==len(newstr)):
        for i in range(len(os)):
            #for j in range(len(strtorep)):
                if os[i] == strtorep[0] :
                    for k in range(len(newstr)):
                        if os[i+k]==strtorep[0+k]:
                            flag=True
                        else :
                            flag=False
                    if flag :
                        for k in range(len(newstr)):
                            new[i+k]=newstr[k]
        pString=""

        print("Modified String:-->"+pString.join(new))
    else :                       
        print("Not Possible ......")
if __name__ == '__main__':
    os = input("Enter Original String:-->")
    strtorep = input("Part of string to replace:-->")
    newstr = input("New string:-->")
    replacer(os,strtorep,newstr)
