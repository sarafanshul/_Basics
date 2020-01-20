import subprocess
from time import asctime

# # for running a simple process
# subprocess.run(['dir'] , shell = True)


# # for capturing the stdout in a variable
# proc = subprocess.run(['dir'] , shell = True)

# # check
# print(proc)

# # for returning arguments
# print(proc.args)

# # for returning ERRORS occured
# print(proc.returncode)

# # for output from the external command
# proc = subprocess.run(['dir'], shell=True , capture_output = True)
# # this returnes output in bytecode 
# # for text output
# print(proc.stdout.decode())

# # for decoded out 
# proc = subprocess.run(['dir'] , shell=True , stdout = subprocess.PIPE)
# print(proc.decode())

# ---------- stdout = f returns output in file , if filename = (f)--
with open('test.txt' , 'a') as tes_file:
    subprocess.run(['ipconfig/displaydns'] , shell = True , stdout = tes_file , text = True)
    tes_file.write(f'{"-"*10} Time = {asctime()} {"-"*10}')
    print(flush=True)
