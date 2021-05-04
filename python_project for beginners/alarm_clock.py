import winsound
from time import strftime

Ht = int(strftime('%H'))
Mt = int(strftime('%M'))
print(str(Ht)+":"+str(Mt))
hour = int(input("enter alarm hour:"))
minute = int(input("enter alarm minute:"))
while True:
      if hour == Ht and minute == Mt:
          print("ALARM RINGING")
          frequency = 500
          duration = 100
          for i in range(0,4):
              winsound.Beep(frequency, duration)
          break
      else :
          print("ALARM NOT RINGING")
          break




