from __future__ import annotations

import os

from dotenv import load_dotenv

load_dotenv()

# ==========================================
# Spotify
# ==========================================

SPOTIFY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

# ==========================================
# yt-dlp
# ==========================================

YTDLP_OPTIONS = {
    "format": "bestaudio/best",
    "noplaylist": True,
    "quiet": True,
    "no_warnings": True,
    "default_search": "ytsearch",
    "extract_flat": False,
    "socket_timeout": 15,
    "cache_dir": False,
    # Evita que FFmpeg descargue bloques fragmentados vacíos
    "http_chunk_size": 1048576, 
    # Fuerza a yt-dlp a simular clientes menos restrictivos (móviles/TV)
    "extractor_args": {
        "youtube": {
            "player_client": ["android", "web", "tv"],
        }
    },
}

# ==========================================
# FFmpeg
# ==========================================

FFMPEG_OPTIONS = {
    "before_options": (
        "-reconnect 1 "
        "-reconnect_streamed 1 "
        "-reconnect_delay_max 5 "
        # ESTO ES CRÍTICO: Fuerza a FFmpeg a enviar las mismas credenciales y User-Agent que yt-dlp
        "-headers \"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36\r\n\""
    ),
    "options": "-vn",
}