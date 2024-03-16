### running the automation code:
#   run following commands in terminal of the workspace: /workspaces/ecs201a-assignment5-natalia-mrinali-3/workloads/array_sum
make
#   make naive-native
#   make naive-gem5
#   make chunking-native
#   make chunking-gem5
#   make res-race-opt-native
#   make res-race-opt-gem5
#   make chunking-res-race-opt-native
#   make chunking-res-race-opt-gem5
#   make block-race-opt-native
#   make block-race-opt-gem5
#   make all-opt-native
#   make all-opt-gem5

# chmod +x naive-native
# chmod +x chunking-native
# chmod +x res-race-opt-native
# chmod +x chunking-res-race-opt-native
# chmod +x block-race-opt-native
# chmod +x all-opt-native

# then run the following command in the terminal at: /workspaces/ecs201a-assignment5-natalia-mrinali-3
chmod +x run_hardware.sh
chmod +x run_simulation.sh
chmod +x automation.sh
./automation.sh


# once it is done running, all the output files will be set

# -----

# you can also try running the following commands in /workspaces/ecs201a-assignment5-natalia-mrinali-3
gem5 run.py

gem5 --outdir=testOut/ run.py

gem5 -re --outdir=myOutput/ run.py

# /workspaces/ecs201a-assignment5-natalia-mrinali-3/workloads/array_sum
# on codespaces, only use 1 or 2 threads; test more threads on real hardware :)
./naive-native 32768 1
./naive-native 32768 2
./chunking-native 32768 1
./chunking-native 32768 2
./res-race-opt-native 32768 1 
./res-race-opt-native 32768 2
./chunking-res-race-opt-native 32768 1 
./chunking-res-race-opt-native 32768 2
./block-race-opt-native 32768 1
./block-race-opt-native 32768 2
./all-opt-native 32768 1
./all-opt-native 32768 2