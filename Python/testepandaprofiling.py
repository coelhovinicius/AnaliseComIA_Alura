# -*- coding: utf-8 -*-
"""TestePandaProfiling.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hPNy3iMsdZ4WJxXCkNyTpY5wjlouMRHh
"""

import pandas as pd

dados = pd.read_csv('/content/Dados_imersao - Dados.csv')
dados.head()

!pip install pandas-profiling

import pandas_profiling

dados.profile_report()

