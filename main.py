# main.py

# --- Importy hypotez ---
from hypothesis.hypothesis import hypoteza1
from hypothesis.hypothesis2 import hypoteza2
from hypothesis.hypothesis3 import hypoteza3
from hypothesis.hypothesis4 import hypoteza4
from hypothesis.hypothesis5 import hypoteza5

# --- Import tříd ---
from chart import Chart
from сhiSquared import ChiSquaredAnalyzer
from anova import AnovaQ34

# --- Import otázek ---
from questions import *

def main():
    # seznam všech hypotéz
    hypotezy = [hypoteza1, hypoteza2, hypoteza3, hypoteza4, hypoteza5]

    for hyp in hypotezy:
        (
            multi_choice_numbers,
            multi_choice_lists,
            group_list,
            split_question,
            group_names,
            groups,
            names_for_grafs,
        ) = hyp()

        # Vykreslení grafů
        chart = Chart(
            multi_choice_numbers,
            multi_choice_lists,
            group_list,
            split_question,
            group_names,
            groups,
            names_for_grafs,
        )
        chart.run()

        # Anova
        anova = AnovaQ34(group_list, group_names)
        anova.run()
        anova.visualize()

        # Chi-squared analýza
        chi = ChiSquaredAnalyzer(group_list, group_names, multi_choice_numbers)
        results = chi.run()
        chi.visualize(results)


if __name__ == "__main__":
    main()

