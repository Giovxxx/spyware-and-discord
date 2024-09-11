import cv2

def capture_camera_image(output_file):
    # Apri la fotocamera (0 per la fotocamera predefinita)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Errore: Impossibile aprire la fotocamera.")
        return

    # Cattura un frame dalla fotocamera
    ret, frame = cap.read()

    if not ret:
        print("Errore: Impossibile catturare un'immagine dalla fotocamera.")
        cap.release()
        return

    # Salva l'immagine catturata
    cv2.imwrite(output_file, frame)
    print(f"Immagine salvata in '{output_file}'.")

    # Rilascia la fotocamera e chiudi tutte le finestre
    cap.release()
    cv2.destroyAllWindows()

# Percorso del file di output
output_file = "camera_image.png"

# Cattura e salva l'immagine dalla fotocamera
capture_camera_image(output_file)
