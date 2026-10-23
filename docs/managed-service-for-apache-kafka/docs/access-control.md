---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/access-control/
title: Access control for Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:54.129650+00:00
---

# Access control for Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Access control for Managed Service for Apache Kafka Stay organized with collections  Save and categorize content based on your preferences. 

In Managed Service for Apache Kafka, you control access to your Kafka clusters and topics by using a combination of Identity and Access Management (IAM) permissions and Kafka access control lists (ACLs):

  * Use IAM to grant permissions for management access, and for clients to connect to a cluster when using [SASL](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/authentication-kafka) authentication.

  * Use Kafka ACLs for data access and operations from open-source Apache Kafka clients.




This page gives an overview of these access control options.

## Managed Kafka Service Agent

Managed Service for Apache Kafka uses a [service agent](https://docs.cloud.google.com/iam/docs/service-agents) to access Google Cloud resources. After you enable the Managed Kafka API, the Managed Kafka Service Agent is created.

The Managed Kafka Service Agent is a principal with the identifier `service-PROJECT_NUMBER@gcp-sa-managedkafka.iam.gserviceaccount.com`, where `PROJECT_NUMBER` is your Google Cloud project number.

This service agent requires the Managed Kafka Service Agent (`roles/managedkafka.serviceAgent`) IAM role on the project. This role is automatically granted when you enable the API. If you revoke this role, Managed Service for Apache Kafka can't create, update or delete clusters.

For some tasks, the Managed Kafka Service Agent requires additional roles. For example, if you use [Kafka Connect](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-connect-overview), then you might need to grant the service agent permission to access sources and sinks, such as Pub/Sub or BigQuery.

## Access control for clients

There are generally two ways to perform operations on Managed Service for Apache Kafka resources:

  * The Managed Kafka API. This option encompasses calling the [REST APIs](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest) directly, as well as using Google Cloud CLI, the Google Cloud console, or the client libraries.

  * The open-source Apache Kafka API. Many open-source Kafka clients use this API.




### Access control using the Managed Kafka API

When using the Managed Kafka API, authorization is performed by Identity and Access Management (IAM). To perform an operation on a resource, the principal must have the required Managed Kafka API permissions for that operation. The documentation for each task lists the IAM roles needed for that task. For example, to allow a principal to [create Kafka topics](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-topic), grant the principal the [Managed Kafka Topic Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.topicEditor) role.

### Access control using the Apache Kafka API

Clients that use the Apache Kafka API authenticate by using either [SASL](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/authentication-kafka) or [mutual TLS](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/authentication-kafka-mtls) (mTLS) authentication.

  * If a client connects with SASL, the authenticating principal needs the `managedkafka.clusters.connect` IAM permission. To give this permission, you can grant the [Managed Kafka Client](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.client) (`roles/managedkafka.client`) role on the principal.

  * If a client connects with mTLS, the `managedkafka.clusters.connect` permission isn't required. Instead, clients use [client certificates](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/authentication-kafka-mtls#kafka-clients) to authenticate.




After the client connects, the service uses [Kafka ACLs](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/access-control-kafka-acls) to authorize the client's operations, such as reading or altering resources.

### Combined access control

For comprehensive security, you must configure the following:

  * IAM permissions for management access.

  * IAM permission to connect to the cluster, if clients use SASL.

  * Kafka ACLs for in-cluster data access and operations from open-source Apache Kafka clients, regardless of the authentication method.




For example, assume that you want to prevent a principal from editing topics. To do so, you would set up the following access controls:

  * Deny the principal the `managedkafka.topics.update` permission, to prevent the principal from using the Managed Kafka API to update topics (for example, by using the Google Cloud console).

  * Optionally, deny the principal the `managedkafka.clusters.connect` permission, to prevent the principal from connecting to the cluster with SASL authentication.

  * If the principal needs SASL access for other reasons, or if the principal connects using mTLS, create a Kafka ACL that denies `ALTER`, `ALTER_CONFIGS`, and `DELETE` operations on topics. For specific examples, see [Deny modifying all topics](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/access-control-kafka-acls#deny-modify-all-topics).




## Resource-level access control

To restrict a principal's IAM permissions to specific Managed Service for Apache Kafka resources within a project, such as individual clusters or topics, use [IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview).

The following example shows an IAM condition that allows access only if the resource type is `managedkafka.googleapis.com/Topic` and the resource name ends in `"test-topic"`:
    
    
    {
        "expression": "resource.name.endsWith(\"topic-1\") &&\nresource.type == \"managedkafka.googleapis.com/Topic\"",
        "title": "topic-1",
        "description": "Grant access only to topic-1"
    }
    

Some Managed Service for Apache Kafka requests, such as cluster creation or updates, return long-running operations. If you grant access at the cluster level, include access for all resources of type `managedkafka.googleapis.com/Operation`, in addition to the per-cluster resource condition. This permission ensures the principal can initiate the operation and monitor its progress.

## What's next

  * To learn more about the fundamental concepts of IAM, see [Overview of IAM](https://docs.cloud.google.com/iam/docs/overview).

  * To learn about the different components of an IAM policy, see [IAM policy](https://docs.cloud.google.com/iam/docs/overview#iam-policy).

  * To learn how to use Kafka ACLs for in-cluster data access, see [Kafka ACLs](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/access-control-kafka-acls).

  * [Managed Service for Apache Kafka roles and permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka).




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
