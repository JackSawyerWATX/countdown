import time

seconds = int(input("Enter seconds for countdown: "))

for i in range(seconds, -1, -1):
  if i == -1:
    print("Finished")
  else:
    print(f" Time left: {i} seconds",
    end='\r')
  time.sleep(1)
print(" Time's up")