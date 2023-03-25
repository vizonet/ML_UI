import pandas as pd
from mlearn import models, models_calc
from front import test_data


x = pd.DataFrame([
    test_data[
        list(test_data.keys())[0]
    ]
]).iloc[0, :4]

y, metrics = models_calc(x)

print(f'y = {y} \n metrics = {metrics}')
