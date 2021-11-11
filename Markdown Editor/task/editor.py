import sys


def bold(local_text):
    return f'**{local_text}**'


def italic(local_text):
    return f'*{local_text}*'


def header(local_level: int, local_text):
    return '#' * local_level + f' {local_text}\n'


def link(local_label, local_url):
    return f'[{local_label}]({local_url})'


def inline_code(local_text):
    return f'`{local_text}`'


def ordered_list(local_list):
    for l in range(len(local_list)):
        local_list[l] = f'{l + 1}. {local_list[l]}\n'
    return local_list


def unordered_list(local_list):
    for l in range(len(local_list)):
        local_list[l] = f'* {local_list[l]}\n'
    return local_list


result = []

while True:
    command = input('Choose a formatter:')
    if command == '!help':
        print('Available formatters: plain bold italic header link inline-code new-line ordered-list unordered-list')
        print('Special commands: !help !done')
    elif command == '!done':
        f = open('output.md', 'w', encoding='utf-8')
        for r in result:
            f.write(r)
        f.close()
        sys.exit()
    elif command == 'plain':
        text = input('Text: ')
        result.append(text)
    elif command == 'bold':
        text = input('Text: ')
        result.append(bold(text))
    elif command == 'italic':
        text = input('Text: ')
        result.append(italic(text))
    elif command == 'header':
        level = int(input('Level: '))
        if  not 1 <= level <= 6:
            while level < 1 or level > 6:
                print('The level should be within the range of 1 to 6')
                level = int(input('Level: '))
        text = input('Text: ')
        result.append(header(level, text))
    elif command == 'link':
        label = input('Label: ')
        url = input('URL: ')
        result.append(link(label, url))
    elif command == 'inline-code':
        text = input('Text: ')
        result.append(inline_code(text))
    elif command == 'new-line':
        result.append('\n')
    elif command == 'ordered-list':
        row_amount = 0
        while row_amount <= 0:
            row_amount = int(input('Number of rows: '))
            if row_amount <= 0:
                print('The number of rows should be greater than zero')
        elements = []
        for i in range(1, row_amount + 1):
            elements.append(input(f'Row #{i}: '))
        elements = ordered_list(elements)
        for element in elements:
            result.append(element)
        elements.clear()
    elif command == 'unordered-list':
        row_amount = 0
        while row_amount <= 0:
            row_amount = int(input('Number of rows: '))
            if row_amount <= 0:
                print('The number of rows should be greater than zero')
        elements = []
        for i in range(1, row_amount + 1):
            elements.append(input(f'Row #{i}: '))
        elements = unordered_list(elements)
        for element in elements:
            result.append(element)
        elements.clear()
    else:
        print('Unknown formatting type or command')
    for r in result:
        print(r, end='')
    print()
