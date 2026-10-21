---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/set-up-project-permissions/
title: Set up a project and permissions \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:07.706588+00:00
---

# Set up a project and permissions  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/set-up-project-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Guides ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)



Send feedback 

#  Set up a project and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to create a Google Cloud project, enable AML AI, create [authentication credentials](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/authentication), and grant your account one or more [IAM roles](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/access-control#roles).

**Important:** After you create your project, the API is not automatically visible. You must contact your Google representative before you can enable the API.

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

  7. Enable the required APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable financialservices.googleapis.com bigquery.googleapis.com cloudkms.googleapis.com

  8. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  9. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/financialservices.admin, roles/cloudkms.admin, roles/bigquery.admin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.

  10. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  11. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  12. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  13. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

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

  14. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  15. Enable the required APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable financialservices.googleapis.com bigquery.googleapis.com cloudkms.googleapis.com

  16. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  17. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/financialservices.admin, roles/cloudkms.admin, roles/bigquery.admin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.

These roles fulfill the following required permissions: 

#### Required permissions

The following permissions are required to complete the [quickstart](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/train-models-to-detect-money-laundering) and are needed to perform many vital operations in AML AI. 

Permission | Description  
---|---  
`resourcemanager.projects.get`| Get a Google Cloud project  
`resourcemanager.projects.list`| List Google Cloud projects  
`cloudkms.keyRings.create`| Create a Cloud KMS key ring  
`cloudkms.cryptoKeys.create`| Create a Cloud KMS key  
`financialservices.v1instances.create`| Create an AML AI instance  
`financialservices.operations.get`| Get an AML AI operation  
`cloudkms.cryptoKeys.getIamPolicy`| Get the IAM policy on a Cloud KMS key  
`cloudkms.cryptoKeys.setIamPolicy`| Set the IAM policy on a Cloud KMS key  
`bigquery.datasets.create`| Create a BigQuery dataset  
`bigquery.datasets.get`| Get a BigQuery dataset  
`bigquery.transfers.get`| Get a BigQuery Data Transfer Service transfer  
`bigquery.transfers.update`| Create or delete a BigQuery Data Transfer Service transfer  
`bigquery.datasets.setIamPolicy`| Set the IAM policy on a BigQuery dataset  
`bigquery.datasets.update`| Update a BigQuery dataset  
`financialservices.v1datasets.create`| Create an AML AI dataset  
`financialservices.v1engineconfigs.create`| Create an AML AI engine config  
`financialservices.v1models.copyFrom`| Copy from an AML AI model  
`financialservices.v1models.copyTo`| Copy to an AML AI instance  
`financialservices.v1models.create`| Create an AML AI model  
`financialservices.v1backtests.create`| Create an AML AI backtest result  
`financialservices.v1backtests.exportMetadata`| Export metadata from an AML AI backtest result  
`financialservices.v1instances.importRegisteredParties`| Import registered parties into an AML AI instance  
`financialservices.v1predictions.create`| Create an AML AI prediction result  
`bigquery.jobs.create`| Create a BigQuery job  
`bigquery.tables.getData`| Get data from a BigQuery table  
`financialservices.v1predictions.delete`| Delete an AML AI prediction result  
`financialservices.v1backtests.delete`| Delete an AML AI backtest result  
`financialservices.v1models.delete`| Delete an AML AI model  
`financialservices.v1engineconfigs.delete`| Delete an AML AI engine config  
`financialservices.v1datasets.delete`| Delete an AML AI dataset  
`financialservices.v1instances.delete`| Delete an AML AI instance  
`bigquery.datasets.delete`| Delete a BigQuery dataset  

**Important:** After you enable the Financial Services API, you must contact your Google representative to allowlist all AML AI functionality before proceeding to [Create an AML AI instance](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/set-up-instance). Make sure to inform the representative of the [location](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations) in which you want to create your API resources. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
