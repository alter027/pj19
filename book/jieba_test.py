import jieba

result = []

with open('./book') as f:
	context = f.read().split('\n')
	for para in context:
		if para == '':
			continue
		seg_list = jieba.cut(para)
		result.append(seg_list)

with open('./book_seg','w') as w:
	for i in result:
		w.write('|'.join(i))
		w.write('\n')