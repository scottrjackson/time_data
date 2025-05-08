import time
import numpy as np
import math
import random
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

iterations = 10_000_000

start = time.process_time()
results = []
for _ in range(iterations):
    this_result = random.randint(1, 1000) ** 3 / math.pi # just a random calculation
    results.append(this_result)
stop = time.process_time()
print(f"This standard loop took {stop - start} seconds.")

start_comp = time.process_time()
comp_results = [random.randint(1, 1000) ** 3 / math.pi for _ in range(iterations)]
stop_comp = time.process_time()
print(f"The list comprehension version took {stop_comp - start_comp} seconds.")

start_numpy = time.process_time()
numpy_results = np.random.randint(1, 1000, iterations) ** 3 / math.pi
stop_numpy = time.process_time()
print(f"The numpy vectorized version took {stop_numpy - start_numpy} seconds.")

########################################
time_dictionary = {"method" : ["loop", "comprehension", "numpy"],
                   "time taken" : [stop - start, stop_comp - start_comp, stop_numpy - start_numpy]}
print(time_dictionary)

time_df = pd.DataFrame.from_dict(time_dictionary)
print(time_df)

sns.barplot(data = time_df, x = "method", y = "time taken")
plt.show()

sns.lineplot(data = time_df, x = "method", y = "time taken")
plt.show()
