---
url: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/prepare-environment/
title: Prepare environment for Parameter Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:52:52.033549+00:00
---

# Prepare environment for Parameter Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/prepare-environment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Parameter Manager ](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview)



Send feedback 

#  Prepare environment for Parameter Manager Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to prepare your environment to get started with Parameter Manager.

## Enable the Parameter Manager API

To enable the Parameter Manager API, follow these steps:

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Parameter Manager API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable parametermanager.googleapis.com 

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the Parameter Manager API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable parametermanager.googleapis.com 




## Configure Parameter Manager to use a regional endpoint

To create regional parameters, you must configure Parameter Manager to use regional endpoints. Regional endpoints are request endpoints that only allow requests to proceed if the affected resource exists in the location specified by the endpoint. Using regional endpoints lets you run your workloads in a manner that complies with [data residency](https://docs.cloud.google.com/assured-workloads/docs/data-residency) and data sovereignty requirements.

Regional endpoints use the following format:
    
    
    SERVICE_NAME.LOCATION.rep.googleapis.com

To use regional endpoints, you must update your configuration with the regional endpoint address depending on how you access the Parameter Manager service.

### gcloud

To configure the Google Cloud CLI to use regional endpoints, complete the following steps:

  1. Make sure you're using the Google Cloud CLI 402.0.0 or newer.

  2. Set the `api_endpoint_overrides/parametermanager` property to the regional endpoint you want to use:
         
         gcloud config set api_endpoint_overrides/parametermanager https://parametermanager.LOCATION.rep.googleapis.com/

Replace LOCATION with the name of the supported Google Cloud location, such as `us-central1`.




### REST

To connect to the Parameter Manager service using the API, replace the generic API endpoint URL (`https://secretmanager.googleapis.com/v1/`) with the specific regional endpoint that you want to use. Regional endpoints use the following format:
    
    
    https://parametermanager.LOCATION.rep.googleapis.com/

Replace LOCATION with the name of the supported Google Cloud location, such as `me-central2`.

To see which locations support regional endpoints, see [Parameter Manager regional endpoint locations](https://docs.cloud.google.com/secret-manager/docs/locations#parameter_manager_locations).

## Configure roles and permissions

Grant the Parameter Manager Admin role to the administrator to provide them with the necessary permissions to work with Parameter Manager.

  * To grant the required role, use the following command:
        
        gcloud projects add-iam-policy-binding PROJECT_ID \
            --member user:USER_IDENTIFIER \
            --role=roles/parametermanager.admin
        

Replace the following:

    * PROJECT_ID: your project ID
    * USER_IDENTIFIER: the identifier you use to access Google Cloud and assign IAM roles. For example, `dana@example.com`. For more information, see [Identities for users](https://docs.cloud.google.com/iam/docs/user-identities).



## What's next

  * Learn about [access control using Identity and Access Management (IAM) roles](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/access-control)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
