import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway
from questions import *

class AnovaQ34:
    def __init__(self, group_list, group_names):
        """
        Inicializace ANOVA třídy.

        Parameters
        ----------
        group_list : list
            Seznam skupin, každá skupina obsahuje indexy respondentů.
        group_names : list
            Názvy skupin pro zobrazení v tabulce.
        """
        self.question_34 = question_34  # data pro otázku 34 z modulu questions
        self.group_list = group_list
        self.group_names = group_names
        self.results_df = None  # sem uložíme výslednou tabulku po run()

    def _prepare_data(self):
        """
        Převod odpovědí na čísla a příprava základní statistiky pro jednotlivé skupiny.

        Returns
        -------
        groups_data : list of list
            Seznam hodnot pro každou skupinu, pro ANOVA test.
        stats_df : pandas.DataFrame
            DataFrame se základními statistikami: počet, průměr, SD.
        """
        projects = []
        # Převod odpovědí na float, chybějící hodnoty jako None
        for x in self.question_34:
            try:
                projects.append(float(str(x).replace(',', '.')))
            except Exception:
                projects.append(None)

        # Doplnění seznamu, aby odpovídal maximálnímu indexu ve skupinách
        max_index = max([max(g[0]) for g in self.group_list if g[0]]) if self.group_list else 0
        if len(projects) <= max_index:
            projects.extend([None] * (max_index + 1 - len(projects)))

        groups_data = []  # seznam pro ANOVA
        stats = []        # seznam pro tabulku statistik

        # Procházení jednotlivých skupin a výpočet základních statistik
        for name, group in zip(self.group_names, self.group_list):
            idxs = group[0]  # indexy respondentů ve skupině
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
        """
        Spustí ANOVA test a vytvoří výslednou tabulku statistik.
        Tabulka obsahuje počet, průměr a SD pro každou skupinu,
        a také řádky s F-statistikou a interpretací.

        Returns
        -------
        pandas.DataFrame
            Výsledná tabulka pro vizualizaci.
        """
        groups_data, stats_df = self._prepare_data()
        valid_groups = [vals for vals in groups_data if len(vals) > 1]

        # ANOVA pouze pokud jsou alespoň 2 skupiny s platnými hodnotami
        if len(valid_groups) >= 2:
            f_stat, p_value = f_oneway(*valid_groups)
            # interpretace podle p-value
            if p_value < 0.001:
                interpretace = "Velmi silně statisticky významný rozdíl (p < 0.001)"
            elif p_value < 0.05:
                interpretace = "Statisticky významný rozdíl (p < 0.05)"
            else:
                interpretace = "Statisticky nevýznamný rozdíl (p ≥ 0.05)"
        else:
            f_stat, p_value, interpretace = np.nan, np.nan, "Nedostatek dat pro ANOVA"

        # Přidání řádku s F-statistikou a interpretací do tabulky
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

        Parameters
        ----------
        show : bool, default True
            Jestli zobrazit tabulku ihned.
        """
        if self.results_df is None:
            raise ValueError("Nejprve je potřeba spustit `run()`")

        df = self.results_df.copy()

        # Převod číselných sloupců pro barevné mapování
        numeric_df = df.copy()
        for col in ['n', 'Průměr', 'SD']:
            numeric_df[col] = pd.to_numeric(numeric_df[col], errors='coerce')

        # Nastavení figure a ax pro tabulku
        fig, ax = plt.subplots(figsize=(max(6, len(df.columns) * 1.5),
                                        max(4, len(df) * 0.6)), dpi=150)
        ax.axis('off')  # odstraníme osy

        # Barevná mapa pro hodnoty
        cmap = sns.light_palette("skyblue", as_cmap=True)

        table_data = []
        for i in range(len(df)):
            row = []
            for col in df.columns:
                val = df.iloc[i][col]
                # barevně pouze číselné sloupce
                if col in ['n', 'Průměr', 'SD'] and pd.notnull(numeric_df.iloc[i][col]):
                    # normalizace hodnot pro mapování do cmap
                    color = cmap((numeric_df.iloc[i][col] - numeric_df[col].min()) /
                                 (numeric_df[col].max() - numeric_df[col].min() + 1e-6))
                else:
                    color = 'white'  # textové buňky bílé
                row.append((val, color))
            table_data.append(row)

        # Vytvoření tabulky
        tbl = ax.table(cellText=[[cell[0] for cell in row] for row in table_data],
                       cellColours=[[cell[1] for cell in row] for row in table_data],
                       colLabels=df.columns,
                       cellLoc='center',
                       loc='center')

        # Nastavení fontu a velikosti sloupců
        tbl.auto_set_font_size(False)
        tbl.set_fontsize(8)
        tbl.auto_set_column_width(col=list(range(len(df.columns))))

        plt.tight_layout()
        if show:
            plt.show()
