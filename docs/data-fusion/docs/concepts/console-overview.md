---
url: https://docs.cloud.google.com/data-fusion/docs/concepts/console-overview/
title: Introduction to Cloud Data Fusion: Console \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:02.544045+00:00
---

# Introduction to Cloud Data Fusion: Console  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/concepts/console-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Introduction to Cloud Data Fusion: Console Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Data Fusion: Console, also known as the _control plane_ , lets you manage a Cloud Data Fusion instance through a set of [API operations](https://docs.cloud.google.com/data-fusion/docs/reference/rest) and a Google Cloud console interface. For example, you can create, delete, restart, or update an instance.

## Before you begin

  * [Enable the Cloud Data Fusion API](https://docs.cloud.google.com/data-fusion/docs/how-to/enable-service).
  * Understand the [costs of Cloud Data Fusion editions](https://cloud.google.com/data-fusion/pricing).
  * Understand [access control](https://docs.cloud.google.com/data-fusion/docs/access-control) and [service accounts](https://docs.cloud.google.com/data-fusion/docs/concepts/service-accounts) in Cloud Data Fusion.



## Cloud Data Fusion: Console overview

The following sections describe important aspects of the console.

### Instances

An _instance_ is a unique deployment of Cloud Data Fusion. To start using Cloud Data Fusion, you create an instance in the Google Cloud console. You can create multiple Cloud Data Fusion instances in a single Google Cloud project. You can specify a Google Cloud region for each instance. Each instance is a unique, independent Cloud Data Fusion deployment, which contains a set of services that handle pipeline lifecycle management, orchestration, coordination, and metadata management. These services run using long-running resources in a [tenant project](https://docs.cloud.google.com/service-infrastructure/docs/glossary#tenant).

When you create the instance, consider the following options.

#### Edition

You create the instance in one of the following Cloud Data Fusion editions: [Developer, Basic, or Enterprise](https://cloud.google.com/data-fusion/pricing#comparison_of_basic_enterprise_and_developer_editions). Choose the edition based on the following criteria:

  * Cost
  * Concurrency limits for pipeline execution
  * Role-based access control (RBAC) availability



The editions are intended for the following use cases:

Cloud Data Fusion edition | Use case  
---|---  
Developer edition | For development, testing, or small-scale integrations  
Basic edition | For production with moderate needs  
Enterprise edition | For large-scale, mission-critical data pipelines with RBAC  
  
#### Public or private instance

Depending on your requirements, decide if you need a public or a private instance. The key differences between private and public instances in Cloud Data Fusion are network connectivity and security:

Cloud Data Fusion instance type | Behavior  
---|---  
Public instance | 

  * **Network connectivity** : uses public IP addresses to connect to the internet.
  * **Data access** : directly accesses data sources on the public internet.

For more information, see [Create a public instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-instance).  
Private instance | 

  * **Network connectivity** : uses private IP addresses within a Virtual Private Cloud (VPC) network.
  * **Data access** : requires preconfigured connections to access data sources. The following connections are supported: 
    * On-premises data sources connected through VPN or Cloud Interconnect.
    * Other Google Cloud services running privately within the same VPC.

  
**Note:** Cloud Data Fusion recommends [creating private instances with Private Service Connect](https://docs.cloud.google.com/data-fusion/docs/how-to/configure-private-service-connect).

#### Authorization and service account

Cloud Data Fusion typically has two service accounts:

Design-time service account
    This Google-managed service account, called the Cloud Data Fusion API Service Agent, is used in the tenant project of Cloud Data Fusion to access customer project resources.
Execution-time service account
    This is the default Compute Engine service account that Cloud Data Fusion creates to deploy jobs that access other Google Cloud resources. By default, it attaches to a Managed Service for Apache Spark cluster VM to enable Cloud Data Fusion to access Managed Service for Apache Spark resources during a pipeline run.

For more information, see [Service accounts in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/service-accounts).

#### Logging and monitoring

Cloud Logging and Cloud Monitoring are crucial for gaining insights into the health and performance of your Cloud Data Fusion pipelines. You enable Logging and Monitoring only when you create the Cloud Data Fusion instance.

Enabling Logging and Monitoring lets you view Cloud Data Fusion pipeline logs in the Google Cloud console on the **Logging viewer** page.

Monitoring provides built-in dashboards for Cloud Data Fusion. You can also create custom dashboards to monitor specific metrics.

**Note:** Enabling Logging and Monitoring in your instance incurs additional costs. For more information, see [Pricing](https://cloud.google.com/stackdriver/pricing#logging-costs).

#### Lineage integration with Knowledge Catalog

Cloud Data Fusion provides an integration with Knowledge Catalog for lineage. For more information, see [View lineage in Knowledge Catalog](https://docs.cloud.google.com/data-fusion/docs/how-to/view-lineage-in-dataplex).

#### Encryption

Customer-managed encryption keys (CMEK) enable encryption of data at rest with a key that you can control through the Cloud Key Management Service. CMEK provides user control over the data written to Google Cloud internal resources in [tenant projects](https://docs.cloud.google.com/data-fusion/docs/concepts/overview#tenant-project) and data written by Cloud Data Fusion pipelines. For more information, see [Customer managed data encryption](https://docs.cloud.google.com/data-fusion/docs/how-to/customer-managed-encryption-keys).

### Manage permissions with role-based access control (RBAC)

Cloud Data Fusion lets you control with Identity and Access Management (IAM).

For granular permissions for actions performed in Cloud Data Fusion: Studio operations, use RBAC. For more information, see the [RBAC overview](https://docs.cloud.google.com/data-fusion/docs/concepts/rbac).

### Version upgrades

Cloud Data Fusion has versions. You can upgrade an instance to a later version in the Cloud Data Fusion console. For more information, see [Versioning in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/versioning).

## What's next

  * Learn more about [Cloud Data Fusion: Studio](https://docs.cloud.google.com/data-fusion/docs/concepts/studio-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
