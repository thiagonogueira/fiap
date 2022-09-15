# Exercício NiFi
---
## Instruções

A entrega deste trabalho deverá ser um documento de evidências de execução dos exercícios solicitados. Para que as atividades estejam bem evidenciadas lembre de sempre apresentar os seguintes prints para todos os casos:

- Fluxo completo, onde se possa visualizar todos os _processors_ utilizados para compor a solução

- Configuração de cada _processor_ para que se possa avaliar os parâmetros utilizados

- Evidência do resultado da operação realizada que permita avaliar o resultado bem sucedido da execução do fluxo completo (como listagem no HDFS do diretório destino do fluxo, print de um terminal, etc.)
  
Lembre-se que a organização do trabalho entregue também é avaliada!

## Antes de iniciar:

Antes de iniciar as atividades propostas, é necessário alguns passos, conforme descrito abaixo:

### Iniciar Serviços do Hadoop

Certifique-se de que os seguintes serviços estejam rodando em sua VM com Hadoop:
   
- HDFS
- Zookeeper
- YARN
- MapReduce2
- Hive
- Kafka

### Instalar pacote Kite no NiFi  
Nas versões atuais do NiFi, os _processors_ do pacote **kite** deixaram de ser distribuídos no pacote de instalação. Para executar uma das atividades, teremos que instalar o pacote manualmente no NiFi. Para a nossa sorte, esse processo limita-se a copiar o arquivo do pacote **kite** ao diretório de bibliotecas de sua instalação no NiFi.

**Observação**:  É muito importante que seja adicionado o arquivo do **kite** exatamente da mesma versão de sua instalação do NiFi. Caso as versões sejam incompatíveis, o pacote não passará na validação do processo de inicialização do NiFi, causando a interrupção do programa.

Para instalação do pacote **kite**, siga as seguintes instruções:

1. Rode o comando ``nifi.sh`` a partir do terminal para obter a versão e local de instalação do NiFi. No caso do exemplo abaixo, a versão instalada é a ``1.13.2`` e o local de instalação é ``/opt/nifi-1.13.2``:

    &nbsp;![image](img/nifi_status.png)&nbsp;

2. A partir da sua VM, baixe o pacote binário do **kite** (nar) para a sua versão de NiFi. No caso da versão apresentada acima, o arquivo pode ser obtido diretamente do link abaixo:
   [nifi-kite-nar-1.13.2.nar](bin/nifi-kite-nar-1.13.2.nar)
   
    Você também poderá encontrar outras versões do pacote no seguinte link:
    https://mvnrepository.com/artifact/org.apache.nifi/nifi-kite-nar

3. Copie o arquivo baixado para o subdiretório ``lib`` do local de instalação do NiFi. No caso apresentado acima, você poderá rodar o seguinte comando no terminal, considerando que o download foi feito no diretório padrão:
    > cp ~/Downloads/nifi-kite-nar-1.13.2.nar /opt/nifi-1.13.2/lib