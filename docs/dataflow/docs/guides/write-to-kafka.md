---
url: https://docs.cloud.google.com/dataflow/docs/guides/write-to-kafka/
title: Write from Dataflow to Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:21.222928+00:00
---

# Write from Dataflow to Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/write-to-kafka/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Write from Dataflow to Apache Kafka Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to write data from Dataflow to Apache Kafka.

For most use cases, consider using the [Managed I/O connector](https://docs.cloud.google.com/dataflow/docs/guides/managed-io-kafka) to write to Kafka.

If you need more advanced performance tuning, consider using the `KafkaIO` connector. The `KafkaIO` connector is available for [Java](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/kafka/KafkaIO.html) or by using the [multi-language pipelines framework](https://beam.apache.org/documentation/programming-guide/#multi-language-pipelines) for [Python](https://beam.apache.org/releases/pydoc/current/apache_beam.io.kafka.html) and [Go](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang/kafkaio).

## Exactly-once processing

By default, the `KafkaIO` connector doesn't provide [exactly-once semantics](https://docs.cloud.google.com/dataflow/docs/concepts/exactly-once) for writes. That means data might be written to your Kafka topic multiple times. To enable exactly-once writes, call the [`withEOS`](https://beam.apache.org/releases/javadoc/2.4.0/org/apache/beam/sdk/io/kafka/KafkaIO.Write.html#withEOS-int-java.lang.String-) method. Exactly-once writes guarantee that data is written to the destination Kafka topic exactly once. However, it also increases the pipeline cost and decreases throughput.

If you don't have strict requirements for exactly-once semantics, and the logic in your pipeline can handle duplicate records, consider enabling at-least-once mode for the entire pipeline to reduce costs. For more information, see [Set the pipeline streaming mode](https://docs.cloud.google.com/dataflow/docs/guides/streaming-modes).

### Pipeline drains

If you drain the pipeline, exactly-once semantics are not guaranteed. The only guarantee is that no acknowledged data is lost. As a result, some data might be processed while the pipeline is draining, without the commit of read offsets back to Kafka. To achieve at-least-once semantics for Kafka when you modify a pipeline, [update the pipeline](https://docs.cloud.google.com/dataflow/docs/guides/updating-a-pipeline) instead of cancelling the job and starting a new job.

### Tune Kafka for exactly-once semantics

Adjusting `transaction.max.timeout.ms` and `transactional.id.expiration.ms` can complement your overall fault-tolerance and exactly-once delivery strategy. However, their impact depends on the nature of the outage and your specific configuration. Set `transaction.max.timeout.ms` close to the retention time of your Kafka topics to prevent data duplication caused by Kafka broker outages.

If a Kafka broker becomes temporarily unavailable (for example, due to network partition or node failure), and a producer has ongoing transactions, those transactions might time out. Increasing the value of `transaction.max.timeout.ms` gives transactions more time to complete after a broker recovers, potentially avoiding the need to restart transactions and resend messages. This mitigation indirectly helps maintain exactly-once semantics, by reducing the chance of duplicate messages caused by transaction restarts. On the other hand, a shorter expiration time can help clean up inactive transactional IDs more quickly, reducing potential resource usage.

## Configure networking

By default, Dataflow launches instances within your default Virtual Private Cloud (VPC) network. Depending on your Kafka configuration, you might need to configure a different network and subnet for Dataflow. For more information, see [Specify a network and subnetwork](https://docs.cloud.google.com/dataflow/docs/guides/specifying-networks). When configuring your network, create [firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls) that allow the Dataflow worker machines to reach the Kafka brokers.

If you are using VPC Service Controls, then place the Kafka cluster within the VPC Service Controls perimeter, or else [extend the perimeters to the authorized VPN or Cloud Interconnect](https://docs.cloud.google.com/vpc-service-controls/docs/overview#hybrid_access).

If your Kafka cluster is deployed outside of Google Cloud, you must create a network connection between Dataflow and the Kafka cluster. There are several networking options with different tradeoffs:

  * Connect using a shared RFC 1918 address space, by using one of the following: 
    * [Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview)
    * [IPsec virtual private network (VPN)](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)
  * Reach your externally hosted Kafka cluster through public IP addresses, by using one of the following: 
    * Public internet
    * [Direct peering](https://docs.cloud.google.com/network-connectivity/docs/direct-peering/direct-peering)
    * [Carrier peering](https://docs.cloud.google.com/network-connectivity/docs/carrier-peering)



Dedicated Interconnect is the best option for predictable performance and reliability, but it can take longer to set up because third parties must provision the new circuits. With a public IP–based topology, you can get started quickly because little networking work needs to be done.

The next two sections describe these options in more detail.

#### Shared RFC 1918 address space

Both Dedicated Interconnect and IPsec VPN give you direct access to RFC 1918 IP addresses in your Virtual Private Cloud (VPC), which can simplify your Kafka configuration. If you're using a VPN–based topology, consider setting up a [high-throughput VPN](https://docs.cloud.google.com/solutions/building-high-throughput-vpns).

By default, Dataflow launches instances on your default [VPC network](https://docs.cloud.google.com/vpc/docs/vpc). In a private network topology with [routes explicitly defined in Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview) that connect subnetworks in Google Cloud to that Kafka cluster, you need more control over where to locate your Dataflow instances. You can use Dataflow to configure the `network` and `subnetwork` [execution parameters](https://docs.cloud.google.com/dataflow/pipelines/specifying-exec-params#setting-other-cloud-pipeline-options).

Make sure that the corresponding subnetwork has enough IP addresses available for Dataflow to launch instances on when it attempts to scale out. Also, when you create a separate network for launching your Dataflow instances, ensure that you have a firewall rule that enables TCP traffic among all virtual machines in the project. The default network already has this firewall rule configured.

#### Public IP address space

This architecture uses Transport Layer Security ([TLS](https://wikipedia.org/wiki/Transport_Layer_Security)) to secure traffic between external clients and Kafka, and uses unencrypted traffic for inter-broker communication. When the Kafka listener binds to a network interface that is used for both internal and external communication, configuring the listener is straightforward. However, in many scenarios, the externally advertised addresses of the Kafka brokers in the cluster differ from the internal network interfaces that Kafka uses. In such scenarios, you can use the `advertised.listeners` property:
    
    
    # Configure protocol map
    listener.security.protocol.map=INTERNAL:PLAINTEXT,EXTERNAL:SSL  
    
    # Use plaintext for inter-broker communication
    inter.broker.listener.name=INTERNAL  
    
    # Specify that Kafka listeners should bind to all local interfaces
    listeners=INTERNAL://0.0.0.0:9092,EXTERNAL://0.0.0.0:9093  
    
    # Separately, specify externally visible address
    advertised.listeners=INTERNAL://kafkabroker-n.mydomain.com:9092,EXTERNAL://kafkabroker-n.mydomain.com:9093
    

External clients connect using port 9093 through an "SSL" channel, and internal clients connect using port 9092 through a plaintext channel. When you specify an address under `advertised.listeners`, use DNS names (`kafkabroker-n.mydomain.com`, in this sample) that resolve to the same instance for both external and internal traffic. Using public IP addresses might not work because the addresses might fail to resolve for internal traffic.

## Logging

Logging from `KafkaIO` can be quite verbose. Consider reducing the logging level in production as follows:
    
    
    sdkHarnessLogLevelOverrides='{"org.apache.kafka.clients.consumer.internals.SubscriptionState":"WARN"}'.
    

For more information, see [Set pipeline worker log levels](https://docs.cloud.google.com/dataflow/docs/guides/logging#SettingLevels).

## What's next

  * [Read from Apache Kafka](https://docs.cloud.google.com/dataflow/docs/guides/read-from-kafka).
  * Learn more about [Managed I/O](https://docs.cloud.google.com/dataflow/docs/guides/managed-io).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
