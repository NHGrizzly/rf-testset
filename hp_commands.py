import pyvisa

class instrument:

inst: instrument

rm = pyvisa.ResourceManager(r'C:\Users\wills\OneDrive\Documents\GitHub\rf-testset\hp5787d.yaml@sim')

inst = rm.open_resource('GPIB0::12::INSTR', read_termination = '\n', write_termination = '\n', query_delay = 0.5)