import json

file = open('versos.txt')
lines = file.readlines()
listVersos = []
for index in range(len(lines)):
    line = lines[index].rstrip('\n')
    print(index)
    if ((index) % 2) == 1:
        listVersos[len(listVersos)-1]['ref'] = line
        
    else:
        listVersos.append({'text': line})

file.close()

newFile = open('bibleVerses.json', 'w')
newFile.write(json.dumps(listVersos, indent=4, sort_keys=True, ensure_ascii=False))
newFile.close()

