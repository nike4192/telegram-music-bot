def check_audio_duration(duration_seconds: float, max_duration: int = 300) -> str:
    """
    Проверяет длительность аудио и возвращает результат
    
    Args:
        duration_seconds: длительность в секундах
        max_duration: максимальная допустимая длительность
        
    Returns:
        Сообщение с результатом проверки
    """
    if duration_seconds > max_duration:
        return f"❌ Слишком длинное аудио! {duration_seconds:.1f} сек > {max_duration} сек"
    
    if duration_seconds < 1:
        return "❌ Слишком короткое аудио! Минимум 1 секунда"
    
    return f"✅ Аудио ок! {duration_seconds:.1f} сек"


def format_time(seconds: float) -> str:
    """
    Форматирует секунды в минуты:секунды
    """
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes:02d}:{seconds:02d}"


# Пример использования
if __name__ == "__main__":
    # Тестируем функцию
    test_durations = [45.5, 350.0, 0.5, 125.0]
    
    for duration in test_durations:
        result = check_audio_duration(duration)
        print(f"{format_time(duration)} - {result}")