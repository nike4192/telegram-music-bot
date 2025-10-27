import random
from audio_checker import check_audio_duration, format_time


class SimpleMusicBot:
    """
    Простой бот для проверки длительности аудио
    """
    
    def __init__(self):
        self.max_duration = 300  # 5 минут
        self.user_data = {}
    
    def process_message(self, message: str, user_id: int) -> str:
        """
        Обрабатывает сообщение от пользователя
        
        Args:
            message: текст сообщения
            user_id: ID пользователя
            
        Returns:
            ответ бота
        """
        message = message.lower().strip()
        
        if message == "/start":
            return "🎵 Привет! Я проверяю длительность аудио. Отправь мне число (секунды)"
        
        elif message == "/help":
            return "Просто отправь длительность аудио в секундах (например: 120)"
        
        elif message == "/settings":
            return f"⚙️ Максимальная длительность: {self.max_duration} сек"
        
        else:
            # Пытаемся понять число
            try:
                duration = float(message)
                result = check_audio_duration(duration, self.max_duration)
                return f"🔍 Проверяю {format_time(duration)}...\n{result}"
            except ValueError:
                return "Отправь число (длительность в секундах) или /help"


# Демонстрация работы бота
def demo():
    """Демонстрация работы бота"""
    bot = SimpleMusicBot()
    
    # Тестовые сообщения
    test_messages = [
        "/start",
        "120",      # нормальное аудио
        "400",      # слишком длинное
        "0.5",      # слишком короткое
        "hello",    # не число
        "/help",
        "65.5"      # нормальное
    ]
    
    print("🤖 Демонстрация работы бота:\n")
    
    for i, message in enumerate(test_messages, 1):
        response = bot.process_message(message, user_id=123)
        print(f"👤 Пользователь: {message}")
        print(f"🤖 Бот: {response}")
        print("-" * 40)


if __name__ == "__main__":
    # Запускаем демо
    demo()