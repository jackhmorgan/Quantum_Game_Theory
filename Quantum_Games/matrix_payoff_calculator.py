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