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

