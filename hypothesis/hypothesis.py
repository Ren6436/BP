from questions import *

def hypoteza1():
    # Multi-choice otázky
    multi_choice_numbers = [15, 20]
    multi_choice_lists = [question_15, question_20]

    # Jednotlivé otázky pro analýzu podle skupin
    h1_question_numbers = [6, 10, 13, 17, 18, 30]
    h1_question = [question_6, question_10, question_13,question_17, question_18, question_30]

    # Skupiny
    introvert_index = [i for i, answer in enumerate(extraversion_answer) if answer == "Introvert"]
    introvert = [introvert_index, h1_question_numbers, h1_question]

    extrovert_index = [i for i, answer in enumerate(extraversion_answer) if answer == "Extrovert"]
    extravert = [extrovert_index, h1_question_numbers, h1_question]

    komb_index = [i for i, answer in enumerate(extraversion_answer) if answer == "Kombinace obojího"]
    kombinace = [komb_index, h1_question_numbers, h1_question]

    # Celkový seznam skupin
    extraverze = [introvert, extravert, kombinace]
    group_names = ["Introvert", "Extrovert", "Kombinace"]
    groups = ["Introvert", "Extrovert", "Kombinace obojího"]

    # Dělící otázka pro pie chart
    split_question = extraversion_answer

    # Název hypotézy pro grafy
    names_for_grafs = ["hypoteza_1"]

    return multi_choice_numbers, multi_choice_lists, extraverze, split_question, group_names, groups, names_for_grafs
