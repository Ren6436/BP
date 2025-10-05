from collections import Counter
import seaborn as sns
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt
import pandas as pd

from questions import *
import questions


class ChiSquaredAnalyzer:
    """
    ChiSquaredAnalyzer: provádí χ² testy pro otázky definované v modulu `questions`.
    """

    def __init__(self, group_list, group_names, multi_choice_numbers):
        # uloží základní parametry třídy
        self.group_list = group_list
        self.group_names = group_names
        self.multi_choice_numbers = multi_choice_numbers

    def _get_question_var(self, qnum):

        return getattr(questions, f"question_{qnum}", None)

    def run(self, question_numbers=None):
        results = {}

        # sjednocení všech otázek
        if question_numbers is None:
            question_numbers = sorted({n for g in self.group_list for n in g[1]} | set(self.multi_choice_numbers))

        # projdeme každou otázku zvlášť
        for qnum in question_numbers:
            q_var = self._get_question_var(qnum)
            if q_var is None:
                print(f"Warning: question_{qnum} not found in questions module, skipping.")
                continue

            data = {}         # zde bude počet odpovědí pro každou skupinu
            all_answers = []  # všechny odpovědi napříč skupinami

            # projdeme všechny skupiny
            for name, group in zip(self.group_names, self.group_list):
                idx_list = group[0]
                answers = [q_var[i] for i in idx_list if i < len(q_var) and q_var[i]]
                answers = [a.strip() for a in answers if isinstance(a, str)]

                # pokud je to multi-choice otázka, rozdělíme odpovědi podle ';'
                if qnum in self.multi_choice_numbers:
                    split_answers = []
                    for ans in answers:
                        split_answers.extend([a.strip() for a in ans.split(';') if a.strip()])
                    data[name] = Counter(split_answers)  # spočítáme četnosti
                    all_answers.extend(split_answers)
                else:
                    # u single-choice bereme odpověď jako jeden celek
                    data[name] = Counter(answers)
                    all_answers.extend(answers)

            # --- U multi-choice otázek omezíme počet kategorií na 4 nejčastější celkově ---
            if qnum in self.multi_choice_numbers and all_answers:
                top4 = [a for a, _ in Counter(all_answers).most_common(4)]
                for name in data:
                    filtered = {k: v for k, v in data[name].items() if k in top4}
                    for ans in top4:
                        if ans not in filtered:
                            filtered[ans] = 0
                    data[name] = Counter(filtered)

            # --- Kontingenční tabulka (řádky = skupiny, sloupce = odpovědi) ---
            df = pd.DataFrame(data).fillna(0).astype(int).T

            # pokud existuje jen jedna kategorie → nelze provést χ² test
            if df.shape[1] < 2:
                print(f"Q{qnum}: jen {df.shape[1]} kategorie → χ² přeskočeno")
                continue

            # χ² test nezávislosti
            try:
                chi2, p, dof, expected = chi2_contingency(df)
            except Exception as e:
                print(f"Q{qnum}: chi2_contingency selhalo: {e}")
                continue

            # očekávané četnosti z testu
            expected_df = pd.DataFrame(expected, index=df.index, columns=df.columns)
            # spočítáme počet buněk s nízkou očekávanou četností
            low_expected = (expected < 5).sum().sum()
            warn_msg = ""
            if low_expected > 0:
                warn_msg = f" (Warning: {low_expected} buňěk s očekávanou frekvencí < 5 — průkaznost χ² může být omezená)"

            # uložíme výsledek dané otázky
            results[qnum] = {
                "table": df,          # kontingenční tabulka
                "chi2": chi2,         # hodnota χ²
                "p_value": p,         # p-hodnota
                "dof": dof,           # stupně volnosti
                "expected": expected_df,
                "warn": warn_msg
            }

        return results

    def visualize(self, results, show=True):
        """
        Vykreslí výsledné kontingenční tabulky jako heatmapy (1 graf na otázku).
        """
        for qnum, res in results.items():
            df = res["table"]

            # velikost grafu závisí na počtu odpovědí a skupin
            fig, ax = plt.subplots(figsize=(max(6, len(df.columns) * 1.2), max(4, len(df) * 0.6)), dpi=150)
            ax.set_title(f"Q{qnum} — Chi-squared Crosstab", fontsize=10, pad=15)

            # případné varování o nízkých očekávaných hodnotách
            warn = res.get("warn", "")
            if warn:
                ax.text(0.5, 1.02, warn, ha="center", va="bottom", fontsize=5, transform=ax.transAxes)

            # heatmapa samotné kontingenční tabulky
            sns.heatmap(df, annot=True, fmt='d', cmap="Blues", cbar=False,
                        linewidths=0.5, ax=ax, annot_kws={"fontsize": 5, "va": "bottom"})

            # úpravy popisků
            ax.set_xlabel("")
            ax.set_ylabel("")
            plt.xticks(rotation=45, ha='right', fontsize=7)
            plt.yticks(rotation=0, fontsize=7)

            # úprava rozložení a vykreslení
            plt.tight_layout()
            if show:
                plt.show()
