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

> A pasta `processed_images/` será criada automaticamente pelo pipeline na etapa de salvamento dos resultados.

## Etapas do Projeto

O desenvolvimento será dividido em seis Sprints:

* **Sprint 1:** Configuração e versionamento
* **Sprint 2:** Estrutura e leitura das imagens
* **Sprint 3:** Pré-processamento básico
* **Sprint 4:** Segmentação e destaque de características
* **Sprint 5:** Refinamento morfológico e padronização
* **Sprint 6:** Salvamento, documentação e apresentação

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

## Pipeline Atual

Até o momento, o pipeline realiza:

```text
Carregamento das imagens
        ↓
Conversão para Grayscale
        ↓
Gaussian Blur
```

O processamento é realizado em lote, permitindo processar automaticamente as imagens encontradas no diretório de entrada.

## Status

🚧 Projeto em desenvolvimento.

### Sprints concluídos

* ✅ **Sprint 1:** Configuração e versionamento
* ✅ **Sprint 2:** Estrutura e leitura das imagens
* ✅ **Sprint 3:** Grayscale e redução de ruído com Gaussian Blur

### Próximas etapas

* ⏳ **Sprint 4:** Thresholding e detecção de bordas
* ⏳ **Sprint 5:** Operações morfológicas e Resize
* ⏳ **Sprint 6:** Salvamento dos resultados, documentação e apresentação
