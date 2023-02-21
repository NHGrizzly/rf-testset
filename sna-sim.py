import pyvisa

rm = pyvisa.ResourceManager(r'C:\Users\wills\OneDrive\Documents\GitHub\rf-testset\hp5787d.yaml@sim')
# tells pyvisa to use a simulated backend based on the local file rf-inst.yaml using a raw string

# print(rm.list_resources()) # prints all of the visa devices visible to the resource manager

inst = rm.open_resource('GPIB0::12::INSTR', read_termination = '\n', write_termination = '\n', query_delay = 0.5)
# opens the gpib instrument on board 0 numbered 4 using line separators and a delay for queries

print(inst) # identifies inst from pyvisa

print(inst.query('OI')) # self identify inst

print(inst.query('IP')) # calibrate the device

print(inst.query('C1 IA C2 IB'))

# print(inst.query('?PENIS')) # harass the instrument