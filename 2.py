def Add(n: int):
  s.add(n)

def Present(n: int):
  print("YES" if n in s else "NO")

def Count():
  print(len(s))

s = set()
n = int(input())
for _ in range(n):
  Command = input().split()
  if Command[0] == "ADD":
    Add(int(Command[1]))
  elif Command[0] == "PRESENT":
    Present(int(Command[1]))
  elif Command[0] == "COUNT":
    Count()
