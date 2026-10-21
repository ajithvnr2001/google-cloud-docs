---
url: https://docs.cloud.google.com/composer/docs/composer-1/environment-architecture/
title: Environment architecture \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:15.434973+00:00
---

# Environment architecture  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-1/environment-architecture/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 1 Guides ](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview)



Send feedback 

#  Environment architecture Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/environment-architecture "View this page for Managed Airflow \(Gen 3\)") | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/environment-architecture "View this page for Managed Airflow \(Gen 2\)") | **Managed Airflow (Legacy Gen 1)**

This page describes the architecture of Managed Airflow environments.

## Environment architecture configurations

Managed Airflow (Legacy Gen 1) environments can have the following architecture configurations:

  * Public IP architecture
  * Private IP architecture with VPC peerings
  * Private IP with Domain restricted sharing (DRS) architecture



## Customer and tenant projects

When you create an environment, Managed Airflow distributes the environment's resources between a tenant and a customer project:

  * _Customer project_ is a Google Cloud project where you create your environments. You can create more than one environment in a single customer project.

  * _Tenant project_ is a Google-managed [tenant project](https://docs.cloud.google.com/service-infrastructure/docs/glossary#tenant) and belongs to the Google.com organization. The tenant project provides unified access control and an additional layer of data security to your environment. Each Managed Airflow environment has its own tenant project.




## Environment components

A Managed Airflow environment consists of environment components.

An _environment component_ is an element of a managed Airflow infrastructure that runs on Google Cloud, as a part of your environment. Environment components run either in the tenant or in the customer project of your environment.

### Environment's cluster

_Environment's cluster_ is a [Standard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters#modes) mode [VPC-native](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters#vpc-clusters) or [Routes-based](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters#vpc-clusters) Google Kubernetes Engine cluster of your environment:

**Caution:** Do not introduce changes in the environment's cluster. Clusters for Managed Airflow and workloads deployed into them are managed by Google. It is possible to change the configuration of your environment's cluster, but doing so might break your environment. If you delete an environment's cluster, it cannot be restored; you must delete the environment and create a new environment.

By default, Managed Airflow enables [node auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades) and [node auto-repair](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair) to protect your environment's cluster from security vulnerabilities. These operations happen during maintenance windows that you specify for your environment.

### Environment's bucket

_Environment's bucket_ is a [Cloud Storage bucket](https://docs.cloud.google.com/composer/docs/composer-1/cloud-storage) that stores DAGs, plugins, data dependencies, and Airflow logs. Environment's bucket is located in the customer project.

When you [upload your DAG files](https://docs.cloud.google.com/composer/docs/composer-1/manage-dags) to the `/dags` folder in your environment's bucket, Managed Airflow synchronizes the DAGs to Airflow components of your environment.

**Note:** Because of a service restriction on App Engine, the `data/` and `logs/` folders are not available to the Airflow web server.

### Airflow web server

_Airflow web server_ runs the Airflow UI of your environment.

In Managed Airflow (Legacy Gen 1), Airflow web server runs in the tenant project of your environment.

The Airflow web server is integrated with Identity-Aware Proxy. Managed Airflow hides the IAP integration details, and provides access to the web server based on user identities and IAM policy bindings defined for users.

In Managed Airflow (Legacy Gen 1), the Airflow web server run on a different service account than Airflow workers and Airflow schedulers. The service account for web server is auto-generated during the environment creation and is derived from the web server domain. For example, if the domain is `example.appspot.com`, the service account is `example@appspot.gserviceaccount.com`.

### Airflow database

_Airflow database_ is a [Cloud SQL instance](https://docs.cloud.google.com/sql/docs/introduction) that runs in the tenant project of your environment. It hosts the Airflow metadata database.

To protect sensitive connection and workflow information, Managed Airflow allows database access only to the [service account](https://docs.cloud.google.com/composer/docs/composer-1/access-control#service-account) of your environment.

### Other airflow components

Other Airflow components that run in your environment are:

  * _Airflow schedulers_ parse DAG definition files, schedule DAG runs based on the schedule interval, and queues tasks for execution by Airflow workers. In Managed Airflow (Legacy Gen 1) Airflow DAG processors run as a part of scheduler components. 

  * _Airflow workers_ execute tasks that are scheduled by Airflow schedulers. 




## Public IP environment architecture

[ ![Public IP Managed Airflow environment resources in the tenant project and the customer project](https://docs.cloud.google.com/static/composer/docs/images/composer-1-public-ip-architecture.svg)](https://docs.cloud.google.com/static/composer/docs/images/composer-1-public-ip-architecture.svg) **Figure 1.** Public IP environment architecture (click to enlarge) 

In a Public IP environment architecture for Managed Airflow (Legacy Gen 1):

  * The tenant project hosts a Cloud SQL instance, Cloud SQL storage, and a App Engine Flex instance that runs the Airflow web server.
  * The customer project hosts all other components of the environment.
  * Airflow schedulers and workers in the customer project communicate with the Airflow database through a Cloud SQL proxy instances located in the customer project.
  * Airflow web server in the tenant project communicates with the Airflow database through a Cloud SQL proxy instance located in the tenant project.



## Private IP environment architecture

[ ![Private IP Managed Airflow environment resources in the tenant project and the customer project](https://docs.cloud.google.com/static/composer/docs/images/composer-1-private-ip-architecture.svg)](https://docs.cloud.google.com/static/composer/docs/images/composer-1-private-ip-architecture.svg) **Figure 2.** Private IP environment architecture (click to enlarge) 

In a Private IP environment architecture:

  * The tenant project hosts a Cloud SQL instance, Cloud SQL storage, and **two App Engine instances** that run the Airflow web server.
  * The customer project hosts all other components of the environment.
  * Airflow schedulers and workers connect to the Airflow database through the **HAProxy process** in the environment's cluster.
  * The HAProxy process load balances traffic to the Cloud SQL instance between **two Cloud SQL Proxy instances** that are located in the tenant project. Private IP environments use two Cloud SQL Proxy instances because the customer project does not access the database directly due to network limitations. Two instances are needed to ensure that components of your environment have access to the database at all times.



## Private IP with DRS

[ ![Private IP with DRS Managed Airflow environment resources in the tenant project and the customer project \(click to enlarge\)](https://docs.cloud.google.com/static/composer/docs/images/composer-1-private-ip-drs-architecture.svg)](https://docs.cloud.google.com/static/composer/docs/images/composer-1-private-ip-drs-architecture.svg) **Figure 3.** Private IP environment architecture (click to enlarge) 

If the [Domain Restricted Sharing (DRS) organizational policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) is turned on in your project, then Managed Airflow uses the Private IP with DRS environment architecture.

In the Private IP with DRS environment architecture:

  * The tenant project hosts a Cloud SQL instance, Cloud SQL storage, and two App Engine instances that run the Airflow web server.

  * The tenant project hosts an **additional environment's bucket**. Airflow web server accesses this bucket directly.

  * The customer project hosts all other components of the environment.

  * The customer project hosts the **Bucket Syncing process** in the environment's cluster. This process synchronizes two environment buckets.

  * Airflow schedulers and workers connect to the Airflow database through the HAProxy process in the environment's cluster.

  * The HAProxy process load balances traffic to the Cloud SQL instance between **two Cloud SQL Proxy instances** that are located in the tenant project. Private IP environments use two Cloud SQL Proxy instances because the customer project does not access the database directly due to network limitations. Two instances are needed to ensure that components of your environment have access to the database at all times.




## Integration with Cloud Logging and Cloud Monitoring

Managed Airflow integrates with Cloud Logging and Cloud Monitoring of your Google Cloud project, so that you have a central place to view [Airflow and DAG logs](https://docs.cloud.google.com/composer/docs/composer-1/view-logs).

Cloud Monitoring collects and ingests metrics, events, and metadata from Managed Airflow to [generate insights through dashboards and charts](https://docs.cloud.google.com/composer/docs/composer-1/monitor-environments).

Because of the streaming nature of Cloud Logging, you can view logs emitted by Airflow components immediately instead of waiting for Airflow logs to appear in the Cloud Storage bucket of your environment.

To limit the number of logs in your Google Cloud project, you can [stop all logs ingestion](https://docs.cloud.google.com/logging/docs/exclusions#stop-logs). Do not disable Logging.

## What's next

  * [Create an environment](https://docs.cloud.google.com/composer/docs/composer-1/create-environments)
  * [Versioning overview](https://docs.cloud.google.com/composer/docs/composer-versioning-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
