import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

def get_custom_dummies(items):
    human = []
    robot = []
    for idx, row in items.iterrows():
        if row['whoAmI'] == 'human':
            human.append(1)
            robot.append(0)
        else:
            human.append(0)
            robot.append(1)
    return {'whoAmI_human': human, 'whoAmI_robot': robot}


print(pd.DataFrame(get_custom_dummies(data)).head())
