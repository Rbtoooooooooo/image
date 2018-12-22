from PIL import Image, ImageDraw, ImageFont
import re


def write_word(img_path, times, text, size, text_depth=0.8, interval=5):
    """
    将原图片转成文字生成的图片
    :param img_path: 图片路径
    :param times: 整数，生成一张为原图times倍的图片
    :param text: 字符串，文字内容
    :param size: 整数，文字大小
    :param text_depth: 正小数，文字颜色的深浅，默认值为0.8
    :param interval: 正整数，间隔度，越小生成的图片越清晰
    :return:
    """
    img = Image.open(img_path)
    width, height = img.size
    img_px = img.getdata()
    print(len(img_px))
    print('w:', width, 'h:', height, 'f:', img.format)
    print('times:', times, 'size:', size)

    text_length = len(text)
    name = re.split('\.', img_path)[0]

    font = ImageFont.truetype("C:\Windows\Fonts\simhei.ttf", size)
    bigger_img = img.resize((width * times, height * times))
    draw = ImageDraw.Draw(bigger_img)

    print('写字')
    for i in range(height)[::interval]:
        print(i / height)
        word_index = int(i / interval)
        for j in range(width)[::interval]:
            index = i * width + j
            px = img_px[index]
            px = (
                int(px[0] * text_depth),
                int(px[1] * text_depth),
                int(px[2] * text_depth),
            )
            word = text[word_index % text_length]
            draw.text((j * times, i * times), word, px, font=font)  # 设置文字位置/内容/颜色/字体
            word_index += 1
    param = '-'.join([str(i) for i in [times, text, size, text_depth, interval]])
    file_name = name + param + '.' + img.format
    print(file_name)
    bigger_img.save(file_name, format=img.format)
    bigger_img.show(file_name)


if __name__ == '__main__':
    img_pathes = ['shiqiu/1.jpeg',
                  'shiqiu/2.jpeg',
                  'shiqiu/3.jpeg',
                  'shiqiu/4.jpeg',
                  'shiqiu/5.jpeg',
                  'shiqiu/6.jpg',
                  'shiqiu/7.jpg'
                  ]
    bigger_size = 10
    texts = ['卡哇伊伊伊多哇',
             '小宝贝',
             '小可爱',
             '小仙女',
             '热情青春漂亮美丽纯洁活泼可爱单纯天真无邪善良热浪漫温柔贤淑甜美大方开朗聪明',
             '躺鸡萌妹',
             '无情冷酷无理取闹'
             ]
    font_size = 21
    text_depth = 0.8
    interval = 2
    for text, img_path in zip(texts, img_pathes):
        write_word(img_path, bigger_size, text, font_size, text_depth, interval)

# if __name__ == '__main__':
#     img_path = 'cat/cat.jpg'
#     bigger_size = 10
#     text = '卡哇伊伊啊多'
#     font_size = 21
#     text_depth = 0.8
#     interval = 2
#     write_word(img_path, bigger_size, text, font_size, text_depth, interval)
#
