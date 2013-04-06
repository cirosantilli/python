#!/usr/bin/env python

"""
template for testing programs (executables or scripts)

feeds args and stdin, and checks stdout, stderr and exit status
"""

import subprocess
import sys
import unittest 

class ProgramInput:

    def __init__(self, stdin, args ):
        self.stdin  = stdin
        self.args   = args

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    def __str__(self):
        return \
            'stdin:\n' + self.stdin + '\n\n' \
            'args: ' + self.args.__repr__() + '\n'

class ProgramOutput:

    def __init__(seing lf, stdout, stderr, exit_status):
        self.stdout         = stdout
        self.stderr         = stderr
        self.exit_status    = exit_status

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    def __str__(self):
        return \
            'stdout:\n' + self.stdout + '\n\n' \
            'stderr:\n' + self.stderr + '\n\n' \
            'exit_status: ' + str(self.exit_status) + '\n'

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test(self):

        for inout in inouts:

            inp, out_expect = inout
            command = [ program_path ]
            command.extend( inp.args )

            process = subprocess.Popen(
                command,
                shell  = False,
                stdin  = subprocess.PIPE,
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE
            )
            stdout, stderr = process.communicate( inp.stdin )
            exit_status = process.wait()
            out = ProgramOutput( stdout, stderr, exit_status )

            #print inp
            #print out
            #print out_expect

            self.assertEqual( out, out_expect )

    def tearDown(self):
        pass

if __name__ == '__main__':

    inouts = [
        ( ProgramInput( "1+1", [] ), ProgramOutput( "Result: 2\n", "", 0 ) ),
    ]

    program_path = sys.argv[1]
    unittest.main( argv = [sys.argv[0]] )
