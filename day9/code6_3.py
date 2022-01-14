userinfo = input('名前と血液型をカンマ区切りで１行入力>>')
[name,blood]=userinfo.split(',')
blood=blood.upper().strip()#upper=大文字変換、よって小文字入力も大文字となる
print('{}さんは{}型なので大吉です'.format(name,blood))
