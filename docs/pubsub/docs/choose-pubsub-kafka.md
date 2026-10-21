---
url: https://docs.cloud.google.com/pubsub/docs/choose-pubsub-kafka/
title: Choose Pub/Sub or Cloud Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:45:56.217872+00:00
---

# Choose Pub/Sub or Cloud Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/choose-pubsub-kafka/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Choose Pub/Sub or Cloud Managed Service for Apache Kafka Stay organized with collections  Save and categorize content based on your preferences. 

This document guides you in choosing between Pub/Sub and Google Cloud Managed Service for Apache Kafka. Both Pub/Sub and Managed Service for Apache Kafka are horizontally scalable, managed messaging services capable of handling high-volume workloads.

This document is intended for developers, architects, or decision-makers who are seeking a managed service for handling streaming data and messaging workloads.

Several options for running Apache Kafka exists, including partner services and self-managed open source software. This document does not cover those options.

For an overview of Pub/Sub concepts, see [Overview of the Pub/Sub service](https://docs.cloud.google.com/pubsub/docs/pubsub-basics).

For an overview of Managed Service for Apache Kafka concepts, see [Managed Service for Apache Kafka overview](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview).

## Operational ease versus portability

The choice between Pub/Sub and Managed Service for Apache Kafka is a tradeoff between **operational simplicity** and **portability**.

### Operational simplicity of Pub/Sub

Pub/Sub is a wholly managed, serverless, and globally distributed service that uses Google Cloud infrastructure. It automatically scales to handle your workload, so you don't need to worry about managing infrastructure. Pub/Sub dynamically adjusts capacity for individual topics and subscriptions. Publishers and subscribers can scale independently, not only across different topics and subscriptions, but also within the same ones.

Pub/Sub also seamlessly moves data across multiple regions. This means publishers and subscribers can connect to their nearest region, and the service handles the rest.

Managed Service for Apache Kafka can also handle large volumes of data. However, you must manage the cluster size and configure several other properties based on the scaling needs of your topics. Most importantly, you must consider the number of partitions to assign to your topics. Too many partitions can waste resources. Too few partitions can overload the brokers in your Kafka cluster. You must also consider the number of replicas that you have to configure per partition depending on your latency and consumer fan-out requirements.

As a Kafka deployment is tied to a specified region, if you move data across regions, that data movement must happen outside of the service. Ensuring the continued health of the data movement and meeting the needs of the topics in your Kafka cluster adds to your operational work.

### Portability of Managed Service for Apache Kafka

While Pub/Sub's autoscaling and global data distribution make it easier to operate, Apache Kafka APIs are much more broadly adopted.

If you plan to use independent messaging systems in different on-premises or cloud-provider environments, Managed Service for Apache Kafka can give you a more consistent experience across your applications. This is because you can standardize on Kafka and use the same API to communicate with the Kafka service in each environment.

While you can certainly use Pub/Sub as a central messaging system across all your environments, it's important to remember that it is a distinct service with its own API. If you need to interact with a messaging system for a specific environment, using Managed Service for Apache Kafka might offer a more unified development experience.

## Which service is right for you

If consistent experience across diverse environments is paramount, choose Managed Service for Apache Kafka. If your focus is on minimal configuration for scaling workloads or inter-region data movement, Pub/Sub offers a compelling advantage.

Choose Pub/Sub if the following factors describe your requirements:

  * You prioritize operational simplicity within Google Cloud.

  * You need a scalable and serverless solution with minimal overhead management.

  * You have unpredictable or changing workload sizes. Pub/Sub also works great when the workload throughput is stable.

  * You require per-message processing tracking to minimize pipeline effects due to single bad messages. Pub/Sub, with its built-in dead-letter queues (DLQs) and support for out-of-order message processing, lets your system remain operational even when encountering problematic messages.

  * You need inter-region data aggregation.

  * You need independent publisher and subscriber scaling.




Choose Managed Service for Apache Kafka if the following factors describe your requirements:

  * Portability across multiple cloud providers or on-premises environments is critical.

  * You have existing Kafka workloads that you want to migrate to Google Cloud. For more information, see Choose based on the existing Kafka setup.

  * You have consistent traffic volume without much variation.

  * You are willing to handle capacity management.

  * You require message ordering at high throughput per key.

  * You want to use the event sourcing pattern with an event log as a source of truth.




### Choose based on the existing Kafka setup

If you're already using Kafka and seek a managed, secure, and reliable solution on Google Cloud, Managed Service for Apache Kafka is the recommended choice.

If you're already running Kafka and willing to rewrite your applications to get the benefits of a highly scalable, autoscaling, global service, Pub/Sub is a good recommendation. To migrate from Kafka to Pub/Sub, see [Migrate from Kafka to Pub/Sub](https://docs.cloud.google.com/pubsub/docs/migrating-from-kafka-to-pubsub).

For new workloads or users new to streaming on Google Cloud, Pub/Sub is recommended due to its ease of use. If you want to move your existing Kafka workloads to the Cloud with minimal code changes, Managed Service for Apache Kafka is the ideal choice.

## Integration with Cloud products

Both Google Managed Service for Apache Kafka and Pub/Sub integrates with various Google Cloud services like Dataflow, BigQuery, Cloud Storage, and more.

If you need a multi-cloud strategy and prioritize portability across different cloud providers, Managed Service for Apache Kafka offers greater flexibility. This is because Kafka integrates with a wider range of systems outside of Google Cloud as compared to Pub/Sub.

## Feature comparison

If these high level decision criteria in the previous sections don't help, you can make a choice based on specific feature support. For a detailed comparison between the two products, see the following table. 

Feature | Pub/Sub | Managed Service for Apache Kafka  
---|---|---  
Ease of use | Easier to set up and maintain | Requires more operational effort  
Cost model | Pay-for-use | Pay-for-capacity for computePay-for-use for networking and storage.  
Exactly once processing | Supports single simultaneous delivery and strong acknowledgement semantics. | Supports exactly-once side effects when reading from one topic and writing to another.  
Scaling | Seamless auto scaling from KBs to GBs per second per topic that even works for unpredictable workloads. | Requires manual configuration  
Ordered delivery | Offers ordering within keys.1 MBps throughput per fine-grained ordering key | Offers ordering within partitions.Per-partition ordering up to throughput capacity of a partition.  
Data retention | 31 days | Indefinite retention  
End-to-end latency | End-to-end latency typically on the order of 100 milliseconds | Typically on the order of 10 milliseconds for well-behaved subscribers.  
Open source Kafka compatibility for lift and shift | No | Yes  
Identity and Access Management and security | Yes | Yes  
Automatic network configuration | Yes | Yes  
Multi-cloud: identical across clouds | No | Yes  
Uptime SLA | [Yes](https://cloud.google.com/pubsub/sla) | Yes  
Data plane SLA | [Yes](https://cloud.google.com/pubsub/sla) | Not at this time  
Logging and monitoring | Yes | Yes  
Partition rebalancing across brokers | Not applicable | Yes  
Automatic capacity | Pub/Sub dynamically adjusts capacity based on the incoming message rate and subscriber demand. | The service manages the underlying infrastructure such as VMs and storage. You control aspects like the number of partitions, and replication factor.  
Automatic storage management | Yes | Yes  
Automatic software upgrades | Yes | Yes  
Customer support | Yes | Yes  
Kafka Connect Service | Not applicable | With user-provided Connect services  
Schema support | Yes | With user-provided schema registry  
Compatible with ks qIDB, KSQL | No | Yes  
Support for OSS connectors | Yes for Kafka and Flink connectors | No  
Integration with Data Lake and Data Warehouse | Yes | Yes  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
