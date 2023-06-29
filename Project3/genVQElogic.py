import sys

file      = open(sys.argv[1])
pauli_str = file.readline().strip()
# print(pauli_str)
num_regis = len(pauli_str)

with open('output.qasm', 'w') as output:
    output.write('OPENQASM 2.0;\n')
    output.write('include "qelib1.inc";\n')
    output.write(f'qreg q[{num_regis}];\n')
    output.write(f'creg c[{num_regis}];\n')

    for i in range(num_regis):
        if pauli_str[i] == 'X':
            output.write(f'h q[{i}];\n')
        elif pauli_str[i] == 'Y':
            output.write(f'h q[{i}];\n')
            output.write(f'sdg q[{i}];\n')

    prev = None
    for i in range(num_regis - 1, -1, -1):
        if pauli_str[i] != 'I':
            if prev != None:
                output.write(f'cx q[{prev}],q[{i}];\n')
            prev = i

    output.write(f'rz(pi/3) q[{prev}];\n')

    prev = None
    for i in range(num_regis):
        if pauli_str[i] != 'I':
            if prev != None:
                output.write(f'cx q[{i}],q[{prev}];\n')
            prev = i

    for i in range(num_regis - 1, -1, -1):
        if pauli_str[i] == 'X':
            output.write(f'h q[{i}];\n')
        elif pauli_str[i] == 'Y':
            output.write(f's q[{i}];\n')
            output.write(f'h q[{i}];\n')

    for i in range(num_regis):
        if pauli_str[i] != 'I':
            output.write(f'measure q[{i}] -> c[{i}];\n')
