from datetime import datetime

class DateFormat:
  def __init__(self,date):
    self.date = date

  def parse(self,date):
    return datetime.strptime(date, "%Y-%m-%d")

  def reformat(self,date):
    return datetime.strftime(date, "%A, %d. %B %Y")

  def __str__(self):
    return self.reformat(self.parse(self.date))