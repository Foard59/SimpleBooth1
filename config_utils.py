import os
import json
import logging

PHOTOS_FOLDER = 'photos'
EFFECT_FOLDER = 'effet'
CONFIG_FILE = 'config.json'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

DEFAULT_CONFIG = {
    'footer_text': 'Photobooth',
    'timer_seconds': 3,
    'high_density': False,
    'slideshow_enabled': False,
    'slideshow_delay': 60,
    'slideshow_source': 'photos',
    'effect_enabled': False,
    'effect_prompt': 'Transform this photo into a beautiful ghibli style',
    'effect_steps': 5,
    'runware_api_key': '',
    'telegram_enabled': False,
    'telegram_bot_token': '',
    'telegram_chat_id': '',
    'telegram_send_type': 'photos',
    'camera_type': 'picamera',
    'usb_camera_id': 0,
    'printer_enabled': True,
    'printer_port': '/dev/ttyAMA0',
    'printer_baudrate': 9600,
    'print_resolution': 384,
    # Configuration for punchlines and animations
    'display': {
        'durationMs': 1500,
        'position': 'center'
    },
    'phrases': [
        "Ok, on se croit sur Insta ?",
        "Allez, pose Kaamelott saison 6.",
        "Regarde l’objectif comme ton grec à 3h.",
        "Sourire niveau passe Navigo.",
        "On dirait la photo de ta carte Vitale.",
        "Fais genre t’as eu le dernier drop.",
        "Hop, future PP Discord.",
        "Tête ‘j’ai trouvé 5€ par terre’.",
        "Coucou, c’est pour le groupe WhatsApp.",
        "Flash nous comme un paparazzi à Cannes."
    ],
    'animation': {
        'enabled': True,
        'probability': 0.25,
        'durationMs': 800,
        'assets': [
            'emoji:🐵'
        ]
    },
    'sound': {
        'enabled': False
    }
}

logger = logging.getLogger(__name__)

def ensure_directories():
    """Create photos and effect folders if missing"""
    logger.info(f"[DEBUG] Création du dossier photos: {PHOTOS_FOLDER}")
    os.makedirs(PHOTOS_FOLDER, exist_ok=True)
    logger.info(f"[DEBUG] Création du dossier effet: {EFFECT_FOLDER}")
    os.makedirs(EFFECT_FOLDER, exist_ok=True)
    logger.info(
        f"[DEBUG] Dossiers créés - Photos: {os.path.exists(PHOTOS_FOLDER)}, Effet: {os.path.exists(EFFECT_FOLDER)}"
    )

def load_config():
    """Load configuration from JSON and merge with defaults"""
    config = DEFAULT_CONFIG.copy()
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, dict):
                    config.update(data)
        except Exception:
            pass
    return config

def save_config(config_data):
    """Save configuration to JSON"""
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(config_data, f, indent=2, ensure_ascii=False)
