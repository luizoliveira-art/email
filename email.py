while True:
    email = input('Digite seu email: ')
    
    if '@' in email and '.com' in email:
        print(f'Email aceito: {email}')
        break
    else:
        print('Inválido. O email precisa ter @ e .com')