
# coding: utf-8

# In[8]:

import os
import platform

if platform.system() == 'Windows':
    home = 'C:/Users/Jake/'
else:
    home = '~/'

os.chdir(home + 'Dropbox/Drive/quantified_self')

