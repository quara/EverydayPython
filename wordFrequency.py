
fhandle = open('Acadia_National_Park.htm')
words = []
counts = []
for line in fhandle:
        zap= line.rstrip()
        if len(words) < 1:
            words.append(zap)
            counts.append(1)
        else:
            count = 0
            for i in range(len(words)):
                if zap == words[i]:
                    index = i
                    count += 1

            if count == 0:
                words.append(zap)
                counts.append(1)
            else:
                counts[index] += count

for i in range(len(words)):
    print 'Word: ',words[i],'\nFrequency: ',counts[i],'\n'

fhandle.close()
