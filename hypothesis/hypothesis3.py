from questions import *

def hypoteza3():
    # Multi-choice otázky
    multi_choice_numbers = [8, 9, 16]
    multi_choice_lists = [question_8, question_9, question_16]

    # Jednotlivé otázky pro analýzu podle skupin
    h3_question_numbers =[7, 14]
    h3_question =[question_7, question_14]

    # Skupiny
    spontaneous_index = [i for i, answer in enumerate(question_27) if answer == "Spíše spontánní"]
    spontaneous = [spontaneous_index, h3_question_numbers, h3_question]

    systematic_index = [i for i, answer in enumerate(question_27) if answer == "Spíše systematický"]
    systematic = [systematic_index, h3_question_numbers, h3_question]

    komb_index = [i for i, answer in enumerate(question_27) if answer == "Kombinace obojího"]
    kombinace = [komb_index, h3_question_numbers, h3_question]

    # Celkový seznam skupin
    conscientiousness= [spontaneous, systematic, kombinace]
    group_names = ["Spontaneous", "Systematic", "Kombinace"]
    groups = ["Spíše spontánní", "Spíše systematický", "Kombinace obojího"]

    # Dělící otázka pro pie chart
    split_question = question_27

    # Název hypotézy pro grafy
    names_for_grafs = ["hypoteza 3"]

    return multi_choice_numbers, multi_choice_lists, conscientiousness, split_question, group_names, groups, names_for_grafs