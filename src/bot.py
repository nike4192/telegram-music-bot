import asyncio
import os
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from dotenv import load_dotenv
from .audio_processor import AudioProcessor

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MusicStemsBot:
    def __init__(self):
        self.bot = Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))
        self.dp = Dispatcher()
        self.audio_processor = AudioProcessor()
        self._setup_handlers()

    def _setup_handlers(self):
        self.dp.message.register(self.start_handler, Command("start"))
        self.dp.message.register(self.audio_handler, F.audio)

    async def start_handler(self, message: types.Message):
        await message.answer(
            "Привет! Отправь мне аудиофайл, и я разделю его на стемы (вокал, барабаны, бас, остальное)"
        )

    async def audio_handler(self, message: types.Message):
        await message.answer("Обрабатываю аудио... Это может занять несколько минут.")

        # Скачивание файла
        file_info = await self.bot.get_file(message.audio.file_id)
        input_path = f"temp_{message.audio.file_id}.mp3"
        await self.bot.download_file(file_info.file_path, input_path)

        try:
            # Обработка через Demucs
            stems_paths = await self.audio_processor.separate_stems(input_path)

            # Отправка результатов
            for stem_name, stem_path in stems_paths.items():
                audio_file = types.FSInputFile(stem_path, filename=f"{stem_name}.wav")
                await message.answer_audio(audio_file)

            await message.answer("Готово! Все стемы отправлены.")

        except Exception as e:
            logger.error(f"Error processing audio: {e}")
            await message.answer("Произошла ошибка при обработке аудио.")

        finally:
            # Очистка временных файлов
            self.audio_processor.cleanup_temp_files()

    async def run(self):
        await self.dp.start_polling(self.bot)


async def main():
    bot = MusicStemsBot()
    await bot.run()


if __name__ == '__main__':
    asyncio.run(main())