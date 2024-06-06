print("A senha deve conter letras e números, deve ter pelo menos uma letra maiúscula e uma minúscula e conter ao menos um caractere especial.")

senha = input("Digite a senha: ")

if len(senha) > 8:
    if not senha.isupper():
        if not senha.islower():
            if not senha.isalnum():
                print("Senha aceita")            
            else:
                print("A senha deve conter ao menos um caractere especial.")
        else:
            print("A senha deve conter pelo menos uma letra maiúscula.")
    else:
        print("A senha deve conter pelo menos uma letra minúscula.")
else:
    print("Senha pequena")