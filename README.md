# ISAIAH

Ion Simulation in AMBER for dIffusion Actions when Hydrated

"When you pass through the waters, I will be with you." -- Isaiah 43:2

A bash->slurm->python hybrid interface for benchmarking ion diffusion coefficients using AMBER MD package. 

Update 11/15/2021: How to calculate water exchange rate? 
Update 03/01/2022: Error handlings added for robustness. 

1. Finish steps 1~3 from the regular User Manual mentioned as below. 
2. Hop to WaterExchange directory. 
3. sbatch Ca.slm.
4. After Ca.slm job done, sbatch cpu.pbs. 
5. The water exchange count will be displayed at the end of WaterExchangeOut file. 

User Manual: 

1. Install AMBER20 following tutorials in this page: http://ambermd.org/. Or load AMBER module if using an HPC system with AMBER included. 

2. Slrum workload manager can be installed from https://slurm.schedmd.com/download.html. Most HPC systems should have Slurm built in already. 

3. Python 2.7.15 and above should fit it well. Anyway it is only used for plotting and numpy linear extrapolation. 

4. Once the three prerequisites above are met, modify the "input.in" file using the format below (example already provided):
   
   "(water model) (element name) (charge) (parameter set) (atomic number) (formula weight) (Rmin/2) (epsilon) (C4)".
   
   Rmin/2, epsilon and C4 values can be found in these publications (please see their citations for earlier water model parameters): 
   
      https://doi.org/10.1021/acs.jctc.0c00194
      
      https://doi.org/10.1021/acs.jctc.0c01320
      
      https://doi.org/10.1021/acs.jcim.0c01390
      
5. Run "sh ISAIAH.sh" to fire MD runs. One line of input will fire 80 jobs (4 box sizes with 20 duplicates at each box size), so please check your Slurm max workload before doing this. 

6. When Slurm says all jobs are done, run "sbatch ISAIAH.pbs" to fire one job to collect data in "test.out". 

7. Run "python ISAIAH.py" to get several final plots, different parameter sets of the same water/ion system will be plotted together. 
