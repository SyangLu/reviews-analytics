data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')

sum_len = 0
for c in data:
	sum_len += len(c)
print('留言平均長度為:', sum_len/len(data))

new =[]
for c in data:
	if len(c) < 100:
		new.append(c)
print('總共有', len(new), '筆留言長度小於100')