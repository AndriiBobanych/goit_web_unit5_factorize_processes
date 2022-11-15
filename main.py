from typing import List
from time import time
from datetime import datetime
from multiprocessing import Pool, cpu_count
from concurrent.futures import ProcessPoolExecutor


def factorize(*numbers) -> List:
    final_numbers_list = []
    for number in numbers:
        result_for_number = []
        for num in range(1, number+1):
            if number % num == 0:
                result_for_number.append(num)
        final_numbers_list.append(result_for_number)
    return final_numbers_list


if __name__ == '__main__':
    test_numbers = (128, 255, 99999, 10651060, 123456789)

    total_cpu = cpu_count()
    print(f"We start the speed testing program")
    print(f"Processes can use the following amount of CPU: {total_cpu}\n")

    print("-----------------------------------------------------------------")
    start_time_1 = time()
    print(f"Simple counting process is started at {datetime.now()}")
    factorize(*test_numbers)
    end_time_1 = time()
    print(f"Simple counting process is finished at {datetime.now()}")
    total_time_1 = end_time_1 - start_time_1
    print(f"Total time for simple counting process is {round(total_time_1, 3)} seconds\n")

    print("-----------------------------------------------------------------")
    start_time_2 = time()
    print(f"Pool counting process is started at {datetime.now()}")
    with Pool(processes=total_cpu) as pool:
        pool.map(factorize, test_numbers)
        pool.close()
        pool.join()
    end_time_2 = time()
    print(f"Pool counting process is finished at {datetime.now()}")
    total_time_2 = end_time_2 - start_time_2
    print(f"Total time for pool counting process is {round(total_time_2, 3)} seconds\n")

    print("-----------------------------------------------------------------")
    start_time_3 = time()
    print(f"Concurrent futures counting process is started at {datetime.now()}")
    with ProcessPoolExecutor(max_workers=total_cpu) as executor:
        executor.map(factorize, test_numbers)
    end_time_3 = time()
    print(f"Concurrent futures counting process is finished at {datetime.now()}")
    total_time_3 = end_time_3 - start_time_3
    print(f"Total time for concurrent futures counting process is {round(total_time_3, 3)} seconds\n")


"""
--->>> Result of testing of the program
"""

'''
We start the speed testing program
Processes can use the following amount of CPU: 8

-----------------------------------------------------------------
Simple counting process is started at 2022-11-15 02:15:58.326122
Simple counting process is finished at 2022-11-15 02:16:06.749028
Total time for simple counting process is 8.423 seconds

-----------------------------------------------------------------
Pool counting process is started at 2022-11-15 02:16:06.749028
Pool counting process is finished at 2022-11-15 02:16:17.040762
Total time for pool counting process is 10.292 seconds

-----------------------------------------------------------------
Concurrent futures counting process is started at 2022-11-15 02:16:17.040762
Concurrent futures counting process is finished at 2022-11-15 02:16:26.790627
Total time for concurrent futures counting process is 9.75 seconds


Process finished with exit code 0
'''