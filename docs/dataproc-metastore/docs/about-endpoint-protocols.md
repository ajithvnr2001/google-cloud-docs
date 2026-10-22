---
url: https://docs.cloud.google.com/dataproc-metastore/docs/about-endpoint-protocols/
title: About Dataproc Metastore endpoint protocols \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:18.997870+00:00
---

# About Dataproc Metastore endpoint protocols  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/about-endpoint-protocols/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  About Dataproc Metastore endpoint protocols Stay organized with collections  Save and categorize content based on your preferences. 

When you create a Dataproc Metastore service, you must choose to use one of the following endpoint protocols:

  * The Apache Thrift protocol
  * The gRPC protocol



This protocol defines how your Hive Metastore clients access metadata stored in your Dataproc Metastore service. This choice can also affect the features that you can integrate and use with your service.

This page explains the conceptual differences between each of the endpoint protocols.

### Apache Thrift

The [Apache Thrift](https://thrift.apache.org/) protocol is the legacy default option that is preselected when you create a Dataproc Metastore service.

The Thrift protocol supports Kerberos only for single-region services configured with VPC peering. It does not support Kerberos for any services configured with Private Service Connect.

If you require Kerberos, we recommend using the gRPC protocol instead. The gRPC protocol supports Kerberos for single-region services with all networking configurations.

If you use a Thrift endpoint, you can choose the port number that the Thrift interface connects to. By default, port number `9083` is used.

#### After choosing the Thrift protocol

After you create a Dataproc Metastore using Thrift, you can connect to it from a [Managed Service for Apache Spark cluster or self-managed cluster](https://docs.cloud.google.com/dataproc-metastore/docs/attach-dataproc). Your cluster then uses Dataproc Metastore as its Hive metastore.

### gRPC

The [gRPC protocol](https://grpc.io/) is the modern, portable, high-performance option that you must explicitly select when you create a Dataproc Metastore service.

If you choose the gRPC protocol, you can't update it to Thrift at a later date. If you want to move from gRPC to Thrift, you must create a new Dataproc Metastore.

If you use a gRPC endpoint, you can't choose the port number that the gRPC interface uses. Instead, port number `443` is automatically assigned to your interface.

**Tip:** We recommend that you use the gRPC protocol because it provides additional security through Identity and Access Management (IAM) (IAM). It also supports federation integrations with other Google Cloud products.

#### After choosing the gRPC protocol

After you create a Dataproc Metastore using the gRPC endpoint protocol, you must grant [additional IAM roles](https://docs.cloud.google.com/dataproc-metastore/docs/grpc-endpoints). After, you can connect to it from a [Managed Service for Apache Spark cluster](https://docs.cloud.google.com/dataproc-metastore/docs/attach-dataproc). Your cluster then uses Dataproc Metastore as its Hive metastore.

## What's next

  * [Choose an endpoint protocol](https://docs.cloud.google.com/dataproc-metastore/docs/endpoint-protocol)
  * [Access gRPC endpoints](https://docs.cloud.google.com/dataproc-metastore/docs/grpc-endpoints)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
