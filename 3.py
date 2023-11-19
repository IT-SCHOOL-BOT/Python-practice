from sys import stdin

allScores = []
for i in stdin:
  line = i.rstrip("\n").split()
  allScores.append((int(line[-2]), int(line[-1])))

allScores.sort(key=lambda x: x[1], reverse=True)
Winers = allScores[:int(len(allScores) / 100 * 45)]
if Winers[-1][1] == allScores[len(Winers)][1] and Winers[-1][1] <= 50:
  Winers = [i[0] for i in Winers if Winers[-1][1] != i[1]]
elif Winers[-1][1] == allScores[len(Winers)][1] and Winers[-1][1] > 50:
  Winers = [i[0] for i in allScores if i[1] >= Winers[-1][1]]
else:
  Winers = [i[0] for i in Winers]
Winers = sorted(set(Winers))
[print(i, end=" ") for i in Winers]