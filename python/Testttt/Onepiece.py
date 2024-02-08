import re


def Onepiece(x):
    # Translate names to correct ones
    name_translations = {
        r'l.*u.*f.*y.*': 'Lufy',
        r'z.*o.*r.*o.*': 'Zoro',
        r's.*a.*n.*g.*i.*': 'Sangi',
        r'n.*a.*m.*i.*': 'Nami',
        r'c.*h.*o.*p.*p.*e.*r.*': 'Chopper'
    }

    # Translate the names in the input string using regular expressions
    for pattern, replacement in name_translations.items():
        x = re.sub(pattern, replacement, x, flags=re.I)

    # Filter names not in the Straw Hat Pirates crew
    valid_names = ['Lufy', 'Zoro', 'Sangi', 'Nami', 'Chopper', 'Brook', 'Franky', 'Usopp', 'Jimbei']
    valid_words = [word for word in x.split() if word.lower() in [v.lower() for v in valid_names]]

    # Capitalize the first letter and sort the valid names
    valid_words = [word.capitalize() for word in valid_words]
    valid_words.sort()

    return ' '.join(valid_words)


if __name__ == '__main__':
    # Example usage
    input_str = 'luffffy zzoro rrrrroiib chhhhopper'
    result = Onepiece(input_str)
    print(result)