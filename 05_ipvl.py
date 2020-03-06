# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 12:13:04 2020

@author: CEC
"""

aclNum=int(input("What is de IPV4 ACL number?"))
if aclNum>=1 and aclNum<=99:
        print("This is a standard IPv4 ACL.")
elif aclNum>=100 and aclNum<=199:
    print("This is a extended IPv4 ACL.")
else:
    print("This is not an IPv4.")
    