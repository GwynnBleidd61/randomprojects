def intcode(x):
    result = "i" + str(x) + "e"
    return result

def stringcode(x):
    result = str(len(x)) + ":" + x
    return result

def bencode(x):
    if type(x) == int:
        return bytes(intcode(x), encoding='utf8')
    elif type(x) == str:
        return bytes(stringcode(x), encoding='utf8')
    elif type(x) == list:
        return bytes(listcode(x), encoding='utf8')
    elif type(x) == dict:
        return bytes(dictcode(x), encoding='utf8')

def check_type(x):
    if type(x) == int:
        return intcode(x)
    elif type(x) == str:
        return stringcode(x)
    elif type(x) == list:
        return listcode(x)
    elif type(x) == dict:
        return dictcode(x)

def listcode(listok):
    result = "l"
    for member in listok:
        result += check_type(member)
    result += 'e'
    return result

def dictcode(dictionary):
    result = 'd'
    dictionary = dict(sorted(dictionary.items(), key=lambda item: item[0]))
    keys = dictionary.keys()
    for key in keys:
        result += (check_type(key) + check_type(dictionary[key]))
    result += 'e'
    return result

def int_decoder(input_string, iterator):
    assert input_string[iterator] == 'i'
    end = input_string.index('e', iterator)
    return int(input_string[iterator + 1:end]), end + 1

def string_decoder(input_string, iterator):
    colon = input_string.index(':', iterator)
    length = int(input_string[iterator:colon])
    start = colon + 1
    end = start + length
    return input_string[start:end], end

def list_decoder(input_string, iterator):
    assert input_string[iterator] == 'l'
    result = []
    iterator += 1
    while input_string[iterator] != 'e':
        value, iterator = decode_next(input_string, iterator)
        result.append(value)
    return result, iterator + 1

def dict_decoder(input_string, iterator):
    assert input_string[iterator] == 'd'
    result = {}
    iterator += 1
    while input_string[iterator] != 'e':
        key, iterator = string_decoder(input_string, iterator)
        value, iterator = decode_next(input_string, iterator)
        result[key] = value
    return result, iterator + 1

def decode_next(input_string, iterator):
    if input_string[iterator] == 'i':
        return int_decoder(input_string, iterator)
    elif input_string[iterator].isdigit():
        return string_decoder(input_string, iterator)
    elif input_string[iterator] == 'l':
        return list_decoder(input_string, iterator)
    elif input_string[iterator] == 'd':
        return dict_decoder(input_string, iterator)
    else:
        raise ValueError(f"Invalid bencode format at position {iterator}")

def bdecode(bencoded):
    decoded_string = bencoded.decode()
    result, _ = decode_next(decoded_string, 0)
    return result
