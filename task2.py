workers = ["John", "Mike", "Tom"]
workers_salary = [10000, 20000, 30000]
workers_extras = ["8.75%", "3.69%", "10.25%"]
extra_dict = {worker: salary * float(extra[:-1]) / 100 for worker, salary, extra
              in zip(workers, workers_salary, workers_extras)}
print(extra_dict)
