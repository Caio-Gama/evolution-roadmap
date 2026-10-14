# Bem-vindo a minha calculadora de média.
# Aqui será possível calcular a média das suas notas e ver se ficou ou não na recuperação! 

media = float(input(" Qual a média para você não ficar de recuperação? ") )

nota1 = float(input("Qual foi a sua nota na primeira avaliação? "))
nota2 = float(input("Qual foi a sua nota na segunda avaliação? "))
nota3 = float(input("Qual foi a sua nota na terceira avaliação? "))

media_nota = (nota1 + nota2 + nota3) / 3 

if media_nota >= media: 
     print(f"Parabéns, você está aprovado! Sua média final foi {media_nota:.2f}." )
else:
     print(f"Infelizmente você está de recuperação. Sua média final foi {media_nota:.2f}." )
