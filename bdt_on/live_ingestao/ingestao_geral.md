# Ingestão geral


## SQOOP

1. Realize o import da tabela LOC_CLI_FISICA para o HDFS:
   ```
   sqoop import --connect jdbc:oracle:thin:@localhost:1521/xe --table HDPADMIN.LOC_CLI_FISICA ----target-dir /data/SQOOP/HDPADMIN.LOC_CLI_FISICA --username hdpadmin --password hadoop
   ```
   

2. Abra um terminal e vá para o diretório **/usr/hdp/current/kafka-broker/bin**
   ``` 
   cd /usr/hdp/current/kafka-broker/bin
   ``` 
   
3. Liste os tópicos existentes no cluster:
   ```
    ./kafka-topics.sh --list --zookeeper localhost:2181
   ```

4. Crie um novo tópico chamado primeiro:
    ```
    ./kafka-topics.sh --zookeeper localhost:2181 --create --topic primeiro --replication-factor 1 --partitions 1
    ```
5. Verifique as informações do tópico criado:
   ```
   ./kafka-topics.sh --zookeeper localhost:2181 --describe --topic primeiro
    ```
6. Abra um novo terminal e crie um **producer** para o tópico recém criado:
   ```
   ./kafka-console-producer.sh --broker-list hdpdemo.local:6667 --topic primeiro
   ```

7.  Abra um novo terminal e crie um **consumer** para o tópico recém criado:
   ```
   ./kafka-console-consumer.sh --zookeeper localhost:2181 --topic primeiro
   ```

10. Altere o número de partições do tópico:
    ```
    ./kafka-topics.sh --zookeeper localhost:2181 --alter --topic primeiro --partitions 40
    ```
    
11. Altere o tempo de retenção das mensagems no tópico:
    ```
    ./kafka-topics.sh --zookeeper localhost:2181 --alter --topic topic1 --config retention.ms=1000
    ```

12. Delete o tópico criado:
    ```
    ./kafka-topics.sh --zookeeper localhost:2181 --delete --topic primeiro
    ```

    
## Estudos livres

Que tal um momento para explorar livremente seu novo cluster Kafka? Nas instruções abaixo estão apresentadas algumas sugestões, mas sinta-se à vontade para explorar à sua maneira. Não se esqueça de controlar e sistematizas as alterações que você faz para conseguir analisar seus impactos no comportamento do cluster.

1. Abra novos terminais de consumers e producers e analise os comportamentos. Para os consumers, procures explorar a flag `--from-beginning` e `--group`
   **Nota:**: Dependendo da versão utilizada, a flag `--group` deve ser substituida por `--consumer-property group.id=nome_do_grupo`

2. Crie novos tópicos alterando so parâmetros `--replication-factor` e `--partitions` e analise os resultados

3. Faça um tópico com 3 partições e crie grupos de consumers para analisar o comportamento.

4. Utilize os comandos utilizado acima apennas com o parâmetro `--help` e avalie as diferentes possibilidades de uso


### DYI

#### API Python:

   Utilize o link abaixo para descobrir como utilizar a API kafka-python.

    [https://pypi.org/project/kafka-python/](https://pypi.org/project/kafka-python/)

#### API Java:

   Utilize os links abaixo para descobrir como utilizar a API kafka para Java.

   [https://kafka.apache.org/documentation/#api]([https://kafka.apache.org/documentation/#api)
   [https://dzone.com/articles/kafka-producer-and-consumer-example](https://dzone.com/articles/kafka-producer-and-consumer-example)


1. Aproveite os exemplos apresentados para desenvolver um producer e um consumer simples. Para ajudar no desenvolvimento, sempre deixe aberto no terminal um produder e um consumer do tópico em que está utilizando.

2. Evolua sua solução para trabalhar com grupos de consumers 
