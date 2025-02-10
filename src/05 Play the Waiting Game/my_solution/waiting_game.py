import random
from datetime import datetime

def waiting_game():
  wait_time = random.choice([2,3,4])
  print(f'Your target time is {wait_time} seconds.')
  print('---Press Enter to Begin--')
  input()
  print(f'...Press Enter again after {wait_time} seconds...')
  start_time = datetime.now()
  input()
  end_time = datetime.now()
  elapsed_time = (end_time - start_time).total_seconds()
  if elapsed_time == wait_time:
    print(f'Elapsed time: {elapsed_time:.3f} seconds')
  elif elapsed_time > wait_time:
    print(f'Elapsed time: {elapsed_time:.3f} seconds({(elapsed_time - wait_time):.3f} too slow)')
  else:
    print(f'Elapsed time: {elapsed_time:.3f} seconds({(wait_time - elapsed_time):.3f} too fast)')

if __name__ == '__main__':
  waiting_game()