import time
import sys

# Blank line for better output formatting
print()

# Integer to keep track of execution time 
crono: int = 0

while True:
    
	# Print the script ETA
    print(f"\rTestApp with Docker - ETA: {crono} seconds ", end="")
    
	# Update script ETA
    crono += 1
    
	# Force the immediate update of the printed line on the terminal
    sys.stdout.flush()
    
	# Wait one second
    time.sleep(1)
