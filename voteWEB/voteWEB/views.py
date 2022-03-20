import datetime

from django.shortcuts import render
from bbsApp.models import Post
from userApp.models import WebMember
import datetime as dt
import pandas as pd

def index(request) :
    print('>>> whovo')
    df = pd.DataFrame(list(WebMember.objects.all().values()))
    # lst1 = []
    # lst2 = []
    # lst3 = []

    # lst1 : 30대 이하 정당 지지도 / lst2 : 4050 정당 지지도 / lst3 : 60대 이상 정당 지지도
    print(df)
    print(df.describe(include='all'))
    print(df.info())
    today = datetime.date.today()
    df['member_age'] = pd.to_datetime(df['member_age'])
    print(df['member_age'], type['member_age'])
    df['birth_year'] = df['member_age'].dt.year
    df['age'] = today.year - df['birth_year'] + 1
    df_target = df[['age', 'member_poli']]
    print(df_target)
    df_l3 = df_target.loc[(df_target['age'] < 40) & (df_target['member_poli'] == '더불어민주당')]
    df_y3 = df_target.loc[(df_target['age'] < 40) & (df_target['member_poli'] == '국민의힘')]
    df_s3 = df_target.loc[(df_target['age'] < 40) & (df_target['member_poli'] == '정의당')]
    print(df_l3, type(df_l3))
    print(df_y3, type(df_y3))
    print(df_s3, type(df_s3))
    lst1 = [len(df_l3), len(df_y3), len(df_s3)]
    print(lst1)
    df_l5 = df_target.loc[(df_target['age'] >= 40) & (df_target['age'] < 60) & (df_target['member_poli'] == '더불어민주당')]
    df_y5 = df_target.loc[(df_target['age'] >= 40) & (df_target['age'] < 60) & (df_target['member_poli'] == '국민의힘')]
    df_s5 = df_target.loc[(df_target['age'] >= 40) & (df_target['age'] < 60) & (df_target['member_poli'] == '정의당')]
    print(df_l5, type(df_l5))
    print(df_y5, type(df_y5))
    print(df_s5, type(df_s5))
    lst2 = [len(df_l5), len(df_y5), len(df_s5)]
    print(lst2)
    df_l6 = df_target.loc[(df_target['age'] >= 60) & (df_target['member_poli'] == '더불어민주당')]
    df_y6 = df_target.loc[(df_target['age'] >= 60) & (df_target['member_poli'] == '국민의힘')]
    df_s6 = df_target.loc[(df_target['age'] >= 60) & (df_target['member_poli'] == '정의당')]
    print(df_l6, type(df_l6))
    print(df_y6, type(df_y6))
    print(df_s6, type(df_s6))
    lst3 = [len(df_l6), len(df_y6), len(df_s6)]
    print(lst3)

    df_poli = df[['member_poli']]
    print(df_poli)
    df_d = df_poli.loc[df_poli['member_poli'] == '더불어민주당']
    df_g = df_poli.loc[df_poli['member_poli'] == '국민의힘']
    df_j = df_poli.loc[df_poli['member_poli'] == '정의당']
    print(len(df_d), len(df_g), len(df_j))
    lst4 = [len(df_d), len(df_g), len(df_j)]
    print(lst4)

    df = pd.DataFrame(list(WebMember.objects.all().values()))
    df_1 = pd.DataFrame(list(Post.objects.all().values()))
    df_lc = df_1.loc[df_1['candidate_num'] == 1]
    df_yc = df_1.loc[df_1['candidate_num'] == 2]
    df_sc = df_1.loc[df_1['candidate_num'] == 3]
    print(len(df_lc), len(df_yc), len(df_sc))

    lst5 = [len(df_lc), len(df_yc), len(df_sc)]

    if request.session.get('member_name') :
        print('>>> our member')
        # 세션을 계속 심어줘야 함

        context = {
            'session_member_name' :  request.session.get('member_name'),
            'session_member_id': request.session.get('member_id'),
            'chart_data1' : lst1,
            'chart_data2': lst2,
            'chart_data3': lst3,
            'chart_data4': lst4,
            'chart_data5': lst5,

        }
        return render(request, 'index.html',context)

    else:
        context = {
            'chart_data1': lst1,
            'chart_data2': lst2,
            'chart_data3': lst3,
            'chart_data4': lst4,
            'chart_data5': lst5,

        }
        return render(request, 'index.html', context)



