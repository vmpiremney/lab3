def count_letters(text):
    letters_count = {char: 0 for char in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"}
    for char in text.lower():
        if char in letters_count:
            letters_count[char] += 1
    return letters_count

def calculate_frequency(letters_count):
    total_letters = sum(letters_count.values())
    frequency = {char: round(count / total_letters, 2) for char, count in letters_count.items()}
    return frequency

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

letters_count = count_letters(main_str)
letters_frequency = calculate_frequency(letters_count)

ordered_letters = []
for char in main_str.lower():
    if char in letters_frequency and char not in ordered_letters:
        ordered_letters.append(char)

for letter in ordered_letters:
    print(f"{letter}: {letters_frequency[letter]:.2f}")