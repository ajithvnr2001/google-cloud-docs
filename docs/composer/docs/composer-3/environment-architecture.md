---
url: https://docs.cloud.google.com/composer/docs/composer-3/environment-architecture/
title: Environment architecture \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:38.171712+00:00
---

# Environment architecture  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/environment-architecture/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Environment architecture Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/environment-architecture "View this page for Managed Airflow \(Gen 2\)") | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/environment-architecture "View this page for Managed Airflow \(Legacy Gen 1\)")

This page describes the architecture of Managed Airflow environments.

## Environment architecture configurations

Managed Airflow (Gen 3) environments have a single configuration that doesn't depend on the networking type:

  * Managed Airflow (Gen 3) architecture



## Customer and tenant projects

When you create an environment, Managed Airflow distributes the environment's resources between a tenant and a customer project:

  * _Customer project_ is a Google Cloud project where you create your environments. You can create more than one environment in a single customer project.

  * _Tenant project_ is a Google-managed [tenant project](https://docs.cloud.google.com/service-infrastructure/docs/glossary#tenant) and belongs to the Google.com organization. The tenant project provides unified access control and an additional layer of data security to your environment. Each Managed Airflow environment has its own tenant project.




## Environment components

A Managed Airflow environment consists of environment components.

An _environment component_ is an element of a managed Airflow infrastructure that runs on Google Cloud, as a part of your environment. Environment components run either in the tenant or in the customer project of your environment.

### Environment's bucket

_Environment's bucket_ is a [Cloud Storage bucket](https://docs.cloud.google.com/composer/docs/composer-3/cloud-storage) that stores DAGs, plugins, data dependencies, and Airflow logs. Environment's bucket is located in the customer project.

When you [upload your DAG files](https://docs.cloud.google.com/composer/docs/composer-3/manage-dags) to the `/dags` folder in your environment's bucket, Managed Airflow synchronizes the DAGs to Airflow components of your environment.

### Airflow web server

_Airflow web server_ runs the Airflow UI of your environment.

Managed Airflow provides access to the interface based on user identities and IAM policy bindings defined for users.

### Airflow database

_Airflow database_ is a [Cloud SQL instance](https://docs.cloud.google.com/sql/docs/introduction) that runs in the tenant project of your environment. It hosts the Airflow metadata database.

To protect sensitive connection and workflow information, Managed Airflow allows database access only to the [service account](https://docs.cloud.google.com/composer/docs/composer-3/access-control#service-account) of your environment.

### Other airflow components

Other Airflow components that run in your environment are:

  * _Airflow schedulers_ parse DAG definition files, schedule DAG runs based on the schedule interval, and queues tasks for execution by Airflow workers. 

  * _Airflow triggerers_ asynchronously monitor all deferred tasks in your environment. If you set the number of triggerers in your environment above zero, then you can use [deferrable operators in your DAGs](https://docs.cloud.google.com/composer/docs/composer-3/use-deferrable-operators).

  * _Airflow DAG processors_ process DAG files and turns them into DAG objects. In Managed Airflow (Gen 3), DAG processors run as separate environment components.

  * _Airflow workers_ execute tasks that are scheduled by Airflow schedulers. The minimum and maximum number of workers in your environment changes dynamically depending on the number of tasks in the queue. 




## Managed Airflow (Gen 3) environment architecture

[ ![Managed Airflow \(Gen 3\) environment resources in the tenant project and the customer project](https://docs.cloud.google.com/static/composer/docs/images/composer-3-architecture.png)](https://docs.cloud.google.com/static/composer/docs/images/composer-3-architecture.png) **Figure 1.** Managed Airflow (Gen 3) environment architecture (click to enlarge) 

In Managed Airflow (Gen 3) environments:

  * The tenant project hosts a Cloud SQL instance with the Airflow database.
  * All Airflow resources run in the tenant project.
  * The customer project hosts the environment's bucket.
  * A custom VPC network attachment in the customer project can be used to attach the environment to a custom VPC network. You can use an existing attachment or Managed Airflow can create it automatically on demand. It is also possible to detach an environment from a VPC network.
  * Google Cloud console, Monitoring, and Logging in the customer project provide ways to manage the environment, DAGs and DAG runs, and to access environment's metrics and logs. You can also use Airflow UI, Google Cloud CLI, Cloud Composer API and Terraform for the same purposes.



In highly-resilient Managed Airflow (Gen 3) environments:

  * The Cloud SQL instance of your environment is configured for high availability (is a regional instance). Within a regional instance, the configuration is made up of a primary instance and a standby instance.

  * Your environment runs the following Airflow components in separate zones:

    * Two Airflow schedulers
    * Two web servers
    * At least two DAG processors (up to 10 total)
    * If triggerers are used, at least two triggerers (up to 10 total)

    * The minimum number of workers is set to two, and your environment's cluster distributes worker instances between zones. In case of a zonal outage, affected worker instances are rescheduled in a different zone.




## Integration with Cloud Logging and Cloud Monitoring

Managed Airflow integrates with Cloud Logging and Cloud Monitoring of your Google Cloud project, so that you have a central place to view [Airflow and DAG logs](https://docs.cloud.google.com/composer/docs/composer-3/view-logs).

Cloud Monitoring collects and ingests metrics, events, and metadata from Managed Airflow to [generate insights through dashboards and charts](https://docs.cloud.google.com/composer/docs/composer-3/monitor-environments).

Because of the streaming nature of Cloud Logging, you can view logs emitted by Airflow components immediately instead of waiting for Airflow logs to appear in the Cloud Storage bucket of your environment.

To limit the number of logs in your Google Cloud project, you can [stop all logs ingestion](https://docs.cloud.google.com/logging/docs/exclusions#stop-logs). Do not disable Logging.

## What's next

  * [Create an environment](https://docs.cloud.google.com/composer/docs/composer-3/create-environments)
  * [Versioning overview](https://docs.cloud.google.com/composer/docs/composer-versioning-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
