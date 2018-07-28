
data = []
count = 0
length = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1 #same as count = count + 1
		length += len(line) #same as length = length + len(line)
		if count % 1000 == 0: #count divided by 1000 mode 0
			print(len(data))
print('finished reading file, in total ', len(data), ' reviews')

print('the average length of the review is ', length/count)
# or print('the average length of the reivew is', length/len(data))