def find_common_participants(group1, group2, delimiter=","):
    participants_1 = set(group1.split(delimiter))
    participants_2 = set(group2.split(delimiter))
    common_participants = participants_1.intersection(participants_2)
    return sorted(common_participants)

participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники:", common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, delimiter="|")
print("Общие участники с |:", common_participants)