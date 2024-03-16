# run.py:
# import workload
from workloads.array_sum_workload import NaiveArraySumWorkload
from workloads.array_sum_workload import ChunkingArraySumWorkload
from workloads.array_sum_workload import NoResultRaceArraySumWorkload
from workloads.array_sum_workload import ChunkingNoResultRaceArraySumWorkload
from workloads.array_sum_workload import NoCacheBlockRaceArraySumWorkload
from workloads.array_sum_workload import ChunkingNoBlockRaceArraySumWorkload

# import gem5 models 
from components.boards import HW5X86Board       # gem5 motherboard
from components.processors import HW5O3CPU
from components.cache_hierarchies import HW5MESITwoLevelCacheHierarchy
from components.memories import HW5DDR4

# import exit
from workloads.roi_manager import exit_event_handler

# import argparse
import argparse

# initialize argument parser
parser = argparse.ArgumentParser(description="Gem5 Configuration Script")
# add optional arguments
parser.add_argument("--cores", type=int, default=4, help="number of cores for simulation")
parser.add_argument("--algorithm", type=int, help="number of cores for simulation")
# parse command-line arguments
args = parser.parse_args()

# import simulator package 
from gem5.simulate.simulator import Simulator

# instantiate an object of each model
if __name__ == "__m5_main__":
    cpu = HW5O3CPU(num_cores=args.cores) # 1 core, 16 cores
    cache = HW5MESITwoLevelCacheHierarchy(xbar_latency=1)
    memory = HW5DDR4()
    board = HW5X86Board(clk_freq="2GHz", processor=cpu, cache_hierarchy=cache, memory=memory)
    
    # setting workload for simulation 
    workload = None
    # - create an object of the imported workload, we want to use this object for the software on specified hardware
    if args.algorithm == 1:
        workload = NaiveArraySumWorkload(32768, args.cores)
    elif args.algorithm == 2:
        workload = ChunkingArraySumWorkload(32768, args.cores)
    elif args.algorithm == 3:
        workload = NoResultRaceArraySumWorkload(32768, args.cores)
    elif args.algorithm == 4:
        workload = ChunkingNoResultRaceArraySumWorkload(32768, args.cores)
    elif args.algorithm == 5:
        workload = NoCacheBlockRaceArraySumWorkload(32768, args.cores)
    else:
        workload = ChunkingNoBlockRaceArraySumWorkload(32768, args.cores)

    # --> call set_workload fcn from HW5X86Board
    board.set_workload(workload)

    # create a simulator object 
    # specify the system to be simulated, what mode of simulation should be used
    # Syscall Emulation (SE) mode: fakes system calls - takes 0 time
    simulator = Simulator(board=board, full_system=False, on_exit_event=exit_event_handler)

    # tell gem5 to run simulation
    simulator.run()
    # print when done :)
    print("Finished simulation.")
