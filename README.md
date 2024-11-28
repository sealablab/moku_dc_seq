# GHDL project template

A template for RTL design project using GHDL.

The directories in the project (and the rule of thumb for each) are:

* source: synthesizable files.
* sim: non-synthesizable files for simulations/testbenches.
* mock: mock files, e.g. mocking a sensor (can be synthesizable).
* in: input files for testbenches, e.g. *.csv*.
* out: output files from testbenches, e.g. *.csv* and *.ghw*.
* .cache: work folder.

The Makefile recursively analyses, elaborates and executes each file accordingly.

For the Makefile options, do ``make help``.

The example code provided was taken from 
[VHDL-guide - testbench](https://vhdlguide.readthedocs.io/en/latest/vhdl/testbench.html)
solely to illustrate this template.

You can undo one commit to clear the example code and remove this README.md.

Tip:
Compile and install [GHDL with LLVM backend and IEEE library](https://ghdl.github.io/ghdl/development/building/LLVM.html).

License: [The Unlicense](https://unlicense.org/)
