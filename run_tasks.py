from tasks import processar_dados_em_lote, processar_dados_um_por_um, processar_dados_varios_arquivos_por_vez

# processar_dados_em_lote.delay('arquivo1.csv')
# processar_dados_um_por_um.delay('arquivo1.csv')
processar_dados_varios_arquivos_por_vez('arquivo1.csv', 'arquivo2.csv', 'arquivo3.csv', 'arquivo4.csv', 'arquivo5.csv',
                                        'arquivo6.csv', 'arquivo7.csv', 'arquivo8.csv')
