import glob

print 'digraph TT{'              
for fileName in glob.iglob("*.ev3p"):
   node = fileName[:-5]
   f = open(fileName)
   list = []
   for line in f:
       if line.find('.ev3p') != -1:
          begin = line.find('Target') + 8
          end = line.find('\\.ev3p')
          myBlock = line[begin:end]
          if myBlock not in list:
              list.append(myBlock)  
   if not list:
       print '"{0}"'.format(node)
   else:
       for item in list:
           print '"{0}"->"{1}"'.format(node,item)
   f.close()
print '}'
   
   
   
   