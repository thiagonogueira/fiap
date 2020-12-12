# Contato inicial com o Kafka

Neste tutorial, tomaremos o primeiro contato com o Kafka. Procure realizá-lo tendo em mente cada um dos conceitos apresentados na parte teórica.

## Demonstração guiada

1. Suba o serviço Kafka através do Ambari

2. Abra um terminal e vá para o diretório **/usr/hdp/current/kafka-broker/bin**
   ``` 
   cd /usr/hdp/current/kafka-broker/bin
   ``` 
   
5. Liste os tópicos existentes no cluster:
   ```
    ./kafka-topics.sh --list --zookeeper localhost:2181
   ```

6. Crie um novo tópico chamado primeiro:
    ```
    ./kafka-topics.sh --zookeeper localhost:2181 --create --topic primeiro --replication-factor 1 --partitions 1
    ```
7. Abra um novo terminal e crie um **producer** para o tópico recém criado:
   ```
   ./kafka-console-producer.sh --broker-list hdpdemo.local:6667 --topic primeiro
   ```

8. Abra um novo terminal e crie um **consumer** para o tópico recém criado:
   ```
   ./kafka-console-consumer.sh --zookeeper localhost:2181 --topic primeiro
   ```

## Estudos livres

Que tal um momento para explorar livremente seu novo cluster Kafka? Nas instruções abaixo estão apresentadas algumas sugestões, mas sinta-se à vontade para explorar à sua maneira. Não se esqueça de controlar e sistematizas as alterações que você faz para conseguir analisar seus impactos no comportamento do cluster.

1. Abra novos terminais de consumers e producers e analise os comportamentos. Para os consumers, procures explorar a flag `--from-beginning` e `--group`

2. Crie novos tópicos alterando so parâmetros `--replication-factor` e `--partitions` e analise os resultados

3. Faça um tópico com 3 partições e crie grupos de consumers para analisar o comportamento.

4. Utilize os comandos utilizado acima apennas com o parâmetro `--help` e avalie as diferentes possibilidades de uso

### APIs

### DYI

1. Página da API:
   Utilize o link abaixo para descobrir como baixar a API kafka-python.

    [https://pypi.org/project/kafka-python/](https://pypi.org/project/kafka-python/)

2. Aproveite os exemplos apresentados para desenvolver um producer e um consumer simples. Para ajudar no desenvolvimento, sempre deixe aberto no terminal um produder e um consumer do tópico em que está utilizando.

3. Evolua sua solução para trabalhar com grupos de consumers 
