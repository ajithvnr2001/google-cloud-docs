---
url: https://docs.cloud.google.com/infrastructure-manager/docs/enable-service/
title: Enable and disable the service \u00a0|\u00a0 Infrastructure Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:14.853465+00:00
---

# Enable and disable the service  |  Infrastructure Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/infrastructure-manager/docs/enable-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Infrastructure Manager ](https://docs.cloud.google.com/infrastructure-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/infrastructure-manager/docs/overview)



Send feedback 

#  Enable and disable the service Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the steps to enable and disable Infrastructure Manager.

See [Pricing](https://docs.cloud.google.com/infrastructure-manager/pricing) for information about charges for Infra Manager.

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

**Note:** On Ubuntu, use the [Debian package](https://docs.cloud.google.com/sdk/docs/install#deb) to install gcloud CLI. The gcloud CLI snap package does not include `kubectl` or extensions to authenticate with Infra Manager using the gcloud CLI.
  7. Enable the API from [Google Cloud console](https://console.cloud.google.com/apis/enableflow?apiid=config.googleapis.com) or with the following `gcloud` command: 
         
         gcloud services enable config.googleapis.com

  8. Optional: In order to use [quota validation](https://docs.cloud.google.com/infrastructure-manager/docs/quotas#quota_validation) with Infra Manager, enable the API from [Google Cloud console](https://console.cloud.google.com/apis/enableflow?apiid=cloudquotas.googleapis.com) or with the following `gcloud` command: 
         
         gcloud services enable cloudquotas.googleapis.com




## Disabling service

When you disable the Infra Manager API, any related resources will continue to exist in the project. Once disabled, you cannot use the service to make any changes to deployments and resources in the project.

If you enable the API again, you can continue to use the service in the same way as when you first enabled the API.

To disable the API from the Google Cloud console:

### console

  1. Go to the [API Overview](https://console.cloud.google.com/apis/library/config.googleapis.com) page for Infra Manager.
  2. Select the project where the API is enabled.
  3. Click **Manage**.
  4. Click **Disable API**.



### gcloud

Run the following command to disable the API for your current project:
    
    
    gcloud services disable config.googleapis.com
    

## What's next

  * Learn more about [Terraform with Google Cloud](https://docs.cloud.google.com/docs/terraform).
  * [Deploy infrastructure using Infra Manager](https://docs.cloud.google.com/infrastructure-manager/docs/deploy-resources).
  * [Update a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/update-deployment).
  * [View the state of a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/view-deployments).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
