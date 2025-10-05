import pandas as pd
import re

# Načtení dat z Excelu
df = pd.read_excel("Dotazník.xlsx")

# Očištění odpovědí: odstranění NaN, odstranění vícenásobných mezer, ořezání
extraversion_answer = df.loc[1:, 'Považujete se spíše za introverta nebo extroverta?'].dropna().apply(lambda x: re.sub(r'\s+', ' ', str(x)).strip()).tolist()
question_6  = df.loc[1:, 'Jak často pracujete na dálku?'].dropna().apply(lambda x: re.sub(r'\s+', ' ', str(x)).strip()).tolist()
question_7  = df.loc[1:, 'Jak hodnotíte svou produktivitu při práci na dálku ve srovnání s prací v kanceláři?'].dropna().apply(lambda x: re.sub(r'\s+', ' ', str(x)).strip()).tolist()
question_8  = df.loc[1:, 'Co vás nejvíce podporuje v udržení produktivity při práci na dálku?'].dropna().apply(lambda x: re.sub(r'\s+', ' ', str(x)).strip()).tolist()
question_9  = df.loc[1:, 'Jaké překážky nejvíce ovlivňují Vaši produktivitu při práci na dálku?'].dropna().apply(lambda x: re.sub(r'\s+', ' ', str(x)).strip()).tolist()
question_10 = df.loc[1:, 'Jak hodnotíte efektivitu komunikace s kolegy při práci na dálku?'].dropna().apply(lambda x: re.sub(r'\s+', ' ', str(x)).strip()).tolist()
question_11 = df.loc[1:, 'Jaké nástroje nejčastěji používáte pro komunikaci při práci na dálku? (vyberte všechny relevantní odpovědi)'].dropna().apply(lambda x: re.sub(r'\s+', ' ', str(x)).strip()).tolist()
question_12 = df.loc[1:, 'Jaký je podle Vás hlavní problém při komunikaci na dálku?'].dropna().apply(lambda x: re.sub(r'\s+', ' ', str(x)).strip()).tolist()
question_13 = df.loc[1:, ' Jak často pracujete v kanceláři?'].dropna().apply(lambda x: re.sub(r'\s+', ' ', str(x)).strip()).tolist()
question_14 = df.loc[1:, 'Jak hodnotíte svou produktivitu při práci v kanceláři?'].dropna().apply(lambda x: re.sub(r'\s+', ' ', str(x)).strip()).tolist()
question_15 = df.loc[1:, ' Jaké faktory Vám v kanceláři nejvíce pomáhají být produktivní?'].dropna().apply(lambda x: re.sub(r'\s+', ' ', str(x)).strip()).tolist()
question_16 = df.loc[1:, 'Jaké překážky nejvíce ovlivňují Vaši produktivitu při práci v kanceláři?\n'].dropna().apply(lambda x: re.sub(r'\s+', ' ', str(x)).strip()).tolist()
question_17 = df.loc[1:, 'Jak hodnotíte efektivitu komunikace s kolegy v kanceláři?\n'].dropna().apply(lambda x: re.sub(r'\s+', ' ', str(x)).strip()).tolist()
question_18 = df.loc[1:, 'Ve kterém prostředí cítíte větší motivaci k práci?'].dropna().apply(lambda x: re.sub(r'\s+', ' ', str(x)).strip()).tolist()
question_19 = df.loc[1:, 'Jaké faktory Vás nejvíce motivují při práci v obou prostředích?'].dropna().apply(lambda x: re.sub(r'\s+', ' ', str(x)).strip()).tolist()
question_20 = df.loc[1:, 'Jaké faktory Vás nejvíce motivují při práci v kanceláři?'].dropna().apply(lambda x: re.sub(r'\s+', ' ', str(x)).strip()).tolist()
question_21 = df.loc[1:, 'Jak hodnotíte rovnováhu mezi pracovním a osobním životem v obou prostředích?'].dropna().apply(lambda x: re.sub(r'\s+', ' ', str(x)).strip()).tolist()
question_22 = df.loc[1:, 'Jak hodnotíte rovnováhu mezi pracovním a osobním životem při práci v kanceláři?'].dropna().apply(lambda x: re.sub(r'\s+', ' ', str(x)).strip()).tolist()
question_23 = df.loc[1:, 'Máte při práci na dálku nebo v kanceláři větší stres?\n'].dropna().apply(lambda x: re.sub(r'\s+', ' ', str(x)).strip()).tolist()
question_24 = df.loc[1:, 'Jak byste hodnotili celkový vliv obou prostředí na kvalitu Vašeho pracovního života?'].dropna().apply(lambda x: re.sub(r'\s+', ' ', str(x)).strip()).tolist()
question_26 = df.loc[1:, 'Jak byste popsali svůj přístup k ostatním lidem?'].dropna().apply(lambda x: re.sub(r'\s+', ' ', str(x)).strip()).tolist()
question_27 = df.loc[1:, 'Jak byste hodnotili svůj přístup k povinnostem a organizaci práce?'].dropna().apply(lambda x: re.sub(r'\s+', ' ', str(x)).strip()).tolist()
question_28 = df.loc[1:, 'Jak obvykle reagujete na stresové situace?'].dropna().apply(lambda x: re.sub(r'\s+', ' ', str(x)).strip()).tolist()
question_29 = df.loc[1:, 'Jak se stavíte k novým myšlenkám a zkušenostem?'].dropna().apply(lambda x: re.sub(r'\s+', ' ', str(x)).strip()).tolist()
question_30 = df.loc[1:, 'Jaký typ úkolů Vás nejvíce motivuje?'].dropna().apply(lambda x: re.sub(r'\s+', ' ', str(x)).strip()).tolist()