def contar_a_na_string(s):
    
    contagem_a = s.lower().count('a')
    
    
    existe_a = contagem_a > 0
    
    return existe_a, contagem_a

def main():
    
    texto = input("Digite uma string para verificar a letra 'a': ")
    
    
    existe_a, contagem_a = contar_a_na_string(texto)
    
    if existe_a:
        print(f"A letra 'a' (maiúscula ou minúscula) aparece {contagem_a} vezes na string.")
    else:
        print("A letra 'a' (maiúscula ou minúscula) não está presente na string.")

if __name__ == "__main__":
    main()
