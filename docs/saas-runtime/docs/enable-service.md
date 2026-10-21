---
url: https://docs.cloud.google.com/saas-runtime/docs/enable-service/
title: Enable the service \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:08:48.598573+00:00
---

# Enable the service  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/saas-runtime/docs/enable-service/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Guides ](https://docs.cloud.google.com/app-lifecycle-manager/overview)



Send feedback 

#  Enable the service Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes the steps to enable and disable App Lifecycle Manager.

## Enabling service

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Install and initialize [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs) if it is not already installed. For an existing installation, update components of the Google Cloud CLI with the command: `gcloud components update`. 

To check your version of the gcloud CLI, run the command:
         
         gcloud version

  7. Enable the API from the Google Cloud console or by using gcloud CLI: 
     1. In the Google Cloud console, to enable the required APIs, on the **Get started** tab of the [**Overview** page](https://console.cloud.google.com/saas/overview/get-started), click **Enable App Lifecycle Manager APIs**.
     2. Using gcloud CLI, to enable the required APIs, run the command:
            
            gcloud services enable saasservicemgmt.googleapis.com
                  gcloud services enable artifactregistry.googleapis.com
                  gcloud services enable cloudbuild.googleapis.com
                  gcloud services enable storage.googleapis.com
                  gcloud services enable developerconnect.googleapis.com
                  gcloud services enable config.googleapis.com
                  gcloud services enable designcenter.googleapis.com
                  gcloud services enable apphub.googleapis.com
                  gcloud services enable cloudresourcemanager.googleapis.com
                  gcloud services enable iam.googleapis.com
                  gcloud services enable cloudasset.googleapis.com
                  gcloud services enable monitoring.googleapis.com
                  gcloud services enable logging.googleapis.com
                  gcloud services enable servicehealth.googleapis.com
                  

You need to enable all of these APIs because the services are used by App Lifecycle Manager.

  8. To use App Lifecycle Manager, you also need the correct permissions. See [Access control with IAM](https://docs.cloud.google.com/app-lifecycle-manager/access-control) for more details. 



## What's next

  * Learn more about [App Lifecycle Manager](https://docs.cloud.google.com/app-lifecycle-manager/overview).
  * To deploy a SaaS application, start with [Create an App offering](https://docs.cloud.google.com/app-lifecycle-manager/create-saas-offering).
  * Try the [quickstart](https://docs.cloud.google.com/app-lifecycle-manager/deploy-sql) to learn how to deploy a VM using App Lifecycle Manager.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
