# automation.sh:
#!/bin/bash

echo "running hardware experiment"
# ./workspaces/ecs201a-assignment5-natalia-mrinali-3/run_hardware.sh
 ./run_hardware.sh

echo "running gem5 experiment"
# ./workspaces/ecs201a-assignment5-natalia-mrinali-3/run_simulation.sh
 ./run_simulation.sh

echo "done"