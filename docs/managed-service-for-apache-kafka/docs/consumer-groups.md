---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/consumer-groups/
title: Overview of consumer groups in Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:28:10.756490+00:00
---

# Overview of consumer groups in Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/consumer-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Overview of consumer groups in Managed Service for Apache Kafka Stay organized with collections  Save and categorize content based on your preferences. 

A consumer group defines a group of consumers that read records from a topic in parallel. Each consumer in the group is assigned a subset of the topic's partitions to read from.

To create a consumer group or add a consumer to an existing group, set the [`group.id`](https://kafka.apache.org/37/configuration/consumer-configs/#consumerconfigs_group.id) configuration in the consumer. For example, when using the Kafka command-line tools, you can specify the consumer group as follows:
    
    
    kafka-console-consumer.sh \
      --topic TOPIC \
      --bootstrap-server BOOTSTRAP \
      --group GROUP \
      --consumer.config client.properties
    

Replace the following:

  * `TOPIC`: the topic name.
  * `BOOTSTRAP`: the bootstrap server.
  * `GROUP`: the consumer group ID.



In Managed Service for Apache Kafka, you can manage consumer groups by using the Google Cloud console, Google Cloud CLI, the client libraries, or the Kafka command-line tools.

## What's next?

  * [View a consumer group](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-consumer-group).

  * [List a consumer group](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/list-consumer-groups).

  * [Edit a consumer group](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/edit-consumer-group).

  * [Delete a consumer group](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/delete-consumer-group).




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
