#!/bin/bash

./script 5 d > submit5d
./script 10 d > submit10d
./script 15 d > submit15d
./script 20 d > submit20d
./script 25 d > submit25d
./script 40 d > submit40d
./script 50 d > submit50d

./script 5 m > submit5m
./script 10 m > submit10m
./script 15 m > submit15m
./script 20 m > submit20m
./script 25 m > submit25m
./script 40 m > submit40m
./script 50 m > submit50m

./script 5 x > submit5x
./script 10 x > submit10x
./script 15 x > submit15x
./script 20 x > submit20x
./script 25 x > submit25x
./script 40 x > submit40x
./script 50 x > submit50x

sbatch --nodes=1 --ntasks=10 submit5d
sbatch --nodes=1 --ntasks=10 submit10d
sbatch --nodes=1 --ntasks=10 submit15d
sbatch --nodes=1 --ntasks=10 submit20d
sbatch --nodes=1 --ntasks=10 submit25d
sbatch --nodes=1 --ntasks=10 submit40d
sbatch --nodes=1 --ntasks=10 submit50d

sbatch --nodes=1 --ntasks=10 submit5m
sbatch --nodes=1 --ntasks=10 submit10m
sbatch --nodes=1 --ntasks=10 submit15m
sbatch --nodes=1 --ntasks=10 submit20m
sbatch --nodes=1 --ntasks=10 submit25m
sbatch --nodes=1 --ntasks=10 submit40m
sbatch --nodes=1 --ntasks=10 submit50m

sbatch --nodes=1 --ntasks=10 submit5x
sbatch --nodes=1 --ntasks=10 submit10x
sbatch --nodes=1 --ntasks=10 submit15x
sbatch --nodes=1 --ntasks=10 submit20x
sbatch --nodes=1 --ntasks=10 submit25x
sbatch --nodes=1 --ntasks=10 submit40x
sbatch --nodes=1 --ntasks=10 submit50x