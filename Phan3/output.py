class Output:
  def __init__(self, output = False):
    self.output = output
  
  def printOutputToFile(self, fileName):
    if (isinstance(self.output, list)):
      self.printOutputListToFile()
      return
    f = open(fileName, "w")
    f.write(output)
    f.close()
  
  def printOutputToScreen(self):
    if (isinstance(self.output, list)):
      self.printOutputListToScreen()
      return
    print(output)

  def printOutputListToFile(self, fileName):
    f = open(fileName, "w")
    for out in self.output:
      f.write(out)
    f.close()

  def printOutputListToScreen(self):
    for out in self.output:
      print(out)
