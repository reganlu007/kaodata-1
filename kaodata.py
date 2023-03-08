import os.path
import math
import sys
from PIL import Image
from game_infos import GAME_INFOS
from numpy import *
from utils import *


# 成吉思汗
KHAN_KAODATA = "/Users/tzengyuxio/DOSBox/KHAN/KAODATA.DAT"
KHAN_PALETTE = ['#302000', '#417120', '#D33030', '#D3B282', '#204182', '#418292', '#C38251',
                '#D3D3B2']  # 黑 綠 紅 粉 藍 青 橙 白


def bytes_to_images(data, size_per_image, w, h, color_table, dh=False):
    """
    Convert binary bytes to image list.
    """
    images = []
    num_images = math.floor(len(data) / size_per_image)
    for i in range(num_images):
        data_bytes = data[size_per_image*i: size_per_image * (i+1)]
        images.append(data_to_image(data_bytes, w, h, color_table, dh))
    return images


def export_faces(tag, path, prefix, with_single=False):
    game_info = GAME_INFOS[tag]

    color_table = []
    for c in game_info['palette']:
        rr, gg, bb = c[1:3], c[3:5], c[5:7]
        color_table.append((int(rr, base=16), int(gg, base=16), int(bb, base=16)))

    # filename = path + '/' + game_info['face_file']
    filename = path
    face_w, face_h = game_info['face_size']
    dh = True if 'double_height' in game_info and game_info['double_height'] else False
    face_count = -1 if 'face_count' not in game_info else game_info['face_count']
    start_pos = 0 if 'start_pos' not in game_info else game_info['start_pos']
    num_bits_per_color = 2 if len(color_table) == 4 else 4 if len(color_table) == 16 else 3
    data_size = int((face_w * face_h) * num_bits_per_color / 8)
    if dh:
        data_size = int(data_size / 2)
    num_face = 0

    filename_postfix = ''
    if tag in ('TEST', 'TEST2', 'TEST3'):
        with_single = False
        pure_base = os.path.basename(filename).split('/')[-1].split('.')[0]
        filename_postfix = '_' + pure_base

    ls11_encoded = False if 'ls11_encoded' not in game_info else game_info['ls11_encoded']
    if ls11_encoded:
        out_filename = '{}.DEC'.format(filename)
        ls11_decode(filename, out_filename)
        filename = out_filename
    with open(filename, 'rb') as f:
        all_face_data_bytes = b''
        if type(start_pos) is not list:
            f.seek(start_pos, os.SEEK_END)
            file_size = f.tell()
            face_count_by_size = file_size // data_size
            num_face = min(face_count, face_count_by_size) if face_count > 0 else face_count_by_size
            # print('  file size   : {}'.format(file_size))
            f.seek(start_pos)
            all_face_data_bytes = f.read(data_size * num_face)
        else:
            parts = []
            num_face = 0
            for sp, fc in zip(start_pos, face_count):
                f.seek(sp)
                db = f.read(fc * data_size)
                num_face += fc
                parts.append(db)
            all_face_data_bytes = all_face_data_bytes.join(parts)
        print('  all data size: {}'.format(len(all_face_data_bytes)))
        print('  face size    : {}x{}, ({} bytes)'.format(face_w, face_h, data_size))
        print('  num of faces : {}'.format(num_face))
        images = bytes_to_images(all_face_data_bytes, data_size, face_w, face_h, color_table, dh)

    if not os.path.exists(tag):
        os.makedirs(tag)

    if True:
        img_w = face_w * 16
        img_h = face_h * math.ceil(num_face / 16)
        back_image = Image.new('RGB', (img_w, img_h), color=BGCOLOR)
        # back_image = Image.new('RGB', (img_w, img_h), color='black')
        for idx, img in enumerate(images):
            pos_x = (idx % 16) * face_w
            pos_y = (idx // 16) * face_h
            back_image.paste(img, (pos_x, pos_y))
        out_filename = '{}/{}00-INDEX{}.png'.format(tag, prefix, filename_postfix)
        back_image.save(out_filename)
        print('...save {}'.format(out_filename))
    if with_single:
        for idx, img in enumerate(images):
            out_filename = '{}/{}{:04d}.png'.format(tag, prefix, idx + 1)
            img.save(out_filename)
            print('...save {}'.format(out_filename))
        print('{} images of face saved in [{}]'.format(num_face, tag))






# 成吉思涵 (色盤未確定)
# export_kaodata('KHAN', KHAN_KAODATA, KHAN_PALETTE)

# ----------------------------------------------------------------------

# 大航海時代
# export_faces('KOUKAI2', '/Users/tzengyuxio/DOSBox/DAIKOH2')
# export_faces('KOUKAI2', '/Users/tzengyuxio/DOSBox/DAIKOH2', all_in_one=True)
# export_faces('KOUKAI2I', '/Users/tzengyuxio/DOSBox/DAIKOH2', all_in_one=True) # items
# export_faces('KOUKAI2M', '/Users/tzengyuxio/DOSBox/DAIKOH2', all_in_one=True) # montage
# ls11_decode('/Users/tzengyuxio/DOSBox/DAIKOH2/KAO.LZW')
# data = b'\x3C\x93\xF8\x17\x13\xF8\x3B\x2F\x13\xF8\x16\xC3'
# print(get_codes(data))


# 航空霸業II (尚未找到)
# export_faces('AIR2', '/Users/tzengyuxio/DOSBox/AIR2', all_in_one=True)

# 獨立戰爭 (尚未找到)
# export_faces('LIBERTY', '/Users/tzengyuxio/DOSBox/LIBERTY')
# export_faces('LIBERTY', '/Users/tzengyuxio/DOSBox/LIBERTY', all_in_one=True)

# ls11_decode('KAODATA/ISHIN2_FACE.I2', 'KAODATA/ISHIN2_FACE.DEC')


def main():
    args = sys.argv[1:]
    if len(args) == 2:
        export_faces(args[0], args[1], args[0])
    elif len(args) == 3:
        export_faces(args[0], args[1], args[2])
    elif len(args) == 4:
        export_faces(args[0], args[1], args[2], args[3])
    else:
        print("Usage: {} KEYWORD FILENAME prefix (all_in_one)".format(sys.argv[0]))


if __name__ == '__main__':
    main()
