def inputscores(name):
    print('{}さんの試験結果を入力してください>>'.format(name))
    network=int(input('ネットワークの得点は>>'))
    database=int(input('データベースの得点は>>'))
    security=int(input('セキュリティの得点は>>'))

    scores=[network,database,security]
    return scores

def calcaverage(scores):
    avg=sum(scores)/len(scores)
    return avg

def outputresult(name,avg):
    print('{}さんの平均点は{}です'.format(name,avg))

 asagiscores=input scores('浅木')
 umezakiscores=input scores('梅﨑')

 asagiavg=calcaverage(asagiscores)
 umezakiavg=calcaverage(umezakiscores)

 outputresult('浅木'.asagiavg)
 outputresult('梅﨑'.umezakiavg)
