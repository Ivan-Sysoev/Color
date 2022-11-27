from PIL import Image, ImageDraw

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

def show(*colors):
    """Показывает цвет по заданному RGB параметру"""
    img_size = (400, 400)
    for color in colors:
        img = Image.new("RGB", img_size, color)
        draw = ImageDraw.Draw(img)
        print(color)
        img.show()

def palette(*args):
    """Смешивает цвета"""
    if len(args) == 1:
        return "there must be more than one argument"
    for i in range(len(args) - 1):
        if i == 0:
            result = [elem[0] + elem[1] for elem in list(zip(args[i], args[i + 1]))]
        else:
            result = [elem[0] + elem[1] for elem in list(zip(result, args[i + 1]))]
    for elem in result:
        if elem > 255:
            result[result.index(elem)] = 255
    return tuple(result)
    
def color_proccent(color, proccent):
    """Возращает часть цвета исходя из заданного процента"""
    return tuple([elem * proccent // 100 for elem in color])

def color_range(color, proccent=10):
    """Возражает градацию цвета от темного к яркому по заданному проценту"""
    result = []
    count = 100 // proccent
    for i in range(count - 1):
        a = i * proccent
        result.append(color_proccent((color), a))
    result.append(color)
    return tuple(result)

def multi_show(*colors):
    """Показывает несколько цветов на одном изображении (удобно для сравнения)"""
    img_size = (360, 360)
    width = img_size[0] / len(colors)
    img = Image.new("RGB", img_size, (255, 255, 255))
    draw = ImageDraw.Draw(img)
    for i in range(len(colors)):
        up_left_point = (0, i * width)
        up_right_point = (img_size[0], i * width)
        down_left_point = (0, (i + 1) * width)
        down_right_point = (img_size[0], (i + 1) * width)
        parametres = (up_left_point, down_left_point, down_right_point, up_right_point)
        draw.polygon(parametres, fill = colors[i])
    img.show()

multi_show(white, blue, red)