# Trabalho de Conclusão
### CRUD - Django

O projeto desenvolvido, se trata de um sistema para registro e controle de alunos. Será possível realizar essa funcionalidade atráves do CRUD, utilizando Django. O ambiente é composto por um código disponibilizado no GitHub, pré configurado, ou seja a única configuração necessária será o domínio. 

#### Funcionalidades:
- Criar
- Ler
- Atualizar
- Excluir

#### Banco de dados (stundentManager\crud_Manager\models.py):

Esta parte é definida para receber os dados e armazenar:
 -  name = Nome do estudante
 - registration = Número de matrícula
 - birthDate = Data de nascimento no formato YYYY-MM-DD
 -  email = E-mail do aluno
 - phone = Telefone do aluno, não é necessário do código do país
 - entryDate = Data de ingressão no curso
 - course = Nome do curso
    
#### Tabela do banco de dados:
```sh
name = models.CharField(max_length=50)
registration = models.PositiveIntegerField()
birthDate = models.DateField()
email = models.CharField(max_length=100)
phone = models.CharField(max_length=20)
entryDate = models.DateField()
course = models.CharField(max_length=20)
```

#### Credenciais de acesso (Basic Authentication):
```sh
Login: gabriella
Senha: 123
``` 
#### Testes da funcionalidade:

 **- Create: Registrar dados**
1. Selecione o método POST na lista suspensa ao lado da URL.
2. Copie os dados do quadro "Pretty" para garantir que os dados estejam formatados corretamente.
3. Clique na opção "Body" para abrir as opções da barra.
4. Clique na opção "Raw" para alternar para a visualização de dados brutos.
5. Cole os dados copiados no corpo da solicitação.
6. Remova o campo ID dos dados, pois geralmente é atribuído automaticamente pelo servidor durante a criação.
7. Faça as alterações necessárias nos dados conforme desejado.
8. Clique em "Send" (Enviar) para enviar a solicitação POST para o servidor. Certifique-se de que os cabeçalhos e o corpo da solicitação estejam corretamente configurados antes de enviar.
 
Você verá a resposta do servidor na área abaixo da solicitação, que incluirá os dados retornados pela solicitação POST.

 ![Create: Registrar dado](https://raw.githubusercontent.com/GabsPeres/python-crud/main/images/post.png)
 
 **- Read: Leitura do sistema** 
1. Abra o Postman e crie uma nova solicitação.
2. Selecione o método GET na lista suspensa ao lado da URL.
3. Insira a URL do endpoint que você deseja ler no campo de URL.
4. Clique em "Send" (Enviar) para enviar a solicitação.

Você verá a resposta do servidor na área abaixo da solicitação, que incluirá os dados retornados pela solicitação GET.

 ![Read:Leitura do sistema](https://raw.githubusercontent.com/GabsPeres/python-crud/main/images/get.png)

 **- Update: Atualização de dados** 
1. Selecione o método PUT na lista suspensa ao lado da URL.
2. Altere a URL para http://127.0.0.1:8000/students/update/(insirar o id desejado)
3. Clique na opção "Body" para abrir as opções da barra.
4. Clique na opção "Raw" para alternar para a visualização de dados brutos.
5. Cole os dados copiados no corpo da solicitação.
6. Faça as alterações necessárias nos dados conforme desejado.
7. Clique em "Send" (Enviar) para enviar a solicitação PUT para o servidor. Verifique se os cabeçalhos e o corpo da solicitação estão corretamente configurados antes de enviar.

Você verá a resposta do servidor na área abaixo da solicitação, que incluirá os dados retornados pela solicitação PUT.

 ![Update: Atualização de dados](https://raw.githubusercontent.com/GabsPeres/python-crud/main/images/put.png)

 **- Delete: Exclusão de dados** 
1. Selecione o método PUT na lista suspensa ao lado da URL.
2. Altere a URL para http://127.0.0.1:8000/students/delete/(insira o id desejado)
3. Clique em "Send" (Enviar) para enviar a solicitação DELETE para o servidor. Verifique se o id está correto antes de enviar.

Você verá a resposta do servidor na área abaixo da solicitação, os dados não seram retornados, concluindo a exclusão do DELETE.

 ![Delete: Exclusão de dados](https://raw.githubusercontent.com/GabsPeres/python-crud/main/images/delete.png)

 **- PATCH: Alteração de parte dos dados** 
1. Selecione o método PUT na lista suspensa ao lado da URL.
2. Altere a URL para http://127.0.0.1:8000/students/update/(insira o id desejado)
3. Clique na opção "Raw" para alternar para a visualização de dados brutos.
4. Cole os dados copiados no corpo da solicitação.
5. Faça as alterações necessárias nos dados conforme desejado.
6. Clique em "Send" (Enviar) para enviar a solicitação PUT para o servidor. Verifique se os cabeçalhos e o corpo da solicitação estão corretamente configurados antes de enviar.

Você verá a resposta do servidor na área abaixo da solicitação, que incluirá os dados retornados pela solicitação PATCH.

 ![PATCH: Alteração de parte dos dados](https://raw.githubusercontent.com/GabsPeres/python-crud/main/images/patch.png)
