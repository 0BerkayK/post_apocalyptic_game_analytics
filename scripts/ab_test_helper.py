# scripts/ab_test_helper.py

import pandas as pd
from scipy.stats import ttest_ind, chi2_contingency, mannwhitneyu


def calculate_metric(df, metric_col, group_col="group"):
    """Control ve Treatment grubu için verilen metrik ortalamasını hesaplar."""
    return df.groupby(group_col)[metric_col].mean().reset_index()


def t_test(df, metric_col, group_col="group"):
    """Control ve Treatment grubu için bağımsız örneklem t-testi uygular."""
    control = df[df[group_col] == "control"][metric_col].dropna()
    treatment = df[df[group_col] == "treatment"][metric_col].dropna()

    t_stat, p_value = ttest_ind(treatment, control, equal_var=False)
    return {"t_stat": t_stat, "p_value": p_value}


def mann_whitney_test(df, metric_col, group_col="group"):
    """Control ve Treatment grubu için non-parametrik Mann-Whitney U testi uygular."""
    control = df[df[group_col] == "control"][metric_col].dropna()
    treatment = df[df[group_col] == "treatment"][metric_col].dropna()

    u_stat, p_value = mannwhitneyu(treatment, control, alternative="two-sided")
    return {"u_stat": u_stat, "p_value": p_value}


def chi_square_test(df, event_col, group_col="group"):
    """Categorical dönüşüm olayları için chi-squared testi uygular."""
    contingency_table = pd.crosstab(df[group_col], df[event_col])
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    return {"chi2": chi2, "p_value": p, "dof": dof}


def summarize_test_result(test_result, alpha=0.05):
    """Test sonuçlarını yorumlayan kısa bir özet döner."""
    significant = test_result["p_value"] < alpha
    return f"p-value: {test_result['p_value']:.4f} → {'Significant' if significant else 'Not significant'} (α = {alpha})"
