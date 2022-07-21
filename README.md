# Teste QA
### Feito por: Matheus Domingos

## Sobre
Para a resolução do desafio, optou-se por utilizar python juntamente com o selenium. Utilizei nesse desafio uma máquina linux com a seguinte versão de python: 3.8.10 (default, Jun 22 2022, 20:18:18) 

## Sobre o tempo
Para que fosse possível visualizar os conteúdos, deixei um default time de sleep de 0,4s. Esse tempo pode ser modificado no arquivo `page_objects.py`.
Deve-se mofificar o conteúdo da linha:
    15. default_time=0.4



## Instruções:
Para utilizar o programa utilizaremos o arquivo `salcedemo.py`.
Utilizaremos ele para inserir os dados:

Para se escolher o usuário, devemos editar na linha 7:

    7. usuario='standard_user'
   
   Obs.: Não é necessário inserir a senha, pois ela é a mesma para todos os usuários de acordo com o site.

Já na lista de itens, fiz uma lista em python com os itens pedidos, mas caso se queira adicionar mais um item, deve-se procurar o id do botão de adicionar desse arquivo e colocar na lista.  (linha 9)

    9. lista_itens=['add-to-cart-test.allthethings()-t-shirt-(red)', 
    'add-to-cart-sauce-labs-onesie']
    
Agora sobre os dados da compra, deve-se editar as seguintes linhas, inserindo-se os dados desejados:

	11. first_name='test'
    
    12. last_name='test'
    
    13. zip='test'

Após serem realizadas as mudanças, pode-se executar o programa.
