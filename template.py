class Template:
  def __init__(self, path, view_data): 
    self.path = path
    self.view_data = view_data 

  def read(self, path):
    content = ""
    with open(path, 'r') as file:
      content = file.read()
    return content
  
  def template(self, stencil, map): 
    for field in map:
      stencil = stencil.replace("$%s$" % field, map[field]) # Warning: This is slow
    return stencil
  
  def __str__(self):
    stencil = self.read(self.path)
    return self.template(stencil, self.view_data)