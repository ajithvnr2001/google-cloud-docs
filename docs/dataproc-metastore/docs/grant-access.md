---
url: https://docs.cloud.google.com/dataproc-metastore/docs/grant-access/
title: Grant basic Dataproc Metastore IAM roles to users \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:41.633625+00:00
---

# Grant basic Dataproc Metastore IAM roles to users  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/grant-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Grant basic Dataproc Metastore IAM roles to users Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to grant a Google Cloud user account or service account access to basic Dataproc Metastore resources in a project. These roles described on this page provide access to create a Dataproc Metastore service.

Depending on the scope of control you want the account to have, you grant it one of these predefined IAM roles:

  * `roles/metastore.editor` to grant full control of Dataproc Metastore resources
  * `roles/metastore.admin` to grant full control of Dataproc Metastore resources, including updating IAM permissions.



For detailed information about the specific IAM permissions these roles provide, see [Dataproc Metastore IAM roles](https://docs.cloud.google.com/dataproc-metastore/docs/iam-roles).

**Note:** Completing other actions with your metastore—such as importing MySQL files—requires you to add extra roles that are not detailed on this page. You can find more information about these roles in the respective feature guides.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Dataproc Metastore API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=metastore.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Dataproc Metastore API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=metastore.googleapis.com)




### Required Roles

You must have the `roles/owner` (Owner) basic IAM role in the Google Cloud project you are using, or a role that grants these permissions:

  * `resourcemanager.projects.get`
  * `resourcemanager.projects.getIamPolicy`
  * `resourcemanager.projects.setIamPolicy`



To gain these permissions while following the principle of least privilege, ask your administrator to grant you the `roles/resourcemanager.projectIamAdmin` (Project IAM Admin) role.

## How to grant access roles

### gcloud

To use the gcloud CLI, you can [install and initialize](https://cloud.google.com/sdk/docs/install) the Google Cloud CLI, or you can use [Cloud Shell](https://cloud.google.com/shell/docs/using-cloud-shell).

Run the following `add-iam-policy-binding` command to grant a Dataproc Metastore predefined role to an IAM principal (user account or service account).
    
    
      gcloud projects add-iam-policy-binding PROJECT_ID \
         --member=PRINCIPAL \
         --role=METASTORE_ROLE

Replace the following:

  * `PROJECT_ID`: The ID of the project you want to enable Metastore access to.
  * `PRINCIPAL`: The type and email ID (email address) of the principal. 
    * For user accounts: user:EMAIL_ID
    * For service accounts: serviceAccount:EMAIL_ID
    * For Google Groups: group:EMAIL_ID
  * `METASTORE_ROLE`: One of the following values, depending on the role you want to grant the principal: `roles/metastore.editor`, or `roles/metastore.admin`. For details about the permissions these roles grant, see [Dataproc Metastore IAM roles](https://docs.cloud.google.com/dataproc-metastore/docs/iam-roles). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
