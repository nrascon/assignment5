# run_hardware.sh:
#!/bin/bash

benchmarks=(
    "/workspaces/assignment5/workloads/array-sum/naive-native"
    "/workspaces/assignment5/workloads/array-sum/chunking-native"
    "/workspaces/assignment5/workloads/array-sum/res-race-opt-native"
    "/workspaces/assignment5/workloads/array-sum/chunking-res-race-opt-native"
    "/workspaces/assignment5/workloads/array-sum/block-race-opt-native"
    "/workspaces/assignment5/workloads/array-sum/all-opt-native"
)

for file in "${benchmarks[@]}"
do 
    for i in 1 2
    do
        for j in 1 2 3 4 5 6                                                                               
        do
            /workspaces/assignment5/run_simulation.sh "$file" "$i" "$j" > "${j}-algorithm-${i}-cores-output.txt"    
        done
    done
done