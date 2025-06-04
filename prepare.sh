#!/bin/bash

./script 5 > submit5
./script 10 > submit10
./script 15 > submit15
./script 20 > submit20
./script 25 > submit25
./script 40 > submit40
./script 50 > submit50

sbatch --nodes=1 --ntasks=10 submit5
sbatch --nodes=1 --ntasks=10 submit10
sbatch --nodes=1 --ntasks=10 submit15
sbatch --nodes=1 --ntasks=10 submit20
sbatch --nodes=1 --ntasks=10 submit25
sbatch --nodes=1 --ntasks=10 submit40
sbatch --nodes=1 --ntasks=10 submit50