from collections import Counter
import textwrap
import matplotlib.pyplot as plt

class Chart:
    """
    Chart:
      - vykreslí pie chart podle rozdělení skupin (split_question a self.groups)
      - pro každou skupinu spočítá nejčastější odpovědi z běžných otázek a multi-choice otázek
      - výsledky vykreslí do sloupcového grafu
    """

    def __init__(self,
                 multi_choice_numbers,
                 multi_choice_lists,
                 group_list,
                 split_question,
                 group_names,
                 groups,
                 names_for_grafs=None):
        # uložení všech vstupních dat do instance třídy
        self.multi_choice_numbers = list(multi_choice_numbers)
        self.multi_choice_lists = list(multi_choice_lists)
        self.group_list = list(group_list)
        self.split_question = split_question
        self.group_names = list(group_names)
        self.groups = list(groups)
        self.names_for_grafs = names_for_grafs if names_for_grafs is not None else []

    def plot_distribution(self, show=True):
        # spočítáme počet odpovědí pro každou skupinu
        counts = [sum(1 for answer in self.split_question if answer == answer_group) for answer_group in self.groups]
        total = len(self.split_question)
        percents = [round((c * 100) / total, 2) for c in counts]  # přepočet na procenta

        fig, ax = plt.subplots(dpi=150)
        # definice barev pro pie chart
        base_colors = ["#08306B", "#2171B5", "#6BAED6"]
        # pokud je více skupin než barev, cyklíme barvy
        colors = [base_colors[i % len(base_colors)] for i in range(len(self.groups))]
        ax.pie(
            percents,
            labels=self.groups,   # názvy skupin
            autopct='%1.2f%%',   # procenta uvnitř výsečí
            shadow=True,
            colors=colors
        )
        ax.set(aspect="equal", title=f"Rozdělení skupin — {self.names_for_grafs[0]}")
        if show:
            plt.show()
        return colors  # vrací barvy pro další použití

    def analyze_groups(self, colors, show=True):
        """
        Pro každou skupinu spočítá nejčastější odpovědi a vykreslí sloupcový graf.
        """
        for name, group in zip(self.group_names, self.group_list):
            idx_list = group[0]       # indexy respondentů v této skupině
            q_numbers = group[1]      # čísla otázek
            q_list = group[2]         # seznam odpovědí na otázky

            # --- Analýza multi-choice otázek ---
            top_multi_answers = []
            top_multi_counts = []
            for question_mc in self.multi_choice_lists:
                # získání odpovědí pro konkrétní skupinu
                answers = [question_mc[i] for i in idx_list if i < len(question_mc) and question_mc[i]]
                split_answers = []
                for ans in answers:
                    # rozdělíme odpovědi podle ';' a odstraníme mezery
                    split_answers.extend([a.strip() for a in ans.split(';')])
                if split_answers:
                    # nejčastější odpověď a její počet
                    top = Counter(split_answers).most_common(1)[0]
                    top_multi_answers.append(top[0])
                    top_multi_counts.append(top[1])
                else:
                    top_multi_answers.append("")
                    top_multi_counts.append(0)

            # --- Analýza běžných otázek ---
            top_answers = []
            top_counts = []
            for question_sg in q_list:
                answers = [question_sg[i] for i in idx_list if i < len(question_sg) and question_sg[i]]
                if answers:
                    top = Counter(answers).most_common(1)[0]
                    top_answers.append(top[0])
                    top_counts.append(top[1])
                else:
                    top_answers.append("")
                    top_counts.append(0)

            # --- Spojení výsledků pro graf ---
            all_numbers = list(q_numbers) + list(self.multi_choice_numbers)
            all_counts = top_counts + top_multi_counts
            all_answers = top_answers + top_multi_answers

            # --- Sloupcový graf ---
            fig, ax = plt.subplots(figsize=(10, 5), dpi=150)
            ax.bar([f"Q{n}" for n in all_numbers], all_counts, color=colors)

            # přidání textu nad sloupce (zalomení dlouhého textu)
            for i, txt in enumerate(all_answers):
                wrapped = "\n".join(textwrap.wrap(str(txt), 20))
                ax.text(i, all_counts[i], wrapped, ha='center', va='bottom', fontsize=5)

            # nastavení y-lim, aby graf nevypadl prázdný
            if all_counts:
                ax.set_ylim(0, max(all_counts) + 2)
            else:
                ax.set_ylim(0, 1)

            ax.set_ylabel('Počet odpovědí')
            ax.set_title(f'Nejčastější odpovědi — {name} (n={len(idx_list)})')
            plt.tight_layout()
            if show:
                plt.show()

    def run(self, show=True):
        """
        Spustí celou vizualizaci:
          1) vykreslí pie chart
          2) analyzuje a vykreslí odpovědi pro každou skupinu
        Vrací (colors, seznam všech čísel otázek z group_list)
        """
        colors = self.plot_distribution(show=show)
        self.analyze_groups(colors=colors, show=show)

        # sjednocení všech čísel otázek pro případ další analýzy
        question_numbers_union = sorted({n for g in self.group_list for n in g[1]})
        return colors, question_numbers_union
