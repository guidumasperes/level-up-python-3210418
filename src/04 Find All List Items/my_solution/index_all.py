########## NOT WORKING

def find_index(search, value):
  if type(search) == type(0):
    return []
  else:
    aux = find_index(search[0], value)
    for i in range(0, len(search)):
      if type(search[i]) == type(0):
        if i == value:
          return aux.append(i)
    return aux.append(0)
  
if __name__ == '__main__':
  print(find_index([[0,2],3],2))