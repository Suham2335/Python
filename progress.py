
from tqdm import tqdm
import time

for i in tqdm(range(20), desc="Completing Study Tasks"):
    time.sleep(0.1)

print("All 20 tasks completed!")
