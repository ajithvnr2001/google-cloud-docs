---
url: https://docs.cloud.google.com/spanner-omni/differences/
title: Differences between Spanner and Spanner Omni \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:58.886745+00:00
---

# Differences between Spanner and Spanner Omni  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner-omni/differences/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner Omni ](https://docs.cloud.google.com/spanner-omni)
  * [ Guides ](https://docs.cloud.google.com/spanner-omni/overview)



Send feedback 

#  Differences between Spanner and Spanner Omni Stay organized with collections  Save and categorize content based on your preferences. 

Use this document to learn about the key differences between the cloud-based, managed Spanner service and the self-managed, downloadable Spanner Omni database.

While both products share the same distributed database engine, they differ in how you deploy, scale, secure, and manage them.

## Core differences and management model

The following table compares the licensing, environments, and service-level agreements (SLAs) for the two products.

Management model and environment differences  Feature | Spanner | Spanner Omni  
---|---|---  
Management model |  Google Cloud fully manages the service. Google handles deployment, patching, backups, and maintenance.  |  You manage the database. You install, patch, back up, and maintain the hardware and software. For more information, see the [Spanner Omni overview](https://docs.cloud.google.com/spanner-omni/overview).   
Deployment environment |  Runs exclusively within Google Cloud infrastructure.  |  Runs on your own hardware, including on-premises data centers, other cloud providers, and your laptop. For more information, see the [system requirements](https://docs.cloud.google.com/spanner-omni/system-requirements).   
Installation |  You access the database as a service. You don't need to install any software.  |  You must download and install the binaries or container images.   
Updates and upgrades |  Google automatically applies updates and upgrades without downtime.  |  You apply updates and patches manually, with no downtime for scale-out deployments. For more information, see [maintain a deployment](https://docs.cloud.google.com/spanner-omni/maintain-deployment).   
Service Level Agreement (SLA) |  Google Cloud service level agreements (SLAs) apply. For more information, see the [Spanner SLA page](https://cloud.google.com/spanner/sla).  |  Spanner Omni doesn't have an SLA. Availability depends on your infrastructure and configuration.   
Pricing |  Google charges based on compute resource capacity (nodes or processing units), database storage, backup storage, replication, Data Boost, and network egress. For more information, see the [Spanner pricing page](https://cloud.google.com/spanner/pricing) (outside this documentation set).  |  You incur self-managed infrastructure costs. Google charges a licensing fee for Spanner Omni production and commercial usage. For more information, see the [Spanner Omni pricing details](https://cloud.google.com/products/spanner/omni).   
  
## Feature support and compatibility

Google strives for feature parity between Spanner and Spanner Omni. However, there are differences between the managed version of Spanner that runs in Google Cloud and Spanner Omni. While Spanner Omni runs the same underlying query engine, it doesn't support all of the features in the cloud-managed service. The following table lists the primary differences.

Feature support and compatibility differences  Feature | Spanner | Spanner Omni  
---|---|---  
Supported features |  Provides the full Spanner feature set.  |  Supports core Spanner features. For more information, see the [Spanner Omni overview](https://docs.cloud.google.com/spanner-omni/overview).  The following features are not supported:

  * BigQuery integration (for example, [federation](https://docs.cloud.google.com/bigquery/docs/spanner-federated-queries), [external schema](https://docs.cloud.google.com/bigquery/docs/spanner-external-datasets), and exporting data to Spanner Omni using [reverse ETL](https://docs.cloud.google.com/bigquery/docs/export-to-spanner)) 
  * [Gemini Enterprise Agent Platform in Databases](https://docs.cloud.google.com/spanner/docs/write-sql-gemini) integration 
  * [`MODEL` DDL statements](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-definition-language#model_statements) and [machine learning and AI functions](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/ml-functions)
  * [Data Boost](https://docs.cloud.google.com/spanner/docs/databoost/databoost-overview)
  * [Knowledge Catalog integration](https://docs.cloud.google.com/spanner/docs/dc-integration)
  * [Geo-partitioning](https://docs.cloud.google.com/spanner/docs/geo-partitioning)
  * [Full-Text Search enhanced query mode](https://docs.cloud.google.com/spanner/docs/full-text-search)
  * High-scale [approximate nearest neighbor (ANN) search](https://docs.cloud.google.com/spanner/docs/vector-search-overview)
  * [Tiered storage](https://docs.cloud.google.com/spanner/docs/tiered-storage)
  * [Incremental backups](https://docs.cloud.google.com/spanner/docs/backup)
  * Built-in customer-managed encryption keys (CMEK) integration 
  * Automatic reconfiguration to a single region in dual-region mode 
  * [Scale-up graph algorithms](https://docs.cloud.google.com/spanner/docs/graph/graph-algorithms-overview)

  
Point-in-Time Recovery (PITR) |  You can configure the version retention period up to seven days. For more information, see [Point-in-Time Recovery](https://docs.cloud.google.com/spanner/docs/pitr).  |  You can configure the version retention period up to 30 days. For more information, see the [timestamp bounds documentation](https://docs.cloud.google.com/spanner/docs/timestamp-bounds#maximum_timestamp_staleness).   
TrueTime implementation |  Uses Google's hardware-based synchronized atomic clocks and GPS receivers in Google Cloud data centers. For more information, see [TrueTime and external consistency](https://docs.cloud.google.com/spanner/docs/true-time-external-consistency).  |  Uses a software-defined TrueTime API to maintain strong external consistency. For more information, see [TrueTime and external consistency](https://docs.cloud.google.com/spanner-omni/true-time-external-consistency).   
Client library support |  Supports a wide range of programming languages. For more information, see [APIs and client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries).  |  Supports Java, Go, and Python. For more information, see [client library support](https://docs.cloud.google.com/spanner-omni/client-library-overview).   
API protocols |  Supports both gRPC and REST APIs.  |  Supports gRPC.   
  
## Security, authentication, and authorization

The security implementation of the self-managed model uses a shared responsibility structure. The following table outlines the security configurations and access controls.

Security, authentication, and authorization differences  Feature | Spanner | Spanner Omni  
---|---|---  
Security model |  Google manages physical and infrastructure security.  |  You secure the compute servers, storage, network perimeter, and container environments. For more information, see [authentication and authorization](https://docs.cloud.google.com/spanner-omni/authentication).   
Encryption at rest |  Data at rest is encrypted by default. You can configure customer-managed encryption keys (CMEK) using Cloud Key Management Service. For more information, see [customer-managed encryption keys](https://docs.cloud.google.com/spanner/docs/cmek).  |  Built-in encryption at rest isn't provided. You must configure disk-level or file-system-level encryption (for example, block device encryption). For more information, see the [security overview](https://docs.cloud.google.com/spanner-omni/authentication).   
Encryption in transit |  Google automatically manages and enforces TLS encryption.  |  You must configure TLS 1.3 for client-server connections and mutual TLS (mTLS) for server-server connections. For more information, see [VM deployment encryption](https://docs.cloud.google.com/spanner-omni/deploy-encryption-vms) or [Kubernetes deployment encryption](https://docs.cloud.google.com/spanner-omni/deploy-encryption-kubernetes).   
Authentication |  You authenticate using Identity and Access Management (IAM) configurations (service accounts, users, and groups). For more information, see [IAM](https://docs.cloud.google.com/spanner/docs/iam).  |  You authenticate using passwords (OPAQUE protocol) or client certificates. For more information, see [authentication](https://docs.cloud.google.com/spanner-omni/authentication).   
Authorization |  You authorize actions using IAM roles and permissions. For more information, see [access control with IAM](https://docs.cloud.google.com/spanner/docs/iam).  |  You authorize actions using an internal, IAM-like role system (for example, `roles/spanner.databaseUser`) that is separate from IAM. This system doesn't support custom roles. For more information, see [authorization](https://docs.cloud.google.com/spanner-omni/authentication).   
Network security |  Spanner integrates with Google Cloud network features, such as VPC Service Controls and private endpoints.  |  Depends on your firewall configurations and network architecture.   
Compliance |  Spanner inherits Google Cloud compliance audits and certifications.  |  You must meet all compliance requirements in your hosting environment.   
  
## What's next

  * [Read the Spanner Omni overview](https://docs.cloud.google.com/spanner-omni/overview).

  * [Get started with the quickstart](https://docs.cloud.google.com/spanner-omni/quickstart).

  * [Understand Spanner Omni key terms](https://docs.cloud.google.com/spanner-omni/key-terms).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
