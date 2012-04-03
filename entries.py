from glob import glob
from json import load
from dateformat import DateFormat

class Entries:
  def read(self):
    entries = []
    for path in glob('./entries/*.json'):
      object = self.read_json_object(path)
      object["date"] = str(DateFormat(object["timestamp"]))
      entries.append(object)
    return entries

  def written_on(self, date):
    return [ entry for entry in self.__iter__() if entry["timestamp"] == date ]

  def sort_by_date(self, entries):
    by_date = lambda object: object["timestamp"]
    entries.sort(key=by_date, reverse=True)

  def __iter__(self):
    entries = self.read()
    self.sort_by_date(entries)
    return entries.__iter__()

  def read_json_object(self,path):
    return load(open(path, 'r'))