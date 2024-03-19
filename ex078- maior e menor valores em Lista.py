listanum = []
maior = 0
menor = 0
for c in range(0,5):
   listanum.append(int(input(f'Digite um valor para posição {c}:')))
   if c == 0:
       maior = menor = listanum[c]
   else:
       if listanum[c] > maior:
           maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]

print('=-'*30)
print(f'Você digitou os números {listanum}')
print(f'O Maior valor digitado foi {maior}')
print(f' O menor valor difitado foi {menor}')
