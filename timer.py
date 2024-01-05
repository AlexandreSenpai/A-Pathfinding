import time


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  # Tempo de início
        result = func(*args, **kwargs)  # Executa a função
        end_time = time.perf_counter()  # Tempo de término
        print(f"Tempo de execução de {func.__name__}: {end_time - start_time} segundos")
        return result
    return wrapper