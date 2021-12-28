scores=[]
scores.append(int(input('国語の点数>>')))
scores.append(int(input('算数の点数>>')))
scores.append(int(input('理科の点数>>')))
scores.append(int(input('社会の点数>>')))
scores.append(int(input('英語の点数>>')))
#console.log('合計点＄{s},平均点＄{avg})
print(f'合計{sum(scores)}点/平均{sum(scores)/len(scores)}点')

#"""
#let li=[]:
#li push(10):
#li push(20);
#let sum=0;
#for(let i=0;i<li.length;i++){
#sum+=li[i];
#}
#console.log(`合計点${sum},平均点${sum/li.length}`)
#"""
#print(f'合計点{sum(li)},平均点{sum(li)/len(li)}')
