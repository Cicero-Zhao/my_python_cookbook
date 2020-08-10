
#######
# decode IMAP header, which can be used to decode email header
######

import re
import base64
pat2=re.compile(r'(([^=]*)=\?([^\?]*)\?([BbQq])\?([^\?]*)\?=([^=]*))',re.IGNORECASE)

def decodeEmailHeader(a):
    data=pat2.findall(a)
    line=[]
    if data:
            for g in data:
                    (raw,extra1,encoding,method,string,extra)=g
                    extra1=extra1.replace('\r','').replace('\n','').strip()
                    if len(extra1)>0:
                            line.append(extra1)
                    if method.lower()=='q':
                            string=quopri.decodestring(string)
                            string=string.replace("_"," ").strip()
                    if method.lower()=='b':
                            string=base64.b64decode(string)
                    line.append(string.decode(encoding,errors='ignore'))
                    extra=extra.replace('\r','').replace('\n','').strip()
                    if len(extra)>0:
                            line.append(extra)
            return "".join(line)
    else:
            return a

print(decodeEmailHeader("=?UTF-8?B?5a+G56CB6YeN6K6+?="))
