# VM Compartilhada para a Data Science

Nesta atividade vamos utilizar uma situação simples para mostrar como decisões simples podem gerar grande economia de recursos.

## Cenário

Imagine que você está gerenciando uma equipe de Data Science de 5 pessoas que encontra-se em um projeto que pode trazer grandes retornos financeiros para a empresa. Neste momento, estão fazendo alguns pequenos treinamentos no próprio notebook de trabalho, apenas para testes iniciais.

O membro mais Sênior da sua equipe lhe chama para uma conversa e demonstra uma preocupação quanto à insatisfação do time com relação à capacidade dos notebooks, pois até mesmo esses treinamentos inicias estão muito demorados, atrapalhando muito o ritmo de trabalho. Além disso, os resultados preliminares mostram que será necessária a utilização de um computador com uma GPU bastante potente (Nvidia Tesla T4).

Ao sair da conversa, você está decido a fazer indicar a seu gestor a necessidade do aporte desse investimento no projeto, mas lhe ocorre que um amigo comentou de um projeto que passou por um problema similar e optou por uma solução bastante criativa: ele criou uma VM em cloud para que todo o grupo pudesse trabalhar. Esta VM colaborativa foi criada e configurada com o pacote Anaconda para permitir que os membros da equipe trabalhem com o Jupyter remotamente, através de um web browser. Além disso, nos momentos do treinamento, a mesma VM era reconfigurada com GPU e, assim que o treinamento finalizasse, a GPU era desabilitada. Com isso, os gastos com GPU ocorreriam apenas nos casos em que se estava utilizando de fato. Além disso, a VM possuía uma configuração suficiente para que os Cientistas de Dados fizessem o trabalho diário num ambiente centralizado, tornando ainda mais fácil a colaboração entre a equipe.

Você resolve fazer algumas simulações de preço e apresentar os dois cenários ao seu gestor para que tomem a melhor decisão.

## Atividades

Frente a este cenário, você deverá realizar as seguintes atividades:

1. Construa um protótipo da VM, com recursos reduzidos, para que possa levar na apresentação ao seu gestor e também para que o time de Data Science possa avaliar a solução;
 
2. Faça um orçamento para a compra de 5 notebooks com configuração padrão e 1 servidor para Treinamento de Modelos;
   
3. Faça o orçamento da criação de uma VM dimensionada para uso concomitante da equipe. Suponha também que a GPU será utilizada 24 horas por semana;
   
4. Construa uma apresentação que contenha uma análise dos preços, os prós e contras de cada solução e deixe claro a sua decisão.

## Entregas

Ao término das atividades cada grupo deverá submeter um trabalho no portal com os seguintes integráveis:
1. Um documento de evidências com prints da criação, configuração da VM e do acesso feito através do Jupyter Notebook;
   
2. Uma apresentação com o comparativo dos dois cenários;

Os dois documentos deverão ser convertidos para pdf e zipados em um único arquivo para subida no portal.

### Nota sobre o documento de evidência

O documento de evidência deve ser desenvolvido com bastante cuidado, sempre explicando claramente qual a atividade está sendo evidenciada. A qualidade, nível de detalhes e organização do documento possuem peso significativo na nota final do trabalho.