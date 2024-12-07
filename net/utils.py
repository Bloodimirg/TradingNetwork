def save_supplier(instance, *args, **kwargs):
    """
    Сохранение для модели Supplier, включая вычисление уровня.
    """
    if not instance.level:
        instance.level = calculate_hierarchy_level(instance.supplier)
    super(instance.__class__, instance).save(*args, **kwargs)

def calculate_hierarchy_level(supplier):
    """
    Вычисляет уровень иерархии для текущего звена сети.
    """
    if supplier is None:
        return 0  # Завод (LEVEL)
    return supplier.level + 1
