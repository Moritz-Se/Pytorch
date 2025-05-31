import os
from PIL import Image

# --- Konfiguration ---
input_folder = "../pictures/Pictures_to_change"         # Ordner mit 320x240 Bildern
output_folder = "../pictures/Changed_pictures"      # Ordner für 32x32 Grayscale Ausschnitte
box_coords = [                        # Liste von Box-Koordinaten: (x1, y1, x2, y2)
    (32, 32, 95, 73),(104, 32, 166, 73),(172, 32, 236, 73),(243, 32, 313, 73),
    (32, 82, 95, 123),(104, 82, 166, 123),(172, 82, 236, 123),(243, 82, 313, 123),
    (32, 129, 95, 169),(104, 129, 166, 169),(172, 129, 236, 169),(243, 129, 313, 169),
    (23, 177, 95, 222),(104, 177, 166, 222),(172, 177, 236, 222),(243, 177, 313, 222),
    # Füge weitere Boxen hier hinzu...
]

# --- Sicherstellen, dass Ausgabeverzeichnis existiert ---
os.makedirs(output_folder, exist_ok=True)

# --- Verarbeitung der Bilder ---
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
        image_path = os.path.join(input_folder, filename)
        image = Image.open(image_path).convert('L')  # Konvertieren in Grayscale

        for idx, (x1, y1, x2, y2) in enumerate(box_coords):
            cropped = image.crop((x1, y1, x2, y2))
            resized = cropped.resize((32, 32), Image.Resampling.LANCZOS)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_box{idx}.png")
            resized.save(output_path)

print("Fertig: Alle Boxen extrahiert, skaliert und als Grayscale gespeichert.")
