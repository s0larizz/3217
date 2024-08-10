latin_dict = {
            "EXCELIANTA": "Mükemmelik.",
            "PULCHRITUDO": "Güzellik.",
            "ANIMA": "Ruh.",
            "PARENTES": "Ebeveynler.",
            "TERROR": "Panik.",
            }
word = input("Türkçesini bilmek istediğiniz kelimeyi yazın.")
if word in latin_dict.keys():
    print(latin_dict[word])
else:
    print("Bu kelime, sözlükte mevcut değil.")
