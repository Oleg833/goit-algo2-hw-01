from random import randint

def quick_select(arr, k):
    """
    Знаходить k-й найменший елемент у несортованому масиві, використовуючи Quick Select.

    :param arr: Список чисел
    :param k: Позиція (1-based) найменшого елемента, який потрібно знайти
    :return: Значення k-го найменшого елемента
    """
    if not 1 <= k <= len(arr):
        raise ValueError("k має бути в межах від 1 до довжини масиву")

    def partition(low, high):
        pivot_index = randint(low, high)
        pivot = arr[pivot_index]
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        i = low
        for j in range(low, high):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i

    def quick_select_helper(low, high, k_smallest):
        if low == high:
            return arr[low]

        pivot_index = partition(low, high)

        if pivot_index == k_smallest:
            return arr[pivot_index]
        elif pivot_index > k_smallest:
            return quick_select_helper(low, pivot_index - 1, k_smallest)
        else:
            return quick_select_helper(pivot_index + 1, high, k_smallest)


    return quick_select_helper(0, len(arr) - 1, k - 1)

if __name__ == "__main__":
    array = [3, 2, 1, 5, 4]
    k = 3
    print(f"{k}-й найменший елемент: {quick_select(array, k)}")
