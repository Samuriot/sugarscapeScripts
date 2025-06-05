
# Sugarscape Disease Research - Scaling to Supercomputer

This README assumes that you have access to the Purdue ANVIL application.

This directory includes the scripts our group used when executing and planning our project.

script: A PYTHON script used to edit and produce varying JSON configuration files for the Sugarscape simulation to run. Additionally, the output of this file should return a SLURM submission script that can be sent onto the ANVIL ssh Linux server

save_batch.py: A PYTHON script used to sift through JSON log files and find the average for population, agentDiseaseDeaths, and sickAgentsPercentage. The averages are stored in its respective disease type as "average_log_<num>" where num is the number of diseases tested. This is run locally due to the smaller scale of the task.

plot.py: A PYTHON script used to plot data sifted through by save_batch.py via matplotlib. Plots are saved in .png files in each respective disease type and number. This is also run locally.

- flag parameters for all scripts mentioned above:
- first parameter: number of diseases you want to test
- second parameter: type of disease you would like to test
- "x": deadly disease (all malicious effects are set to [-5, 0] and [0, 5])
- "m": slightly modified disease (all malicious effects are set to [-1, 0] and [0, 1])
- "d": default disease (all malicious effects are set to [0,0])

prepare.sh: A BASH SHELL script that runs 7 instances of Sugarscape with varying numbers of diseases {5, 50} with each disease type. This file also creates submission scripts for each job and submits them via SLURM to ANVIL ssh Linux server

prepare_plots.sh: A BASH SHELL script that runs save_batch.py iteratively 21 times, one for each disease/starting number combination.

plot_average.sh: A BASH SHELL script that runs plot.py iteratively 21 times, producing 63 total plots.


**To run our research scripts: use "make research" command**\n\n
**To run our data plotting scripts: use "make plot" command**\n\n
**To clean the rest of the files, use "make clean" command**