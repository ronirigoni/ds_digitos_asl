# Classificador de Dígitos ASL

Neste projeto criamos um classificador de dígitos (de 0 a 9) para a linguagem de sinais americana (*ASL - American Sign Language*).

Para treinar o modelo nós utilizamos uma base de dados disponível no Kaggle ([veja aqui](https://www.kaggle.com/datasets/rayeed045/american-sign-language-digit-dataset)), que consiste em 5.000 imagens (400x400px) de sinais feitos com as mãos, que representam os dígitos de 0 a 9, e estão devidamente identificados (em pastas numeradas de 0 a 9, sendo 500 imagens por dígito). Apesar das imagens serem coloridas, transformamos em preto e branco para diminuir a complexidade do nosso modelo.

Primeiramente desenvolvemos um modelo de *Deep Learning* com 5 camadas convolutivas seguidas de duas densas, que após alguns ajustes chegou a uma acurácia de 99,10% na base de testes (modelo salvo como modelo-cnn-v20), que é bastante satisfatório para este problema.

