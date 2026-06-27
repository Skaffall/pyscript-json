import time
import json
import os 
import pprint
import math

start_time = time.time()
dfw = 1.0

if os.path.exists('dt.json'):
    with open('dt.json','r',encoding='utf-8') as f:
        oldw = json.load(f)
        w = oldw["metadata"]["Version"]
else:
    print("Error")

w = round(w + 0.1,1)
end_time = time.time()
data = {
    
    "metadata":{
        "Version": w,
        "Creator":"Kirassan"
    },
   "base":{
        "Time_init":time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        "Time_scwork":end_time - start_time
   }
}

with open('dt.json','w') as f:
    f.write(json.dumps(data,ensure_ascii=False,indent=4))

