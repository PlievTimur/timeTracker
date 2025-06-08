import json
import os
from typing import Dict, Any

class Translator:
    def __init__(self, lang: str = "en"):
        self.lang = lang
        self.translations = self.load_translations()

    def load_translations(self) -> Dict[str, Any]:
        file_path = os.path.join("lang","translations", f"{self.lang}.json")
        if not os.path.exists(file_path):
            file_path = os.path.join("translations", "en.json")  # Fallback
        with open(file_path, encoding="utf-8") as f:
            return json.load(f)

    def translate(self, key: str, **kwargs) -> str:
        result = self.translations
        for k in key.split("."):
            result = result.get(k, "")
        return result.format(**kwargs) if isinstance(result, str) else result