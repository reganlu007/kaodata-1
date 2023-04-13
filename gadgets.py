#!/usr/bin/env python3

import csv
import os
import requests
from bs4 import BeautifulSoup
from pytablewriter import MarkdownTableWriter
from pytablewriter.style import Style
from utils import to_unicode_name

# 18 位帝國元帥之一，但未出現在遊戲中
# https://zh.wikipedia.org/wiki/纪尧姆·布律纳

lempe_persons_wiki = [
    'https://zh.wikipedia.org/wiki/拿破仑一世',  # [0]
    'https://zh.wikipedia.org/wiki/约瑟夫·波拿巴',  # 拿破崙兄
    'https://zh.wikipedia.org/wiki/吕西安·波拿巴',  # 拿破崙弟
    'https://zh.wikipedia.org/wiki/拿破仑三世',  # 約瑟芬外孫
    'https://zh.wikipedia.org/wiki/热罗姆·波拿巴',  # 拿破崙幼弟
    'https://zh.wikipedia.org/wiki/拿破崙四世',  # 拿破崙三世獨生子
    'https://zh.wikipedia.org/wiki/讓-馬蒂厄-菲利貝爾·塞律里埃',  # 帝國元帥(榮譽)
    'https://zh.wikipedia.org/wiki/拉扎尔·卡诺',
    'https://zh.wikipedia.org/wiki/路易-亚历山大·贝尔蒂埃',  # 帝國元帥
    'https://zh.wikipedia.org/wiki/夏尔·莫里斯·德塔列朗-佩里戈尔',
    'https://zh.wikipedia.org/wiki/邦·阿德里安·让诺·德·蒙塞',  # [10] 帝國元帥
    'https://zh.wikipedia.org/wiki/保羅·巴拉斯',
    'https://zh.wikipedia.org/wiki/弗朗索瓦·约瑟夫·勒菲弗',  # 帝國元帥(榮譽)
    'https://zh.wikipedia.org/wiki/皮埃尔·奥热罗',  # 帝國元帥
    'https://zh.wikipedia.org/wiki/让-巴蒂斯特·儒尔当',  # 帝國元帥; 用中文名找, 英文 "La Mette" 找不到對應人物
    'https://zh.wikipedia.org/wiki/安德烈·马塞纳',  # 帝國元帥
    'https://zh.wikipedia.org/wiki/约瑟夫·富歇',  # [16]
    'https://zh.wikipedia.org/wiki/卡尔十四世·约翰',  # Bernadotte, 帝國元帥
    'https://zh.wikipedia.org/wiki/克洛德·维克托-佩兰',
    'https://zh.wikipedia.org/wiki/洛朗·古维翁-圣西尔',
    'https://en.wikipedia.org/wiki/Pierre_Dupont_de_l%27Étang',
    'https://en.wikipedia.org/wiki/Jean-Baptiste_Drouet,_Comte_d%27Erlon',
    'https://zh.wikipedia.org/wiki/艾蒂安·麦克唐纳',
    'https://zh.wikipedia.org/wiki/埃马纽埃尔·德·格鲁希',
    'https://zh.wikipedia.org/wiki/让-巴蒂斯特·贝西埃',  # 帝國元帥, 出生年 1768, 火間虫入道 記為 1766
    'https://en.wikipedia.org/wiki/Édouard_Jean_Baptiste_Milhaud',
    'https://zh.wikipedia.org/wiki/若阿尚·缪拉',  # 帝國元帥
    'https://zh.wikipedia.org/wiki/路易·德賽',
    'https://zh.wikipedia.org/wiki/爱德华·莫蒂埃',  # 帝國元帥
    '',  # 墨勃格, Mobrogue, モーブルグ (1768) 查無此人
    'https://zh.wikipedia.org/wiki/让·德迪厄·苏尔特',  # 帝國元帥
    'https://zh.wikipedia.org/wiki/米歇尔·内伊',  # 帝國元帥
    'https://en.wikipedia.org/wiki/Louis_Friant',  # [32]
    'https://zh.wikipedia.org/wiki/让·拉纳',  # 帝國元帥
    'https://en.wikipedia.org/wiki/Dominique_Vandamme',
    'https://en.wikipedia.org/wiki/Pierre_Cambronne',
    'https://en.wikipedia.org/wiki/François_Étienne_de_Kellermann',
    'https://zh.wikipedia.org/wiki/路易·加布里埃尔·絮歇',
    'https://zh.wikipedia.org/wiki/路易·尼古拉·达武',  # 帝國元帥
    'https://en.wikipedia.org/wiki/Louis_Antoine_Fauvelet_de_Bourrienne',  # 法國外交官
    'https://en.wikipedia.org/wiki/Louis-Pierre_Montbrun',  # 博羅金諾戰役
    'https://zh.wikipedia.org/wiki/让·维克托·马里·莫罗',
    'https://zh.wikipedia.org/wiki/讓-安多什·朱諾',
    'https://zh.wikipedia.org/wiki/讓·拉普',
    'https://en.wikipedia.org/wiki/Jean_Reynier',
    'https://zh.wikipedia.org/wiki/奥拉斯·塞巴斯蒂亚尼',
    '',  # 布代, Bruyes, プティ (1772)
    'https://zh.wikipedia.org/wiki/奧古斯特·德·馬爾蒙',
    'https://zh.wikipedia.org/wiki/艾蒂安·莫里斯·热拉尔',  # [48]
    'https://zh.wikipedia.org/wiki/安托萬·夏爾·路易·拉薩爾',
    '',  # 雷耶, Ledru, レイユ (1775)
    'https://zh.wikipedia.org/wiki/阿尔芒·德·科兰古',
    'https://en.wikipedia.org/wiki/Gaspard_Gourgaud',
    'https://en.wikipedia.org/wiki/Charles_Tristan,_marquis_de_Montholon',  # 穆頓, Montholon, モントロン (1783)
    'https://en.wikipedia.org/wiki/Charles_de_la_Bédoyère',  # [54]
    'https://zh.wikipedia.org/wiki/喬治三世',
    'https://zh.wikipedia.org/wiki/喬治四世',
    'https://zh.wikipedia.org/wiki/维多利亚女王',
    'https://zh.wikipedia.org/wiki/第一代西德默斯子爵亨利·阿丁頓',  # 英國首相 (1801-1804)
    'https://zh.wikipedia.org/wiki/理查德·布林斯利·谢立丹',  # 海軍財務官
    'https://en.wikipedia.org/wiki/Thomas_Picton',
    'https://zh.wikipedia.org/wiki/小威廉·皮特',
    '',  # 巴紹特, Basaust, バスアースト (1762)
    '',  # 比藍特, Bylandt, ビラント (1763)
    '',  # [64] 戈登, Gordon, ゴードン (1764), Gordon 太多不知道是誰, https://en.wikipedia.org/wiki/George_Gordon,_5th_Duke_of_Gordon
    '',  # 奧蘭治, Orange, オレンジ (1766)
    'https://en.wikipedia.org/wiki/John_Moore_(Irish_politician)',
    'https://zh.wikipedia.org/wiki/第一代安格尔西侯爵亨利·佩吉特',  # Uxbridge
    '',  # 藍伯特, Lambert, ランバート (1768)
    'https://en.wikipedia.org/wiki/William_Beresford,_1st_Viscount_Beresford',
    'https://zh.wikipedia.org/wiki/第一代威靈頓公爵阿瑟·韋爾斯利',
    'https://en.wikipedia.org/wiki/Frederick_Maitland',
    '',  # 康瓦利斯, Cornwallis, コーンウォリス (1769), https://en.wikipedia.org/wiki/Charles_Cornwallis,_2nd_Marquess_Cornwallis
    '',  # 華亭, Alten, アルテン (1770)
    'https://en.wikipedia.org/wiki/Antoine_Le_Picard_de_Phélippeaux',  # フィリッポー (1770); 條目這個 (1767), 在埃及打敗拿破崙
    'https://en.wikipedia.org/wiki/Ormsby_Vandeleur',
    'https://en.wikipedia.org/wiki/Hussey_Vivian,_1st_Baron_Vivian',
    'https://en.wikipedia.org/wiki/FitzRoy_Somerset,_1st_Baron_Raglan',  # https://en.wikipedia.org/wiki/Lord_Robert_Somerset
    'https://en.wikipedia.org/wiki/Rowland_Hill,_1st_Viscount_Hill',
    '',  # 波謝, Pershey, パーシー (1772)
    'https://en.wikipedia.org/wiki/Frederick_Cavendish_Ponsonby',  # [80]
    '',  # 麥克唐納, McDonnel, マクドネル (1773)
    '',  # 科伯恩, Colburn, コルボーン (1774)
    'https://zh.wikipedia.org/wiki/卡蘇里子爵羅伯特·史都華',
    '',  # 昂吉迪, Wade, アーチディーケ (1777)
    'https://en.wikipedia.org/wiki/Cavalié_Mercer',
    'https://en.wikipedia.org/wiki/William_Howe_De_Lancey',
    '',  # 拉姆齊, Ramsay, ラムゼイ (1781)
    'https://en.wikipedia.org/wiki/John_Pitt,_2nd_Earl_of_Chatham',  # 與 小威廉彼特 (William Pitt the Younger) 是兄弟
    '',  # 諾莫爾	Nomire, ノーマイル (1782)
    'https://en.wikipedia.org/wiki/Georg_Baring',
    'https://en.wikipedia.org/wiki/John_Dawson,_2nd_Earl_of_Portarlington',  # [91]
]


def get_title(url):
    print(f'fetching title from {url}...', end=None)
    # 發送 GET 請求
    response = requests.get(url)
    # 使用 BeautifulSoup 解析回應的 HTML 內容
    soup = BeautifulSoup(response.content, 'html.parser')
    # 找到 HTML 中的 <title> 標籤的內容，並返回
    title = soup.title
    if title is not None:
        title = title.text.split(' - ')[0]
    # title = soup.find('span', {'class': 'mw-page-title-main'}).text
    print(title)
    return title


def fetch_name(id: int, default: str = ''):
    if id < len(lempe_persons_wiki) and lempe_persons_wiki[id] != '':
        url = lempe_persons_wiki[id]
        # name = url.split('/')[-1]
        if '/zh.' in url:
            url = url.replace('/wiki/', '/zh-tw/')
        return get_title(url)
    else:
        return f'({default})'


def lempe_combine_persons():
    CSV_TW = 'PERSONS_TABLE/lempe-persons-s1-zh.csv'
    CSV_EN = 'PERSONS_TABLE/lempe-persons-s1-en.csv'
    with open(CSV_TW, 'r', encoding='utf-8') as ftw, open(CSV_EN, 'r', encoding='utf-8') as fen:
        csv_tw = csv.reader(ftw)
        csv_en = csv.reader(fen)

        header = next(csv_tw)
        header = header[0:2] + ['中文版', '英文版', '國家'] + header[2:-2]
        next(csv_en)

        persons = []
        for row_tw, row_en in zip(csv_tw, csv_en):
            id = row_tw[0]
            name = fetch_name(int(id), row_tw[1])
            person = [id, name] + [row_tw[1], row_en[1], row_tw[-1]] + row_tw[2:-2]
            persons.append(person)
        # for person in persons:
            # person[1] = '[{}](/人物/拿破崙時代/{})'.format(person[1], person[1])

    writer = MarkdownTableWriter(
        table_name='拿破崙 人物資料',
        headers=header,
        value_matrix=persons,
        column_styles=[
            Style(),
            Style(),
            Style(),
            Style(),
            Style(align='center'),
            Style(align='center'),
            Style(align='center'),
            Style(align='center'),
            Style(align='center'),
            Style(align='center'),
            Style(align='center'),
            Style(align='center'),
            Style(align='center'),
            Style(align='center'),
            Style(align='center'),
            Style(align='center'),
        ]
    )
    writer.write_table()


def lempe_list_cities_and_nations():
    HOME_DIR = os.path.expanduser('~')
    NPDATA_EN = HOME_DIR + '/DOSBox/empereur/NPDATA.CIM'
    NPDATA_TW = HOME_DIR + '/DOSBox/lempereur/NPDATA.CIM'
    with open(NPDATA_EN, 'rb') as fen, open(NPDATA_TW, 'rb') as ftw:
        cities = []
        nations = []

        # extract nations
        fen.seek(7220)
        ftw.seek(7220)
        for _ in range(15):
            nation_en = to_unicode_name(fen.read(10)[:9])
            nation_tw = to_unicode_name(ftw.read(10)[:8])
            nations.append((nation_en, nation_tw))

        # extract cities
        for _ in range(46):
            city_en = to_unicode_name(fen.read(34)[:15])
            city_tw = to_unicode_name(ftw.read(34)[:14])
            cities.append((city_en, city_tw))

    # print(nations)
    # print(cities)
    # print('nations:', len(nations))
    # print('cities:', len(cities))

    writer = MarkdownTableWriter(
        table_name='拿破崙 國家',
        headers=['ID', '中文', '英文'],
        value_matrix=[(i, nation[1], nation[0]) for i, nation in enumerate(nations)],
    )
    writer.write_table()

    writer = MarkdownTableWriter(
        table_name='拿破崙 城市',
        headers=['ID', '中文', '英文'],
        value_matrix=[(i, city[1], city[0]) for i, city in enumerate(cities)],
    )
    writer.write_table()


if __name__ == '__main__':
    lempe_combine_persons()  # 拿破崙 合併中英文人名
    # lempe_list_cities_and_nations()  # 拿破崙 列出所有城市與國家
