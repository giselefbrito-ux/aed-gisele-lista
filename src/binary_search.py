from src.my_array import MyArray


def binary_search(array: MyArray, target: int) -> int:
    """
    Realiza busca binária em um array ordenado.

    Deve retornar o índice do elemento ou -1 caso não encontrado.
    """
    esquerda_array = 0
    direita_array = -1

    while esquerda_array <= direita array:
        meio =  esquerda_array+direita_array // 2
        value = array.get(mid)

        if value == target:
            return meio
        elif value < target:
            esquerda_array = meio + 1
        else:
             direita_array = meio - 1
            
