class Hero:
    def _init_(self,name,hp):
        self.name=name
        self.hp=hp
    name='松田'
    hp=100
    def sleep(self,hours):
        print('{}は{}時間寝た'.format(self.name,hours))
        self.hp+=hours

#ゲーム開始
print('すっきりファンタジーxii ~金色の理想郷~')
h=Hero()
h.sleep(3)
print('{}のHPは現在{}です'.format(h.name,h.hp))
