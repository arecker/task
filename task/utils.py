def yada_yada(text, max_chars=30, ending='...'):
    words = text.split(' ')
    shortened_text = ''

    while len(shortened_text) <= max_chars - len(ending):
        try:
            word = words.pop(0)
            if shortened_text:
                word = ' ' + word
            shortened_text += word
        except IndexError:
            return text

    return '{}{}'.format(shortened_text, ending)
