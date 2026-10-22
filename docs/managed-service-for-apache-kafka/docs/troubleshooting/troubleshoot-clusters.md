---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/troubleshooting/troubleshoot-clusters/
title: Troubleshoot Kafka cluster errors \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:58.869826+00:00
---

# Troubleshoot Kafka cluster errors  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/troubleshooting/troubleshoot-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Troubleshoot Kafka cluster errors Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues when creating or configuring a Managed Service for Apache Kafka cluster.

## Kafka cluster creation errors

This section lists errors that you might encounter when creating a Kafka cluster.

### The service doesn't have permission to access the Cloud KMS key

The following issue occurs when the Managed Service for Apache Kafka service agent is missing the required permission to access the Cloud KMS key.
    
    
    Service agent service-${PROJECT_NUMBER}@gcp-sa-managedkafka.iam.gserviceaccount.com
    has not been granted the required role cloudkms.cryptoKeyEncrypterDecrypter to
    encrypt data using the KMS key.`
    

To resolve this issue, grant the service account the **Cloud KMS CryptoKey Encrypter/Decrypter** role on the Cloud KMS key. For more information, see [required roles for configuring CMEK](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/encryption#required-roles-and-permissions).

### The service doesn't have permission to retrieve the subnet

The following issue occurs when the Managed Service for Apache Kafka [service agent](https://docs.cloud.google.com/iam/docs/service-agents) is missing the required role to configure networking in the VPC network that the Kafka clients run in.
    
    
    Service does not have permission to retrieve subnet. Please grant
    service-${PROJECT_NUMBER}@gcp-sa-managedkafka.iam.gserviceaccount.com the
    managedkafka.serviceAgent role in the IAM policy of the project
    ${SUBNET_PROJECT} and ensure the Compute Engine API is enabled in project
    ${SUBNET_PROJECT}`
    

To resolve this issue, grant the service account the **Managed Kafka Service Agent** role. For more information, see [Connect a cluster across projects](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/networking-kafka#cross-project-vpc).

## Networking errors

This section lists errors that you might encounter when configuring networking for a Kafka cluster.

### The service failed to set up networking

The following issue occurs if when Managed Service for Apache Kafka can't connect the Kafka cluster to your Virtual Private Cloud subnet.
    
    
    Managed Service for Apache Kafka failed to set up networking in VPC subnet.
    

To resolve this issue, perform the following steps:

  * Enable the Compute Engine and Cloud DNS APIs in the parent project of the consumer VPC network.

  * If the Managed Service for Apache Kafka cluster and consumer VPC network are in different projects, configure the required permissions. See [Connect a cluster across projects](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/networking-kafka#cross-project-vpc).

  * Ensure that no [organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) prevent the service from creating the necessary resources in the consumer VPC network's project.




For more information, see [Configure networking for Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/networking-kafka).

### Client applications can't connect

If your client applications can't connect to your cluster, check for the following issues:

  * Make sure that clients are using the correct [bootstrap address](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster#view-bootstrap-address).

  * Ensure that the Kafka clients run in a VPC network that is configured to access the Managed Service for Apache Kafka cluster.

  * If you run the Kafka client on a computer or laptop, you can set up a Compute Engine instance to use as a proxy to access to the Managed Service for Apache Kafka cluster. For more information, see [Set up a client machine](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quickstart#set_up_a_client_machine).




## Authentication errors

This section lists errors that you might encounter when client applications authenticate to your Kafka cluster.

### SASL authentication fails

The following issue occurs when a client can't connect to the cluster by using SASL authentication.
    
    
    Exception in thread "main" java.util.concurrent.ExecutionException:
    org.apache.kafka.common.errors.SaslAuthenticationException:
    Authentication failed: Invalid username or password
    

To resolve the issue, check for the following causes:

  * The password is malformed, and doesn't represent a valid service account key JSON blob when base64 decoded, or a valid access token.

  * The authenticating principal doesn't have the `managedkafka.clusters.connect` permission on the cluster.

  * The provided username doesn't match the credential's principal.




If a client experiences frequent disconnections every 30 minutes, this can be due to the client not supporting periodic re-authentication. Managed Service for Apache Kafka brokers require clients to re-authenticate every 30 minutes, enforced by the `connections.max.reauth.ms` broker property. Verify that your Kafka client library version is 2.2.0 or later, and supports re-authentication.

For more information, see [Configure SASL authentication](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/authentication-kafka).

## Operational errors

This section lists errors that might occur while your Kafka workloads are running.

### Out-of-disk errors

If a broker runs out of disk space, brokers can't roll active segments or write new segments, which prevents clients from producing or consuming messages. Symptoms include the following:

  * Client performance degrades unexpectedly. For example, producers experience timeout errors and lag steadily increases in consumers.

  * Broker disk utilization is very high (>85%).

  * In-sync replica (ISR) counts drop below the replication factor.

  * Cluster logs show errors like the following:
        
        Error processing append operation on partition PARTITION_ID.
        org.apache.kafka.common.errors.NotEnoughReplicasException: The size of the current ISR Set(10)
        is insufficient to satisfy the min.isr requirement of 2 for partition PARTITION_ID
        




To avoid out-of-disk errors, monitor cluster capacity and partition replication. For more information, see [Monitor Kafka clusters for reliability](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/monitor-reliability).

If a broker runs out of disk space, [increase the broker disk size](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers/configure-disk-size). Also consider [scaling up the cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/update-cluster#resizing) to add new brokers.

[Log compaction](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/edit-topic#log-compaction) combined with a very large key space can result in out-of-disk errors. When log compaction is enabled, Kafka stores the latest message for each key in local storage, so broker disk utilization grows with the number of unique keys.

### Clients experience temporary disconnections

Managed Service for Apache Kafka might perform updates that require rolling restarts on brokers. During this process, requests to individual brokers might fail, but these failures are transient. For more information, see [Upgrades and patches](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview#upgrades).

You don't need to take any action during broker restarts. However, you might observe the following:

  * Pauses in processing while partition leaders and consumer group coordinators fail over to other brokers.

  * Rebalancing of consumer groups, temporarily pausing consumption.

  * Temporary connection errors or timeouts when committing offsets. Commonly used client libraries automatically handle these errors.

  * A temporary spike in the count of under-replicated partitions ([`broker/under_replicated_partitions`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#managedkafka/broker/under_replicated_partitions)) when a broker restarts.

  * A spike in the **Under-MinISR Partitions** metric ([`broker/under_min_isr_partitions`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#managedkafka/broker/under_min_isr_partitions)). This spike likely corresponds to an internal monitoring topic that is not replicated, and is expected behavior as long the count is 1 for each broker. A value greater than 1 might indicate a problem with data or metadata topics.




Manually updating certain cluster properties, such as vCPU count and memory, can also cause the service to perform a rolling restart. See [Update a Managed Service for Apache Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/update-cluster).

## What's next

  * [Use audit logs to troubleshoot](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/troubleshooting/troubleshoot-audit-logs#use_managedkafka_audit_logs)
  * [Troubleshoot mTLS issues](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/troubleshooting/troubleshoot-mTLS)



_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
