other_reserves_columns = [['res1', 'res2', 'res3', 'res4', 'res5'], ['n_res1', 'n_res2', 'n_res3', 'n_res4', 'n_res5']]
print(len(other_reserves_columns[0]))
for j in range(len(other_reserves_columns[0])):     #All reserve search
                if df_reserves[other_reserves_columns[0][j]][i] != '':
                    for k in range(len(other_reserves)):        #if held datas have new data, add number
                        if df_reserves[other_reserves_columns[0][j]][i] == other_reserves[k][0]:
                            other_reserves[k][1] = other_reserves[k][1] + df_reserves[other_reserves_columns[1][j]][i]
                            break
                        if k == len(other_reserves)-1:
                            other_reserves.append({df_reserves[other_reserves_columns[0][j]][i], df_reserves[other_reserves_columns[1][j]][i]})



print('-------------other_reserves-------------')
    print(other_reserves)
    print('-------------undone_other_reserves-------------')
    print(undone_other_reserves)
    print('-------------done_other_reserves-------------')
    print(done_other_reserves)