from collections import namedtuple
from struct import unpack
import click
from utils import *
from ls11 import *
from rich.progress import track
from rich.table import Table
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True  # for KOUKAI3 palette file


@click.group()
def europe():
    """歐陸戰線

    FACE.DAT
    """
    pass


@click.command(help='顏 CG 解析')
@click.option('-f', '--face', 'face_file', help="頭像檔案", required=True)
@click.option('--out_dir', 'out_dir', default='_output', help='output directory')
@click.option('--prefix', 'prefix', default='', help='filename prefix of output files')
def europe_face(face_file, out_dir, prefix):
    palette = color_codes_to_palette(
        ['#000000', '#419241', '#B24120', '#F3C361', '#104192', '#6FAEAE', '#D371B2', '#F3F3F3']
    )
    face_w, face_h = 64, 80

    extract_images(face_file, face_w, face_h, palette, out_dir, prefix)


europe.add_command(europe_face, 'face')

##############################################################################


@click.group()
def kohryuki():
    """項劉記

    KAO.KR1
    """
    pass


@click.command(help='顏 CG 解析')
@click.option('-f', '--face', 'face_file', help="頭像檔案", required=True)
@click.option('--out_dir', 'out_dir', default='_output', help='output directory')
@click.option('--prefix', 'prefix', default='', help='filename prefix of output files')
def kohryuki_face(face_file, out_dir, prefix):
    palette = color_codes_to_palette(
        ['#000000', '#418200', '#C34100', '#E3A251', '#0030A2', '#71A2B2', '#B27171', '#F3E3D3']
    )
    face_w, face_h = 64, 80

    extract_images(face_file, face_w, face_h, palette, out_dir, prefix)


kohryuki.add_command(kohryuki_face, 'face')

##############################################################################


@click.group()
def ishin():
    """維新之嵐

    """
    pass


@click.command(help='顏 CG 解析')
@click.option('-f', '--face', 'face_file', help="頭像檔案", required=True)
@click.option('--out_dir', 'out_dir', default='_output', help='output directory')
@click.option('--prefix', 'prefix', default='', help='filename prefix of output files')
def ishin_face(face_file, out_dir, prefix):
    """
    ./dekoei.py ishin face -f kao/ISHIN_維新の嵐A.fdi --prefix ISHIN_PC98_F

    專有顏:106, 守衛:1, 背景:8, 大眾:約56格大小
    """
    palette = color_codes_to_palette(
        ['#000000', '#00FF00', '#FF0000', '#FFFF00', '#0000FF', '#00FFFF', '#FF00FF', '#FFFFFF']
    )
    face_w, face_h = 48, 80
    num_part = 105
    hh = True
    loader = create_floppy_image_loader(face_file, [(582656, num_part * 720)])

    extract_images(face_file, face_w, face_h, palette, out_dir, prefix, hh=hh, data_loader=loader)


ishin.add_command(ishin_face, 'face')

##############################################################################


@click.group()
def ishin2():
    """維新之嵐2

    """
    pass


@click.command(help='顏 CG 解析')
@click.option('-f', '--face', 'face_file', help="頭像檔案", required=True)
@click.option('--out_dir', 'out_dir', default='_output', help='output directory')
@click.option('--prefix', 'prefix', default='', help='filename prefix of output files')
def ishin2_face(face_file, out_dir, prefix):
    pass


ishin2.add_command(ishin2_face, 'face')

##############################################################################


@click.group()
def koukai():
    """大航海時代"""
    pass


@click.command(help='顏 CG 解析')
@click.option('-f', '--face', 'face_file', help="頭像檔案", required=True)
@click.option('--out_dir', 'out_dir', default='_output')
@click.option('--prefix', 'prefix', default='')
def koukai_face(face_file, out_dir, prefix):
    """
    KAO.PUT
    """
    palette = color_codes_to_palette(
        ['#000000', '#55FF55', '#FF5555', '#FFFF55', '#5555FF', '#55FFFF', '#FF55FF', '#FFFFFF']
    )
    face_w, face_h = 64, 80

    def loader() -> bytes:
        with open(face_file, 'rb') as f:
            f.seek(47616)
            return f.read()

    extract_images(face_file, face_w, face_h, palette, out_dir, prefix, num_part=34, hh=True, data_loader=loader)


koukai.add_command(koukai_face, 'face')

##############################################################################


@click.group()
def koukai2():
    """大航海時代II

    KAO.LZW     顏 CG (64x80) x 128
                道具 CG (48x48) x 128 (start_pos: 245,760, ls11)
                大眾臉 CG (start_pos: 292,514)
    """
    pass


@click.command(help='顏 CG 解析')
@click.option('-f', '--face', 'face_file', help="頭像檔案", required=True)
@click.option('--out_dir', 'out_dir', default='_output')
@click.option('--prefix', 'prefix', default='')
def koukai2_face(face_file, out_dir, prefix):
    """KAO2.LZW

    /dekoei.py koukai2 face -f kao/KOUKAI2_KAO.LZW
    """
    palette = color_codes_to_palette(
        ['#000000', '#00A261', '#D34100', '#F3A261', '#0041D3', '#00A2F3', '#D361A2', '#F3E3D3']
    )
    face_w, face_h = 64, 80

    extract_images(face_file, face_w, face_h, palette, out_dir, prefix, num_part=128)


koukai2.add_command(koukai2_face, 'face')

##############################################################################


@click.group()
def koukai3():
    """大航海時代III"""
    pass


@click.option('-f', '--face', 'face_file', help="頭像檔案", required=True)
@click.option('-p', '--palette', 'palette_file', default='cds95FaceHeader.bmp', help="色盤檔案")
@click.option('--out_dir', 'out_dir', default='_output', help='output directory')
@click.option('--prefix', 'prefix', default='', help='filename prefix of output files')
@click.command(help='顏 CG 解析')
def koukai3_face(face_file, palette_file, out_dir, prefix):
    """
    ./dekoei.py koukai3 face --face kao/KOUKAI3_FEMALE.CDS --palette kao/cds95FaceHeader.bmp
    ./dekoei.py koukai3 face --face kao/KOUKAI3_MALE.CDS --palette kao/cds95FaceHeader.bmp
    """
    # load palette
    palette_img = Image.open(palette_file)
    # palette_img.mode: "P"
    # palette_img.palette.getdata()[0]: "BGRX"
    #   "P" means using a color palette
    #   "BGRX" means the color order in palette with padding('X')
    #   see https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes

    # get palette with "RGB" mode, return list like [R0, G0, B0, R1, G1, B1, R2...]
    palette = list(grouper(palette_img.getpalette(rawmode='RGB'), 3))

    face_w, face_h = 80, 96

    extract_images(face_file, face_w, face_h, palette, out_dir, prefix)


koukai3.add_command(koukai3_face, 'face')

##############################################################################


def unpack_abi(b):
    lookup = {0: 'D', 1: 'C', 2: 'B', 3: 'A'}
    ability = [lookup[(b >> 2*i) & 0b11] for i in range(4)]
    return ability


def unpack_mask(b):
    # 0b00000100 幸運
    # 0b00001000 魅力
    # 0b00010000 勇氣
    # 0b00100000 膽小
    # 0b01000000 冷靜
    # 0b10000000 單純
    masks = [''] * 4
    if b & 0b11000000 == 0b01000000:
        masks[0] = '冷靜'
    elif b & 0b11000000 == 0b10000000:
        masks[0] = '單純'

    if b & 0b00110000 == 0b00010000:
        masks[1] = '勇氣'
    elif b & 0b00110000 == 0b00100000:
        masks[1] = '膽小'

    if b & 0b00001000:
        masks[2] = '魅力'
    if b & 0b00000100:
        masks[3] = '幸運'
    return masks


PersonRaw = namedtuple('PersonRaw', 'name, face, masks, nation, city, ability1, ability2')
Person = namedtuple(
    'Person', 'name, face, pol, eco, sup, buld, lead, soldier, horse, cannon, nation, city, luk, chrm, brave, cool')


def lempe_convert(pr: PersonRaw) -> Person:
    a, b, c, d = unpack_mask(pr.masks)
    pol, eco, sup, buld = unpack_abi(pr.ability1)  # 政治 經濟 補給 建設
    lead, soldier, horse, cannon = unpack_abi(pr.ability2)  # 統帥 步兵 騎兵 砲兵
    p = Person(
        name=to_unicode_name(pr.name),
        face=pr.face,
        pol=pol,
        eco=eco,
        sup=sup,
        buld=buld,
        lead=lead,
        soldier=soldier,
        horse=horse,
        cannon=cannon,
        nation=pr.nation,
        city=pr.city,
        luk=a,
        chrm=b,
        brave=c,
        cool=d,
    )
    return p


@click.group()
def lempe():
    """拿破崙

    KAODATA.DAT

    "nations": [
        "France", "Holland", "Bavaria", "Denmark", "Turkey", "Italy", "Venice", "Naples",
        "Portugal", "Sweden", "Spain", "Prussia", "Russia", "Austria", "England", "Dublin"
    ]
    """
    pass


@click.command(help='顏 CG 解析')
@click.option('-f', '--face', 'face_file', help="頭像檔案", required=True)
@click.option('--out_dir', 'out_dir', default='_output', help='output directory')
@click.option('--prefix', 'prefix', default='', help='filename prefix of output files')
def lempe_face(face_file, out_dir, prefix):
    palette = color_codes_to_palette(
        ['#000000', '#55FF55', '#FF5555', '#FFFF55', '#5555FF', '#55FFFF', '#FF55FF', '#FFFFFF']
    )
    face_w, face_h = 64, 80

    extract_images(face_file, face_w, face_h, palette, out_dir, prefix, hh=True)


@click.command(help='人物資料解析')
@click.option('-f', '--file', 'file', help="劇本檔案", required=True)
def lempe_person(file):
    """
    人物資料解析

    NPDATA.CIM
    """
    console = Console()
    table = Table(title="Sangokushi III Person Data")
    table.add_column('ID', justify='right', style='cyan')
    table.add_column('姓名')
    table.add_column('顏', justify='right', style='magenta')
    table.add_column('政治', justify='right', style='green')
    table.add_column('經濟', justify='right', style='green')
    table.add_column('補給', justify='right', style='green')
    table.add_column('建設', justify='right', style='green')
    table.add_column('統帥', justify='right', style='green')
    table.add_column('步兵', justify='right', style='green')
    table.add_column('騎兵', justify='right', style='blue')
    table.add_column('砲兵', justify='right', style='blue')
    table.add_column('個性1', justify='right', style='blue')
    table.add_column('個性2', justify='right', style='blue')
    table.add_column('個性3', justify='right', style='blue')
    table.add_column('個性4', justify='right', style='blue')

    # 4E61706F 6C656F6E 00000000 0000005F 06  # BCBA AACA 1111
    # 4E61706F 6C656F6E 00000000 0000005F 06  # start[22204]
    # 4E61706F 6C656F6E 00000000 0000005F 06  # start[35474]
    # 4E61706F 6C656F6E 00000000 0000005F 06  # start[48744]
    # 4E61706F 6C656F6E 00000000 0000005F 06  # start[62014]
    #  N a p o  l e o n
    #
    # 4A6F7365 70680000 00000000 00000103 06  # CCCB CCDD 0000, 2nd, Joseph
    # 4C756369 656E0000 00000000 00000203 06  # BBCC CDDD 0000, 3rd, Lucien
    # 42657274 68696572 00000000 00000842 06  # CCAB ACDC 1000, 9th, Berthier
    # 57697474 67656E73 7465696E 00007201 06  # CDBC BBCB 0000, Wittgenstein
    # 47656F72 67652049 49490000 00003A82 06  # George III
    # 47656F72 67652049 56000000 00003B82 00  # George IV
    # 56696374 6F726961 00000000 00003C5E 00  # Victoria
    # 4B757475 736F7600 00000000 00006346 06  # Kutusov (single eye?)
    # 42617272 61730000 00000000 00000B20 06  # Barras
    # 4C656665 62767265 00000000 00000C12 06  # Lefebvre -o--
    # 41756765 72656175 00000000 00000D81 06  # Augereau x---
    # ^^^^^^^^ ^^^^^^^^ ^^^^^^^^     ^^
    # 名字                            序號
    # 00 1AE6DF00 411C0505 00525705 0000 # BCBA AACA 1111, 1769
    # 00 1B950500 491E0500 00303904 0000 # CCCB CCDD 0000, 1768
    # 00 1B5A0100 42170000 00000004 0000 # BBCC CDDD 0000, 1775
    # 00 1E610500 31140000 00000000 0000 # CDBC CCDD 0000, 1778
    # 00 1E515500 2D0E0000 00000000 0000 # CDCC CCCC -000, 1784
    # 0E 04AF6A00 64E96464 00646401 0000 # AABB BBBC 1111, 1819
    # ^^ ^ ^^^^   ^^  ^^     ^^^^
    # 國 城 能     忠  兵      訓士
    #             誠  力      練氣

    # NAME, FACE, MASKS, x, NAT., CITY, ABI1, ABI2,
    fmt = '<14sBBxBBBBxxxxxxxxxxx'

    # "start_pos": [8934, 13274],
    # "data_size": [17, 15],
    # "data_count": 255

    def kao2str(face):
        if face <= 265:
            return '[red]'+str(face)
        else:
            # convert face from number to hex string
            return hex(face)[2:].upper()

    with open(file, 'rb') as f:
        for i in range(255):
            f.seek(8934+17*i)
            d1 = f.read(17)
            f.seek(13274+15*i)
            d2 = f.read(15)
            data = b''.join([d1, d2])

            pr = PersonRaw._make(unpack(fmt, data))
            p = lempe_convert(pr)
            table.add_row(str(i), p.name, str(p.face), str(p.pol), str(p.eco), str(p.sup), p.buld, p.lead,
                          p.soldier, p.horse, p.cannon, p.luk, p.chrm, p.brave, p.cool)
    console.print(table)


lempe.add_command(lempe_face, 'face')
lempe.add_command(lempe_person, 'person')

##############################################################################


@click.group()
def liberty():
    """獨立戰爭

    FACE.IDX
    """
    pass


@click.command(help='顏 CG 解析')
@click.option('-f', '--face', 'face_file', help="頭像檔案", required=True)
@click.option('--out_dir', 'out_dir', default='_output', help='output directory')
@click.option('--prefix', 'prefix', default='', help='filename prefix of output files')
def liberty_face(face_file, out_dir, prefix):
    """
    ./dekoei.py liberty face -f ~/DOSBox/LIBERTY/FACE.IDX --out_dir LIBERTY --prefix "FACE"
    ./dekoei.py liberty face -f ~/DOSBox/LIBERTY/GRAPHICS.IDX --out_dir LIBERTY --prefix "GRAPHICS"
    """
    palette = color_codes_to_palette(
        ['#000000', '#55FF55', '#FF5555', '#FFFF55', '#5555FF', '#55FFFF', '#FF55FF', '#FFFFFF']  # NOT READY
    )
    face_w, face_h = 64, 80

    def avg(x):
        s = 0
        for xx in x:
            s += xx
        return s / len(x)

    os.makedirs(out_dir, exist_ok=True)

    file_size = os.stat(face_file).st_size
    with open(face_file, 'rb') as f:
        f.read(3)  # 'IDX'

        count = int.from_bytes(f.read(1), LITTLE_ENDIAN)
        print('count: {}'.format(count))
        # count = 999 # switch for FACE.IDX
        offsets = []
        while len(offsets) < count:
            offset = int.from_bytes(f.read(4), LITTLE_ENDIAN)
            if offset == 5242944:  # 0x40005000LE
                break
            offsets.append(offset)
        print('offset count: {}'.format(len(offsets)))
        block_sizes = []
        table = Table(title=face_file)
        table.add_column("ID", justify="right", style="cyan", no_wrap=True)
        table.add_column("width", style="magenta")
        table.add_column("height", style="magenta")
        table.add_column("block size", justify="right", style="green")
        table.add_column("times", justify="right", style="green")
        table.add_column("first byte", justify="right", style="green")
        for i in range(len(offsets)):
            offset = offsets[i]
            f.seek(offset)
            fb = f.read(4)  # first block
            next_offset = file_size if i == len(offsets)-1 else offsets[i+1]
            print('[{:02d}] {}, {} {}'.format(i, offset, next_offset - offset, fb))
            block_size = next_offset - offset
            block_sizes.append(block_size)
            w = int.from_bytes(fb[:2], LITTLE_ENDIAN)
            h = int.from_bytes(fb[2:], LITTLE_ENDIAN)
            out_filename = '{}/{}{:04d}_{}x{}'.format(out_dir, prefix, i, w, h)
            with open(out_filename, 'wb') as fout:
                raw_data = f.read(block_size-4)
                first_byte = int.from_bytes(raw_data[:2], LITTLE_ENDIAN)
                fout.write(raw_data)
                table.add_row(str(i), str(w), str(h), str(len(raw_data)), str((len(raw_data)-2)/w/h), str(first_byte))
        # print block_infos in rows
        console = Console()
        console.print(table)
        print('block size: min({}), max({}), avg{}'.format(min(block_sizes), max(block_sizes), avg(block_sizes)))


liberty.add_command(liberty_face, 'face')

##############################################################################


@click.group()
def royal():
    """魔法皇冠

    ./dekoei.py royal face -f kao/ROYAL_KAODATA.DAT
    ./dekoei.py royal face -f kao/ROYAL_PC98_ロイヤルブラッド_B.fdi
    """
    pass


@click.command(help='顏 CG 解析')
@click.option('-f', '--face', 'face_file', help="頭像檔案", required=True)
@click.option('--out_dir', 'out_dir', default='_output', help='output directory')
@click.option('--prefix', 'prefix', default='', help='filename prefix of output files')
def royal_face(face_file, out_dir, prefix):
    """
    KAODATA.DAT
    PC98_ロイヤルブラッド_B.fdi
    """
    palette = color_codes_to_palette(
        ['#000000', '#55FF55', '#FF5555', '#FFFF55', '#5555FF', '#55FFFF', '#FF55FF', '#FFFFFF']
    )
    face_w, face_h = 64, 80
    loader = None
    num_part = 91
    hh = True

    # PC98 floppy image as face_file
    if '.fdi' in face_file.lower():
        palette = color_codes_to_palette(
            ['#000000', '#00BA65', '#FF5555', '#EFCF55', '#0065BA', '#459ADF', '#FF55FF', '#FFFFFF']
        )
        hh = False
        offset_infos = [(414720, num_part*1920)]  # (offset, face_count * part_size)
        loader = create_floppy_image_loader(face_file, offset_infos)

    extract_images(face_file, face_w, face_h, palette, out_dir, prefix, num_part=num_part, hh=hh, data_loader=loader)


royal.add_command(royal_face, 'face')

##############################################################################


@click.group()
def suikoden():
    """水滸傳

    """
    pass


@click.command(help='顏 CG 解析')
@click.option('-f', '--face', 'face_file', help="頭像檔案", required=True)
@click.option('--out_dir', 'out_dir', default='_output', help='output directory')
@click.option('--prefix', 'prefix', default='', help='filename prefix of output files')
def suikoden_face(face_file, out_dir, prefix):
    """
    KAOIBM.DAT
    水滸伝2.FDI
    """
    palette = color_codes_to_palette(
        ['#000000', '#55FF55', '#FF5555', '#FFFF55', '#5555FF', '#55FFFF', '#FF55FF', '#FFFFFF']
    )
    face_w, face_h = 64, 80
    loader = None
    hh = True

    # PC98 floppy image as face_file
    if '.fdi' in face_file.lower():
        palette = color_codes_to_palette(
            ['#000000', '#00FF00', '#FF0000', '#FFFF00', '#0000FF', '#00FFFF', '#FF00FF', '#FFFFFF']
        )
        hh = False
        num_part = 260
        offset_infos = [(15360, num_part*1920)]  # (offset, face_count * part_size)
        loader = create_floppy_image_loader(face_file, offset_infos)

    extract_images(face_file, face_w, face_h, palette, out_dir, prefix, hh=hh, data_loader=loader)


@click.command(help='人物資料解析')
@click.option('-f', '--file', 'file', help="劇本檔案", required=True)
def suikoden_person(file):
    """
    人物資料解析

    SUIDATA1.CIM
    SUIDATA2.CIM
    SUIDATA3.CIM
    SUIDATA4.CIM
    """


suikoden.add_command(suikoden_face, 'face')
suikoden.add_command(suikoden_person, 'person')

##############################################################################


@click.group()
def taikoh():
    """太閤立志傳

    KAO.PUT
    """
    pass


@click.command(help='顏 CG 解析')
@click.option('-f', '--face', 'face_file', help="頭像檔案", required=True)
@click.option('--out_dir', 'out_dir', default='_output', help='output directory')
@click.option('--prefix', 'prefix', default='', help='filename prefix of output files')
def taikoh_face(face_file, out_dir, prefix):
    palette = color_codes_to_palette(
        ['#000000', '#41C341', '#F35100', '#F3D300', '#2061A2', '#00C3F3', '#F361B2', '#F3F3F3']
    )
    face_w, face_h = 64, 80

    extract_images(face_file, face_w, face_h, palette, out_dir, prefix)


taikoh.add_command(taikoh_face, 'face')
##############################################################################


@click.group()
def tk2():
    """提督之決斷II

    KAO.TK2
    """
    pass


@click.command(help='顏 CG 解析')
@click.option('-f', '--face', 'face_file', help="頭像檔案", required=True)
@click.option('--out_dir', 'out_dir', default='_output', help='output directory')
@click.option('--prefix', 'prefix', default='', help='filename prefix of output files')
def tk2_face(face_file, out_dir, prefix):
    palette = color_codes_to_palette(
        ['#000000', '#417100', '#D32000', '#E3A261', '#0030A2', '#7192B2', '#C36161', '#F3F3F3']
    )
    face_w, face_h = 48, 64

    extract_images(face_file, face_w, face_h, palette, out_dir, prefix)


tk2.add_command(tk2_face, 'face')

##############################################################################


@click.group()
def winning():
    """光榮賽馬, 賽馬大亨

    (有大眾臉)
    """
    pass


@click.option('-d', '--dir', 'game_dir', help="遊戲目錄", required=True)
@click.option('--out_dir', 'out_dir', default='_output')
@click.option('--prefix', 'prefix', default='')
@click.command(help='顏 CG 解析')
def winning_face(game_dir, out_dir, prefix):
    """

    /dekoei.py winning face --dir ~/DOSBox/winning
    """
    palette = color_codes_to_palette(
        ['#000000', '#20D320', '#F30000', '#F3D300', '#0061C3', '#00B2F3', '#F351F3', '#F3F3F3']
    )
    face_w, face_h, bpp = 64, 80, 3
    part_size = int(face_w*face_h*bpp/8)

    def loader() -> bytes:
        raw_data = bytearray()
        with open(game_dir+'/KAO.DAT', 'rb') as f:
            raw_data.extend(f.read())
        with open(game_dir+'/TEXTGRP.DAT', 'rb') as f:
            # 有馬桜子
            raw_data.extend(f.read(part_size))
        return bytes(raw_data)

    extract_images('', face_w, face_h, palette, out_dir, prefix, data_loader=loader)


winning.add_command(winning_face, 'face')
