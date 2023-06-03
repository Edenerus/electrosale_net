from django.core.exceptions import ValidationError


def validate_provider(value):
    if value.type == 0 and value.provider:
        raise ValidationError(f"{value} является заводом и не может иметь поставщиков")
    if value.provider.level == 2:
        raise ValidationError(f"{value.provider} не может быть поставщиком для {value}, т.к его уровень сети 2 ")