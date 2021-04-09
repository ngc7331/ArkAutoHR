import json
with open('history.log', 'r', encoding='UTF-8') as f:
    lines = f.readlines()

d = {}
i = 1
for line in lines:
    _, tag, choose, name, star = line.strip().split('; ')
    d.update({
        i: {
            'id': i,
            'tag_list': tag,
            'tag_chosen': choose,
            'name': name,
            'rarity': int(star)
        }
    })
    i += 1

with open('history.json', 'w', encoding='UTF-8') as f:
    f.write(json.dumps(
        d,
        indent=2,
        separators=(',', ': '),
        ensure_ascii=False
    ))