# Pipeline de Visão Computacional

## Descrição

Pipeline de pré-processamento de imagens de peças metálicas utilizando OpenCV, preparando os dados para futuras aplicações de Machine Learning e Visão Computacional.

## Objetivo

Desenvolver um pipeline em Python para realizar o pré-processamento de um conjunto de imagens de peças metálicas, utilizando técnicas de Visão Computacional para padronizar e destacar características estruturais das imagens.

O projeto **não tem como objetivo classificar as peças entre com defeito e sem defeito**. O foco é preparar as imagens para uma futura etapa de modelagem com Machine Learning.

## Tecnologias

* Python
* OpenCV
* NumPy
* Git
* GitHub

## Estrutura do Projeto

```text
Pipeline_Visao_Computacional/
│
├── data/
│   └── raw/
│       ├── ok_front/
│       └── def_front/
│
├── src/
│   ├── __init__.py
│   └── image_processor.py
│
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

> A pasta `data/` contém as imagens do dataset e não será enviada ao GitHub, pois está incluída no `.gitignore`.

> A pasta `processed_images/` é criada automaticamente pelo pipeline para armazenar as imagens processadas e também está incluída no `.gitignore`.

## Etapas do Projeto

O desenvolvimento foi dividido em seis Sprints:

* **Sprint 1:** Configuração e versionamento
* **Sprint 2:** Estrutura e leitura das imagens
* **Sprint 3:** Pré-processamento básico
* **Sprint 4:** Segmentação e destaque de características
* **Sprint 5:** Refinamento morfológico e padronização
* **Sprint 6:** Salvamento dos resultados, documentação e apresentação

## Como Executar

1. Clone o repositório.
2. Crie e ative o ambiente virtual.
3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Faça o download do dataset disponibilizado na atividade.
5. Coloque as imagens na pasta `data/raw/`, mantendo as subpastas originais:

```text
data/
└── raw/
    ├── ok_front/
    └── def_front/
```

6. Execute o pipeline:

```bash
py main.py
```

7. A pasta `processed_images/` será criada automaticamente pelo pipeline para armazenar as imagens processadas.

> O dataset não é enviado ao GitHub, pois a pasta `data/` está incluída no `.gitignore`.

## Pipeline

O pipeline realiza as seguintes etapas:

```text
Carregamento das imagens
        ↓
Conversão para Grayscale
        ↓
Gaussian Blur
        ↓
Thresholding de Otsu
        ↓
Operações morfológicas
        ↓
Detecção de bordas com Canny
        ↓
Resize para 256x256
        ↓
Salvamento das imagens processadas
```

O processamento é realizado em lote, permitindo processar automaticamente todas as imagens encontradas no diretório de entrada.

### Thresholding

O método de thresholding utiliza **Otsu**, que calcula automaticamente um valor de limiar para separar regiões da imagem.

### Operações morfológicas

São utilizadas operações de dilatação e erosão para refinar a máscara binária e reduzir pequenos ruídos antes da detecção de bordas.

### Detecção de bordas

A detecção de bordas utiliza o algoritmo **Canny**, aplicado após a redução de ruído e o refinamento da máscara, para destacar contornos e características estruturais presentes nas imagens.

### Padronização

As imagens processadas são redimensionadas para **256x256 pixels**, garantindo um tamanho padronizado para uma futura etapa de Machine Learning.

### Salvamento

As imagens processadas são salvas automaticamente na pasta `processed_images/`, mantendo a organização das categorias `ok_front` e `def_front`.

## Status

✅ **Projeto concluído.**

### Sprints concluídos

* ✅ **Sprint 1:** Configuração e versionamento
* ✅ **Sprint 2:** Estrutura e leitura das imagens
* ✅ **Sprint 3:** Grayscale e redução de ruído com Gaussian Blur
* ✅ **Sprint 4:** Thresholding e detecção de bordas com Canny
* ✅ **Sprint 5:** Operações morfológicas e Resize para 256x256
* ✅ **Sprint 6:** Salvamento dos resultados e documentação
