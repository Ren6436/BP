from questions import *

def hypoteza4():
    # Multi-choice otázky
    multi_choice_numbers = [9, 16]
    multi_choice_lists = [question_9, question_16]

    # Jednotlivé otázky pro analýzu podle skupin
    h4_question_numbers = [21, 22, 23, 24, 28]
    h4_question = [question_21, question_22, question_23, question_24, question_28]

    # Skupiny
    calmly_index = [i for i, answer in enumerate(question_28) if answer == "Spíše klidně a odolně"]
    calmly = [calmly_index, h4_question_numbers, h4_question]

    sensitively_index = [i for i, answer in enumerate(question_28) if answer == "Spíše citlivě a emotivně"]
    sensitively = [sensitively_index, h4_question_numbers, h4_question]

    komb_index = [i for i, answer in enumerate(question_28) if answer == "Kombinace obojího"]
    kombinace = [komb_index, h4_question_numbers, h4_question]

    # Celkový seznam skupin
    neuroticism = [calmly, sensitively, kombinace]
    group_names = ["Calmly", "Sensitively", "Kombinace"]
    groups = ["Spíše klidně a odolně", "Spíše citlivě a emotivně", "Kombinace obojího"]

    # Dělící otázka pro pie chart
    split_question = question_28

    # Název hypotézy pro grafy
    names_for_grafs = ["hypoteza 4"]

    return multi_choice_numbers, multi_choice_lists, neuroticism, split_question, group_names, groups, names_for_grafs




