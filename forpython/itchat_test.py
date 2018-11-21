import itchat
import pandas as pd
import jieba
from PIL import Image
from wordcloud import WordCloud,ImageColorGenerator
import numpy as np
import matplotlib.pyplot as plt
import re


sex=["none","男","女"]
chatroom_name=""
itchat.auto_login(hotReload=True)
room=itchat.get_chatrooms(contactOnly=True)
for i in room:
	if i["NickName"]=="不贰传说":
		chatroom_name=i
		break
#print(len(room))
get_chatroom_msg=itchat.update_chatroom(chatroom_name["UserName"],detailedMember=True)
# print(get_chatroom_msg)
# print(get_chatroom_msg["MemberList"])
keys=["Name","Sex","City","Signature"]
message_dict=dict.fromkeys(keys)
Name=[]
Sex=[]
City=[]
Signature=[]
for i in get_chatroom_msg["MemberList"]:
	if i["DisplayName"]:
		#print(f'{i["DisplayName"]} {sex[i["Sex"]]} 城市:{i["Province"]}{i["City"]} 签名:{i["Signature"]}')
		Name.append(i["DisplayName"])
	else:
		#print(f'{i["NickName"]} {sex[i["Sex"]]} 城市:{i["Province"]}{i["City"]} 签名:{i["Signature"]}')
		Name.append(i["NickName"])
	Sex.append(sex[i["Sex"]])
	if i["City"]:
		City.append(i["City"])
	elif i["Province"]:
		City.append(i["Province"])
	else:
		City.append("")
	if i["Signature"]:
		Signature.append(i["Signature"])
	else:
		Signature.append("")
message_dict[keys[0]]=Name
message_dict[keys[1]]=Sex
message_dict[keys[2]]=City
message_dict[keys[3]]=Signature

Signature_text=''.join(Signature)
pattern=re.compile(r'<span (.+)</span>|\d+|&(.+);')
Signature_text=pattern.sub('',Signature_text)


cut_text=jieba.cut(Signature_text,cut_all=False)
cut_text=' '.join(cut_text)
print(cut_text)
image=Image.open(r'/home/stenwaves/forpython/itchat1.jpg')
graph=np.array(image)

image_color=ImageColorGenerator(graph)
wc=WordCloud(font_path=r'/home/stenwaves/forpython/simkai.ttf',mask=graph,color_func=image_color,background_color='white',min_font_size=12,prefer_horizontal=1.0)
wc.generate(cut_text)





plt.imshow(wc)
plt.axis("off")
plt.show()


#print(cut_text)
#to_excel:
# message_to_excel=pd.DataFrame(message_dict)
# #print(message_to_excel)
# writer=pd.ExcelWriter('/home/stenwaves/forpython/itchat1.xls')
# message_to_excel.to_excel(writer,'Sheet1',index=False)
# writer.save()


#print(room)
# for i in range(len(room)):
# 	print(room[i]["NickName"])
#print(len(get_chatroom_msg["MemberList"]))
#print(Name,len(Name))
#print(message_dict)

itchat.run()