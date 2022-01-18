def add_suffix(names):
    for i in range(len(names)):
        names[i]=names[i]+'さん'
    return names

before_names=['梅﨑','折原','加藤']
after_names=add_suffix(before_names)
print('さん付け後:'+after_names[0])
print('さん付け前:'+before_names[0])
