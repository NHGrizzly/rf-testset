import pyvisa

class instrument:
    def hp_assign(self):
        self.query('IP') # reset to instrument preset
        self.write('SW1') # swept mode
        self.write('ME') # display measurement data on CRT
        self.write('FD0') # output data in ASCII

    def hp_display(self, channel: int = 1, reference_position: float = -30.0, reference_level: float = 4, scale: int = 20, frq_rsp: bool = False):
        if(channel==1):
            self.write('C2 C0')
            self.write('C1')
        else:
            self.write('C' + str(channel))
        
        self.write('MY')
        self.write('RP' + str(reference_position))
        self.write('RL' + str(reference_level))
        self.write('SD' + str(scale))
        self.write('WM')

    def hp_run_test():
        pass

inst: instrument

rm = pyvisa.ResourceManager(r'C:\Users\wills\OneDrive\Documents\GitHub\rf-testset\hp5787d.yaml@sim')

inst = rm.open_resource('GPIB0::12::INSTR', read_termination = '\n', write_termination = '\n', query_delay = 0.5)