import os
import struct
import numpy as np

"""
Loosely inspired by http://abel.ee.ucla.edu/cvxopt/_downloads/mnist.py
which is GPL licensed.
"""

def read(imagens = "testing", path = "./dataset"):
    """
    Python function for importing the MNIST data set.  It returns an iterator
    of 2-tuples with the first element being the label and the second element
    being a numpy.uint8 2D array of pixel data for the given image.
    """

    if imagens is "training":
        fname_img = os.path.join(path, 'train-images-idx3-ubyte')
        fname_lbl = os.path.join(path, 'train-labels-idx1-ubyte')
    elif imagens is "testing":
        fname_img = os.path.join(path, 't10k-images-idx3-ubyte')
        fname_lbl = os.path.join(path, 't10k-labels-idx1-ubyte')
    else:
        print("imagens must be 'testing' or 'training'")
        raise ValueError


    # Load everything in some numpy arrays
    with open(fname_lbl, 'rb') as flbl:
        magic, num = struct.unpack(">II", flbl.read(8))
        lbl = np.fromfile(flbl, dtype=np.int8)

    with open(fname_img, 'rb') as fimg:
        magic, num, rows, cols = struct.unpack(">IIII", fimg.read(16))
        img = np.fromfile(fimg, dtype=np.uint8).reshape(len(lbl), rows, cols)

    get_img = lambda idx: (lbl[idx], img[idx])

    # Create an iterator which returns each image in turn
    for i in range(len(lbl)):
        yield get_img(i)

def show(image):
    """
    Render a given numpy.uint8 2D array of pixel data.
    """
    from matplotlib import pyplot
    import matplotlib as mpl
    fig = pyplot.figure()
    ax = fig.add_subplot(1,1,1)
    imgplot = ax.imshow(image, cmap=mpl.cm.Greys)
    imgplot.set_interpolation('nearest')
    ax.xaxis.set_ticks_position('top')
    ax.yaxis.set_ticks_position('left')
    pyplot.show()


# arq = lista de tuplas: [(label, np.array([[p1,..p28],[p29,..]...],dtype=uint8),(label, array([[p1,..p28],[p29,..]...],dtype=uint8)...]
# labels, imagens, aux, imagens_grafico = [], [], [], []

arq_treino = list(read(imagens="training"))
for linha in range(len(arq_treino)):
    label, imagem = arq_treino[linha]
    labels.append(label)
    imagens_grafico.append(imagem)
    for linha_matriz in imagem:
        for pixel in linha_matriz:
            aux.append(pixel)
    imagens.append(aux)
    aux = []


arq_teste = list(read())
for linha in range(len(arq_teste)):
    label, imagem = arq_teste[linha]
    labels.append(label)
    imagens_grafico.append(imagem)
    for linha_matriz in imagem:
        for pixel in linha_matriz:
            aux.append(pixel)
    imagens.append(aux)
    aux = []

show(imagens_grafico[9])
print(imagens_grafico[9])

c = np.array(imagens)
print(len(imagens), len(imagens[0]),len(labels))
# # print(labels[1])

camiseta, calca, casaco, vestido, sobretudo, sandalia, camisa, tenis, bolsa, bota = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
classes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
posicoes = []
for classe in classes:
    pos = labels.index(classe)
    print(pos)
    posicoes.append(pos)
    show(imagens_grafico[pos])

for l in range(len(labels)):
    if labels[l]==4:
        show(imagens_grafico[l])

