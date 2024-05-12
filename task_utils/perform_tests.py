import pandas as pd
import requests
from threading import Thread
import timeit
from typing import Any, Callable, Dict, List, Tuple, Union

from task_utils.search_algorithms import booyer_moore_search, kmp_search, rabin_karp_search


def get_algo_results(search_func: Callable, **kwargs) -> Tuple[float, any]:
    text: str = kwargs.get("text")
    pattern: str = kwargs.get("pattern")
    start_time = timeit.default_timer()
    result = search_func(text, pattern)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    return execution_time, result


def test_algo(search_func: Callable, text: str, pattern: str) -> Dict[str, Union[str, int, float]]:
    search_res = get_algo_results(search_func, text=text, pattern=pattern)
    results = {
        "Pattern Presence": search_res[1] != -1,
        "Algorithm": search_func.__name__,
        "Time": search_res[0],
        "Text Length": len(text),
        "Pattern Length": len(pattern)
    }
    return results


def run_search_tests(res: list, text: str, pattern: str, runs_number: int = 1) -> list:
    for _ in range(runs_number):
        for call in [booyer_moore_search, kmp_search, rabin_karp_search]:
            t = Thread(target=res.append, args=(test_algo(call, text, pattern),))
            t.start()
            t.join()
    return res


def run_tests(res: pd.DataFrame,
              runs_number: int = 3,
              ) -> pd.DataFrame:
    results = []
    text_1 = requests.get("https://drive.usercontent.google.com/u/0/uc?id=18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh&export=download").text
    text_2 = requests.get("https://drive.usercontent.google.com/u/0/uc?id=13hSt4JkJc11nckZZz2yoFHYL89a4XkMZ&export=download").text
    valid_patterns = ["хеш-таблиці", "підход", "до", "для", "програм", "а"]
    invalid_patterns = ["інтернет", "фізика", "математика", "хімія", "біологія", "сг"]
    for text, pattern in [(t, p) for t in [text_1, text_2] for p in valid_patterns]:
        t = Thread(target=run_search_tests, args=(results, text, pattern, runs_number))
        t.start()
        t.join()
    for text, pattern in [(t, p) for t in [text_1, text_2] for p in invalid_patterns]:
        t = Thread(target=run_search_tests, args=(results, text, pattern, runs_number))
        t.start()
        t.join()
    res = pd.concat([pd.DataFrame(results), res])
    return res

