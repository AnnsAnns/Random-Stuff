import random
import time

thomlegisstupid = ["Patching Binaries", "Loading XML^2*pi", "Finding Offsets", "Loading Patch", "Kernel Saving",
                   "Installing Matrix", "Collecting Flux", "Testing Kernel", "Checking Kernel",
                   "Downloading Kernel Data"]

while True:
    print(random.choice(thomlegisstupid))
    loading = 0
    while loading < 100:
        print(str(loading) + "%")
        time.sleep(60)
        loading += 1
    print("Done task - Checking for Errors ...")
    loading = 0
    while loading < 100:
        print(str(loading) + "%")
        time.sleep(20)
        loading += 1
