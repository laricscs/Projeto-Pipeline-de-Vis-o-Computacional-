from src.image_processor import ImageProcessor
import cv2


def main():
    """Executa o pipeline de processamento das imagens."""

    # Cria o processador informando a pasta das imagens de entrada.
    processor = ImageProcessor("data/raw")

    # Localiza todas as imagens disponíveis na pasta de entrada.
    image_paths = processor.find_images()

    print(f"Imagens encontradas: {len(image_paths)}")

    # Carrega as imagens encontradas.
    images = processor.load_images(image_paths)

    print(f"Imagens carregadas: {len(images)}")

    # Conta quantas imagens serão processadas.
    processed_count = 0

    # Percorre todas as imagens carregadas.
    for image_path, image in images:

        # Converte a imagem para escala de cinza.
        gray_image = processor.grayscale(image)

        # Reduz ruídos antes das próximas etapas.
        blurred_image = processor.blur(gray_image)

        # Cria a máscara binária da imagem.
        threshold_image = processor.threshold(blurred_image)

        # Detecta as bordas da peça.
        edge_image = processor.canny(blurred_image)

        # Incrementa o contador após concluir o processamento.
        processed_count += 1



    print(f"Imagens processadas: {processed_count}")



if __name__ == "__main__":
    main()