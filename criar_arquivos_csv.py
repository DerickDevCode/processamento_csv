import csv
import time

inicio = time.perf_counter()

for num in range(1, 9):
    with open(f'arquivo{num}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['nome'] + ['idade'] + ['cidade'])

        for n in range(1, 1_000_001):
            if num == 1:
                writer.writerow(['Dérick Eduardo', '20', 'Buritis'])
            if num == 2:
                writer.writerow(['João Paulo', '30', 'Ariquemes'])
            if num == 3:
                writer.writerow(['Maria da Silva', '25', 'Cacoal'])
            if num == 4:
                writer.writerow(['Jonatan Oliveira', '35', 'Vilhena'])
            if num == 5:
                writer.writerow(['José Fonseca', '60', 'Porto Velho'])
            if num == 6:
                writer.writerow(['Marta da Silva', '47', 'Monte Negro'])
            if num == 7:
                writer.writerow(['Lucas Santana', '17', 'Ouro Preto'])
            if num == 8:
                writer.writerow(['Matheus Pereira', '25', 'Campo Novo'])
        fim = time.perf_counter()

tempo_total = fim - inicio
print(tempo_total)

# with open('arquivo2.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile, delimiter=',')
#     writer.writerow(['nome'] + ['idade'] + ['cidade'])
#
#     inicio = time.perf_counter()
#     for n in range(1, 10001):
#         writer.writerow(['João Paulo', '30', 'Ariquemes'])
#     fim = time.perf_counter()
#
#     tempo_total = fim - inicio
#     print(tempo_total)
