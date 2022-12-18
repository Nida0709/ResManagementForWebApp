def makesentence(i, df_reservers):
    text = '　 氏名 　：' + df_reserves['name'][i] + '\n'\
            + ' 電話番号 ：' + df_reserves['tell'][i] + '\n'\
            + '　 日付 　：' + df_reserves['date'][i] + '\n'\
            + '食パン(本)：' + df_reserves['n_hon'][i] + '本' + '\n'\
            + '食パン(斤)：' + df_reserves['n_kin'][i] + '斤' + '\n'\
            + '　 予約 　：' + '\n'\
                + df_reserves['res1'][i] + 'x' + df_reserves['n_res1'][i] '\n'\
                + df_reserves['res2'][i] + 'x' + df_reserves['n_res2'][i] '\n'\
                + df_reserves['res3'][i] + 'x' + df_reserves['n_res3'][i] '\n'\
                + df_reserves['res4'][i] + 'x' + df_reserves['n_res4'][i] '\n'\
                + df_reserves['res5'][i] + 'x' + df_reserves['n_res5'][i] '\n'\
            + ' 伝達事項 ：' + df_reserves['other'][i]

    return text