---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/service-accounts/
title: Service accounts and keys \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:25:38.953894+00:00
---

# Service accounts and keys  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/service-accounts/

**Version 1.11**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.11 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/overview)



Send feedback 

#  Service accounts and keys Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.11 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/service-accounts)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/service-accounts)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This document explains the Google Cloud service accounts and keys that you need to create clusters in your Google Distributed Cloud implementation. 

The instructions here are complete. For a shorter introduction to using a service account, see [Set up minimal infrastructure](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/minimal-infrastructure).

## Before you begin

[Create Google Cloud projects](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/multiple-gcp-projects).

## Overview of service accounts

Before you create your admin and user clusters, you need to have these service accounts:

  * Component access service account
  * Connect-register service account
  * Logging-monitoring service account



Depending on the features you want to enable, you might also need to have some optional service accounts.

## Understanding service accounts and Google Cloud projects

When you create a service account, you associate it with a Google Cloud project. This Google Cloud project is called the _parent project_ of the service account.

You can determine the parent project of a service account by looking at the email address of the service account. For example, here is the email address of a service account named `logger`. The parent project is `alice-123`.
    
    
    logger@alice-123.iam.gserviceaccount.com
    

When you grant an [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) role to a service account, you grant the role _to_ the service account _on_ a particular Google Cloud project. This follows the general pattern of [granting a role to an identity on a resource](https://docs.cloud.google.com/iam/docs/overview#how_cloud_iam_works).

For example, you could grant the `bigquery.dataEditor` role to the `logger@alice-123.iam.gserviceaccount.com` service account on the `bob-456` project. In this case, the service account is the identity, and the Google Cloud project is the resource.

It is important to understand that you can grant a role to a service account on a Google Cloud project that is not the parent project of the service account.

## Permissions for granting roles to service accounts

Each of your service accounts must be granted certain roles on the relevant Google Cloud project. For example, your connect-register service account must be granted the `gkehub.admin` role on your fleet host project.

To grant roles on a Google Cloud project, you must have certain permissions on the project. For details, see `roles/resourcemanager.projectIamAdmin` in [Understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

If you have the required permissions, you can grant the roles yourself. Otherwise, someone else in your organization must grant the roles for you.

## Using `gkeadm` to automatically create service accounts

This page shows how to manually create service accounts and grant roles to service accounts. As an alternative to doing these steps manually, you can have `gkeadm` create some of the service accounts, and grant roles, for you when you create an admin workstation. For more information, see [Creating your admin workstation](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/create-admin-workstation).

## Component access service account

Google Distributed Cloud uses this service account to download cluster components, on your behalf, from Container Registry.

To create a component access service account:
    
    
    gcloud iam service-accounts create component-access-sa \
        --display-name "Component Access Service Account" \
        --project PROJECT_ID
    

Replace PROJECT_ID with the ID of the Google Cloud project that you want to be the parent project of your service account.

To create a JSON key for your component access service account:
    
    
    gcloud iam service-accounts keys create component-access-key.json \
       --iam-account SERVICE_ACCOUNT_EMAIL
    

Replace SERVICE_ACCOUNT_EMAIL with the email address of your component access service account.

### Granting roles to your component access service account

The admin and user cluster configuration files have several fields that specify a project ID.

In the admin cluster configuration file:
    
    
    stackdriver:
      projectID: ""
    ...
    cloudAuditLogging:
      projectid: ""
    

In the user cluster configuration file:
    
    
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
      projectid: ""
    

The project IDs in your configuration files do not have to be distinct. For example, `gkeConnect.projectID` could be the same as `cloudAuditLogging.projectID`. In fact, all of the project IDs in your configuration files could be the same.

Your component access service account must be granted the following [IAM roles](https://docs.cloud.google.com/iam/docs/understanding-roles) on each Google Cloud project that is specified in your admin and user cluster configuration files. These roles are required so that Google Distributed Cloud can do preflight checks:

  * `serviceusage.serviceUsageViewer`
  * `iam.roleViewer`
  * `iam.serviceAccountViewer`



For each Google Cloud project that you specified in your cluster configuration files, run the following commands to grant the required roles to your component access service account:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member "serviceAccount:SERVICE_ACCOUNT_EMAIL" \
        --role "roles/serviceusage.serviceUsageViewer"
    
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member "serviceAccount:SERVICE_ACCOUNT_EMAIL" \
        --role "roles/iam.roleViewer"
    
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member "serviceAccount:SERVICE_ACCOUNT_EMAIL" \
        --role "roles/iam.serviceAccountViewer"
    

Replace the following:

  * PROJECT_ID: the ID of one of the Google Cloud projects you specified in your configuration files.

  * SERVICE_ACCOUNT_EMAIL: the email address of your component access service account.




## Connect-register service account

Google Distributed Cloud uses this service account to register your user clusters with Google Cloud.

To create a connect-register service account:
    
    
    gcloud iam service-accounts create connect-register-sa \
        --project PROJECT_ID
    

Replace PROJECT_ID with the ID of the Google Cloud project that you want to be the parent of your connect-register service account.

To create a JSON key for your connect-register service account:
    
    
    gcloud iam service-accounts keys create connect-register-key.json \
       --iam-account SERVICE_ACCOUNT_EMAIL
    

Replace SERVICE_ACCOUNT_EMAIL with the email address of your connect-register service account.

Your connect-register service account must be granted the `gkehub.admin` role on your [fleet host project](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/multiple-gcp-projects#fleet_host_project). This is the Google Cloud project where you want to view and manage your clusters.

**Note:** In version 1.11.2 and later patches of 1.11, it is sufficient to grant the `gkehub.editor` role to your connect-register service account.

To grant the `gkehub.admin` role to your connect-register service account:
    
    
    gcloud projects add-iam-policy-binding FLEET_HOST_PROJECT_ID \
        --member "serviceAccount:SERVICE_ACCOUNT_EMAIL" \
        --role "roles/gkehub.admin"
    

Replace FLEET_HOST_PROJECT_ID with the ID of your fleet host project.

### Logging-monitoring service account

Google Distributed Cloud uses this service account to export logs and metrics from clusters to [Cloud Logging](https://docs.cloud.google.com/logging/docs) and [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs).

To create a logging-monitoring service account:
    
    
    gcloud iam service-accounts create logging-monitoring-sa \
        --project=PROJECT_ID
    

Replace PROJECT_ID with the ID of the Google Cloud project that you want to be the parent of your logging-monitoring service account.

To create a JSON key for your logging-monitoring service account:
    
    
    gcloud iam service-accounts keys create logging-monitoring-key.json \
        --iam-account SERVICE_ACCOUNT_EMAIL
    

Replace SERVICE_ACCOUNT_EMAIL with the email address of your logging-monitoring service account.

Your logging-monitoring service account must be granted the following roles on your [logging-monitoring project](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/multiple-gcp-projects#logging_monitoring_project). This is the Google Cloud project where you want to view logs for your clusters.

  * `stackdriver.resourceMetadata.writer`
  * `opsconfigmonitoring.resourceMetadata.writer`
  * `logging.logWriter`
  * `monitoring.metricWriter`
  * `monitoring.dashboardEditor`



To grant the required roles to your logging-monitoring service account:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member "serviceAccount:SERVICE_ACCOUNT_EMAIL" \
        --role "roles/stackdriver.resourceMetadata.writer"
    
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member "serviceAccount:SERVICE_ACCOUNT_EMAIL" \
        --role "roles/opsconfigmonitoring.resourceMetadata.writer"
    
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member "serviceAccount:SERVICE_ACCOUNT_EMAIL" \
        --role "roles/logging.logWriter"
    
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member "serviceAccount:SERVICE_ACCOUNT_EMAIL" \
        --role "roles/monitoring.metricWriter"
    
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member "serviceAccount:SERVICE_ACCOUNT_EMAIL" \
        --role "roles/monitoring.dashboardEditor"
    

Replace PROJECT_ID with the ID of your [logging-monitoring project](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/multiple-gcp-projects#logging_monitoring_project).

## Optional service accounts

### Usage metering service account

Google Distributed Cloud uses this service account to store usage data in a BigQuery dataset.

To create a usage metering service account:
    
    
    gcloud iam service-accounts create usage-metering-sa \
        --project PROJECT_ID
    

Replace PROJECT_ID with the ID of the Google Cloud project that you want to be the parent of your usage metering service account.

To create a JSON key for your usage metering service account:
    
    
    gcloud iam service-accounts keys create usage-metering-key.json \
       --iam-account SERVICE_ACCOUNT_EMAIL
    

Replace SERVICE_ACCOUNT_EMAIL with the email address of your usage metering service account.

Your usage metering service account must be grantesd the `bigquery.dataEditor` role on your [usage metering project](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/multiple-gcp-projects#usage_metering_project). This is the Google Cloud project where you want to view usage data for your user cluster.

To grant the `bigquery.dataEditor` role to your usage metering service account:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member "serviceAccount:SERVICE_ACCOUNT_EMAIL" \
        --role "roles/bigquery.dataEditor"
    

Replace PROJECT_ID with the ID of your usage metering project.

### Audit logging service account

Google Distributed Cloud uses this service account to send Kubernetes audit logs from your cluster to [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit).

To create an audit logging service account:
    
    
    gcloud iam service-accounts create audit-logging-sa \
        --project PROJECT_ID
    

Replace PROJECT_ID with the ID of the Google Cloud project that you want to be the parent of your audit logging service account.

To create a JSON key for your audit logging service account:
    
    
    gcloud iam service-accounts keys create audit-logging-key.json \
       --iam-account SERVICE_ACCOUNT_EMAIL
    

Replace SERVICE_ACCOUNT_EMAIL with the email address of your audit logging service account.

You do not need to grant any roles to your audit logging service account. The permission for Cloud Audit Logging is automatically granted at user cluster creation time. If the admin cluster uses a different project ID or service account for audit logging with all its user clusters, follow the steps in [known issues](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/known-issues#audit-logging-permission) to grant permission.

### Binary authorization service account

Google Distributed Cloud uses this service account to call the [Binary Authorization API](https://docs.cloud.google.com/binary-authorization/docs/reference/rest).

For information on creating a binary authorization service account, see [Binary Authorization in GKE on-prem](https://docs.cloud.google.com/binary-authorization/docs/setting-up-on-prem).

## What's next

[Create an admin workstation](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/create-admin-workstation).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
