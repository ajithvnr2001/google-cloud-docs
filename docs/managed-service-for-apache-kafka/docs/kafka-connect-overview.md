---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-connect-overview/
title: Kafka Connect overview \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:28:15.723455+00:00
---

# Kafka Connect overview  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-connect-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Kafka Connect overview Stay organized with collections  Save and categorize content based on your preferences. 

Kafka Connect is the preferred tool for data integration for Kafka developers. It provides a framework for connecting Kafka with external systems such as databases, message queues, and file systems.

Kafka Connect provides a curated set of built-in connector plugins, vetted and maintained by Google Cloud. These connector plugins are automatically patched and upgraded, simplifying maintenance and ensuring compatibility. Google Cloud also provides built-in monitoring and logging to maintain the health of your pipelines.

Kafka Connect APIs are offered as part of the Google Cloud Managed Service for Apache Kafka service. These APIs are accessible through `managedkafka.googleapis.com` and are integrated into the Google Cloud console and client libraries. To manage Kafka Connect, you can use the Google Cloud console, the gcloud CLI, the Managed Kafka API, the cloud client libraries, or Terraform.

## Kafka Connect use cases

Kafka Connect supports data integration between your Managed Service for Apache Kafka cluster and various other systems. Here are some key use cases:

  * Migrate your existing Kafka deployments to Managed Service for Apache Kafka.

  * Replicate your Managed Service for Apache Kafka cluster to another region for disaster recovery.

  * Stream data from Managed Service for Apache Kafka to BigQuery, Cloud Storage, Pub/Sub.




## Connect clusters

A Connect cluster is a distributed deployment of Kafka Connect with pre-packaged connector plugins and configurations. Each Connect cluster is associated with a primary Managed Service for Apache Kafka cluster. This primary cluster stores the state of the connectors running on the Connect cluster.

Generally, the primary Managed Service for Apache Kafka cluster also serves as the target for all source connectors and the source for all sink connectors running on the associated Connect cluster.

A single Managed Service for Apache Kafka cluster can have multiple Connect clusters. If running MirrorMaker 2.0, a Connect cluster can connect to non-primary Managed Service for Apache Kafka clusters or self-managed Kafka clusters to read or write topic data. This process enables topic replication between different clusters.

From the perspective of the resource model, a Connect cluster is a separate resource from a [Managed Service for Apache Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-cluster).

Assume that you have a Managed Service for Apache Kafka cluster where you store website traffic data. You want to stream this data into BigQuery for analysis. You can create a Connect cluster and use a BigQuery sink connector to move the data from your Kafka topics to BigQuery. This Connect cluster is associated with your Managed Service for Apache Kafka cluster as its primary cluster.

## Connectors

Connectors are the software components that transfer data between your Kafka cluster and other systems.

  * A _source connector_ writes data from a source to a Managed Service for Apache Kafka cluster.

  * A _sink connector_ writes data from a Managed Service for Apache Kafka cluster to a sink.




A connector is deployed, configured, and managed within the Connect cluster. It can be started, stopped, paused, restarted, and its configuration can be updated.

To learn more about the connector types that Managed Service for Apache Kafka supports, see [Connectors overview](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/connectors-overview).

## Manage Kafka Connect

With Kafka Connect, you can focus on deploying connectors while Managed Service for Apache Kafka handles the underlying infrastructure and operational complexities.

The Kafka Connect service automates the following:

  * **Provisioning of Kafka Connect workers** : When you create a Connect cluster, the Kafka Connect service automatically provisions a cluster of workers in Kubernetes.

  * **Networking** : The Kafka Connect service configures the network to enable communication between the workers, Managed Service for Apache Kafka brokers, and external systems. In some cases, you might need to make some changes to your existing network settings.

  * **Zonal resiliency** : The Kafka Connect service distributes workers across a minimum of three zones, ensuring that data processing can proceed in the event of a zonal outage.

  * **Authentication** : The Kafka Connect service also configures authentication with Kafka brokers, ensuring secure connections.

  * **Rollouts and upgrades** : The Kafka Connect service manages worker configuration changes, version upgrades, and security patches, ensuring your deployments are always up-to-date.




Within the Kafka Connect service, you can perform the following configurations:

  * **Capacity and network constraints** : Define resource limits and network configurations to optimize performance and cost.

  * **Monitoring and logging** : Access logs and metrics for your connectors to monitor performance and troubleshoot issues.

  * **Connector lifecycle management** : Pause, resume, restart, or stop connectors as needed to manage your data pipelines.




## Limitations

  * The primary Kafka cluster must be a Managed Service for Apache Kafka cluster. The primary cluster is the cluster to which the Kafka Connect cluster writes its metadata.

  * You can't upload custom connector plugins to your Kafka Connect cluster.

  * The service doesn't support validation against a remote schema by using Schema Registry.




## What's next?

  * [Create a Connect cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster)
  * [Connectors overview](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/connectors-overview)



_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
