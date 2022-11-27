import pandas as pd
import numpy as np
titanic = pd.read_csv('C:/Users/Aftab Ali/Documents/python work/Titanic.csv')

survived_womens = titanic.loc[(titanic.Survived == 1) & (titanic.Sex == 'female')]
print(survived_womens)
print('woemens that survived =', np.shape(survived_womens))
total_womens = titanic.loc[(titanic.Sex == "female")]
total_children = titanic.loc[(titanic.Age < 16)]
total_boys = titanic.loc[(titanic.Age < 16) & (titanic.Sex =='male')]
total_boys_survived = titanic.loc[(titanic.Age < 16) & (titanic.Sex =='male') & (titanic.Survived == 1)]
total_girls = titanic.loc[(titanic.Age < 16) & (titanic.Sex =='female')]
total_girls_survived = titanic.loc[(titanic.Age < 16) & (titanic.Sex =='female') & (titanic.Survived == 1)]
print('total childrens =', np.shape(total_children))
print('total boys=', np.shape(total_boys))
print('total boys survived=', np.shape(total_boys_survived))
print('total boys survived=', np.shape(total_boys_survived))
print('total girls=', np.shape(total_girls))
print('total girls survived=', np.shape(total_girls_survived))
print('Total womens= ', np.shape(total_womens))


