'''
Copyright 2025 Jack Morgan

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

import pandas as pd
import numpy as np


def matrix_payoff_calculator(results_df : pd.DataFrame,
                                               payoff_matrix : np.ndarray):
    payoff_df = pd.DataFrame(index=results_df.index)
    for col in results_df:
        payoff_df[col] = None
    
    for shot in results_df.iterrows():
        payoffs = payoff_matrix[tuple(shot[1].values)]
        for i, col_payoff in enumerate(payoff_df):
            payoff_df.loc[shot[0], col_payoff] = payoffs[i]

    return payoff_df