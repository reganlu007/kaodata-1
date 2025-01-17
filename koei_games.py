import click
from ls11 import *
from rich.table import Table
from PIL import ImageFile
from utils import *
from koei_person import *
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


@click.command(help='人物資料解析')
@click.option('-d', '--dir', 'game_dir', help="遊戲目錄", required=True)
@click.option('-t', '--to', 'to', help="Specify output format", default='rich', type=click.Choice(['rich', 'csv', 'json', 'markdown', 'md']))
@click.option('-s', '--scenario', 'scenario', help="Specify scenario number (starts from 1)", default=0)
def kohryuki_person(game_dir, to, scenario):
    """
    人物資料解析

    MAIN.EXE    人名 (offset: 264260, 17bytes)
    SNDT1.KR1   劇本1
    SNDT2.KR1   劇本2
    SNDT3.KR1   劇本3
    SNDT4.KR1   劇本4

    TODO(yuxioz): 中日文版差異
        - main.exe filename
        - main.exe offset
        - decode name with different encoding

    ./dekoei.py kohryuki person -d ~/DOSBox/kanso/
    ./dekoei.py kohryuki person -d ~/DOSBox/kanso/ --to csv > PERSONS_TABLE/kohryuki-persons-s1.csv
    """
    main_exe = os.path.join(game_dir, 'MAIN.EXE')
    # main_exe = os.path.join(game_dir, 'output.000.exe')

    def person_loader(main_exe, scenario=scenario):
        sn_file = os.path.join(game_dir, 'SNDT{}.KR1'.format(scenario+1))
        with open(main_exe, 'rb') as fmain, open(sn_file, 'rb') as fsn:
            fmain.seek(264260)  # 日文版
            # fmain.seek(276180) # 中文版
            fsn.seek(4)
            person_data = []
            for _ in range(92):
                d1 = fmain.read(17)
                d2 = fsn.read(10)
                person_data.append(b''.join([d1, d2]))
        return person_data
    person_data = person_loader(main_exe)

    persons = load_person(person_data, kohryuki_format, KOHRYUKIPerson)
    print_table(kohryuki_table_title, kohryuki_headers, persons, to)


kohryuki.add_command(kohryuki_face, 'face')
kohryuki.add_command(kohryuki_person, 'person')

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

    專有顏:105, 守衛:1, 背景:8, 大眾:約56格大小
    """
    palette = color_codes_to_palette(
        ['#000000', '#00FF00', '#FF0000', '#FFFF00', '#0000FF', '#00FFFF', '#FF00FF', '#FFFFFF']
    )
    face_w, face_h = 48, 80
    num_part = 105
    part_size = calc_part_size(face_w, face_h, len(palette), hh=True)
    loader = create_floppy_image_stream(face_file, [(582656, num_part * part_size)], part_size)

    extract_images(face_file, face_w, face_h, palette, out_dir, prefix, hh=True, data_loader=loader)


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
    part_size = calc_part_size(face_w, face_h, len(palette), hh=True)

    def stream() -> typing.Generator[bytes, None, None]:
        with open(face_file, 'rb') as f:
            f.seek(47616)
            for _ in range(34):
                yield f.read(part_size)

    extract_images(face_file, face_w, face_h, palette, out_dir, prefix, num_part=34, hh=True, data_loader=stream)


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


@click.group()
def lempe():
    """拿破崙

    KAODATA.DAT

    "nations": [
        "France", "Holland", "Bavaria", "Denmark", "Turkey", "Italy", "Venice", "Naples",
        "Portugal", "Sweden", "Spain", "Prussia", "Russia", "Austria", "England", "Dublin"
    ]

    "places": {
        "start_pos": 7404,
        "data_size": 34,
        "data_count": 45 # 1-46?
    },
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
@click.option('-t', '--to', 'to', help="Specify output format", default='rich', type=click.Choice(['rich', 'csv', 'json', 'markdown', 'md']))
@click.option('-s', '--scenario', 'scenario', help="Specify scenario number (starts from 1)", default=0)
def lempe_person(file, to, scenario):
    """
    人物資料解析
    TODO:
      - [ ] check names of following person in game
        - [183] 默函特二世

    NPDATA.CIM

    ./dekoei.py lempe person -f ~/DOSBox/lempereur/NPDATA.CIM
    ./dekoei.py lempe person -f ~/DOSBox/empereur/NPDATA.CIM --to csv --scenario 2 > lempe-persons-s2-en.csv
    ./dekoei.py lempe person -f ~/DOSBox/lempereur/NPDATA.CIM --to csv --scenario 4 > lempe-persons-s4-zh.csv
    """
    def person_loader(file, scenario=scenario-1):
        offsets1 = [8934, 22204, 35474, 48744, 62014]
        offsets2 = [x-8930 for x in offsets1]  # offsets2 = [4, 13274, 26544, 39814, 53084]
        read_count, read_size1, read_size2 = 255, 17, 15
        person_data = []
        with open(file, 'rb') as f:
            for i in range(read_count):
                f.seek(offsets1[scenario]+read_size1*i)
                d1 = f.read(read_size1)
                f.seek(offsets2[scenario]+read_size2*i)
                d2 = f.read(read_size2)
                person_data.append(b''.join([d1, d2]))
        return person_data
    person_data = person_loader(file, scenario=0)

    persons = load_person(person_data, lempe_format, LEMPEPerson)
    print_table(lempe_table_title, lempe_headers, persons, to)


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

    def avg(x):  # average
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
        part_size = calc_part_size(face_w, face_h, len(palette), hh=hh)
        offset_infos = [(414720, num_part*part_size)]  # (offset, face_count * part_size)
        loader = create_floppy_image_stream(face_file, offset_infos, part_size)

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
        part_size = calc_part_size(face_w, face_h, len(palette), hh=hh)
        offset_infos = [(15360, num_part*part_size)]  # (offset, face_count * part_size)
        loader = create_floppy_image_stream(face_file, offset_infos, part_size)

    extract_images(face_file, face_w, face_h, palette, out_dir, prefix, hh=hh, data_loader=loader)


@click.command(help='人物資料解析')
@click.option('-d', '--dir', 'game_dir', help="遊戲目錄", required=True)
@click.option('-t', '--to', 'to', help="Specify output format", default='rich', type=click.Choice(['rich', 'csv', 'json', 'markdown', 'md']))
@click.option('-s', '--scenario', 'scenario', help="Specify scenario number (starts from 1)", default=0)
@click.option('-f', '--file', 'file', help="劇本檔案")
def suikoden_person(game_dir, to, scenario, file):
    """
    人物資料解析

    SUIDATA1.CIM
    SUIDATA2.CIM
    SUIDATA3.CIM
    SUIDATA4.CIM

    ./dekoei.py suikoden person -d ~/DOSBox/sui/
    ./dekoei.py suikoden person -d ~/DOSBox/sui/ --to csv > PERSONS_TABLE/suikoden-persons-s1.csv
    """
    def person_loader(scenario=scenario):
        sn_file = os.path.join(game_dir, 'SUIDATA{}.CIM'.format(scenario+1))
        with open(sn_file, 'rb') as fsn:
            offset1 = 7124  # name
            offset2 = 4  # ability
            read_count, read_size1, read_size2 = 255, 45, 22
            person_data = []
            for i in range(read_count):
                fsn.seek(offset1+read_size1*i)
                d1 = fsn.read(read_size1)
                fsn.seek(offset2+read_size2*i)
                d2 = fsn.read(read_size2)
                person_data.append(b''.join([d1, d2]))
        return person_data
    person_data = person_loader(scenario)

    persons = load_person(person_data, suikoden_format, SUIKODENPerson)
    print_table(suikoden_table_title, suikoden_headers, persons, to)


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

    def stream() -> typing.Generator[bytes, None, None]:
        with open(game_dir+'/KAO.DAT', 'rb') as f:
            while part := f.read(part_size):
                yield part
        with open(game_dir+'/TEXTGRP.DAT', 'rb') as f:
            # 有馬桜子
            yield f.read(part_size)

    extract_images('', face_w, face_h, palette, out_dir, prefix, data_loader=stream)


winning.add_command(winning_face, 'face')
