import pytest
import datetime
from zoneinfo import ZoneInfo

def format_price(price: str) -> str:
    """
    Форматирует строковое представление цены в человекочитаемый вид.

    Функция:
    - пытается преобразовать входное значение в число (`float`);
    - округляет значение до двух знаков после запятой;
    - разделяет целую часть на группы по три цифры с пробелом;
    - всегда использует точку как десятичный разделитель.

    Если входное значение нельзя преобразовать в число (например, это
    не строка или строка не является числом), функция возвращает его
    без изменений.

    Примеры:
        >>> format_price("1234")
        '1 234.00'
        >>> format_price("1234567.8")
        '1 234 567.80'
        >>> format_price("99.999")
        '100.00'
        >>> format_price("abc")
        'abc'
        >>> format_price(None)
        None

    :param price: Цена в виде строки, содержащей числовое значение.
    :return: Отформатированная строка цены или исходное значение,
             если форматирование невозможно.
    """
    try:
        price_float = float(price)
        price_str = f"{price_float:.2f}"
        integer_part, decimal_part = price_str.split(".")
        formatted_parts = []
        for i in range(len(integer_part), 0, -3):
            start = max(0, i - 3)
            formatted_parts.insert(0, integer_part[start:i])
        return " ".join(formatted_parts) + "." + decimal_part
    except (ValueError, AttributeError):
        return price


@pytest.mark.parametrize("input_price,expected_output", [
    ("0", "0.00"),
    ("5", "5.00"),
    ("50.7", "50.70"),
    ("100", "100.00"),
    ("-1234", "-1 234.00"),
    ("99.999", "100.00"),
    ("0.001", "0.00"),
    ("1000000", "1 000 000.00"),
    ("-57899.67", "-57 899.67"),
    ("00123", "123.00"),
])
def test_positive_formatprice(input_price, expected_output):
    result = format_price(input_price)
    assert format_price(input_price) == expected_output

@pytest.mark.parametrize("input_value,expected_output", [
    ("cat", "cat"),
    (None, None),
    (True, True),
    (45.67, 45.67),
    (123, 123),
    ("", ""),
    (" ", " "),
    ("$@#", "$@#"),
    ("12.34.56", "12.34.56"),
    ("99,999", "99,999"),

])
def test_negative_formatprice(input_value, expected_output):
    result = format_price(input_value)
    assert format_price(input_value) == expected_output