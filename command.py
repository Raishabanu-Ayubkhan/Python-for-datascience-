#Command line arguments help us pass input directly from the command prompt
#without asking the user during execution.
#Python uses the sys.argv list from the sys module to handle this.

import sys
a=int(sys.argv[1])
b=int(sys.argv[2])

print(a+b)


