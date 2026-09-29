import hashlib
import itertools
import string

# Senha usada apenas para a demonstração
senha = "abc"

# Criando o hash da senha
hash_alvo = hashlib.sha256(
    senha.encode("utf-8")
).hexdigest()

print("Hash a ser descoberto:")
print(hash_alvo)
print("\nIniciando ataque de força bruta...")

# Caracteres que serão testados
caracteres = string.ascii_lowercase

encontrada = False

# Testa combinações de 1 até 3 caracteres
for tamanho in range(1, 4):

    for tentativa in itertools.product(caracteres, repeat=tamanho):

        tentativa = "".join(tentativa)

        hash_tentativa = hashlib.sha256(
            tentativa.encode("utf-8")
        ).hexdigest()

        print("Testando:", tentativa)

        if hash_tentativa == hash_alvo:
            print("\nSenha encontrada!")
            print("Senha:", tentativa)
            print("Hash:", hash_tentativa)

            encontrada = True
            break

    if encontrada:
        break

if not encontrada:
    print("\nSenha não encontrada.")