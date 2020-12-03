
###1. Optimizers
The most commonly used optimizers are 
COBYLA
L_BFGS_B
SLSQP
SPSA

###2. Qubit mapping
There are several different mappings for your qubit Hamiltonian, 
parity
bravyi_kitaev
jordan_wigner
which in some cases can allow you to further reduce the problem size.


### 3. Initial state
initial_state = Zero(qubitOp.num_qubits)
initial_state = HartreeFock(qubitOp.num_qubits, num_spin_orbitals, num_particles, map_type, qubit_reduction)

###4. Parameterized circuit
There are different choices you can make on the form of variational forms of your parameterized circuit.
UCCSD_var_form = UCCSD(num_qubits, depth=depth, num_orbitals=num_spin_orbitals, num_particles=num_particles)
RY_var_form = RY(num_qubits, depth=depth)
RYRZ_var_form = RYRZ(num_qubits, depth=depth)

###5. Simulation backend
There are different simulation backends that you can use to perform your simulation
backend = BasicAer.get_backend('statevector_simulator')
backend=Aer.get_backend('qasm_simulator')
swaprz_var_form = SwapRZ(num_qubits, depth=depth)
