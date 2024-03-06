def inverter_string(s):
    caracteres = list(s)

    tamanho = len(caracteres)

    for i in range(tamanho // 2):
        caracteres[i], caracteres[tamanho - 1 -
                                  i] = caracteres[tamanho - 1 - i], caracteres[i]

    string_invertida = ''.join(caracteres)

    return string_invertida


string_original = input("Digite uma string: ")
string_invertida = inverter_string(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)
