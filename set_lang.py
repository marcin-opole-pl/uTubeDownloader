import locale



def lang():
    '''
    Returns pharse in selected language 
    '''

    # address request, downloading from..., internet and url error, 
    english = ['Movie www address please: ']
    polish = [
        'Podaj adres www filmu: ',
        'Pobieram informacje z: ',
        'Błąd! Sprawdź połączenie z internetem / Sprawdź czy adres jest poprawny.'
    ]

    # Check OS language
    os_locale = locale.getlocale()
    # Get language name
    os_lang = ''
    for char in os_locale[0]:
        if char != '_':
            os_lang = os_lang + char
        else:
            break
    # Set app language based on OS language
    if os_lang == 'Polish':
        app_lang = polish
    else:
        app_lang = english
    return app_lang

print(lang()[0])
