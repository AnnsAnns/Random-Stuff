import time
import random

thomlegisstupid = ["Patching Binaries", "Loading XML^2*pi", "Finding Offsets", "Loading Patch", "Kernel Saving", "Installing Matrix", "Collecting Flux", "Testing Kernel", "Checking Kernel", "Downloading Kernel Data"]

while True:
    print(random.choice(thomlegisstupid))
    Loading = 0
    while Loading != 100:
        print(str(Loading) + "%")
        time.sleep(60)
        Loading = Loading + 1
    print("Done task - Checking for Errors ...")
    Loading = 0
    while Loading != 100:
        print(str(Loading) + "%")
        time.sleep(20)
        Loading = Loading + 1