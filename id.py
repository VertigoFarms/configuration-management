#!./env/bin/python3

import uuid
import yaml

class ID:
  def __init__(self, idfile=".id"):
    try:
      with open(idfile, 'r') as f:
        tmp = yaml.load(f, Loader=yaml.Loader)
        self.__id = uuid.UUID(tmp['id'])
    except:
      self.__id = uuid.uuid4()
      with open(idfile, 'w+') as f:
        yaml.dump({'id':self.__id.hex}, f)

  def get(self):
    return self.__id.hex
