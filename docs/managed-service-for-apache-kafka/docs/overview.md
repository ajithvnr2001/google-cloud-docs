---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview/
title: Managed Service for Apache Kafka overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:58:36.475057+00:00
---

# Managed Service for Apache Kafka overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Managed Service for Apache Kafka overview Stay organized with collections  Save and categorize content based on your preferences. 

Managed Service for Apache Kafka is a Google Cloud service that helps you run secure, scalable open source Apache Kafka clusters. This page is an overview of what the service automates and simplifies for you. For more information about Apache Kafka, see the [Apache Kafka website](https://kafka.apache.org/).

## Simple sizing and scaling

When you create a Managed Service for Apache Kafka cluster, you specify the total vCPU count and memory for the cluster. The service automatically provisions a number of brokers based on the vCPU count.

To keep up with demands of clients, you can monitor resource utilization, and if needed, scale your cluster by updating the vCPU count and memory. Scaling up a cluster might result in additional brokers being provisioned. If increasing the cluster size requires a new broker, the service can automatically rebalance partitions across brokers.

For information about choosing a cluster size, see [Plan the size of your Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/plan-cluster-size).

## Storage management

Managed Service for Apache Kafka uses [tiered storage](https://kafka.apache.org/37/operations/tiered-storage/). Tiered storage combines two tiers of storage: 

  * A limited amount of fast _local storage_ , in the form of pre-provisioned disks attached to the brokers.
  * Effectively unlimited _remote storage_. Remote storage is less expensive and doesn't need to be pre-provisioned.



The tiered storage system lets you store large volumes of data with less risk of running out of disk space. It can also cost less than using local storage alone.

You are responsible for setting the [retention time](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/edit-topic#retention) on individual topics to control cost or satisfy your data retention policies.

## Flexible networking

The service makes a cluster accessible from any VPC securely. This includes access from multiple VPCs, projects, and regions.

To configure networking for a cluster, you provide the set of subnets where the cluster is accessible. The service provisions private IP addresses for the bootstrap servers and brokers in each subnet. It also sets up private Cloud DNS with URLs for each IP address. The bootstrap servers have a load balancer, so there is a single bootstrap URL per cluster. The URLs are the same across all VPCs so client configurations can be consistent across environments.

This level of flexibility is achieved thanks to [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) (PSC). Each IP address allocated for a cluster requires a PSC endpoint. The endpoints are provisioned automatically.

## Secure clusters

The service offers the following features for security of the clusters: authentication, authorization, encryption, patching, and resource isolation. It also disallows unauthenticated and unencrypted connections and storage.

### Authentication

The service supports two authentication methods: Simple Authentication and Security Layer (SASL) and mutual TLS (mTLS). mTLS authentication is available on clusters created after June 24, 2025. All connections to managed clusters authenticate with a principal that is an [IAM identity](https://docs.cloud.google.com/iam/docs/principal-identifiers) using SASL or a client certificate using mTLS. Human, service, and federated accounts are supported as principals when using SASL.

The service does not support other protocols, including SASL/GSSAPI, SASL/SCRAM-SHA-256, and SASL/SCRAM-SHA-512. The service also does not allow unauthenticated connections.

### Authorization

The service employs a layered approach to authorization. IAM controls cluster management actions such as creating, updating, and deleting resources. Authorization for authenticated principals depends on the method used:

  * **SASL** : Principals using IAM are authorized through Google Cloud IAM role bindings or with Kafka ACLs on the cluster. For more information, see [Configure SASL authentication](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/authentication-kafka).

  * **mTLS** : Principals authenticating with mTLS are authorized through Kafka ACLs. For more information, see [Configure mTLS authentication](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/authentication-kafka-mtls).




You can manage Kafka ACLs with the Google Cloud tools or third-party Kafka tools. For more information about configuring IAM and Kafka ACLs, see [Access control with IAM and Kafka ACLs](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/access-control).

### Encryption

Encryption is required. All connections to clusters must use TLS. The TLS certificates presented by the brokers are signed by the Public Certificate Authority. Stored data is always encrypted. Choose whether to use Google-managed or Customer-managed encryption keys ([CMEK](https://docs.cloud.google.com/kms/docs/cmek)) for encryption at rest.

### Patching

The service team tracks security vulnerabilities discovered in the open source code. When the service discovers vulnerabilities, it patches your clusters automatically.

### Resource isolation

Another security feature of the service is resource isolation. The managed service deploys clusters in [tenant projects](https://docs.cloud.google.com/service-infrastructure/docs/manage-tenant-projects) in a private VPC inaccessible through public IP addresses. Each of your projects has a dedicated tenant project, with a dedicated [service agent](https://docs.cloud.google.com/iam/docs/service-agents) account. This helps limit the scope of access granted to the service.

## Schema registry

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To simplify coordination between producers and consumers, Managed Service for Apache Kafka includes a schema registry API. A registry provided by the service acts as a repository of schemas that are shared among applications.

The service implements the [Confluent Schema Registry REST API](https://docs.confluent.io/platform/current/schema-registry/develop/api.html) that helps in integration with existing Kafka applications. Apache Avro and Protocol Buffer (Protobuf) schema formats are supported. JSON is not supported.

Managed Service for Apache Kafka also offers an administrative API and toolset for managing schema registries and schemas. The toolset includes the Google Cloud console, gcloud CLI, and client libraries.

For more information about schema registry, see the [Schema registry overview](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/schema-registry-overview).

## Data integration with Kafka Connect

Managed Service for Apache Kafka simplifies data integration through Kafka Connect. Kafka Connect offers several built-in connector plugins hosted in Connect clusters. These connectors are used for migration, backup, disaster recovery, high availability, and data integration. These connectors let you connect your Managed Service for Apache Kafka clusters to various systems, including other Kafka deployments and Google Cloud services like BigQuery, Cloud Storage, and Pub/Sub. Kafka Connect provides scalable, reliable data integration with lower operational overhead and integrated monitoring and logging.

To know more about Kafka Connect, see the [Kafka Connect overview](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-connect-overview).

## High availability clusters

The goal of the service is to provide regional clusters for mission-critical applications. Specifically, the service protects you from failures of individual zones or brokers.

To achieve this, all clusters are provisioned in a rack-aware three-zone configuration. The default topic configuration requires at least three replicas. Rack-awareness makes sure that replicas are created in different zones. The default minimum number of in-sync replicas is two. This means that your cluster can tolerate complete loss of a zone or a broker.

When a broker fails, due to software, hardware or networking failure, it is replaced automatically. When the service detects broker failure, it automatically restarts it, on a different machine if necessary. After the broker is available, Apache Kafka integrates the broker into the cluster. Complete zone failure might make it impossible to create a new broker. However, the cluster continues operating as long as the other two zones remain available.

In addition to these specific features, a growing list of internal tools and processes proactively maintain the health of the service, Apache Kafka code, and updates. Data and metadata backups are maintained at multiple levels, allowing the service to recover from many human errors and software failures.

The service does not provide protection from regional or dual-zone failures. For applications that require this level of protection, we recommend running two separate regional clusters. You can synchronize the data between two clusters by using tools such as MirrorMaker 2.0 from Kafka Connect.

## Tools for your style of administration

The service aims to offer a complete set of tools for your style of cluster management and troubleshooting. This includes tools for administering, monitoring, and logging.

The Managed Service for Apache Kafka is exposed as a [Google Cloud API](https://docs.cloud.google.com/apis). This means that you can manage clusters and cluster resources using REST and gRPC APIs. Several clients and interfaces are provided for these APIs, including

  * Terraform providers if you prefer the infrastructure as code approach.
  * UI in Google Cloud console for interactive work in a browser.
  * The gcloud CLI for interactive work in a shell.
  * Client libraries in Java, Python, Go and other languages for custom development and scripting.



For monitoring and troubleshooting, the service exports metrics to Cloud Monitoring. Some of the metrics are available in the service UI. A complete set is available in Cloud Monitoring for interactive work, configuring alerts, and export to other systems.

The service also exports broker logs to Cloud Logging. These are searchable and can be used to create log-based metrics and alerts.

## Upgrades and patches

Managed Service for Apache Kafka clusters run on Apache Kafka version 3.7.1. The service automatically patches critical security vulnerabilities.

Updates to the underlying infrastructure, including the operating system and orchestration layers, are continuous and automatic. Brokers are updated with a rolling restart, with no downtime to the cluster.

The service doesn't automatically upgrade the Apache Kafka code running on the brokers to new minor versions.

## Transparent cost

The pricing model for Managed Service for Apache Kafka is similar to the charges you see when you run Apache Kafka yourself on [Compute Engine](https://cloud.google.com/products/compute). You pay for the resources you provision—vCPU, RAM, and local storage—and consume—persistent storage and data transfer. Persistent storage and vCPU cost more with Managed Service for Apache Kafka compared to setting up a similar system yourself. In contrast, data transfer and local storage prices are similar between Managed Service for Apache Kafka and self-managed Kafka. For more information about pricing, see [Managed Service for Apache Kafka pricing](https://cloud.google.com/managed-service-for-apache-kafka/pricing).

## Compatible because we run Apache Kafka

Finally, Managed Service for Apache Kafka runs the same [open source software](https://kafka.apache.org) you may already run in your environment. You don't have to change your application code to migrate it to the service.

## Limitations

Managed Service for Apache Kafka has the following limitations:

  * Each cluster must have equal resources in each of the three zones. Single-zone or two-zone Managed Service for Apache Kafka clusters are not supported.

  * You cannot choose the zones when you create the cluster.

  * You cannot configure the volume of local storage on a cluster.

  * Managed Service for Apache Kafka runs in the [KRaft mode](https://kafka.apache.org/37/operations/kraft/). Zookeeper mode is not supported.

  * JMX APIs for metrics are not supported.

  * While you can change broker configurations with `read-only` update mode at any time, these changes take effect only when the brokers restart. Restarts happen periodically as part of Google's maintenance and upgrade processes, but there's no set schedule or a way to manually trigger them. As a result, you can't control when these changes take effect. Examples of `read-only` configurations include `auto.create.topics.enable` and `background.threads`. Updates to configurations with the `cluster-wide` update mode, such as `message.max.bytes`, don't require restarts and take effect immediately.

  * Some broker configuration parameters are managed by the service and cannot be updated. This includes `broker.id` and storage-related settings, such as `remote.log.storage.system.enable`.




## What's next?

  * [Create a Managed Service for Apache Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quickstart-cluster).
  * [Send and receive messages by using a Managed Service for Apache Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quickstart).
  * [Generate synthetic data for a Managed Service for Apache Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quickstart-synthetic-data).
  * Review the [Managed Service for Apache Kafka limitations](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/limitations).
  * Learn about [Managed Service for Apache Kafka pricing](https://cloud.google.com/managed-service-for-apache-kafka/pricing).



_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
