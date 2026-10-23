---
url: https://docs.cloud.google.com/datastream/docs/overview/
title: Datastream overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:42.306782+00:00
---

# Datastream overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Datastream overview Stay organized with collections  Save and categorize content based on your preferences. 

Datastream is a serverless change data capture (CDC) and replication service that lets you synchronize data across heterogeneous databases and applications with minimal latency. Because Datastream is serverless, it scales automatically without requiring you to provision or manage resources.

You can replicate data into BigQuery for near real-time analytics or write change event streams into Cloud Storage for event-driven architectures. Integrating with Pub/Sub and Dataflow templates lets you load data into destinations such as Cloud SQL and Spanner. Datastream also integrates with Knowledge Catalog for centralized metadata and lineage management across Google Cloud.

Datastream supports database sources including MySQL, Oracle, PostgreSQL, AlloyDB for PostgreSQL, SQL Server, MongoDB, and Spanner. You can also stream data from Salesforce and from [Preview](https://cloud.google.com/products#product-launch-stages) sources such as Salesforce Marketing Cloud, Microsoft Dataverse, ServiceNow, and Workday. Private connectivity options, status reporting, and schema change handling support reliable replication for migrations and hybrid-cloud deployments.

## Use cases

The streaming capabilities of Datastream enable a variety of use cases:

  * **Replicating and synchronizing data across your organization with minimal latency**

You can synchronize data across heterogeneous databases and applications reliably, with low latency, and with minimal impact to the performance of your source. Unlock the power of data streams for analytics, database replication, cloud migration, and event-driven architectures across hybrid environments.

  * **Scale up or down with a serverless architecture seamlessly**

Get up and running fast with a serverless and easy-to-use service that scales seamlessly as your data volumes shift. Focus on deriving up-to-date insights from your data and responding to high-priority issues, instead of managing infrastructure, performance tuning, or resource provisioning.

  * **Integrate with the Google Cloud data integration suite**

Connect data across your organization with the Google Cloud data integration suite of products. Integrate Datastream with Dataflow job templates to read data from a Cloud Storage bucket and load it into a variety of destinations, such as BigQuery, Spanner, and Cloud SQL.




## Experience elements

There are three main elements in Datastream:

  * **Private connectivity configurations** enable Datastream to communicate with a data source over a private network (internally within Google Cloud, or with external sources connected over VPN or Interconnect). This communication happens through a Virtual Private Cloud (VPC) peering connection.
  * **Connection profiles** represent connectivity information to both a source and a destination. This information will be used by a stream.
  * **Streams** use the information in the connection profiles to transfer CDC and backfill data from the source to the destination.



## What's next

  * Start replicating your data [from a source database to BigQuery datasets](https://docs.cloud.google.com/datastream/docs/quickstart-replication-to-bigquery).
  * Learn more about [key concepts and features](https://docs.cloud.google.com/datastream/docs/behavior-overview) of Datastream.
  * Find out how to create [private connectivity configurations](https://docs.cloud.google.com/datastream/docs/create-a-private-connectivity-configuration), [connection profiles](https://docs.cloud.google.com/datastream/docs/create-connection-profiles) and [streams](https://docs.cloud.google.com/datastream/docs/create-a-stream).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
