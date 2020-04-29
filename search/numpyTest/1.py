def Name_List():
    name_list_length = int(input())

    s_name_new = ''
    for i in range(name_list_length):
        name_old = input().split()[0]   ##咱也不会
      #这个条件可以不用，
        if name_old == 'WYS':
            s_name_new += 'KXZSMR'
        elif name_old == 'CQ':
            s_name_new += 'CHAIQIANG'
        elif name_old == 'LC':
            s_name_new += 'DRAGONNET'
        elif name_old in ['SYT', 'SSD', 'LSS', 'LYF']:
            s_name_new += 'STUDYFATHER'
        else:
            s_name_new += 'DENOMINATOR'


        s_name_new += '\n'
    print(s_name_new)
Name_List()



##########

