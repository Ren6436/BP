from collections import Counter
import textwrap
from questions import *
import random


def run_hypothesis2(plt, cm, split_question, groups, questions_dict, multi_questions=None, title=""):
    """
    Obecná funkce pro spuštění hypotézy.
    - split_question: třídicí otázka (list odpovědí)
    - groups: seznam hodnot (odpovědí), podle kterých rozdělíme respondenty
    - questions_dict: dict { group: ([čísla otázek], [listy odpovědí]) }
    - multi_questions: volitelné [(číslo, list)], pokud má otázka více odpovědí oddělených ";"
    """

    # ----------------------------
    # Koláčový graf rozložení skupin
    # ----------------------------
    counts = [sum(1 for v in split_question if v == g) for g in groups]
    total = len(split_question)
    percents = [round((c * 100) / total, 2) for c in counts]

    fig, ax = plt.subplots()
    colors = [(random.random(), random.random(), random.random()) for _ in range(len(groups))]
    ax.pie(
        percents,
        labels=groups,
        autopct='%1.2f%%',
        shadow=True,
        colors=colors
    )
    ax.set(aspect="equal", title=title)
    plt.show()

    # ----------------------------
    # Pomocná funkce: analyzuj skupinu
    # ----------------------------
    def analyze_group(indices, questions, question_numbers, multi_lists=None, multi_numbers=None, subtitle=""):
        top_answers, top_counts = [], []

        # single odpovědi
        for q in questions:
            ans_list = [q[i] for i in indices if q[i]]
            if ans_list:
                top = Counter(ans_list).most_common(1)[0]
                top_answers.append(top[0])
                top_counts.append(top[1])
            else:
                top_answers.append("")
                top_counts.append(0)

        # multi odpovědi
        if multi_lists and multi_numbers:
            for q_idx, q in enumerate(multi_lists):
                counts = Counter()
                for i in indices:
                    if q[i]:
                        parts = [x.strip() for x in q[i].split(';')]
                        counts.update(parts)
                if counts:
                    top_answer, top_count = counts.most_common(1)[0]
                    top_answers.append(top_answer)
                    top_counts.append(top_count)
                else:
                    top_answers.append("")
                    top_counts.append(0)
            question_numbers = question_numbers + list(multi_numbers)

        # graf
        fig_width = max(8, len(question_numbers) * 1.2)
        max_lines = max([len(textwrap.wrap(txt, 20)) for txt in top_answers]) if top_answers else 1
        y_buffer = max_lines * 0.5
        y_max = max(top_counts) + y_buffer if top_counts else 1

        fig, ax = plt.subplots(figsize=(fig_width, 6))
        colors = [(random.random(), random.random(), random.random()) for _ in question_numbers]
        bar_container = ax.bar([f"Q{n}" for n in question_numbers], top_counts, color=colors)
        wrapped_answers = ["\n".join(textwrap.wrap(txt, 20)) for txt in top_answers]

        ax.bar_label(bar_container, labels=wrapped_answers, label_type='edge', fontsize=8)

        ax.set_ylabel('Počet odpovědí')
        ax.set_title(subtitle)
        ax.set_ylim(0, y_max)

        plt.show()

    # ----------------------------
    # Pro každou skupinu spustíme graf
    # ----------------------------
    for g in groups:
        indices = [i for i, v in enumerate(split_question) if v == g]
        if not indices:  # pokud žádný respondent, přeskočíme
            continue

        q_nums, q_lists = questions_dict[g]
        multi_nums, multi_lists = [], []
        if multi_questions:
            multi_nums, multi_lists = zip(*multi_questions)
        analyze_group(
            indices,
            q_lists,
            q_nums,
            multi_lists,
            multi_nums,
            subtitle=f"Nejčastější odpovědi – {g}"
        )

def run_hypotheses2(plt, cm):

        # H3: Svědomitost
    run_hypothesis2(
        plt, cm,
        split_question=question_27,
        groups=["Spíše spontánní", "Spíše systematický", "Kombinace obojího"],
        questions_dict={
            g: ([7, 8, 9, 14, 15, 16], [question_7, question_8, question_9,
                                        question_14, question_15, question_16]) for g in
            ["Spíše spontánní", "Spíše systematický", "Kombinace obojího"]
        },
        multi_questions=[(8, question_8), (9, question_9), (15, question_15), (16, question_16)],
        title="Hypotéza 3 – Svědomitost"
    )



    # H5: Otevřenost
    run_hypothesis2(
        plt, cm,
        split_question=question_29,
        groups=["Spíše zvědavě a otevřeně", "Spíše konzervativně a opatrně", "Kombinace obojího"],
        questions_dict={
            g: ([12, 30], [question_12, question_30]) for g in
            ["Spíše zvědavě a otevřeně", "Spíše konzervativně a opatrně", "Kombinace obojího"]
        },
        multi_questions=[(12, question_12)],
        title="Hypotéza 5 – Otevřenost"
    )
