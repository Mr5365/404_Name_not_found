import subprocess
import os

# ✅ CONFIRMED COLMAP PATH
COLMAP_BAT = r"C:\Users\keven\OneDrive\Desktop\COLMAP\COLMAP.bat"

IMAGES_DIR = "uploads"
WORKSPACE_DIR = "colmap_workspace"

def run_colmap():
    os.makedirs(WORKSPACE_DIR, exist_ok=True)

    images = os.listdir(IMAGES_DIR)
    if not images:
        print("❌ No images found in uploads folder")
        return

    print(f"✅ Found {len(images)} images")
    print("🚀 Launching COLMAP...")

    command = (
        f'"{COLMAP_BAT}" automatic_reconstructor '
        f'--image_path "{IMAGES_DIR}" '
        f'--workspace_path "{WORKSPACE_DIR}" '
        f'--quality low'
    )

    print("🧾 Running command:")
    print(command)

    subprocess.run(command, shell=True)

    print("✅ COLMAP finished reconstruction")

if __name__ == "__main__":
    run_colmap()
