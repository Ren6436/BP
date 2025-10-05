from questions import *

def hypoteza5():
    # Multi-choice otázky
    multi_choice_numbers = [8, 19]
    multi_choice_lists = [question_8, question_19]

    # Jednotlivé otázky pro analýzu podle skupin
    h5_question_numbers = [30]
    h5_question = [question_30]

    # Skupiny
    curiously_index = [i for i, answer in enumerate(question_29) if answer == "Spíše zvědavě a otevřeně"]
    curiously = [curiously_index, h5_question_numbers, h5_question]

    conservatively_index = [i for i, answer in enumerate(question_29) if answer == "Spíše konzervativně a opatrně"]
    conservatively = [conservatively_index, h5_question_numbers, h5_question]

    komb_index = [i for i, answer in enumerate(question_29) if answer == "Kombinace obojího"]
    kombinace = [komb_index, h5_question_numbers, h5_question]

    # Celkový seznam skupin
    conscientiousness = [curiously, conservatively, kombinace]
    group_names = ["Curiously", "Conservatively", "Kombinace"]
    groups = ["Spíše zvědavě a otevřeně", "Spíše konzervativně a opatrně", "Kombinace obojího"]

    # Dělící otázka pro pie chart
    split_question = question_29

    # Název hypotézy pro grafy
    names_for_grafs = ["hypoteza 5"]

    return multi_choice_numbers, multi_choice_lists, conscientiousness, split_question, group_names, groups, names_for_grafs
