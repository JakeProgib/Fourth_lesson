
first_list = ["яблоко","клубника","киви","груша"]
second_list = ["яблоко","киви","виноград"]
third_list=[]
if len(first_list)>len(second_list):
    for itm in second_list:
        for itm2 in first_list:
            if (itm==itm2) and (itm not in third_list):
                third_list.append(itm)
            else:continue
print(third_list)
