#!/usr/bin/env python3

# by Rachid AZGAOU

import requests as req
import sys

param_nbr_pages=int(sys.argv[1])            # NBR OF PAGES TO EXTRACT
param_file_output=sys.argv[2]               # FILE WHERE TO REDIRECT THE OUTPUT, EMPTY -> CONSOLE
param_show_output=int(sys.argv[3])          # SILENT OR SHOW INFO


if param_show_output==0:
    param_show_output="FALSE"
else:    
    param_show_output="TRUE"

if param_show_output=="TRUE":
    print("RUNNING ... ")
    print("NUMBER OF PAGES REQUESTED (0 -> ALL PAGES ) : "+str(param_nbr_pages))
    print("------------ ")


if param_show_output=="TRUE":
    print("SHOW OUTPUT CONSOLE :  " +param_show_output )






resp = req.get("https://www.startimes.com/f.aspx?search_member=&prev_mode=posts&members=posts&order=D&pg=1")


if int(resp.status_code) != 200:
    print("ERROR CAN NOT ACCESS TO THE SITE, RETURNED CODE: "+ str(resp.status_code))
    quit()

site_nbr_pages=resp.text.split("var totalpages = ")[1].split(";")[0]
nbr_users=resp.text.split("var totalmembers = ")[1].split(";")[0]
if param_show_output=="TRUE":
    print("TOTAL PAGES NUMBER: "+str(site_nbr_pages))
    print("TOTAL USERS NUMBER: "+nbr_users)
#print(resp.text)
a=resp.text.index("var members = new Array (")
# print(a)
b=resp.text.split("var members = new Array (")[1]
# print(b)
c=b.split('"",0,"",0,"","",0,0,0,"","");')[0].replace("\n", " ")
#print("result : -------------------------")
if param_show_output=="TRUE":
    print(c)


f = open(param_file_output, mode='w', encoding='utf-8')
f.writelines(c)
f.close()



index=0
if param_nbr_pages == 0:
    index=site_nbr_pages
else:
    index=param_nbr_pages


#if param_show_output=="TRUE":
 #   print("Number of pages actual : "+str(index))

for x in range(2,int(index)+1):
    resp = req.get("https://www.startimes.com/f.aspx?search_member=&prev_mode=posts&members=posts&order=D&pg="+str(x))
    #print(x)
    a=resp.text.index("var members = new Array (")
    b=resp.text.split("var members = new Array (")[1]
    c=b.split('"",0,"",0,"","",0,0,0,"","");')[0].replace("\n", " ")
    if param_show_output=="TRUE":
        print(c)
    f = open(param_file_output, mode='a', encoding='utf-8')
    f.writelines(c)
    f.close()    