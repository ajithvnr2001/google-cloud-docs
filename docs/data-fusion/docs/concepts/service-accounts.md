---
url: https://docs.cloud.google.com/data-fusion/docs/concepts/service-accounts/
title: Service accounts in Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:59.270689+00:00
---

# Service accounts in Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/concepts/service-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Service accounts in Cloud Data Fusion Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how service accounts are used in Cloud Data Fusion. For more information, see [Use service accounts](https://docs.cloud.google.com/iam/docs/service-accounts).

### Tenant and customer projects

Cloud Data Fusion sets up service accounts to access resources in the following projects:

Tenant project
    

Cloud Data Fusion creates a tenant project to hold the resources and services it needs to manage pipelines on your behalf. For example: running pipelines on your Managed Service for Apache Spark clusters that reside in your customer project. A tenant project is not exposed to you, but when you create a private instance, you might need to use the tenant project name to set up VPC peering.

For more information, see the Service Infrastructure documentation about [tenant projects](https://docs.cloud.google.com/service-infrastructure/docs/glossary#tenant).

Customer project
    

You create and own this project. By default, Cloud Data Fusion creates an ephemeral Managed Service for Apache Spark cluster in this project to run the your pipelines.

The following diagram shows a Cloud Data Fusion instance running in a tenant project and a pipeline running on a Managed Service for Apache Spark cluster in a customer project.

![Deploy the pipeline in Cloud Data Fusion.](https://docs.cloud.google.com/static/data-fusion/docs/images/concepts/cdf-projects-2x.png)

## Service accounts in Cloud Data Fusion

A service account provides an identity for Cloud Data Fusion, which gives Cloud Data Fusion access to your resources.

When you enable the Cloud Data Fusion API and create a Cloud Data Fusion instance, a service account is added to your project to access resources like Service Networking, Managed Service for Apache Spark, Cloud Storage, BigQuery, Spanner, and Bigtable. This service account is called the [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent). Roles are automatically granted to this service agent.

A service account is identified by its email address, which is unique to the account.

The following types of service accounts are used in Cloud Data Fusion. For more information, see [Types of service accounts](https://docs.cloud.google.com/iam/docs/service-account-types).

Service account | Description  
---|---  
`service-CUSTOMER_PROJECT_NUMBER@gcp-sa- datafusion.iam.gserviceaccount.com` | The **service agent** , called the [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent), which Cloud Data Fusion creates to gain access to customer resources so that it can act on the customer's behalf. It is used in the _tenant project_ to access _customer project_ resources. For example, Preview runs in memory instead of in a Managed Service for Apache Spark cluster.  The [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) Identity and Access Management role assigned to the Cloud Data Fusion Service Account by default, includes additional permissions to ensure an optimal user experience. To enhance security, you can create a custom role with a set of [minimum permissions required](https://docs.cloud.google.com/data-fusion/docs/concepts/minimum-permissions) for a task, and assign it to the Cloud Data Fusion Service Account.   
`CUSTOMER_PROJECT_NUMBER- compute@developer.gserviceaccount.com` | The **default Compute Engine service account** that Cloud Data Fusion creates to deploy jobs that access other Google Cloud resources. By default, it attaches to a Managed Service for Apache Spark cluster VM to enable Cloud Data Fusion to access Managed Service for Apache Spark resources during a pipeline run. In the Cloud Data Fusion [Enterprise edition](https://docs.cloud.google.com/data-fusion/pricing#comparison_of_basic_and_enterprise_editions), you can run pipelines from a **user-managed service account** by creating a profile from the Cloud Data Fusion console→System Admin→Configuration tab and adding the custom service account. In versions 6.2.3 and later, you can choose a custom service account to attach to the Managed Service for Apache Spark cluster when creating a Cloud Data Fusion instance. For more information, see [ Service accounts in Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/service-accounts#service_accounts_in_dataproc).  
  
## What's next

  * Learn about [controlling access to data](https://docs.cloud.google.com/data-fusion/docs/access-control).
  * [Give Service Account User permissions](https://docs.cloud.google.com/data-fusion/docs/how-to/granting-service-account-permission).
  * See Cloud Data Fusion [pricing](https://cloud.google.com/data-fusion/pricing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
