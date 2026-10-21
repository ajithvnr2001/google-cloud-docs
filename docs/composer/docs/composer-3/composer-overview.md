---
url: https://docs.cloud.google.com/composer/docs/composer-3/composer-overview/
title: Managed Airflow overview \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:15.202166+00:00
---

# Managed Airflow overview  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/composer-overview/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Managed Airflow overview Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/composer-overview "View this page for Managed Airflow \(Gen 2\)") | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview "View this page for Managed Airflow \(Legacy Gen 1\)")

This page provides a brief introduction to Airflow and DAGs, and describes the features and capabilities of Managed Airflow.

For more information about new features in Managed Airflow releases, see [Release notes](https://docs.cloud.google.com/composer/docs/release-notes).

## About Managed Airflow

Managed Airflow is a fully managed workflow orchestration service, enabling you to create, schedule, monitor, and manage workflow pipelines that span across clouds and on-premises data centers.

Managed Airflow is built on the popular [Apache Airflow](https://airflow.apache.org) open source project and operates using the Python programming language.

By using Managed Airflow instead of a local instance of Apache Airflow, you can benefit from the best of Airflow with no installation or management overhead. Managed Airflow helps you create managed Airflow environments quickly and use Airflow-native tools, such as the powerful Airflow web interface and command-line tools, so you can focus on your workflows and not your infrastructure.

## Differences between Managed Airflow versions

For more information about differences between major versions of Managed Airflow, see [Managed Service for Apache Airflow versioning overview](https://docs.cloud.google.com/composer/docs/composer-versioning-overview).

## Airflow and Airflow DAGs (workflows)

In data analytics, a _workflow_ represents a series of tasks for ingesting, transforming, analyzing, or utilizing data. In Airflow, workflows are created using DAGs, or "Directed Acyclic Graphs".

![Relationship between DAGs and tasks](https://docs.cloud.google.com/static/composer/docs/images/overview-dag-and-tasks.svg)**Figure 1.** Relationship between DAGs and tasks 

A _DAG_ is a collection of tasks that you want to schedule and run, organized in a way that reflects their relationships and dependencies. DAGs are created in Python files, which define the DAG structure using code. The DAG's purpose is to ensure that each task is executed at the right time and in the right order.

Each _task_ in a DAG can represent almost anything—for example, one task might perform any of the following functions:

  * Preparing data for ingestion
  * Monitoring an API
  * Sending an email
  * Running a pipeline



In addition to running a DAG on a schedule, you can trigger DAGs manually or in response to events, such as changes in a Cloud Storage bucket. For more information, see [Schedule and trigger DAGs](https://docs.cloud.google.com/composer/docs/composer-3/schedule-and-trigger-dags).

For more information about DAGs and tasks, see the [Apache Airflow documentation](https://airflow.apache.org/docs/stable/concepts.html).

## Managed Airflow environments

_Managed Airflow environments_ are self-contained Airflow deployments based on Google Kubernetes Engine. They work with other Google Cloud services using connectors built into Airflow. You can [create one or more environments](https://docs.cloud.google.com/composer/docs/composer-3/create-environments) in a single Google Cloud project, in any [supported region](https://docs.cloud.google.com/about/locations).

Managed Airflow provisions Google Cloud services that run your workflows and all Airflow components. The main components of an environment are:

  * _GKE cluster_ : Airflow components such as Airflow schedulers, triggerers, and workers run as GKE workloads in a single cluster created for your environment, and are responsible for processing and executing DAGs.

The cluster also hosts [other Managed Airflow components](https://docs.cloud.google.com/composer/docs/composer-3/environment-architecture) like Composer Agent and Airflow Monitoring, which help manage the Managed Airflow environment, gather logs to store in Cloud Logging, and gather metrics to upload to Cloud Monitoring.

  * _Airflow web server_ : The web server runs the Apache Airflow UI.

  * _Airflow database_ : The database holds the Apache Airflow metadata.

  * _Cloud Storage bucket_ : Managed Airflow associates a Cloud Storage bucket with your environment. This bucket, also called _environment's bucket_ , stores the [DAGs](https://docs.cloud.google.com/composer/docs/composer-3/manage-dags), [logs](https://docs.cloud.google.com/composer/docs/composer-3/view-logs), custom [plugins](https://docs.cloud.google.com/composer/docs/composer-3/install-plugins), and data for the environment. For more information about the environment's bucket see [Data stored in Cloud Storage](https://docs.cloud.google.com/composer/docs/composer-3/cloud-storage).




For an in-depth look at the components of an environment, see [Environment architecture](https://docs.cloud.google.com/composer/docs/composer-3/environment-architecture).

## Managed Airflow interfaces

Managed Airflow provides interfaces for managing environments, Airflow instances that run within environments, and individual DAGs.

For example, you can [create](https://docs.cloud.google.com/composer/docs/composer-3/create-environments) and configure Managed Airflow environments in Google Cloud console, Google Cloud CLI, [Cloud Composer API](https://docs.cloud.google.com/composer/docs/apis), or Terraform.

As another example, you can [manage DAGs](https://docs.cloud.google.com/composer/docs/composer-3/manage-dags) from Google Cloud console, [native Airflow UI](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-web-interface), or by running Google Cloud CLI and [Airflow CLI commands](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-cli).

## Airflow features in Managed Airflow

When using Managed Airflow, you can manage and use Airflow features such as:

  * [Airflow DAGs](https://docs.cloud.google.com/composer/docs/composer-3/manage-dags): You can add, update, remove, or trigger Airflow DAGs in Google Cloud console or using the native Airflow UI.

  * [Airflow configuration options](https://docs.cloud.google.com/composer/docs/composer-3/override-airflow-configurations): You can change Airflow configuration options from default values used by Managed Airflow to custom values. In Managed Airflow, some of the configuration options are [blocked](https://docs.cloud.google.com/composer/docs/airflow-configurations), and you cannot change their values.

  * [Airflow connections](https://docs.cloud.google.com/composer/docs/composer-3/manage-airflow-connections).

  * [Airflow UI](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-web-interface).

  * [Airflow CLI](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-cli).

  * [Custom plugins](https://docs.cloud.google.com/composer/docs/composer-3/install-plugins): You can install [custom Airflow plugins](https://airflow.apache.org/docs/apache-airflow/stable/plugins.html), such as custom, in-house Apache Airflow operators, hooks, sensors, or interfaces, into your Managed Airflow environment.

  * [Python dependencies](https://docs.cloud.google.com/composer/docs/composer-3/install-python-dependencies): You can install Python dependencies from the [Python Package Index](https://pypi.org) in your environment or from a private package repository, including Artifact Registry repositories. If the dependencies are not in the package index, you can also use plugins.

  * Logging and monitoring for DAGs, Airflow components, and Managed Airflow environments:

    * You can view Airflow logs that are associated with single DAG tasks in the [Airflow web interface](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-web-interface) and the `logs` folder in the [environment's bucket](https://docs.cloud.google.com/composer/docs/composer-3/cloud-storage).

    * [Cloud Monitoring logs and environment metrics](https://docs.cloud.google.com/composer/docs/composer-3/monitor-environments) for Managed Airflow environments.




## Access control in Managed Airflow

You manage security at the Google Cloud project level and can [assign IAM roles](https://docs.cloud.google.com/composer/docs/composer-3/access-control) that allow individual users to modify or create environments. If someone does not have access to your project or does not have an appropriate Managed Airflow IAM role, that person cannot access any of your environments.

In addition to IAM, you can use [Airflow UI access control](https://docs.cloud.google.com/composer/docs/composer-3/airflow-rbac), which is based on the Apache Airflow Access Control model.

For more information about security features in Managed Airflow, see [Managed Airflow security overview](https://docs.cloud.google.com/composer/docs/composer-3/composer-security-overview).

## Environment networking

Managed Airflow supports several networking configurations for environments, with many configuration options. For example, in a Private IP environment, DAGs and Airflow components are fully isolated from the public internet.

For more information about networking in Managed Airflow, see pages for individual networking features:

  * [Public IP and Private IP environments](https://docs.cloud.google.com/composer/docs/composer-3/change-networking-type)
  * [Connecting an environment to your VPC network](https://docs.cloud.google.com/composer/docs/composer-3/connect-vpc-network)
  * [Shared VPC environments](https://docs.cloud.google.com/composer/docs/composer-3/configure-shared-vpc)
  * [Configuring VPC Service Controls](https://docs.cloud.google.com/composer/docs/composer-3/configure-vpc-sc)



## Other features of Managed Airflow

Other Managed Airflow features include:

  * [Autoscaling environments](https://docs.cloud.google.com/composer/docs/composer-3/scale-environments)
  * [Development with local Airflow environments](https://docs.cloud.google.com/composer/docs/composer-3/run-local-airflow-environments)
  * [Highly resilient environments](https://docs.cloud.google.com/composer/docs/composer-3/set-up-highly-resilient-environments)
  * [Environment snapshots](https://docs.cloud.google.com/composer/docs/composer-3/save-load-snapshots)
  * [Data lineage integration with Knowledge Catalog](https://docs.cloud.google.com/composer/docs/composer-3/lineage-integration)
  * [Encryption with customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/composer/docs/composer-3/configure-cmek-encryption)



## Frequently Asked Questions

### What version of Apache Airflow does Managed Airflow use?

Managed Airflow environments are based on [Managed Airflow images](https://docs.cloud.google.com/composer/docs/composer-versions#images). When you create an environment, you can select an image with a specific Airflow version:

  * Managed Airflow (Gen 3) supports Airflow 2. 
  * Managed Airflow (Gen 2) supports Airflow 2.
  * Managed Airflow (Legacy Gen 1) supports Airflow 1 and Airflow 2. 



You have control over the Apache Airflow version of your environment. You can decide to [upgrade your environment](https://docs.cloud.google.com/composer/docs/composer-3/upgrade-environments) to a later version of Managed Airflow image. Each [Managed Airflow release](https://docs.cloud.google.com/composer/docs/release-notes) supports several Apache Airflow versions.

### Can I use native Airflow UI and CLI?

You can access the Apache Airflow web interface of your environment. Each of your environments has its own Airflow UI. For more information about accessing the Airflow UI, see [Airflow web interface](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-web-interface).

To run Airflow CLI commands in your environments, use `gcloud` commands. For more information about running Airflow CLI commands in Managed Airflow environments, see [Airflow command-line interface](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-cli).

### Can I use my own database as the Airflow database?

Managed Airflow uses a managed database service for the Airflow database. It is not possible to use a user-provided database as the Airflow database.

### Can I use my own cluster as a Managed Airflow cluster?

Managed Airflow uses Google Kubernetes Engine service to create, manage and delete environment clusters where Airflow components run. These clusters are fully managed by Managed Airflow.

It is not possible to build a Managed Airflow environment based on a self-managed Google Kubernetes Engine cluster.

### Can I use my own container registry?

Managed Airflow uses Artifact Registry service to manage container image repositories used by Managed Airflow environments. It is not possible to replace it with a user-provided container registry.

### Are Managed Airflow environments zonal or regional?

When you create an environment, you specify a region for it:

  * Standard Managed Airflow environments have a zonal Airflow database and a multi-zonal Airflow execution layer. The Airflow database is located in one of the zones in the specified region and the Airflow components are distributed between several zones.
  * [Highly resilient](https://docs.cloud.google.com/composer/docs/composer-3/set-up-highly-resilient-environments) (Highly Available) Managed Airflow environments have a multi-zonal Airflow database and a multi-zonal Airflow execution layer. A highly resilient environment runs across at least two zones of the selected region. Managed Airflow automatically distributes the components of your environment between zones. The Cloud SQL component that stores the Airflow database has a primary instance and a standby instance distributed between zones in the selected region.

**Important:** For production use cases, we strongly recommend using [highly resilient environments](https://docs.cloud.google.com/composer/docs/composer-3/set-up-highly-resilient-environments).

## What's next

  * [Security overview](https://docs.cloud.google.com/composer/docs/composer-3/composer-security-overview)
  * [Create environments](https://docs.cloud.google.com/composer/docs/composer-3/create-environments)
  * [Environment architecture](https://docs.cloud.google.com/composer/docs/composer-3/environment-architecture)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
