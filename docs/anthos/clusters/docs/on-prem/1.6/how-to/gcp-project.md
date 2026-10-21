---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/gcp-project/
title: Google Cloud project (quickstart) \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:57:28.425508+00:00
---

# Google Cloud project (quickstart)  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/gcp-project/

**Version 1.6**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.6 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/overview)



Send feedback 

#  Google Cloud project (quickstart) Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to set up a Google Cloud project and grant roles to a Google Account.

The instructions here are part of a quickstart. For full instructions on using Google Cloud projects with Google Distributed Cloud, see [Using multiple Google Cloud projects](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/multiple-gcp-projects).

## Before you begin

Read the [Google Distributed Cloud overview](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/overview).

[Install Google Cloud CLI](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/cloud-sdk).

## Choose or create a Google Cloud project

An GKE cluster on VMware must be associated with one or more Google Cloud projects. This quickstart uses only one Google Cloud project. You can use an existing Google Cloud project or you can [create a new Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). Make a note of your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

## Enable services in your Google Cloud project

Your Google Cloud project must have the following services enabled:
    
    
    anthos.googleapis.com
    anthosgke.googleapis.com
    anthosaudit.googleapis.com
    cloudresourcemanager.googleapis.com
    container.googleapis.com
    gkeconnect.googleapis.com
    gkehub.googleapis.com
    serviceusage.googleapis.com
    stackdriver.googleapis.com
    monitoring.googleapis.com
    logging.googleapis.com
    

To enable services in a project, you must have certain permissions on your Google Cloud project. For details, see the required permissions for `services.enable` in [Access control](https://docs.cloud.google.com/service-usage/docs/access-control).

If you have the required permissions, you can enable the services yourself. Otherwise, someone else in your organization must enable the services for you.

To enable the required services:

### Linux and macOS
    
    
    gcloud services enable --project=PROJECT_ID \
        anthos.googleapis.com \
        anthosgke.googleapis.com \
        anthosaudit.googleapis.com \
        cloudresourcemanager.googleapis.com \
        container.googleapis.com \
        gkeconnect.googleapis.com \
        gkehub.googleapis.com \
        serviceusage.googleapis.com \
        stackdriver.googleapis.com \
        monitoring.googleapis.com \
        logging.googleapis.com
    

### Windows
    
    
    gcloud services enable --project=PROJECT_ID ^
        anthos.googleapis.com ^
        anthosgke.googleapis.com ^
        anthosaudit.googleapis.com ^
        cloudresourcemanager.googleapis.com ^
        container.googleapis.com ^
        gkeconnect.googleapis.com ^
        gkehub.googleapis.com ^
        serviceusage.googleapis.com ^
        stackdriver.googleapis.com ^
        monitoring.googleapis.com ^
        logging.googleapis.com
    

Enabling `anthos.googleapis.com` might incur charges. See the [Pricing](https://cloud.google.com/anthos/pricing) guide for details.

## Log in and set SDK properties

The `gkeadm` command-line tool uses your SDK `account` and SDK `project` [properties](https://docs.cloud.google.com/sdk/docs/properties) to create service accounts and to populate fields in your cluster configuration files. So it is important that you set these properties before you run `gkeadm` to create an admin workstation.

Log in with any Google Account. This sets your SDK `account` property:
    
    
    gcloud auth login
    

Next, set your SDK `project` property:
    
    
    gcloud config set project PROJECT_ID
    

Verify that your SDK `account` and `project` properties are set correctly:
    
    
    gcloud config list
    

The output shows the values of your SDK `account` and SDK `project` properties. For example:
    
    
    [core]
    account = my-name@google.com
    disable_usage_reporting = False
    project = my-project-123
    Your active configuration is: [default]
    

## Grant roles to your SDK account

The Google Account that is set as your SDK `account` property must have these [IAM roles](https://docs.cloud.google.com/iam/docs/overview) so that `gkeadm` can create and manage service accounts for you:

  * `resourcemanager.projectIamAdmin`
  * `serviceusage.serviceUsageAdmin`
  * `iam.serviceAccountCreator`
  * `iam.serviceAccountKeyAdmin`



To grant roles, you must have certain permissions on your Google Cloud project. For details, see [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

If you have the required permissions, you can grant the roles yourself. Otherwise, someone else in your organization must grant the roles for you.

To grant the roles:

### Linux and macOS
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="user:ACCOUNT" \
        --role="roles/resourcemanager.projectIamAdmin"
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="user:ACCOUNT" \
        --role="roles/serviceusage.serviceUsageAdmin"
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="user:ACCOUNT" \
        --role="roles/iam.serviceAccountCreator"
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="user:ACCOUNT" \
        --role="roles/iam.serviceAccountKeyAdmin"
    

### Windows
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID ^
        --member="user:ACCOUNT" ^
        --role="roles/resourcemanager.projectIamAdmin"
    
    gcloud projects add-iam-policy-binding PROJECT_ID ^
        --member="user:ACCOUNT" ^
        --role="roles/serviceusage.serviceUsageAdmin"
    
    gcloud projects add-iam-policy-binding PROJECT_ID ^
        --member="user:ACCOUNT" ^
        --role="roles/iam.serviceAccountCreator"
    
    gcloud projects add-iam-policy-binding PROJECT_ID ^
        --member="user:ACCOUNT" ^
        --role="roles/iam.serviceAccountKeyAdmin"
    

Replace the following:

  * `PROJECT_ID`: the value of your SDK `project` property
  * `ACCOUNT`: the value of your SDK `account` property.



## What's next

[Create a service account (quickstart)](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/service-account-quickstart)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
