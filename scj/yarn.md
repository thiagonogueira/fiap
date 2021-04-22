# Laboratório: MapReduce / YARN

**Objetivo:** Familiarizar-se com os exemplos de MapReduce e acompanhamento de Jobs no YARN

1. Inicie a máquina virtual e dê um start nos serviços HDFS, YARN e MapReduce2 e aguarde o termino do carregamento.
2. Siga as instruções em sala para criar o arquivo center_earth.txt
3. Abra um terminal novo terminal
4. Rode o comando a seguir para ver quais são os exemplos disponíveis:

    ```hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-mapreduce-examples.jar```

5. Rode o exemplo wordcount para ver quais parâmetros devem ser utilizados:

    ```hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-mapreduce-examples.jar wordcount```

6. Crie no hdfs o diretório /user/hdpadmin/wordcount

    ```hdfs dfs -mkdir /user/hdpadmin/wordcount```


7. Copie o arquivo center_earth.txt para o diretório criado

    ```hdfs dfs -copyFromLocal center_earth.txt /user/hdpadmin/wordcount```

8. Altere a permissão do diretório criado recursivamente para 777

    ```hdfs dfs -chmod -R 777 /user/hdpadmin/wordcount```

9. Abra a página de monitoramento de processos do YARN e faça uma rápida análise dos processos listados

    ```Ambari -> YARN -> Quick Links -> ResourceManager UI```

10. Submeta o programa wordcount ao YARN

    ```hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-mapreduce-examples.jar wordcount /user/hdpadmin/wordcount /user/hdpadmin/wordcount/output```

11. Acompanhe a execução do processo na UI do YARN e evidencie que o processo foi finalizado com sucesso
12. Liste os arquivos presentes no diretório de saída do comando:

    ```hdfs dfs -ls /user/hdpadmin/wordcount/output```

13. Faça uma análise dos arquivos presentes no diretório, explicando cada um deles do ponto de vista dos conceitos de MapReduce

14. Verifique o resultado do processo de wordcount imprimindo o conteúdo do arquivo no terminal:

    ```hdfs dfs -cat /user/hdpadmin/wordcount/output/part-r-00000```