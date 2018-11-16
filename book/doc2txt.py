import os
import docx2txt

datas = os.listdir('./docx')
clear_text = []

for data in datas:
	text = docx2txt.process('./docx/'+data).split('\n')
	for i in text:
		if len(i)>0:
			if i[0]=='▲':
				continue
			elif i[0]=='\uf075':
				continue
			elif i[0]=='▼':
				continue
			elif i[0]=='\uf070':
				continue
			elif i[0]=='\uf074':
				continue
			elif i[0]=='\uf071':
				continue
			elif i[0]=='第' and i[2]=='章':
				continue
			elif i[0]=='第' and i[2]=='節':
				continue
			elif len(i)<=30 and i!='問題與討論':
				continue
			elif len(i)>1 and i[1]=='、':
				continue
			elif len(i)>3 and i[0]=='(' and i[2]==')':
				continue
			elif i[0:4]=='資料來源':
				continue
			elif i=='問題與討論':
				break
			else:
				temp = i.split('\t')
				i = ''.join(temp)
				if i[0]>='0' and i[0]<='9' and i[1]=='.':
					i=i[2:]
				clear_text.append(i)

with open('book','w') as f:
	for i in clear_text:
		f.write(i)
		f.write('\n')

print(len(clear_text))