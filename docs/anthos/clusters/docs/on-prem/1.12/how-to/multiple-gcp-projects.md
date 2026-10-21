---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/multiple-gcp-projects/
title: Using multiple Google Cloud projects \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:06:31.349205+00:00
---

# Using multiple Google Cloud projects  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/multiple-gcp-projects/

**Version 1.12**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.12 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/overview)



Send feedback 

#  Using multiple Google Cloud projects Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.12 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/multiple-gcp-projects)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/multiple-gcp-projects)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This document shows how to use separate Google Cloud projects for different aspects of Google Distributed Cloud.

The instructions here are complete. For a shorter introduction to using a Google Cloud project, see [Set up minimal infrastructure](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/minimal-infrastructure).

## Before you begin

[Install Google Cloud CLI](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/cloud-sdk).

## Cluster configuration files

The [admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/admin-cluster-configuration-file) and [user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/user-cluster-configuration-file) configuration files have several fields where you can specify a Google Cloud project ID:
    
    
    stackdriver:
      projectID: ""
    ...
    gkeConnect:
      projectID: ""
    ...
    usageMetering:
      bigQueryProjectID: ""
    ...
    cloudAuditLogging:
      projectID: ""
    

The idea is that you can have one project for managing your cluster from the Google Cloud console, another project for viewing logs and metrics, and so on. The one exception is that your audit logging project must be the same as your fleet host project.

You do not have to use separate project IDs. For example, you could use the same project for both managing and logging. If you like, you can use the same project for everything.

## Enabling services in a Google Cloud project

Each of your Google Cloud projects must have certain services enabled. For example, your fleet host project must have these services enabled:
    
    
    cloudresourcemanager.googleapis.com
    container.googleapis.com
    gkeconnect.googleapis.com
    gkehub.googleapis.com
    serviceusage.googleapis.com
    iam.googleapis.com
    

To enable services in a project, you must have certain permissions on the Google Cloud project. For details, see the required permissions for `services.enable` in [Access control](https://docs.cloud.google.com/service-usage/docs/access-control).

If you have the required permissions, you can enable the services yourself. Otherwise, someone else in your organization must enable the services for you.

## Fleet host project

When you create a user cluster, Google Distributed Cloud uses [Connect](https://docs.cloud.google.com/anthos/multicluster-management/connect/overview) to register the cluster with a Google Cloud project of your choice. After your cluster is registered, you can view and manage your cluster in this project in the Google Cloud console.

Connect uses a [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) called the _Connect Agent_ to establish a connection between your user cluster and your Google Cloud project.

In your user cluster configuration file, set `gkecConnect.projectID` to the ID of the Google Cloud project where you want to view and manage your cluster.

**Note:** The Google Cloud project where you view and manage your cluster might be different from the Google Cloud project where you view your cluster's logs and metrics. The project where you view logs and metrics is called the logging-monitoring project.

### Enabling APIs in your fleet host project

To enable the required APIs in your fleet host project:

### Linux and macOS

If you want to manage the lifecycle of user clusters in the Google Cloud console, enable the following APIs:
    
    
    gcloud services enable --project [PROJECT_ID] \
        anthos.googleapis.com \
        anthosgke.googleapis.com \
        anthosaudit.googleapis.com \
        cloudresourcemanager.googleapis.com \
        container.googleapis.com \
        gkeconnect.googleapis.com \
        gkehub.googleapis.com \
        serviceusage.googleapis.com \
        stackdriver.googleapis.com \
        opsconfigmonitoring.googleapis.com \
        monitoring.googleapis.com \
        logging.googleapis.com \
        iam.googleapis.com \
        storage.googleapis.com
    

If you don't plan to use the Google Cloud console to manage the lifecycle of user clusters, enable the following:
    
    
    gcloud services enable --project [PROJECT_ID] \
        cloudresourcemanager.googleapis.com \
        container.googleapis.com \
        gkeconnect.googleapis.com \
        gkehub.googleapis.com \
        serviceusage.googleapis.com \
        iam.googleapis.com
    

where [PROJECT_ID] is the ID of your fleet host project.

### Windows

If you want to manage the lifecycle of user clusters in the Google Cloud console, enable the following APIs:
    
    
    gcloud services enable --project [PROJECT_ID] ^
        anthos.googleapis.com ^
        anthosgke.googleapis.com ^
        gkehub.googleapis.com ^
        gkeconnect.googleapis.com ^
        stackdriver.googleapis.com ^
        storage.googleapis.com
    

If you don't plan to use the Google Cloud console to manage the lifecycle of user clusters, enable the following:
    
    
    gcloud services enable --project [PROJECT_ID] ^
        cloudresourcemanager.googleapis.com ^
        container.googleapis.com ^
        gkeconnect.googleapis.com ^
        gkehub.googleapis.com ^
        serviceusage.googleapis.com ^
        iam.googleapis.com ^
        cloudresourcemanager.googleapis.com

where [PROJECT_ID] is the ID of your fleet host project.

### Granting roles to service accounts on your fleet host project

Your connect-register service account must be granted certain roles on your fleet host project. For details see [Connect-register service account](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/service-accounts#connect_register_service_account)

## Logging-monitoring project

In a user cluster, logging and metrics agents collect data and make it available to Cloud Logging and Cloud Monitoring. To view logs and metrics from your cluster, you must specify an associated Google Cloud project.

In your user cluster configuration file, set `stackdriver.projectID` to the ID of the Google Cloud project that you want to associate with logging and monitoring. This is the project where you will view the cluster's logs and metrics.

**Note:** The Google Cloud project where you view your cluster's logs and metrics might be different from the Google Cloud project where you view and manage your cluster. The project where you view and manage your cluster is called the fleet host project.

### Enabling APIs in your logging-monitoring project

To enable the required APIs in your logging-monitoring project:

### Linux and macOS
    
    
    gcloud services enable --project [PROJECT_ID] \
        stackdriver.googleapis.com \
        opsconfigmonitoring.googleapis.com \
        monitoring.googleapis.com \
        logging.googleapis.com \
        serviceusage.googleapis.com \
        iam.googleapis.com \
        cloudresourcemanager.googleapis.com

where [PROJECT_ID] is the ID of your logging-monitoring project.

### Windows
    
    
    gcloud services enable --project [PROJECT_ID] ^
        stackdriver.googleapis.com ^
        opsconfigmonitoring.googleapis.com ^
        monitoring.googleapis.com ^
        logging.googleapis.com ^
        serviceusage.googleapis.com ^
        iam.googleapis.com ^
        cloudresourcemanager.googleapis.com

where [PROJECT_ID] is the ID of your logging-monitoring project.

### Granting roles to service accounts on your logging-monitoring project

Your logging-monitoring service account must be granted certain roles on your logging-monitoring project.

For details, see [Logging-monitoring service account](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/service-accounts#logging_monitoring_service_account).

## Audit logging project

If you enable [Cloud Audit Logs](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/audit-logging) for a cluster, the audit log entries from the cluster's Kubernetes API server are sent to Google Cloud.

The project where your view audit logs is called your _audit logging project_. Your audit logging project must be the same as your fleet host project.

In the cluster configuration file, set `cloudAuditLogging.projectID` to the ID of your fleet host project.

## Enabling APIs in your audit logging project

To enable the required APIs in your audit logging project:

### Linux and macOS
    
    
    gcloud services enable --project [PROJECT_ID] \
        anthosaudit.googleapis.com \
        serviceusage.googleapis.com \
        iam.googleapis.com \
        cloudresourcemanager.googleapis.com

where [PROJECT_ID] is the ID of your audit logging project.

### Windows
    
    
    gcloud services enable --project [PROJECT_ID] ^
        anthosaudit.googleapis.com ^
        serviceusage.googleapis.com ^
        iam.googleapis.com ^
        cloudresourcemanager.googleapis.com

where [PROJECT_ID] is the ID of your audit logging project.

### Granting roles to service accounts on your audit logging project

Your audit logging service account must be granted certain roles on your audit logging project.

For details, see [Audit logging service account](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/service-accounts#audit_logging_service_account).

## Parent project of your component access service account

Before you create a cluster, you must have a service account that Google Distributed Cloud can use to download components from Container Registry. This service account is called your _component access service account_.

The Google Cloud project where you created your component access service account is called the _parent_ of your component access service account. This project can be the same as one of the projects that you specify in your cluster configuration files, or it can be different from all of the projects that you specify in your configuration files. For more information about service accounts and parent projects see [Understanding service accounts and Google Cloud projects](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/service-accounts#understanding_service_accounts_and).

To enable the required APIs for the parent project of your component access service account:

### Linux and macOS
    
    
    gcloud services enable --project [PROJECT_ID] \
        serviceusage.googleapis.com \
        iam.googleapis.com \
        cloudresourcemanager.googleapis.com

where [PROJECT_ID] is the ID of the parent project of your component access service account.

### Windows
    
    
    gcloud services enable --project [PROJECT_ID] ^
        serviceusage.googleapis.com ^
        iam.googleapis.com ^
        cloudresourcemanager.googleapis.com

where [PROJECT_ID] is the ID of the parent project of your component access service account.

## Usage metering project

If you enable [GKE usage metering](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering) for a user cluster, Google Distributed Cloud stores usage data in a BigQuery dataset that is associated with a Google Cloud project of your choice.

In your [user cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/user-cluster-configuration-file), set `usageMetering.bigQueryProjectID` to the ID of the Google Cloud project where you want to store usage data.

### Enabling APIs in your usage metering project

To enable the required APIs in your usage metering project:

### Linux and macOS
    
    
    gcloud services enable --project [PROJECT_ID] \
        bigquery.googleapis.com \
        serviceusage.googleapis.com \
        iam.googleapis.com \
        cloudresourcemanager.googleapis.com

where [PROJECT_ID] is the ID of your usage metering project.

### Windows
    
    
    gcloud services enable --project [PROJECT_ID] ^
        bigquery.googleapis.com ^
        serviceusage.googleapis.com ^
        iam.googleapis.com ^
        cloudresourcemanager.googleapis.com

where [PROJECT_ID] is the ID of your usage metering project.

### Granting roles to service accounts on your usage metering project

Your usage metering service account must be granted certain roles on your usage metering project.

For details see [usage metering service account](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/service-accounts#usage_metering_service_account).

## What's next

[Create service accounts and keys](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/service-accounts).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
