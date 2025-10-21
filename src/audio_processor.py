import os
import tempfile
import demucs.separate
from pathlib import Path


class AudioProcessor:
    def __init__(self):
        self.temp_dir = tempfile.mkdtemp()
        self.model_name = "htdemucs"  # Быстрая модель

    async def separate_stems(self, input_path: str) -> dict:
        """Разделяет аудио на стемы"""
        output_dir = Path(self.temp_dir) / "separated"

        # Запуск Demucs
        demucs.separate.main([
            "--mp3",
            "--mp3-bitrate", "320",
            "-n", self.model_name,
            "-o", str(output_dir),
            input_path
        ])

        # Поиск созданных файлов
        stems_dir = output_dir / self.model_name / Path(input_path).stem
        stems = {}

        for stem_file in stems_dir.glob("*.mp3"):
            stem_name = stem_file.stem
            stems[stem_name] = str(stem_file)

        return stems

    def cleanup_temp_files(self):
        """Очистка временных файлов"""
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)