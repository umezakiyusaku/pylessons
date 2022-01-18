names=list()
print('変更前のlistのidentity:{}'.format(id(names)))
names.append('梅﨑')
print('変更前のlistのidentity:{}'.format(id(names)))
name='梅﨑'
print('変更後のstrのidentity:{}'.format(id(name)))
name='スーパー'+name
print('変更前のstrのidentity:{}'.format(id(name)))
name2='梅﨑'
print('name2のlistのidentity:{}'.format(id(names)))



