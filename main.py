import timeit
from typing import Dict, List, Tuple


def find_coins_greedy(amount: int, coins: List[int]) -> Dict[int, int]:
    """
    Жадібний алгоритм видачі мінімальної кількості монет.
    
    Args:
        amount (int): Сума, яку потрібно видати.
        coins (List[int]): Доступні номінали монет.

    Returns:
        Dict[int, int]: Словник з номіналами монет та їх кількістю.
    """
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= count * coin
    return result


def find_min_coins(amount: int, coins: List[int]) -> Dict[int, int]:
    """
    Динамічний алгоритм видачі мінімальної кількості монет.
    
    Args:
        amount (int): Сума, яку потрібно видати.
        coins (List[int]): Доступні номінали монет.

    Returns:
        Dict[int, int]: Словник з номіналами монет та їх кількістю.
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)
    
    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    if dp[amount] == float('inf'):
        return {}  # Неможливо видати цю суму
    
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    
    return result


def measure_time(func, amount: int, coins: List[int]) -> Tuple[Dict[int, int], float]:
    """
    Вимірює час виконання алгоритму.
    
    Args:
        func: Функція для вимірювання.
        amount (int): Сума для видачі.
        coins (List[int]): Доступні номінали монет.

    Returns:
        Tuple[Dict[int, int], float]: Результат функції та час виконання.
    """
    start_time = timeit.default_timer()
    result = func(amount, coins)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    return result, execution_time


if __name__ == "__main__":
    coins = [50, 25, 10, 5, 2, 1]
    amounts = [56, 98, 113, 560, 982]
    
    for amount in amounts:
        print(f"\nAmount: {amount}")
        
        greedy_result, greedy_time = measure_time(find_coins_greedy, amount, coins)
        print(f"Greedy algorithm result: {greedy_result}")
        print(f"Greedy algorithm execution time: {greedy_time:.8f} seconds")
        
        dp_result, dp_time = measure_time(find_min_coins, amount, coins)
        print(f"Dynamic programming result: {dp_result}")
        print(f"Dynamic programming execution time: {dp_time:.8f} seconds")