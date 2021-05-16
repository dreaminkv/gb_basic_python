import os

folder = r'C:\Users\inkve\Desktop\Tolstov_Mikhail_dz_6'
py_files = [item
            for item in os.listdir(folder)
            if item.lower().endswith('.py')]
print(py_files)
