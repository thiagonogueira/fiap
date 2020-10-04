# Criação de VM na Azure

Este tutorial ensina como criar um VM na Azure. Como pŕe requisito, você deverá ter uma subscrição válida em sua conta Azure. É possível criar uma subscrição para estudantes com o seu email FIAP e garantir um crédito de USD 100 sem a necessidade da entrada de informações de cartão de crédito. Este valor será mais do que suficiente para as atividades desenvolvidas nesta disciplina.

Para criar a sua conta de estudante acesse o link abaixo e siga as instruções. Não esqueça de utilizar o seu email FIAP para fazer o login na conta da microsoft:

​	[Azure for Students](https://azure.microsoft.com/pt-br/free/students/)

**Atenção**: É altamente recomendado que você delete a sua VM ao final de cada atividade. Além de garantir que seus créditos não sejam desperdiçados, você ainda ficará craque e ágil nas criação de VMs...

## Criando sua Virtual Machine

Para iniciar a criação da VM, acesse o [Portal da Azure](https://portal.azure.com/#home) e siga os passos a seguir:

1. Clique em Virtual Machines:

   ![](img/azure-home.png)

2. No canto superior direito clique em **+ Add**  e depois em **+ Virtual Machine**:

   ![](/home/tnascimn/Documents/fiap/bdt/cloud/img/azure_vm_add_menu.png)

3. Em **Project details**, verifique que a opação de Subscription é *Azure para Estudantes*. Escolha um *Resource Group* ou, caso ainda não tenha um Resource Group, crie um novo:

   ![](/home/tnascimn/Documents/fiap/bdt/cloud/img/azure_new_resource_group.png)

4. Na seção **Instance Details** escolha um nome para sua VM, uma região, uma imagem e um tamanho (configuração de hardware).

   **Observação** : Tome cuidado com a opção de tamanho pois poderá gerar um custo muito alto.

   ![](/home/tnascimn/Documents/fiap/bdt/cloud/img/azure_vm_instance_details.png)

5. Em **Administrator account** escolha a opção SSH public key. Providencie um nome de usuário e deixe que a Azure crie o par  de chaves pública e privada para você. No final da criação da VM você sera orientado a fazer o download da chave privada. Guarde essa chave em local seguro e lembre-se de que sem ela, não será possível acessar a sua VM.

   Em **Inbound port rules**  deixe a opção padrão *Allow selected ports*, apenas com o SSH (22) selecionado.

   ![](/home/tnascimn/Documents/fiap/bdt/cloud/img/azure_vm_admnistracao_e_portas.png)

6. Clique no botão Review + Create:

   ![](/home/tnascimn/Documents/fiap/bdt/cloud/img/azure_vm_review_create.png)

7. Verifique todos os parâmetros de criação da VM e clique no botão Create caso esteja tudo correto:

   ![](/home/tnascimn/Documents/fiap/bdt/cloud/img/azure_vm_create.png)

8. Clique no botão Download private key and create resource. Esta chave será necessária para que você possa acessar a VM:

   ![](/home/tnascimn/Documents/fiap/bdt/cloud/img/azure_vm_generate_new_key_pair.png)

9. Aguarde um tempo até que a VM seja criada. Se tudo ocorrer certo, você receberá uma mensagem confirmando que o *deploy* está completo. Para exibir os detalhes da VM, clique em **Go to resource**:

   ![](/home/tnascimn/Documents/fiap/bdt/cloud/img/azure_vm_go_to_resource.png)

10. Neste painel é possível visualizar e alterar as configuraçẽos de sua VM. Aproveite e anote o endereço público de IP, pois essa informação será necessária para acessar a VM posteriormente

    ![](/home/tnascimn/Documents/fiap/bdt/cloud/img/azure_vm_public_ip_address.png)

## Acessando a sua VM

Agora que você criou a sua VM com sucesso, vamos acessá-la atravś de uma conexão SSH. Para isso, utilizaremos um cliente SSH chamado MobaXterm. Caso ainda não o tenha instalado em sua máquina, utilize o link abaixo para fazer o download. Se tiver restrições para instalar programas em seu computador, você deve optar pela utilização da versão portable. Neste caso, basta fazer o download, descompactar o arquivo e iniciar diretamente o executável.

[Download MobaXterm](https://mobaxterm.mobatek.net/download-home-edition.html)
