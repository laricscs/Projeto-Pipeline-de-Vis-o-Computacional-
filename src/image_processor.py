import os
import cv2


class ImageProcessor:
    """Classe responsável pelo processamento das imagens."""

    def __init__(self, input_dir):
        """Inicializa o processador com o diretório das imagens de entrada."""
        self.input_dir = input_dir

    def find_images(self):
        """Localiza os arquivos de imagem dentro do diretório de entrada."""
        image_extensions = (".jpg", ".jpeg", ".png")
        images = []

        for root, _, files in os.walk(self.input_dir):
            for file in files:
                if file.lower().endswith(image_extensions):
                    images.append(os.path.join(root, file))

        return images

    def load_images(self, image_paths):

        """Carrega as imagens e mantém seus respectivos caminhos."""
        images = []

        for image_path in image_paths:
            image = cv2.imread(image_path)

            if image is not None:
                images.append((image_path, image))

        return images

    def grayscale(self, image):
        """Converte uma imagem BGR para escala de cinza."""

        # Converte a imagem colorida para tons de cinza.
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        return gray_image


    def blur(self, image):
        """Aplica Gaussian Blur para reduzir ruídos da imagem."""

        # Aplica um desfoque gaussiano para suavizar pequenas variações.
        blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

        return blurred_image


    def threshold(self, image):
        """Aplica thresholding de Otsu para separar objeto e fundo."""

        # Converte a imagem em uma representação binária.
        # O Otsu calcula automaticamente o melhor valor de limiar.
        _, threshold_image = cv2.threshold(
            image,
            0,
            255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )

        return threshold_image

    def morphology(self, image):
        """Aplica operações morfológicas para refinar a máscara."""

        # Cria um kernel 3x3 para realizar as operações morfológicas.
        kernel = cv2.getStructuringElement(
            cv2.MORPH_RECT,
            (3, 3)
        )

        # Dilata as regiões brancas, reforçando a estrutura da peça.
        dilated_image = cv2.dilate(
            image,
            kernel,
            iterations=1
        )

        # Aplica erosão para reduzir pequenos excessos e ruídos.
        morphed_image = cv2.erode(
            dilated_image,
            kernel,
            iterations=1
        )

        return morphed_image


    def canny(self, image):
        """Detecta bordas da imagem utilizando o algoritmo de Canny."""

        # Detecta as bordas presentes na imagem.
        edge_image = cv2.Canny(
            image,
            50,
            150
        )

        return edge_image


    def resize(self, image):
        """Redimensiona a imagem para um tamanho padronizado."""

        # Define o tamanho padrão das imagens.
        resized_image = cv2.resize(
            image,
            (256, 256)
        )

        return resized_image

