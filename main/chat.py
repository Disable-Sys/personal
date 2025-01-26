
#模块语法参数：chat(url,key,model,消息列表)
#模块返回的是字典，包含添加gpt回答的消息列表与gpt的回答

import openai 
import datetime
now_time = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def chat(url,key,model,message_list: list):
    openai.base_url = url
    openai.api_key = key
    res = openai.chat.completions.create(
        model= model,
        max_tokens=4096,
        temperature=0.5,
        messages=message_list
    )
    content = res.choices[0].message.content
    message_list.append({"role":"assistant","content":content})
    output = {}
    output["message_list"] = message_list
    output["output"] = content
    return output
    


