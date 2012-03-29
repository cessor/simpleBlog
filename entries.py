from json import load
from glob import glob
from convert_date import convert_date

class Entries:
  def read(self):
    entries = []
    for path in glob('./entries/*.json'):
      object = read_json_object(path)
      object["date"] = convert_date(object["timestamp"])
      entries.append(object)
    return entries

  def sort_by_date(self, entries):
    by_date = lambda object: object["timestamp"]
    entries.sort(key=by_date, reverse=True)

  # iterator pattern: http://en.wikipedia.org/wiki/Iterator
  def __iter__(self):
    entries = self.read()
    self.sort_by_date(entries)
    return entries.__iter__()

def read_json_object(path):
  return load(open(path, 'r'))
