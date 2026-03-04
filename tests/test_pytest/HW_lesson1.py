import pytest
from datetime import datetime, timedelta
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


def generate_week_schedule(
    days_ahead: int = 7, tz: str = "Europe/Helsinki"
) -> list[tuple[str, str, str]]:
    """
    Генерирует расписание на несколько дней вперёд с учётом часового пояса.

    Для каждого дня формируется кортеж из трёх элементов:
    - сокращённое название дня недели (Mo, Tu, We, Th, Fr, Sa, Su);
    - дата в формате DD/MM;
    - строка с временем работы или значением "Closed" для выходных.

    Логика работы:
    - отсчёт начинается с текущей даты в указанном часовом поясе;
    - для будних дней (понедельник–пятница) время работы фиксировано:
      "00:05–22:55";
    - для выходных (суббота и воскресенье) возвращается "Closed";
    - количество дней определяется параметром `days_ahead`.

    Примеры:
        >>> generate_week_schedule(3, tz="Europe/Helsinki")
        [('Mo', '01/01', '00:05–22:55'),
         ('Tu', '02/01', '00:05–22:55'),
         ('We', '03/01', '00:05–22:55')]

        >>> generate_week_schedule(2, tz="Europe/Helsinki")
        [('Sa', '06/01', 'Closed'),
         ('Su', '07/01', 'Closed')]

    :param days_ahead: Количество дней вперёд, для которых нужно сгенерировать
                       расписание (по умолчанию 7).
    :param tz: Часовой пояс в формате IANA (например, "Europe/Helsinki").
    :return: Список кортежей вида (день_недели, дата, время_работы).
    """
    day_names = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
    today = datetime.now(ZoneInfo(tz)).date()
    lst = []
    for i in range(days_ahead):
        d = today + timedelta(days=i)
        wd = d.weekday()  # 0..6
        day_abbr = day_names[wd]
        date_str = d.strftime("%d/%m")
        time_str = "Closed" if wd >= 5 else "00:05–22:55"
        lst.append((day_abbr, date_str, time_str))
    return lst

@pytest.mark.parametrize("days_ahead, expected_length", [
    (1, 1),
    (5, 5),
    (7, 7),
    (14, 14),
    (0, 0),
    (30, 30),
])
def test_schedule_length(days_ahead, expected_length):
    result = generate_week_schedule(days_ahead)
    assert len(result) == expected_length

@pytest.mark.parametrize("tz_name", [
    "Europe/Helsinki",
    "Pacific/Honolulu",
    "Asia/Tokyo",
    "America/New_York",
    "Europe/London",
    "Australia/Sydney",
    "America/Los_Angeles",
])
def test_timezone_consistency(tz_name):

    result = generate_week_schedule(1, tz_name)
    now = datetime.now(ZoneInfo(tz_name)).date()

    day_names = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]

    assert result[0][0] == day_names[now.weekday()]
    assert result[0][1] == now.strftime("%d/%m")
