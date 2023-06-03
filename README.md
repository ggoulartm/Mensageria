# Diretrizes para cada etapa:

## Configuração do Kafka:

Instalar e configurar um cluster do Kafka, que consiste em pelo menos um nó de broker. Criar os seguintes tópicos necessários para receber os eventos de telemetria veicular:

    -Velocidade do veículo

    -RPM do motor

    -Temperatura do motor

    -Nível de combustível

    -Quilometragem percorrida

    -Localização GPS

    -Status das luzes (faróis, lanternas, etc.)



## Aplicação de Publicação de Eventos:

Desenvolver uma aplicação em Python para capturar e publicar eventos de telemetria veicular no Kafka.
Gerar informações de telemetria simulando um dispositivo de sensoriamento.
Processar e estruture os dados em formato JSON, incluindo o tipo de informação, horário de criação do evento e valor relacionado ao evento.
Publicar as mensagens nos tópicos específicos do Kafka, identificados de acordo com o tipo de evento.


## Aplicação de Consumo de Informações:

Desenvolver uma aplicação em Python para consumir as informações de telemetria veicular do Kafka.
Conectar-se ao cluster do Kafka e subscreva-se aos tópicos relevantes.
Receba as mensagens de telemetria veicular do Kafka.
Processar as mensagens de acordo com as necessidades do projeto, como análise, armazenamento ou exibição dos dados.


## Resultado esperado:

O sistema deve permitir o envio e recebimento de dados em tempo real, usando o Kafka como plataforma de streaming de dados.

Implementarma interface gráfica (GUI) para monitorar o tráfego de informações.
A interface deve permitir visualizar os eventos de telemetria em tempo real, realizar consultas e exibir métricas relevantes.
