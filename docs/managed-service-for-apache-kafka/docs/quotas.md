---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quotas/
title: Quotas and limits \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:29.736007+00:00
---

# Quotas and limits  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Resources ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and system limits that apply to Google Cloud Managed Service for Apache Kafka.

  * _Quotas_ have default values, but you can typically request adjustments.
  * _System limits_ are fixed values that can't be changed.



Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

There are also _system limits_ on Managed Service for Apache Kafka resources. System limits can't be changed. 

## View and manage quotas

For a given project, you can use the **Quotas & System Limits** dashboard to view current quota limits and usage. You can also use this dashboard to do the following:

  * Reduce your quota limits
  * Initiate a process to apply for higher quota limits



[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas)

## Managed Service for Apache Kafka quotas

You can view and edit the quotas listed in the following table for each project in the [**Quotas & System Limits**](https://console.cloud.google.com/iam-admin/quotas) dashboard.

Quota | Default quota limit | Description  
---|---|---  
Clusters per project per region | 5  | The maximum number of clusters allowed per project in a given region.   
CPU capacity per project per region | 750 | The maximum CPU capacity allowed for brokers within a project in given region.  
Memory capacity per project per region | 6,000 GiB | The maximum memory capacity allowed for brokers within a project in a given region.  
Broker local disk capacity per project per region | 200 TiB | The maximum storage capacity allowed for brokers' local disks within a project in a given region.  
Cluster write requests per minute per project per region | 100 | The number of write requests for clusters, such as `UpdateCluster` and `DeleteCluster`, allowed per minute per project in a given region. This quota doesn't limit the rate at which producers can publish records.  
Cluster create requests per minute per project per region | 1  | The number of `CreateCluster` requests allowed per minute per project in a given region.  
Cluster read requests per minute per project per region. | 600  | The number of read requests for clusters, such as `GetCluster` and `ListClusters`, allowed per minute per project in a given region. This quota doesn't limit the rate at which consumers can read records.  
Cluster authenticate connection requests per minute per project per region. | 1200  | The number of client connections that can be authenticated, per minute per project in a given region.  
Topic write requests per minute per project per region. | 100 | The number of write requests for topics, such as `CreateTopic`, `UpdateTopic`, and `DeleteTopic`, allowed per minute per project in a given region.  
Topic read requests per minute per project per region. | 600  | The number of read requests for topics, such as `GetTopic` and `ListTopics`, allowed per minute per project in a given region.  
Consumer group write requests per minute per project per region. | 100 | The number of write requests for consumer groups, such as `UpdateConsumerGroup` and `DeleteConsumerGroup`, allowed per minute per project in a given region.  
Consumer group read requests per minute per project per region. | 600  | The number of read requests for consumer groups, such as `GetConsumerGroup` and `ListConsumerGroups`, allowed per minute per project in a given region.  
Operations requests per minute per project per region | 1200  | The number of requests for long-running operations allowed per minute per project in a given region.  
Connect clusters per region | 5 | The maximum number of Connect clusters allowed per project in a given region.  
Connect cluster memory capacity per region | 800 GiB | The maximum memory capacity allowed for Connect clusters within a project in a given region.  
Connect cluster CPU capacity per region | 800 | The maximum CPU capacity allowed for Connect clusters within a project in a given region.  
Connect cluster create requests per minute, per region | 1 | The number of `CreateConnectCluster` requests allowed per minute per project in a given region.  
Connect cluster read requests per minute, per region | 600 | The number of read requests for Connect clusters, such as `GetConnectCluster` and `ListConnectClusters`, allowed per minute per project in a given region.  
Connect cluster write requests per minute, per region | 100 | The number of write requests for Connect clusters, such as `UpdateConnectCluster` and `DeleteConnectCluster`, allowed per minute per project in a given region.  
Connector read requests per minute, per region | 600 | The number of read requests for connectors, such as `GetConnector` and `ListConnectors`, allowed per minute per project in a given region.  
Connector write requests per minute, per region | 100 | The number of write requests for connectors, such as `CreateConnector`, `UpdateConnector`, `DeleteConnector`, `PauseConnector`, `ResumeConnector`, and `RestartConnector`, allowed per minute per project in a given region.  
**Note:** Default quota limits can vary among projects depending on the project's history. The values quoted here are typical.

## Request a quota increase

To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

## Managed Service for Apache Kafka limits

Managed Service for Apache Kafka has the following limits:

  * [Disk capacity](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers/configure-disk-size): At least 100 GiB per vCPU, and at most 32768 GiB (32 TiB) per broker.
  * Default maximum message size (`message.max.bytes`) of 10 MiB
  * Default number of partitions per topic of 1.



_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
