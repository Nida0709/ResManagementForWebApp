    restext1 = []
    restext2 = []
    restext3 = []
    restext4 = []
    for i in range(len(df_reserves)):
        if df_reserves['date'][i] >= target_uni_date and df_reserves['date'][i] < target_uni_date * second_baked * 3600:
            text = '　 氏名 　：' + str(df_reserves['name'][i]) + '\n'\
                    + ' 電話番号 ：' + str(df_reserves['tell'][i]) + '\n'\
                    + '　 日付 　：' + str(df_reserves['date'][i]) + '\n'\
                    + '食パン(本)：' + str(df_reserves['n_hon'][i]) + '本' + '\n'\
                    + '食パン(斤)：' + str(df_reserves['n_kin'][i]) + '斤' + '\n'\
                    + '　 予約 　：' + '\n'\
                        + str(df_reserves['res1'][i]) + 'x' + str(df_reserves['n_res1'][i]) + '\n'\
                        + str(df_reserves['res2'][i]) + 'x' + str(df_reserves['n_res2'][i]) + '\n'\
                        + str(df_reserves['res3'][i]) + 'x' + str(df_reserves['n_res3'][i]) + '\n'\
                        + str(df_reserves['res4'][i]) + 'x' + str(df_reserves['n_res4'][i]) + '\n'\
                        + str(df_reserves['res5'][i]) + 'x' + str(df_reserves['n_res5'][i]) + '\n'\
                    + ' 伝達事項 ：' + str(df_reserves['other'][i])
            restext1.append(text)
        elif df_reserves['date'][i] >= target_uni_date * second_baked * 3600 and df_reserves['date'][i] < target_uni_date * third_baked * 3600:
            text = '　 氏名 　：' + str(df_reserves['name'][i]) + '\n'\
                    + ' 電話番号 ：' + str(df_reserves['tell'][i]) + '\n'\
                    + '　 日付 　：' + str(df_reserves['date'][i]) + '\n'\
                    + '食パン(本)：' + str(df_reserves['n_hon'][i]) + '本' + '\n'\
                    + '食パン(斤)：' + str(df_reserves['n_kin'][i]) + '斤' + '\n'\
                    + '　 予約 　：' + '\n'\
                        + str(df_reserves['res1'][i]) + 'x' + str(df_reserves['n_res1'][i]) + '\n'\
                        + str(df_reserves['res2'][i]) + 'x' + str(df_reserves['n_res2'][i]) + '\n'\
                        + str(df_reserves['res3'][i]) + 'x' + str(df_reserves['n_res3'][i]) + '\n'\
                        + str(df_reserves['res4'][i]) + 'x' + str(df_reserves['n_res4'][i]) + '\n'\
                        + str(df_reserves['res5'][i]) + 'x' + str(df_reserves['n_res5'][i]) + '\n'\
                    + ' 伝達事項 ：' + str(df_reserves['other'][i])
            restext2.append(text)
        elif df_reserves['date'][i] >= target_uni_date * third_baked * 3600 and df_reserves['date'][i] < target_uni_date * forth_baked * 3600:
            text = '　 氏名 　：' + str(df_reserves['name'][i]) + '\n'\
                    + ' 電話番号 ：' + str(df_reserves['tell'][i]) + '\n'\
                    + '　 日付 　：' + str(df_reserves['date'][i]) + '\n'\
                    + '食パン(本)：' + str(df_reserves['n_hon'][i]) + '本' + '\n'\
                    + '食パン(斤)：' + str(df_reserves['n_kin'][i]) + '斤' + '\n'\
                    + '　 予約 　：' + '\n'\
                        + str(df_reserves['res1'][i]) + 'x' + str(df_reserves['n_res1'][i]) + '\n'\
                        + str(df_reserves['res2'][i]) + 'x' + str(df_reserves['n_res2'][i]) + '\n'\
                        + str(df_reserves['res3'][i]) + 'x' + str(df_reserves['n_res3'][i]) + '\n'\
                        + str(df_reserves['res4'][i]) + 'x' + str(df_reserves['n_res4'][i]) + '\n'\
                        + str(df_reserves['res5'][i]) + 'x' + str(df_reserves['n_res5'][i]) + '\n'\
                    + ' 伝達事項 ：' + str(df_reserves['other'][i])
            restext3.append(text)
        elif df_reserves['date'][i] >= target_uni_date * forth_baked * 3600 and df_reserves['date'][i] < target_uni_date * tomorrow * 3600:
            text = '　 氏名 　：' + str(df_reserves['name'][i]) + '\n'\
                    + ' 電話番号 ：' + str(df_reserves['tell'][i]) + '\n'\
                    + '　 日付 　：' + str(df_reserves['date'][i]) + '\n'\
                    + '食パン(本)：' + str(df_reserves['n_hon'][i]) + '本' + '\n'\
                    + '食パン(斤)：' + str(df_reserves['n_kin'][i]) + '斤' + '\n'\
                    + '　 予約 　：' + '\n'\
                        + str(df_reserves['res1'][i]) + 'x' + str(df_reserves['n_res1'][i]) + '\n'\
                        + str(df_reserves['res2'][i]) + 'x' + str(df_reserves['n_res2'][i]) + '\n'\
                        + str(df_reserves['res3'][i]) + 'x' + str(df_reserves['n_res3'][i]) + '\n'\
                        + str(df_reserves['res4'][i]) + 'x' + str(df_reserves['n_res4'][i]) + '\n'\
                        + str(df_reserves['res5'][i]) + 'x' + str(df_reserves['n_res5'][i]) + '\n'\
                    + ' 伝達事項 ：' + str(df_reserves['other'][i])
            restext4.append(text)


    reserves1 = [{'content': restext1}]
    reserves2 = [{'content': restext2}]
    reserves3 = [{'content': restext3}]
    reserves4 = [{'content': restext4}]

    print(reserves1)
    print(reserves2)
    print(reserves3)
    print(reserves4)
    reserves2 = [{'content': "aaa"}]
