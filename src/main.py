import debugpy
import time
debugpy.listen(("0.0.0.0", 5678))  # Listen for a debugger on port 5678
print("Waiting for debugger to attach...")
debugpy.wait_for_client()  # Blocks execution until debugger is attached

from mylib import say_hello

for i in range(20):
    time.sleep(1)
    say_hello("John", "Doe")