import palettes from './palettes';

const gameInfos = {
  san2: {
    id: 'san2',
    name: '三國志II',
    filename: 'kaodata.dat',
    width: 64,
    height: 80,
    palette: palettes.default.codes,
    count: -1,
    halfHeight: true,
    names: [
      '伊籍',
      '袁熙',
      '袁紹',
      '袁尚',
      '袁術',
      '袁譚',
      '王粲',
      '王雙',
      '諸葛誕',
      '王朗',
      '蒯越',
      '蒯良',
      '華歆',
      '賈詡',
      '郭奕',
      '郭嘉',
      '郭汜',
      '郝昭',
      '郭圖',
      '夏侯威',
      '夏侯淵',
      '夏侯恩',
      '夏侯惠',
      '夏侯尚',
      '夏侯惇',
      '夏侯德',
      '夏侯霸',
      '華佗',
      '華雄',
      '關羽',
      '韓玄',
      '夏侯和',
      '關興',
      '關索',
      '韓遂',
      '韓嵩',
      '闞澤',
      '母丘儉',
      '甘寧',
      '韓馥',
      '關平',
      '郭攸之',
      '顏良',
      '姜維',
      '許靖',
      '許褚',
      '許攸',
      '紀靈',
      '金環結',
      '金旋',
      '牛金',
      '魏延',
      '鍾會',
      '虞翻',
      '邢道榮',
      '薛綜',
      '嚴顏',
      '嚴峻',
      '黃蓋',
      '黃權',
      '侯成',
      '黃祖',
      '公孫越',
      '公孫瓚',
      '黃忠',
      '高定',
      '孔融',
      '公孫淵',
      '吳懿',
      '吳蘭',
      '蔡冒',
      '沙摩可',
      '周倉',
      '周瑜',
      '諸葛恪',
      '諸葛瑾',
      '諸葛亮',
      '審配',
      '司馬懿',
      '司馬師',
      '司馬昭',
      '周泰',
      '朱桓',
      '蔣琬',
      '尚寵',
      '鍾繇',
      '辛毘',
      '荀彧',
      '荀攸',
      '徐榮',
      '徐晃',
      '徐庶',
      '文欽',
      '曹叡',
      '曹休',
      '曹洪',
      '曹昂',
      '曹彰',
      '曹植',
      '曹真',
      '曹純',
      '曹仁',
      '曹操',
      '曹丕',
      '沮授',
      '孫堅',
      '孫乾',
      '孫權',
      '孫策',
      '孫翊',
      '太史慈',
      '朵思王',
      '趙雲',
      '張紘',
      '張郃',
      '張昭',
      '張松',
      '張任',
      '趙統',
      '張飛',
      '張苞',
      '張遼',
      '張魯',
      '陳宮',
      '趙廣',
      '陳群',
      '程昱',
      '程普',
      '典韋',
      '田豐',
      '董允',
      '陶謙',
      '鄧芝',
      '董卓',
      '董余奴',
      '馬休',
      '馬謖',
      '馬超',
      '馬鐵',
      '馬騰',
      '馬良',
      '費禕',
      '糜竺',
      '鄧艾',
      '文醜',
      '文聘',
      '法正',
      '龐統',
      '龐德',
      '滿寵',
      '孟獲',
      '孟優',
      '楊修',
      '楊奉',
      '雷同',
      '劉焉',
      '劉琦',
      '劉璋',
      '劉禪',
      '劉表',
      '劉備',
      '劉曄',
      '呂布',
      '呂蒙',
      '李傕',
      '陸遜',
      '李儒',
      '魯肅',
      '劉琮',
      '劉循',
      '孫亮',
      '張衛',
      '張休',
      '陳震',
      '典滿',
      '董衡',
      '袁胤',
      '司馬徽', // NBC
      '程秉',
      '樊稠',
      '李恢',
      '凌統',
      '凌操',
      '呂霸',
      '李異',
      '呂曠',
      '逢紀',
      '龐義',
      '馬岱',
      '閻圃',
      '',
      '新武將',
      '新武將',
      '新武將',
      '新武將',
      '新武將',
      '新武將',
      '新武將',
      '新武將',
      '新武將',
      '新武將',
      '新武將',
      '新武將',
      '女兒',
      '',
      '',
      '',
      '女兒',
      '',
      '',
      '',
      '女兒',
      '',
      '',
      '',
      '',
      '',
      '',
      '',
    ],
  },
  san3: {
    id: 'san3',
    name: '三國志III',
    filename: 'kaodata.dat',
    width: 64,
    height: 80,
    palette: palettes.san3.codes,
    count: -1,
    halfHeight: false,
    names: [
      '伊籍',
      '袁熙',
      '袁紹',
      '袁尚',
      '袁術',
      '袁譚',
      '王桀',
      '王雙',
      '諸葛誕',
      '王朗',
      '蒯越',
      '蒯良',
      '華歆',
      '賈詡',
      '郭奕',
      '郭嘉',
      '郭汜',
      '郝昭',
      '郭圖',
      '夏侯威',
      '夏侯淵',
      '夏侯恩',
      '夏侯惠',
      '夏侯尚',
      '夏侯惇',
      '夏侯德',
      '夏侯霸',
      '華佗', // NBC (not check name in game yet)
      '華雄',
      '關羽',
      '韓玄',
      '夏侯和',
      '關興',
      '關索',
      '韓遂',
      '韓嵩',
      '闞澤',
      '毋丘儉',
      '甘寧',
      '韓馥',
      '關平',
      '郭攸之',
      '顏良',
      '姜維',
      '許靖',
      '許褚',
      '許攸',
      '紀靈',
      '金環結',
      '金旋',
      '牛金',
      '魏延',
      '鍾會',
      '虞翻',
      '邢道榮',
      '薛綜',
      '嚴顏',
      '嚴畯',
      '黃蓋',
      '黃權',
      '侯成',
      '黃祖',
      '公孫越',
      '公孫瓚',
      '黃忠',
      '孫瑜',
      '孔融',
      '公孫淵',
      '吳懿',
      '吳蘭',
      '蔡瑁',
      '沙摩可',
      '周倉',
      '周瑜',
      '諸葛恪',
      '諸葛瑾',
      '諸葛亮',
      '審配',
      '司馬懿',
      '司馬師',
      '司馬昭',
      '周泰',
      '朱桓',
      '蔣琬',
      '向寵',
      '鐘繇',
      '辛毘',
      '荀彧',
      '荀攸',
      '徐榮',
      '徐晃',
      '徐庶',
      '文欽',
      '曹叡',
      '曹休',
      '曹洪',
      '曹昂',
      '曹彰',
      '曹植',
      '曹真',
      '曹純',
      '曹仁',
      '曹操',
      '曹丕',
      '沮授',
      '孫堅',
      '孫乾',
      '孫權',
      '孫策',
      '孫翊',
      '太史慈',
      '朵思王',
      '趙雲',
      '張鈜',
      '張郃',
      '張昭',
      '張松',
      '張任',
      '趙統',
      '張飛',
      '張苞',
      '張遼',
      '張魯',
      '陳宮',
      '趙廣',
      '陳韋',
      '程昱',
      '程普',
      '典韋',
      '田豐',
      '董允',
      '陶謙',
      '鄧芝',
      '董卓',
      '董荼奴',
      '馬休',
      '馬謖',
      '馬超',
      '馬鐵',
      '馬騰',
      '馬良',
      '費禕',
      '糜竺',
      '鄧艾',
      '文醜',
      '文聘',
      '法正',
      '龐統',
      '龐德',
      '滿寵',
      '孟獲',
      '孟優',
      '楊修',
      '楊奉',
      '雷銅',
      '劉焉',
      '劉琦',
      '劉璋',
      '劉禪',
      '劉表',
      '劉備',
      '劉曄',
      '呂布',
      '呂蒙',
      '李傕',
      '陸遜',
      '李儒',
      '魯肅',
      '劉琮',
      '劉循',
      '淳于瓊',
      '張衛',
      '張休',
      '陳震',
      '徐盛',
      '董衡',
      '袁胤',
      '司馬徽', // NBC (not check name in game yet)
      '高覽',
      '樊稠',
      '李恢',
      '凌統',
      '凌操',
      '蔣義渠',
      '李異',
      '呂曠',
      '逢紀',
      '郭淮',
      '馬岱',
      '閻圃',
      '許子將', // NBC
      '喬瑁',
      '孔秀',
      '劉繇',
      '嚴白虎',
      '樂進',
      '于禁',
      '賈逵',
      '王甫',
      '王允',
      '吳班',
      '顧雍',
      '蔣欽',
      '辛評',
      '孫禮',
      '張嶷',
      '張縤',
      '陳泰',
      '陳登',
      '丁奉',
      '馬忠',
      '孟達',
      '楊儀',
      '李嚴',
      '李典',
      '劉封',
      '廖化',
      '呂凱',
      '簡雍',
      '譚雄',
      '王平',
      '韓當',
      '糜芳',
      '獻帝', // NBC (not check name in game yet)
      '吉平', // NBC (not check name in game yet)
      '于吉', // NBC (not check name in game yet)
      '左慈', // NBC
      '管輅', // NBC (not check name in game yet)
      '紫虛上人', // NBC (not check name in game yet)
      '李意', // NBC (not check name in game yet)
      '新君主男',
      '新君主男',
      '新君主男',
      '新君主男',
      '新君主男',
      '新君主男',
      '新君主男',
      '新君主男',
      '新君主女',
      '新君主女',
      '新君主女',
      '新君主女',
      '新君主女',
      '新君主女',
      '新君主女',
      '新君主女',
      '新武將男',
      '新武將男',
      '新武將男',
      '新武將男',
      '新武將男',
      '新武將男',
      '新武將男',
      '新武將男',
      '新武將男',
      '新武將男',
      '新武將男',
      '新武將男',
      '新武將男',
      '新武將男',
      '新武將男',
      '新武將男',
      '新武將男',
      '新武將男',
      '新武將男',
      '新武將男',
      '新武將男',
      '新武將男',
      '新武將男',
      '新武將男',
      '新武將男',
      '新武將男',
      '新武將男',
      '新武將男',
      '新武將男',
      '新武將男',
      '新武將女',
      '新武將女',
      '新武將女',
      '新武將女',
      '新武將女',
      '新武將女',
      '新武將女',
      '新武將女',
      '新武將女',
      '新武將女',
      '新武將女',
      '新武將女',
      '新武將女',
      '新武將女',
      '新武將女',
      '新武將女',
      '新武將女',
      '新武將女',
      '新武將女',
      '新武將女',
      '新武將女',
      '新武將女',
      '新武將女',
      '新武將女',
      '新武將女',
      '新武將女',
      '新武將女',
      '新武將女',
      '新武將女',
      '新武將女',
      '貂蟬',
    ],
  },
  san4: {
    id: 'san4',
    name: '三國志IV',
    filename: 'kaodatap.s4',
    width: 64,
    height: 80,
    palette: palettes.san4.codes,
    count: -1, // 701 or 818
    halfHeight: false,
    names: [],
  },
  san5: {
    id: 'san5',
    name: '三國志V',
    filename: 'kaodata.s5',
    width: 64,
    height: 80,
    palette: palettes.san5.codes,
    count: -1,
    halfHeight: false,
    names: [],
  },
  kohryuki: {
    id: 'kohryuki',
    name: '項劉記',
    filename: 'kao.kr1',
    width: 64,
    height: 80,
    palette: palettes.kohryuki.codes,
    count: -1,
    halfHeight: false,
    names: [
      '項羽',
      '劉邦',
      '英布',
      '韓信',
      '范增',
      '章邯',
      '項莊',
      '司馬欣',
      '董翳',
      '章平',
      '趙歇',
      '陳餘',
      '張耳',
      '蕭公角',
      '田假',
      '鄭昌',
      '周殷',
      '鍾離昧',
      '夏說',
      '李左車',
      '項聲',
      '曹咎',
      '張逸',
      '武涉',
      '張良',
      '陳嬰',
      '項伯',
      '夏侯嬰',
      '蕭何',
      '周勃',
      '盧綰',
      '曹參',
      '審食其',
      '隨何',
      '周蘭',
      '陳平',
      '魏無知',
      '灌嬰',
      '紀信',
      '雍齒',
      '周苛',
      '樅公',
      '袁生',
      '鄭忠',
      '劉賈',
      '柴武',
      '楊喜',
      '呂馬童',
      '王翳',
      '楊武',
      '呂勝',
      '季布',
      '周昌',
      '叔孫通',
      '婁敬',
      '彭越',
      '孔聚',
      '陳賀',
      '楊',
      '申陽',
      '共敖',
      '張敖',
      '田榮',
      '龍且',
      '王陵',
      '貫高',
      '田橫',
      '田廣',
      '王吸',
      '薛歐',
      '任敖',
      '田既',
      '田光',
      '田吸',
      '侯公',
      '魏豹',
      '薛公',
      '丁公',
      '欒布',
      '臧荼',
      '司馬卬',
      '樊噲',
      '靳彊',
      '吳芮',
      '酈商',
      '蒯徹',
      '酈食其',
      '呂澤',
      '陸賈',
      '樓煩',
      '韓王信',
      '利幾',
      '',
      '長老',
      '',
      '',
      '虞姬',
    ],
  },
  suikoden: {
    id: 'suikoden',
    name: '水滸傳・天命之誓',
    filename: 'kaoibm.dat',
    width: 64,
    height: 80,
    palette: palettes.default.codes,
    count: -1,
    halfHeight: true,
    names: [
      '宋江',
      '盧俊義',
      '吳用',
      '公孫勝',
      '關勝',
      '林沖',
      '秦明',
      '呼延灼',
      '花榮',
      '柴進',
      '李應',
      '朱同',
      '魯智深',
      '武松',
      '董平',
      '張清',
      '楊志',
      '徐寧',
      '索超',
      '戴宗',
      '劉唐',
      '李逵',
      '史進',
      '穆弘',
      '雷橫',
      '李俊',
      '阮小二',
      '張橫',
      '阮小五',
      '張順',
      '阮小七',
      '楊雄',
      '石秀',
      '解珍',
      '解寶',
      '燕青',
      '朱武',
      '黃信',
      '宣贊',
      '裴宣',
      '鄧飛',
      '燕順',
      '楊林',
      '皇甫端',
      '王英',
      '扈三娘',
      '樊瑞',
      '孟康',
      '鄭天壽',
      '龔旺',
      '丁得孫',
      '宋萬',
      '杜遷',
      '薛永',
      '李忠',
      '湯窿',
      '杜興',
      '朱貴',
      '蔡福',
      '蔡慶',
      '李云',
      '顧大嫂',
      '孫二娘',
      '石遷',
      '段景住',
      '孫立',
      '單廷珪',
      '魏定國',
      '蕭讓',
      '呂方',
      '郭盛',
      '安道全',
      '孔明',
      '孔亮',
      '金大堅',
      '侯健',
      '樂和',
      '鄒淵',
      '石勇',
      '郁保四',
      '袁朗',
      '王煥',
      '王慶',
      '王進',
      '王倫',
      '丘岳',
      '喬冽',
      '許貫忠',
      '瓊英',
      '高俅',
      '寇威',
      '高廉',
      '扈成',
      '蔡京',
      '崔道成',
      '宿元景',
      '祝龍',
      '蕭嘉穗',
      '蔣忠',
      '史文恭',
      '任原',
      '西門慶',
      '石寶',
      '曾塗',
      '段三娘',
      '晁蓋',
      '張叔夜',
      '張文遠',
      '田虎',
      '鄧元覺',
      '童貫',
      '裴如海',
      '白秀英',
      '潘金蓮',
      '潘巧雲',
      '馬靈',
      '費保',
      '武大',
      '聞煥章',
      '卞祥',
      '方杰',
      '包道乙',
      '龐萬春',
      '方腊',
      '楊戩',
      '羅真人',
      '欒廷玉',
      '李鬼',
      '李師師',
      '李瑞蘭',
      '郝思文',
      '韓滔',
      '彭汜',
      '歐鵬',
      '凌振',
      '蔣敬',
      '鮑旭',
      '項充',
      '李袞',
      '馬麟',
      '童威',
      '童猛',
      '陳達',
      '楊春',
      '陶宗旺',
      '宋清',
      '穆春',
      '曹正',
      '施恩',
      '周通',
      '鄒潤',
      '朱富',
      '李立',
      '焦挺',
      '孫新',
      '張青',
      '王定六',
      '白勝',
      '葉清',
      '祝彪',
      '諸享',
      '方瓊',
      '呂師囊',
      '孫安',
      '鈕文忠',
      '張開',
      '胡顯',
      '李達',
      '蔡得章',
      '胡俊',
      '杜微',
      '黃安',
      '山士奇',
      '周謹',
      '上青',
      '白欽',
      '諸能',
      '仲良',
      '薛燦',
      '曾魁',
      '韓存保',
      '聞達',
      '曾昇',
      '蘇定',
      '黃文譁',
      '董澄',
      '家余慶',
      '范全',
      '時文彬',
      '曾索',
      '元興',
      '縻勝',
      '錢振鵬',
      '伍應星',
      '田彪',
      '苟正',
      '吳值',
      '何玄通',
      '唐斌',
      '史定',
      '王寅',
      '田豹',
      '季三思',
      '黨士英',
      '孔賓',
      '牛邦喜',
      '劉夢龍',
      '鄭之端',
      '張翔',
      '沈壽',
      '徐方',
      '曾密',
      '鄔福',
      '蔡澤',
      '項元鎮',
      '賀吉',
      '黨士雄',
      '盛本',
      '劉敏',
      '郭世廣',
      '張威',
      '于玉麟',
      '魚得源',
      '方貌',
      '鄔梨',
      '王義',
      '葉春',
      '耿恭',
      '何濤',
      '成貴',
      '程勝祖',
      '浦文英',
      '冷恭',
      '張世開',
      '雲宗武',
      '張蒙方',
      '安士榮',
      '梁士傑',
      '房學度',
      '溫克讓',
      '祝虎',
      '李懷',
      '文仲容',
      '衛忠',
      '方天定',
      '余深',
      '李吉',
      '丘小乙',
      '馬萬里',
      '何清',
      '黃文炳',
      '張保',
      '鄧龍',
      '劉高',
      '毛仲義',
      '造船所',
      '雜貨店',
      '兵工廠',
      '徽宗皇帝',
      '太宗',
    ],
  },
};

export default function getGameInfos() {
  return gameInfos;
}
