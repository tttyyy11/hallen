
# coding=utf-8

class A(object):
    def go(self):
        print ("go A go!")
    def stop(self):
        print ("stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")
class B(A):
    def go(self):
        super(B, self).go()
        print ("go B go!")
class C(A):
    def go(self):
        super(C, self).go()
        print ("go C go!")
    def stop(self):
        super(C, self).stop()
        print ("stop C stop!")
class D(B,C):
    def go(self):
        super(D, self).go()
        print ("go D go!")
    def stop(self):
        super(D, self).stop()
        print ("stop D stop!")
    def pause(self):
        print ("wait D wait!")
class E(B,C):
    pass

a = A()
b = B()
c = C()
d = D()
e = E()

# a.go()
# print('--------')
# b.go()
# print('--------')
# c.go()
# print('--------')
# d.go()
# print('--------')
e.go()
print('--------')
# a.stop()
# print('--------')
# b.stop()
# print('--------')
# c.stop()
# print('--------')
# d.stop()
# print('--------')
# e.stop()
# print(D.mro())
# a.pause()
# b.pause()
# c.pause()
# d.pause()
# e.pause()

# print"-----------------------------------------------------"
# a = [1,1,2,3,3,4,5,34,35,23,56,33,77,88,99,11]
# b = list(set(a))
# print b 
# b.sort()
# print b
# print"-----------------------------------------------------"
# s = sum(range(0,101))
# print s

# dictn = {"a":1,
#          "b":2,
#          "c":3,
#          "d":4}
# dic = {"f":5,
#         "s":6}
# print dictn
# del dictn["a"]
# print dictn
# dic.update(dictn)
# print dic

# import random
# # import numpy as np
# print random.randint(1,10)
# print random.random()

#!/usr/bin/python
# import re
 
# line = "Cats are smarter than dogs ssh jijiji hhhh jjjj ki ";
 
# # matchObj = re.match( r'dogs', line, re.M|re.I)
# # if matchObj:
# #     print "match --> matchObj.group() : ", matchObj.group()
# # else:
# #     print "No match!!"
 
# matchObj = re.search( r'ki', line, re.M|re.I)
# if matchObj:
#     print "search --> searchObj.group() : ", matchObj.group()
# else:
#     print "No match!!"

# numstr = "wo shi zhong guo ren ,wo aini jake 132 jake eee"
# matchObj = re.search(r"jake (\d+) (.*)",numstr,re.M|re.I)
# if matchObj:
#     print  matchObj.group()
# else:
#     print "nothing" 




# L = ['j', 'xiaohong', '12', 'adf12', '14']
# for i in range(len(L)):
#   if re.findall(r'^[^\d]\w+', L[i]):
#     print(re.findall(r'^\w+$', L[i])[0])

# L = ['xiaohong', '12', 'adf12', '14', 'j']
# for x in L:
#   try:
#     int(x)
#   except:
#     print(x)


# lis = [1,2,4,6]
# def multiplication(x):
#     return x**2
# t = map(multiplication,lis)
# print t

# dictionary ={"city":"beijing", "time":12,"age":18,"name":"wang"}
# listi = sorted(dictionary.items(),key=lambda i:i[0],reverse=False)
# print listi
# newdic = {}
# newdic = dict(listi)
# # for i in listi:
# # 	newdic[i[0]] = i[1]
# # 	print i[1]
# # 	print newdic
# print newdic

# from collections import Counter
# a = "sjjsjag;jsjdiajg;23twiig;67ghghjj:gt"
# res = Counter(a)
# print res




# import re
# import sys

# a = 'ffy  jjiii zhang   wang  13435   李四'
# print a
# list = a.split(" ")
# print list
# sat = re.search(r"(\d+|[a-zA-Z]+)+",a,re.M|re.I)
# if sat:
# 	print sat.group()
# else:
# 	print "nothing"

# ass = re.findall(r"\d+|[a-zA-Z]+",a)
# for i in ass:
# 	print i
# 	if i in list:
# 		list.remove(i)
# newss = " ".join(list)
# print newss
# print "-----------------------------------------"
# ab = [1,2,3,4,5,33,2,34]
# cd = [4,52,5,8,9,15]
# cf = ab+cd
# print cf 
# newcf = sorted(cf,reverse = False) 
# print newcf
# b = list(set(newcf))
# print b

# import os
# AP_SSID = "wolooo"
# dos_command = "netsh wlan connect " + AP_SSID
# print "PC CMD: %s"%(dos_command)
# cmd_handler = os.popen(dos_command)
# output_text = cmd_handler.read()
# output_text = unicode(output_text, "gbk")
# print output_text
# if u'成功完成连接' in output_text:
#     print "pc connect ap %s successful"%(AP_SSID)
#     PC_connect_AP = True
# else:
#     print "pc connect ap %s failed"%(AP_SSID)
#     PC_connect_AP = True



# if net == "WLAN":
#             dos_command = 'netsh wlan connect '+ AP_SSID
#             print "[ATE LOG] PC CMD: %s"%dos_command
#             cmd_handler = os.popen(dos_command)
#             output_text = cmd_handler.read() 
#             u_output_text = unicode(output_text, "gbk")
#             print u_output_text
            
#             # check if received '成功完成连接' 
#             if (u'成功完成连接' in u_output_text): 
#                 ret_connect_ap = True
#             else:
#                 print "Connect %s failed! Quit PC_connect_AP."%AP_SSID
#                 ret_connect_ap = False  
                           
#             cmd_handler.close() 
        
#         ret_connect_ap = True
#         time.sleep(2) 
#         if(ret_connect_ap == True):
#             dos_command = 'ipconfig'
#             cmd_handler = os.popen(dos_command)
#             output_text = cmd_handler.read()             
#             u_output_text = unicode(output_text, "gbk")
#             print u_output_text
#             # get WLAN ip address 
#             IP_address_search_keyword = '[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*'
#             if u_output_text.find(net)!=-1:
#                 IP_STR = u_output_text[u_output_text.find(net):]
#             else:
#                 print "[ATE_LOG]:Can't find param %s, or can't math required IP address!"%net
#                 return False
#             ret_message = re.findall(IP_address_search_keyword, IP_STR , re.I|re.M )
#             if len(ret_message)>=3:
#                 wlan_ip_addr = ret_message[0]
#                 ap_ip_addr   = ret_message[2] 
#             else:
#                 print "[ATE log]PC have not IPV4 address."
#                 return False                   
#             #print "wlan_ip_addr = %s"%wlan_ip_addr
#             cmd_handler.close()
#             time.sleep(1) 
#             # check if ping operation is correct or not 
#             '''
#             ip_addr_array = wlan_ip_addr.split('.')
#             ap_ip_addr = ip_addr_array[0]+'.'+ip_addr_array[1]+'.'+ip_addr_array[2]+'.1' 
#             '''
#             dos_command = 'ping ' + ap_ip_addr
#             cmd_handler = os.popen(dos_command)
#             output_text = cmd_handler.read()
#             #print output_text
#             u_output_text = unicode(output_text, "gbk")
#             #print u_output_text
#             if(u'100% 丢失' in u_output_text):  # ping is successful
#                 print " Ping %s failed! "%ap_ip_addr  
#                 ret_status = False
#             else: 
#                 self.iperf_server_ip_addr =  wlan_ip_addr 
#                 print " Ping %s success, Iperf PC IP = %s"%(ap_ip_addr,self.iperf_server_ip_addr)                
#                 ret_status = True
#             cmd_handler.close()

        
#         return ret_status







# class Employee:

#    empCount = 0
 
#    def __init__(self, name, salary):
#       self.name = name
#       self.salary = salary
#       Employee.empCount += 1
#       print "iiiiiiiiiiiii"
   
#    def displayCount(self):
#      print "Total Employee %d" % Employee.empCount
 
#    def displayEmployee(self):
#       print "Name : ", self.name,  ", Salary: ", self.salary
 

# emp1 = Employee("Zara", 2000)
# emp2 = Employee("Manni", 5000)
# # emp1.displayEmployee()
# # emp2.displayEmployee()
# print "Total Employee %d" % Employee.empCount


# class  sjjjj:
#     def __init__(self,an,ni):
#         self.an = an
#         self.ni = ni
#         print "9i"
#     def mooi(self):
#         print self.an
# a = sjjjj(3,4)
