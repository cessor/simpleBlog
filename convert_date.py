from datetime import datetime

def parse_date(date):
  return datetime.strptime(date, "%Y-%m-%d")

def reformat_date(date):
  return datetime.strftime(date, "%A, %d. %B %Y")

def convert_date(date):
  return reformat_date(parse_date(date))
