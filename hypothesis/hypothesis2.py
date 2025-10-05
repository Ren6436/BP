from questions import *

def hypoteza2():
    # Multi-choice otázky
    multi_choice_numbers = [15, 20]
    multi_choice_lists = [question_15, question_20]

    # Jednotlivé otázky pro analýzu podle skupin
    h2_question_numbers = [10, 17, 23]
    h2_question = [question_10, question_17, question_23]

    # Skupiny
    friendly_index = [i for i, answer in enumerate(question_26) if answer == "Spíše přátelský a vstřícný"]
    friendly = [friendly_index, h2_question_numbers, h2_question]

    critical_index = [i for i, answer in enumerate(question_26) if answer == "Spíše kritický a asertivní"]
    critical = [critical_index, h2_question_numbers, h2_question]

    komb_index = [i for i, answer in enumerate(question_26) if answer == "Kombinace obojího"]
    kombinace = [komb_index, h2_question_numbers, h2_question]

    # Celkový seznam skupin
    friendlys = [friendly, critical, kombinace]
    group_names = ["Friendly", "Critical", "Kombinace"]
    groups = ["Spíše přátelský a vstřícný", "Spíše kritický a asertivní", "Kombinace obojího"]

    # Dělící otázka pro pie chart
    split_question = question_26

    # Název hypotézy pro grafy
    names_for_grafs = ["hypoteza_2"]

    return multi_choice_numbers, multi_choice_lists, friendlys, split_question, group_names, groups, names_for_grafs
