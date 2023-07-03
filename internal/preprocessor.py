special_symbols = [
    '\n',
    '\v',
    '\t'
]

scip_symbols = [
    '--',
    '\\d',
    '\\set'
]

def file_preprocess(lines):
    result = []
    common_strin = ""
    for line in lines:
        not_interesting_string = False
        for symbol in scip_symbols:
            not_interesting_string = (not_interesting_string or (symbol in line))
        if not_interesting_string:
            continue
        processed_line = line
        for symbol in special_symbols:
            processed_line = processed_line.replace(symbol, ' ')
        common_strin += processed_line.lower()
    return [(line + ';').lstrip() for line in common_strin.split(';')]
