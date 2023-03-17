import sys
# Buffer Optimization
# Wrapper class to override the write function(Pipe stdout)
class unBuffered(object):
    def __init__(self, stream):
        self.stream = stream
    
    def write(self, data):
        self.stream.write(data)
        self.stream.flush()

    def writelines(self, datas):
        self.stream.writelines(datas)
        self.stream.flush() 
    
    def __getattr__(self, attr):
        return getattr(self.stream, attr)

sys.stdout = unBuffered(sys.stdout) # redid the sys.stdout class
sys.stderr = unBuffered(sys.stderr) # redid the sys.stderr class
sys.stderr.write("#This is Standard Error\n") # Override the write function
sys.stdout.write("#This is Standard Output and Not an Error \n") # Override the write function
print("Hello World")
