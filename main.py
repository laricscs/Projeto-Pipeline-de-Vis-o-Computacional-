from src.image_processor import ImageProcessor


def main():
    """Executa o pipeline de processamento de imagens."""

    # Cria o processador informando a pasta de imagens de entrada.
    processor = ImageProcessor("data/raw")

    # Localiza todas as imagens disponíveis na pasta de entrada.
    image_paths = processor.find_images()

    # Carrega todas as imagens encontradas na memória.
    images = processor.load_images(image_paths)

    print(f"Imagens encontradas: {len(image_paths)}")
    print(f"Imagens carregadas: {len(images)}")

    # Conta quantas imagens foram percorridas.
    processed_count = 0

    for image_path, image in images:
        processed_count += 1

    print(f"Imagens percorridas: {processed_count}")

if __name__ == "__main__":
    main()