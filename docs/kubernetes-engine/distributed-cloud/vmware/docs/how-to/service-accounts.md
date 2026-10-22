---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts/
title: Service accounts and keys \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:08.466409+00:00
---

# Service accounts and keys  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Service accounts and keys Stay organized with collections  Save and categorize content based on your preferences. 

This document explains the Google Cloud service accounts and keys that you need to create clusters in your Google Distributed Cloud implementation.

The instructions here are complete. For a shorter introduction to using a service account, see [Set up minimal infrastructure](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/minimal-infrastructure).

## Before you begin

[Create Google Cloud projects](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/multiple-gcp-projects).

## Overview of service accounts

Before you create your admin and user clusters, you need to have these service accounts:

  * Component access service account
  * Connect-register service account
  * Logging-monitoring service account



Depending on the features you want to enable, you might also need to have some optional service accounts.

## Understanding service accounts and Google Cloud projects

When you create a service account, you associate it with a Google Cloud project. This Google Cloud project is called the _parent project_ of the service account. In this document, all `gcloud iam service-accounts create` commands use the placeholder variable `PROJECT_ID`, which is the project ID of the parent project of the service account.

You can determine the parent project of a service account by looking at the email address of the service account. For example, here is the email address of a service account named `logger`. The parent project is `alice-123`.
    
    
    logger@alice-123.iam.gserviceaccount.com
    

When you grant an [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) role to a service account, you grant the role _to_ the service account _on_ a particular Google Cloud project. This follows the general pattern of [granting a role to a principle on a resource](https://docs.cloud.google.com/iam/docs/overview#how_cloud_iam_works).

For example, you could grant the `bigquery.dataEditor` role to the `logger@alice-123.iam.gserviceaccount.com` service account on the `bob-456` project. In this case, the service account is the principle, and the Google Cloud project is the resource.

You can grant a role to a service account on a Google Cloud project that isn't the parent project of the service account, or the projects can be the same. To allow for this flexibility, in this document the `gcloud projects add-iam-policy-binding` commands for the component access service account, the connect-register service account, and the logging-monitoring service account use the placeholder variable `FLEET_HOST_PROJECT_ID`. This is the ID of the [fleet host project](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/multiple-gcp-projects#fleet_host_project). The ID that you specify as the `FLEET_HOST_PROJECT_ID` in the `gcloud projects add-iam-policy-binding` commands must be the same.

## Permissions for granting roles to service accounts

Each of your service accounts must be granted certain roles on the relevant Google Cloud project. For example, your connect-register service account must be granted the `gkehub.editor` role on your fleet host project.

To grant roles on a Google Cloud project, you must have certain permissions on the project. For details, see `roles/resourcemanager.projectIamAdmin` in [Understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

If you have the required permissions, you can grant the roles yourself. Otherwise, someone else in your organization must grant the roles for you.

## Using `gkeadm` to automatically create service accounts

This page shows how to manually create service accounts and grant roles to service accounts. As an alternative to doing these steps manually, you can have the `gkeadm` command-line tool create some of the service accounts and grant roles when you create an admin workstation. Even if you let `gkeadm` create service accounts, you must manually create the component access service account and grant the required IAM roles, as described in the next section. For more information about the service accounts that `gkeadm` can create, see [Creating your admin workstation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-workstation).

## Component access service account

Google Distributed Cloud uses this service account to download cluster components, on your behalf, from Artifact Registry.

  1. Create a component access service account:
         
         gcloud iam service-accounts create component-access-sa \
             --display-name "Component Access Service Account" \
             --project PROJECT_ID
         

Replace `PROJECT_ID` with the ID of the Google Cloud project that you want to be the parent project of your service account.

  2. Get the email address of the newly-created component access service account:
         
         gcloud iam service-accounts list \
             --project PROJECT_ID
         

  3. Create a JSON key for your component access service account:
         
         gcloud iam service-accounts keys create component-access-key.json \
         --iam-account COMPONENT_ACCESS_SERVICE_ACCOUNT_EMAIL
         

Replace `COMPONENT_ACCESS_SERVICE_ACCOUNT_EMAIL` with the email address of your component access service account.




### Grant roles to your component access service account

Your component access service account must be granted the following [IAM roles](https://docs.cloud.google.com/iam/docs/understanding-roles) on your project. These roles are required so that Google Distributed Cloud can do preflight checks:

  * `serviceusage.serviceUsageViewer`
  * `iam.roleViewer`
  * `iam.serviceAccountViewer`
  * `compute.viewer`



To grant the roles:
    
    
    gcloud projects add-iam-policy-binding FLEET_HOST_PROJECT_ID \
        --member "serviceAccount:COMPONENT_ACCESS_SERVICE_ACCOUNT_EMAIL" \
        --role "roles/serviceusage.serviceUsageViewer"
    gcloud projects add-iam-policy-binding FLEET_HOST_PROJECT_ID \
        --member "serviceAccount:COMPONENT_ACCESS_SERVICE_ACCOUNT_EMAIL" \
        --role "roles/iam.roleViewer"
    gcloud projects add-iam-policy-binding FLEET_HOST_PROJECT_ID \
        --member "serviceAccount:COMPONENT_ACCESS_SERVICE_ACCOUNT_EMAIL" \
        --role "roles/iam.serviceAccountViewer"
    gcloud projects add-iam-policy-binding FLEET_HOST_PROJECT_ID \
        --member "serviceAccount:COMPONENT_ACCESS_SERVICE_ACCOUNT_EMAIL" \
        --role "roles/compute.viewer"
    

Replace `FLEET_HOST_PROJECT_ID` with the ID of your fleet host project. This can be the same project in which the service account was created, or it can be a different project. The project ID that you specify here must be the same ID that you specify when you grant IAM roles to the connect-register service account and the logging-monitoring service account.

## Connect-register service account

Google Distributed Cloud uses this service account to register your clusters to a [fleet](https://docs.cloud.google.com/anthos/fleet-management/docs).

  1. Create a connect-register service account:
         
         gcloud iam service-accounts create connect-register-sa \
             --display-name "Connect-register Service Account" \
             --project PROJECT_ID
         

Replace `PROJECT_ID` with the ID of the Google Cloud project that you want to be the parent of your connect-register service account.

  2. Get the email address of the newly-created connect-register service account:
         
         gcloud iam service-accounts list \
             --project PROJECT_ID
         

  3. Create a JSON key for your connect-register service account:
         
         gcloud iam service-accounts keys create connect-register-key.json \
         --iam-account CONNECT_REGISTER_SERVICE_ACCOUNT_EMAIL
         

Replace `CONNECT_REGISTER_SERVICE_ACCOUNT_EMAIL` with the email address of your connect-register service account.

  4. Grant the `gkehub.editor` role to your connect-register service account:
         
         gcloud projects add-iam-policy-binding FLEET_HOST_PROJECT_ID \
             --member "serviceAccount:CONNECT_REGISTER_SERVICE_ACCOUNT_EMAIL" \
             --role "roles/gkehub.editor"
         

The project ID that you specify here must be the same ID that you specify when you grant IAM roles to the component access service account and the logging-monitoring service account.




### Logging-monitoring service account

Google Distributed Cloud uses this service account to export logs and metrics from clusters to [Cloud Logging](https://docs.cloud.google.com/logging/docs) and [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs).

  1. Create a logging-monitoring service account:
         
         gcloud iam service-accounts create logging-monitoring-sa \
             --display-name "Logging-monitoring Service Account" \
             --project=PROJECT_ID
         

Replace `PROJECT_ID` with the ID of the Google Cloud project that you want to be the parent of your logging-monitoring service account.

  2. Get the email address of the newly-created logging-monitoring service account:
         
         gcloud iam service-accounts list \
             --project PROJECT_ID
         

  3. Create a JSON key for your logging-monitoring service account:
         
         gcloud iam service-accounts keys create logging-monitoring-key.json \
             --iam-account LOGGING_MONITORING_SERVICE_ACCOUNT_EMAIL
         

Replace `LOGGING_MONITORING_SERVICE_ACCOUNT_EMAIL` with the email address of your logging-monitoring service account.




### Grant roles to your logging-monitoring service account

Your logging-monitoring service account must be granted the following roles on your project:

  * `opsconfigmonitoring.resourceMetadata.writer`
  * `logging.logWriter`
  * `monitoring.metricWriter`
  * `monitoring.dashboardEditor`
  * `kubernetesmetadata.publisher`



To grant the required roles to your logging-monitoring service account:
    
    
    gcloud projects add-iam-policy-binding FLEET_HOST_PROJECT_ID \
        --member "serviceAccount:LOGGING_MONITORING_SERVICE_ACCOUNT_EMAIL" \
        --role "roles/opsconfigmonitoring.resourceMetadata.writer"
    gcloud projects add-iam-policy-binding FLEET_HOST_PROJECT_ID \
        --member "serviceAccount:LOGGING_MONITORING_SERVICE_ACCOUNT_EMAIL" \
        --role "roles/logging.logWriter"
    gcloud projects add-iam-policy-binding FLEET_HOST_PROJECT_ID \
        --member "serviceAccount:LOGGING_MONITORING_SERVICE_ACCOUNT_EMAIL" \
        --role "roles/monitoring.metricWriter"
    gcloud projects add-iam-policy-binding FLEET_HOST_PROJECT_ID \
        --member "serviceAccount:LOGGING_MONITORING_SERVICE_ACCOUNT_EMAIL" \
        --role "roles/monitoring.dashboardEditor"
    gcloud projects add-iam-policy-binding FLEET_HOST_PROJECT_ID \
        --member "serviceAccount:LOGGING_MONITORING_SERVICE_ACCOUNT_EMAIL" \
        --role "roles/kubernetesmetadata.publisher"
    

The project ID that you specify here must be the same ID that you specify when you grant IAM roles to the component access service account and connect-register service account.

## Optional service accounts

The service accounts described in this section are optional.

### Audit logging service account

Google Distributed Cloud uses this service account to send Kubernetes audit logs from your cluster to [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit).

If you plan to create clusters with [advanced cluster enabled](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#enable-advanced-cluster-field), (which is required for [setting up topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up)), then use the logging-monitoring service account and key for audit logging instead of creating another service account.

  1. Create an audit logging service account:
         
         gcloud iam service-accounts create audit-logging-sa \
             --project PROJECT_ID
         

Replace `PROJECT_ID` with the ID of the Google Cloud project that you want to be the parent of your audit logging service account.

  2. Get the email address of the newly-created audit logging service account:
         
         gcloud iam service-accounts list \
             --project PROJECT_ID
         

  3. Create a JSON key for your audit logging service account:
         
         gcloud iam service-accounts keys create audit-logging-key.json \
         --iam-account AUDIT_LOGGING_SERVICE_ACCOUNT_EMAIL
         

Replace `AUDIT_LOGGING_SERVICE_ACCOUNT_EMAIL` with the email address of your audit logging service account.




You don't need to grant any roles to your audit logging service account.

### Binary Authorization service account

Google Distributed Cloud uses this service account to call the [Binary Authorization API](https://docs.cloud.google.com/binary-authorization/docs/reference/rest).

For information on creating a Binary Authorization service account, see [Binary Authorization in GKE on-prem](https://docs.cloud.google.com/binary-authorization/docs/setting-up-on-prem).

## What's next

[Create an admin workstation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-workstation)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
