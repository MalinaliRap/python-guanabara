# Função para detectar o tipo de um input
def detect_input_type(user_input):
    # Tenta converter para inteiro
    try:
        int_value = int(user_input)
        return 'int', int_value
    except ValueError:
        pass
    
    # Tenta converter para float
    try:
        float_value = float(user_input)
        return 'float', float_value
    except ValueError:
        pass
    
    # Tenta converter para boolean
    if user_input.lower() in ['true', 'false']:
        bool_value = user_input.lower() == 'true'
        return 'bool', bool_value
    
    # Tenta converter para None
    if user_input.lower() == 'none':
        return 'NoneType', None
    
    # Se nenhuma conversão funcionar, retorna como string
    return 'str', user_input

user_input = input('digite algo:')

# Detecta e exibe o tipo
input_type, converted_value = detect_input_type(user_input)

                        
print('O tipo primitivo desse valor é: {}'.format(input_type))
print('Valor convertido: {}'.format(converted_value))
print('So tem espaços?', user_input.isspace())
print('E um numero?', user_input.isnumeric())
print('E alfabetico?', user_input.isalpha())
print('E alfanumerico?', user_input.isalnum())
print('Esta em maiusculas?', user_input.isupper())
print('Esta em minusculas?', user_input.islower())
print('Esta capitalizado?', user_input.istitle())