---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/multiple-gcp-projects/
title: Using multiple Google Cloud projects \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:03:16.921539+00:00
---

# Using multiple Google Cloud projects  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/multiple-gcp-projects/

**Version 1.13**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.13 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/overview)



Send feedback 

#  Using multiple Google Cloud projects Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.13 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/multiple-gcp-projects)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/multiple-gcp-projects)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This document shows how to associate one or more Google Cloud projects with an GKE Enterprise cluster on VMware.

The instructions here are complete. For a shorter introduction to using a Google Cloud project, see [Set up minimal infrastructure](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/minimal-infrastructure).

## Before you begin

[Install Google Cloud CLI](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/cloud-sdk).

## Fleet host project

Every admin cluster must be registered to a [fleet](https://docs.cloud.google.com/anthos/fleet-management/docs). And every user cluster managed by an admin cluster must be registered to the same fleet as the admin cluster.

When an admin or user cluster is registered to a fleet, it is associated with a _fleet host project_. An admin cluster and all the user clusters it manages have the same fleet host project. In the Google Cloud console, in the fleet host project, you can see and manage your admin and user clusters.

To specify a fleet host project for an admin cluster, enter a project ID in the `gkeConnect.projectID` field of the [admin cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-cluster-configuration-file#gkeconnect-section).

If you use the `gkectl` command-line tool to create a user cluster, enter a project ID in the `gkeConnect.projectID` field of the [user cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/user-cluster-configuration-file#gkeconnect-section).

If you use the Google Cloud console to create a user cluster, the current Google Cloud project automatically becomes the fleet host project.

### Enable APIs in your fleet host project

### Linux and macOS

Enable the required APIs in your fleet host project:
    
    
    gcloud services enable --project FLEET_HOST_PROJECT_ID \
        anthos.googleapis.com \
        container.googleapis.com \
        gkehub.googleapis.com \
        gkeconnect.googleapis.com \
        connectgateway.googleapis.com \
        stackdriver.googleapis.com \
        monitoring.googleapis.com \
        logging.googleapis.com \
        opsconfigmonitoring.googleapis.com \
        serviceusage.googleapis.com \
        iam.googleapis.com \
        cloudresourcemanager.googleapis.com
    

If you want to manage the lifecycle of user clusters in the Google Cloud console, the Google Cloud CLI, or Terraform, enable these additional APIs in your fleet host project:
    
    
    gcloud services enable --project FLEET_HOST_PROJECT_ID \
        gkeonprem.googleapis.com \
        anthosaudit.googleapis.com \
        storage.googleapis.com
    

### Windows

Enable the required APIs in your fleet host project:
    
    
    gcloud services enable --project FLEET_HOST_PROJECT_ID ^
        anthos.googleapis.com ^
        container.googleapis.com ^
        gkehub.googleapis.com ^
        gkeconnect.googleapis.com ^
        connectgateway.googleapis.com ^
        stackdriver.googleapis.com ^
        monitoring.googleapis.com ^
        logging.googleapis.com ^
        opsconfigmonitoring.googleapis.com ^
        serviceusage.googleapis.com ^
        iam.googleapis.com ^
        cloudresourcemanager.googleapis.com
    

If you want to manage the lifecycle of user clusters in the Google Cloud console, the Google Cloud CLI, or Terraform, enable these additional APIs in your fleet host project:
    
    
    gcloud services enable --project FLEET_HOST_PROJECT_ID ^
        gkeonprem.googleapis.com ^
        anthosaudit.googleapis.com ^
        storage.googleapis.com
    

### View logs and metrics in your fleet host project

If you want to view cluster logs and metrics in the Google Cloud console, enter the ID of your fleet host project in the `stackdriver.projectID` field of your [admin](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-cluster-configuration-file#stackdriver-projectid-field) and [user](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-cluster-configuration-file#stackdriver-projectid-field) cluster configuration files.

This `stackdriver` section is required by default. That is, if you don't fill in the `stackdriver` section, you must include the `--skip-validation-stackdriver` flag when you run `gkectl create`.

You cannot enter any other project ID in the `stackdriver.projectID` field. If you enter a value, it must be the ID of your fleet host project.

If you choose to view cluster logs and metrics in the Google Cloud console, enable the these APIs in your fleet host project:

### Linux and macOS
    
    
    gcloud services enable --project FLEET_HOST_PROJECT_ID \
        stackdriver.googleapis.com \
        monitoring.googleapis.com \
        logging.googleapis.com \
        opsconfigmonitoring.googleapis.com \
        serviceusage.googleapis.com \
        iam.googleapis.com \
        cloudresourcemanager.googleapis.com
    

### Windows
    
    
    gcloud services enable --project FLEET_HOST_PROJECT_ID ^
        stackdriver.googleapis.com ^
        monitoring.googleapis.com ^
        logging.googleapis.com ^
        opsconfigmonitoring.googleapis.com ^
        serviceusage.googleapis.com ^
        iam.googleapis.com ^
        cloudresourcemanager.googleapis.com
    

### View audit logs in your fleet host project

If you want to view audit logs and in the Google Cloud console, enter the ID of your fleet host project in the `cloudAuditLogging.projectID` field of your [admin](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-cluster-configuration-file#cloudauditlogging-projectid-field) and [user](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/user-cluster-configuration-file#cloudauditlogging-projectid-field) cluster configuration files.

You cannot enter any other project ID in the `cloudAuditLogging.projectID` field. If you enter a value, it must be the ID of your fleet host project.

If you choose to view audit logs in the Google Cloud console, enable these APIs in your fleet host project:

### Linux and macOS
    
    
    gcloud services enable --project FLEET_HOST_PROJECT_ID \
        anthosaudit.googleapis.com \
        serviceusage.googleapis.com \
        iam.googleapis.com \
        cloudresourcemanager.googleapis.com
    

### Windows
    
    
    gcloud services enable --project FLEET_HOST_PROJECT_ID ^
        anthosaudit.googleapis.com ^
        serviceusage.googleapis.com ^
        iam.googleapis.com ^
        cloudresourcemanager.googleapis.com
    

### Granting roles to service accounts on your fleet host project

Your connect-register service account must be granted certain roles on your fleet host project. For details see [Connect-register service account](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/service-accounts#connect_register_service_account).

Your logging-monitoring service account must be granted certain roles on your fleet host project. For details, see [Logging-monitoring service account](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/service-accounts#logging_monitoring_service_account).

Your audit logging service account must be granted certain roles on your fleet host project. For details, see [Audit logging service account](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/service-accounts#audit_logging_service_account).

## Usage metering project

If you enable [GKE usage metering](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering) for a user cluster, Google Distributed Cloud stores usage data in a BigQuery dataset that is associated with a Google Cloud project of your choice. This Google Cloud project is called your _usage metering project_.

Your usage metering project can be the same as your fleet host project, or it can be different.

To enable usage metering, in your [user cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/user-cluster-configuration-file), set `usageMetering.bigQueryProjectID` to the ID of your usage metering project.

If you choose to enable usage metering, enable these APIs in your usage metering project:

### Linux and macOS
    
    
    gcloud services enable --project USAGE_METERING_PROJECT_ID] \
        bigquery.googleapis.com \
        serviceusage.googleapis.com \
        iam.googleapis.com \
        cloudresourcemanager.googleapis.com
    

### Windows
    
    
    gcloud services enable --project USAGE_METERING_PROJECT_ID ^
        bigquery.googleapis.com ^
        serviceusage.googleapis.com ^
        iam.googleapis.com ^
        cloudresourcemanager.googleapis.com
    

### Granting roles to service accounts on your usage metering project

Your usage metering service account must be granted certain roles on your usage metering project.

For details see [usage metering service account](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/service-accounts#usage_metering_service_account).

## Parent project of your component access service account

Before you create a cluster, you must have a service account that Google Distributed Cloud can use to download components from Container Registry. This service account is called your _component access service account_.

The Google Cloud project where you created your component access service account is called the _parent_ of your component access service account. This project can be the same as one of the projects that you specify in your cluster configuration files, or it can be different from all of the projects that you specify in your configuration files. For more information about service accounts and parent projects see [Understanding service accounts and Google Cloud projects](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/service-accounts#understanding_service_accounts_and).

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

## What's next

[Create service accounts and keys](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/service-accounts).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
