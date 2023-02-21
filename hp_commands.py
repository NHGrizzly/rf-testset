import pyvisa

class instrument:
    def assign(self):
        self.query('IP') # reset to instrument preset
        self.write('SW1') # swept mode
        self.write('ME') # display measurement data on CRT
        self.write('FD0') # output data in ASCII

inst: instrument

rm = pyvisa.ResourceManager(r'C:\Users\wills\OneDrive\Documents\GitHub\rf-testset\hp5787d.yaml@sim')

inst = rm.open_resource('GPIB0::12::INSTR', read_termination = '\n', write_termination = '\n', query_delay = 0.5)