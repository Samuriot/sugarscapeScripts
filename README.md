
# Sugarscape Disease Research - Scaling to Supercomputer

This README assumes that you have access to the Purdue ANVIL application.

This directory includes the scripts our group used when executing and planning our project.

script: A PYTHON script used to edit and produce varying JSON configuration files for the Sugarscape simulation to run. Additionally, the output of this file should return a SLURM submission script that can be sent onto the ANVIL ssh Linux server

- flag parameters for script:
- first parameter: number of diseases you want to test
- second parameter: type of disease you would like to test
- "x": deadly disease (all malicious effects are set to [-5, 0] and [0, 5])
- "m": slightly modified disease (all malicious effects are set to [-1, 0] and [0, 1])
- "d": default disease (all malicious effects are set to [0,0])

prepare.sh: A BASH SHELL script that runs 7 instances of Sugarscape with varying numbers of diseases {5, 50} with each disease type. This file also creates submission scripts for each job and submits them via SLURM to ANVIL ssh Linux server

**To run our research scripts: use "make research" command**
**To clean the rest of the files, use "make clean" command**
