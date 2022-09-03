# Publicando um modelo online

Nesta atividade, vamos trabalhar com a publicação de um modelo de análise de sentimento. Você notará como estar em um ambiente ambiente cloud facilita muito esta jornada.

## Cenário 1

Depois da bem sucedida experiência de trabalhar em projetos de Data Science com uma VM compartilhada pela equipe, esta prática se torna muito comum em sua empresa.

Em certa ocasião você é convocado a apresentar uma Prova de Conceito (POC) para solução de análise de sentimento para um possível novo cliente da empresa. Apesar da oportunidade lhe parecer extremamente interessante, o prazo de dois dias para colocar a POC no ar parece um objetivo inalcançável. Para sua sorte, você fica sabendo que já há um protótipo de uma solução feita anteriormente que está disponível em um repositório Git da empresa.

Você pede a Clever, um dos Cientistas de Dados, da sua equipe para dar uma olhada no código e avaliar se é possível construir um ambiente para a POC neste prazo. Na apresentação da POC deverá ser apresentado um protótipo do produto que recebe requisições via web, analisa o sentimento de uma frase e devolve uma resposta, classificando como positivo, negativo ou neutro.

Após fazer a análise, Clever vem lhe chamar entusiasmado informando que conseguiu rodar o código localmente e que parece que está tudo muito bem encaminhado para publicar como um serviço web. Ele também lembra que há uma VM Compartilhada já disponível que pode ser utilizada para construir o ambiente da POC. Esta novidade te deixa muito animado e você pede para que ele toque a construção da POC. Nesse momento, ele então faz uma cara muito séria e fala "Então... preciso conversar com você... recebi uma proposta irrecusável e estou iniciando na nova empresa amanhã. Hoje é meu último dia na empresa". Recomposto do susto você percebe: desta vez sobrou pra você...

Apesar desse cenário tenso, Clever se dispõe a lhe apresentar sua análise sobre o projeto. Você então faz uma reunião com ele ouvindo atentamente cada uma de suas explicações.

### Atividades:

Frente a este cenário você deverá realizar as seguintes atividades:

1. Baixar o arquivo do projeto em sua VM e descompactar. Para fazer o download via terminal, você pode rodar o comando:
   ``wget https://drive.google.com/uc?export=download&id=11i233LEHAJxYQtLl71G2F83gJeoHdmzu``
2. Rodar o projeto localmente a partir do terminal e testar algumas frases para conferir seu funcionamento;
3. Rodar o projeto expondo o serviço de predição localmente e testar seu funcionamento enviando mensagens para o endpoint. Para isso, rode o seguinte comando do terminal:
   ``curl -H 'Content-Type: application/json' -X POST --data '{"message": "não confio nesse governo"}' localhost:5000/predict``
4. Abrir a porta 5000 da VM para que o modelo para que fique acessível para consultas pela internet;

## Cenário 2:

Depois de conseguir preparar todo o ambiente da POC, você está extremamente satisfeito com o resultado! Duas horas  antes antes da apresentação você faz um teste rápido e não consegue acessar o endpoint. Você tenta acessar a VM via ssh também sem sucesso. Ao acessar o portal de configuração de seu provedor cloud, você percebe que alguém, inadvertidamente, apagou a VM por achar que não seria mais utilizada.

Desesperado, você pensa em desistir, mas antes disso resolve ligar para o Arquiteta Chefe de Cloud da companhia, Carla. Depois de alguns questionamentos, Carla acredita ter uma solução para o problema. Ela lhe orienta a utilizar um serviço da cloud, o Serviço de Aplicativo (App Service), um serviço gerenciado da Azure que permite a publicação de aplicativos Web e APIs diretamente de um repositório Git. Você provavelmente terá que fazer algumas alterações no projeto para adaptar aos padrões do serviço, mas resolve encarar o desafio. Será que conseguirá finalizar a tempo?

### Atividades:

1. Criar uma conta no github;
2. Clonar o repositório
https://github.com/thiagonogueira/sentiment-analysis-ptbr
4. Configurar o App Service e configurar para que utilize o repositório criado;
5. Faça uma análise do arquivo index.html, altere o texto do botão e publique no github;
6. Aguarde um momento e verifique que a alteração foi publicada automaticamente.


## Entregáveis

Todas as atividades realizadas devem ser cuidadosamente evidenciadas. Estes documentos serão fundamentais para que o cliente tome a decisão final de qual fornecedor irá contratar. Portanto caprichem!
