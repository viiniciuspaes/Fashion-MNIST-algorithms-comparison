from Intro_Inteligencia_Artificial.FashionMNIST import ImagePlot
import os
imagens = ImagePlot.imagens
labels = ImagePlot.labels

path = "./dataset"
csvname = os.path.join(path,"fashion-mnist_train.csv")
g = open(csvname, "r")

atributos = g.readlines()[0][6:-1].split(",")
g.close()

arffname = os.path.join(path,"FashionMNIST_Train.arff")
f = open(arffname,"w")
cabecalho = "%FashionMNIST Dataset\n\n@RELATION fashion_mnist_train\n\n"
f.write(cabecalho)
for pixel in range(len(atributos)):
    n = atributos[pixel]
    atributo = "@ATTRIBUTE {}  numeric\n".format(n)
    f.write(atributo)
classe = "@ATTRIBUTE class 	{0,1,2,3,4,5,6,7,8,9}\n\n"
f.write(classe)
f.write("@DATA\n")

for imagem in range(len(imagens)):
    linha = imagens[imagem]
    for pixel in linha:
        f.write(str(pixel)+",")
    f.write(str(labels[imagem]) + "\n")

f.close()