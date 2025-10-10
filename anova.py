import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway
from questions import *

class AnovaQ34:
    def __init__(self, group_list, group_names):
        """
        ANOVA Q34 – porovnání počtu projektů mezi skupinami.
        Data se načítají přímo z questions.question_34.
        """
        self.question_34 = question_34
        self.group_list = group_list
        self.group_names = group_names
        self.results_df = None

    def _prepare_data(self):
        projects = []
        for x in self.question_34:
            try:
                projects.append(float(str(x).replace(',', '.')))
            except Exception:
                projects.append(None)

        max_index = max([max(g[0]) for g in self.group_list if g[0]]) if self.group_list else 0
        if len(projects) <= max_index:
            projects.extend([None] * (max_index + 1 - len(projects)))

        groups_data = []
        stats = []

        for name, group in zip(self.group_names, self.group_list):
            idxs = group[0]
            vals = [projects[i] for i in idxs if i < len(projects) and projects[i] is not None]
            groups_data.append(vals)

            stats.append({
                "Skupina": name,
                "n": len(vals),
                "Průměr": round(np.mean(vals), 2) if vals else np.nan,
                "SD": round(np.std(vals, ddof=1), 2) if len(vals) > 1 else np.nan
            })

        return groups_data, pd.DataFrame(stats)

    def run(self):
        groups_data, stats_df = self._prepare_data()
        valid_groups = [vals for vals in groups_data if len(vals) > 1]

        if len(valid_groups) >= 2:
            f_stat, p_value = f_oneway(*valid_groups)
            if p_value < 0.001:
                interpretace = "Velmi silně statisticky významný rozdíl (p < 0.001)"
            elif p_value < 0.05:
                interpretace = "Statisticky významný rozdíl (p < 0.05)"
            else:
                interpretace = "Statisticky nevýznamný rozdíl (p ≥ 0.05)"
        else:
            f_stat, p_value, interpretace = np.nan, np.nan, "Nedostatek dat pro ANOVA"

        # přidání řádku s výsledky ANOVY do tabulky
        stats_df.loc[len(stats_df)] = {
            "Skupina": " ANOVA výsledek",
            "n": "",
            "Průměr": f"F = {f_stat:.3f}" if not np.isnan(f_stat) else "",
            "SD": f"p = {p_value:.4f}" if not np.isnan(p_value) else ""
        }
        stats_df.loc[len(stats_df)] = {
            "Skupina": "Interpretace",
            "n": "",
            "Průměr": interpretace,
            "SD": ""
        }

        self.results_df = stats_df
        return stats_df

    def visualize(self, show=True):
        """
        Vykreslí výslednou tabulku ANOVA jako barevnou grafickou tabulku.
        """
        if self.results_df is None:
            raise ValueError("Nejprve je potřeba spustit `run()`")

        df = self.results_df.copy()

        # Převod číselných hodnot na float pro barevné mapování, text zůstane pro Skupina
        numeric_df = df.copy()
        for col in ['n', 'Průměr', 'SD']:
            numeric_df[col] = pd.to_numeric(numeric_df[col], errors='coerce')

        fig, ax = plt.subplots(figsize=(max(6, len(df.columns) * 1.5), max(4, len(df) * 0.6)), dpi=150)
        ax.axis('off')

        # Barevná mapa podle Průměru
        cmap = sns.light_palette("skyblue", as_cmap=True)

        table_data = []
        for i in range(len(df)):
            row = []
            for col in df.columns:
                val = df.iloc[i][col]
                if col in ['n', 'Průměr', 'SD'] and pd.notnull(numeric_df.iloc[i][col]):
                    # barevné pozadí
                    color = cmap((numeric_df.iloc[i][col] - numeric_df[col].min()) /
                                 (numeric_df[col].max() - numeric_df[col].min() + 1e-6))
                else:
                    color = 'white'
                row.append((val, color))
            table_data.append(row)

        # Vytvoření tabulky
        tbl = ax.table(cellText=[[cell[0] for cell in row] for row in table_data],
                       cellColours=[[cell[1] for cell in row] for row in table_data],
                       colLabels=df.columns,
                       cellLoc='center',
                       loc='center')
        tbl.auto_set_font_size(False)
        tbl.set_fontsize(8)
        tbl.auto_set_column_width(col=list(range(len(df.columns))))

        plt.tight_layout()
        if show:
            plt.show()