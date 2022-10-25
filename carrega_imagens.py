import numpy as np
import os
import cv2
from sklearn.model_selection import train_test_split

diretorio_imgs = 'dataset/'

'''
    Esta função carrega todas as imagens de um diretório 'digito_dir', sendo este o dígito representado em todas as fotos.
    Por exemplo: no diretório "7" estão todas as imagens que representam o dígito 7 na linguagem de sinais
'''
def carrega_imagem_do_dir(digito_dir):
    diretorio = diretorio_imgs + str(digito_dir) + '/'
    imgs = []
    for arq in os.listdir(diretorio):
        img = cv2.imread(os.path.join(diretorio,arq), cv2.IMREAD_GRAYSCALE) # lê em preto&branco
        if img is not None:
            imgs.append(img)
    return imgs

def load():    
    # Para cada subpasta (de nomes 0 a 9) dentro da pasta "dataset", carregamos todas as imagens no vetor X e todos respectivos 
    # rótulos (labels), que coincidem com o número da subpasta, no vetor y.
    X = []
    y = np.array([])
    for dig_num in range(10):
        imgs = carrega_imagem_do_dir(dig_num)
        X.append(imgs)
        n_amostras = len(imgs)
        labels = np.repeat(dig_num, n_amostras)
        y = np.append(y, labels)
    X = np.array(X)

    # Colapsamos as duas primeiras dimensões de X para ficar compatível com y e também normalizamos 
    # os valores de entrada (de 0 a 255 para 0 a 1.0):
    X = X.reshape(X.shape[0]*X.shape[1], 400, 400)
    # X = X / 255.0
    # print(X.shape, y.shape)

    # Finalmente dividimos as entradas e saídas em dois grupos: de treino (80%) e de testes (20%). 
    # Também aplicamos *One Hot Encoding* nas saídas, para conseguirmos realizar a classificação:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

    #np.savez_compressed('Xs_and_ys', X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test)
    
    return (X_train, X_test, y_train, y_test)