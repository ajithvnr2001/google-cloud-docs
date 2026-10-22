---
url: https://docs.cloud.google.com/app-lifecycle-manager/deploy-sql/
title: Quickstart: Deploy a MySQL instance with App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:31.582334+00:00
---

# Quickstart: Deploy a MySQL instance with App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/deploy-sql/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Guides ](https://docs.cloud.google.com/app-lifecycle-manager/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deploy a MySQL instance with App Lifecycle Manager

Learn how to deploy a Cloud SQL instance using App Lifecycle Manager.

## Before you begin

  1. [ Sign in](https://accounts.google.com/Login) to your Google Account.

If you don't already have one, [ sign up for a new account](https://accounts.google.com/SignUp).

  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the App Lifecycle Manager, Artifact Registry, Cloud Build, Cloud Storage, Developer Connect, Infrastructure Manager, Design Center, App Hub, Cloud Resource Manager, Identity and Access Management, Cloud Asset Inventory, Cloud Monitoring, Cloud Logging, and Service Health APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=saasservicemgmt.googleapis.com,artifactregistry.googleapis.com,cloudbuild.googleapis.com,storage.googleapis.com,developerconnect.googleapis.com,config.googleapis.com,designcenter.googleapis.com,apphub.googleapis.com,cloudresourcemanager.googleapis.com,iam.googleapis.com,cloudasset.googleapis.com,monitoring.googleapis.com,logging.googleapis.com,servicehealth.googleapis.com)

  5. Create a service account: 

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
     3. Select your project. 
     4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

     5. Click **Create and continue**. 
     6. Grant the **Project > Owner** role to the service account. 

To grant the role, find the **Select a role** list, then select **Project > Owner**. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. In production environments, do not grant the Owner, Editor, or Viewer roles. Instead, grant a [predefined role](https://docs.cloud.google.com/iam/docs/understanding-roles#predefined_roles) or [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) that meets your needs. 
     7. Click **Continue**. 
     8. Click **Done** to finish creating the service account. 

  6. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  7. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  8. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  9. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  10. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  11. Enable the App Lifecycle Manager, Artifact Registry, Cloud Build, Cloud Storage, Developer Connect, Infrastructure Manager, Design Center, App Hub, Cloud Resource Manager, Identity and Access Management, Cloud Asset Inventory, Cloud Monitoring, Cloud Logging, and Service Health APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=saasservicemgmt.googleapis.com,artifactregistry.googleapis.com,cloudbuild.googleapis.com,storage.googleapis.com,developerconnect.googleapis.com,config.googleapis.com,designcenter.googleapis.com,apphub.googleapis.com,cloudresourcemanager.googleapis.com,iam.googleapis.com,cloudasset.googleapis.com,monitoring.googleapis.com,logging.googleapis.com,servicehealth.googleapis.com)

  12. Create a service account: 

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
     3. Select your project. 
     4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

     5. Click **Create and continue**. 
     6. Grant the **Project > Owner** role to the service account. 

To grant the role, find the **Select a role** list, then select **Project > Owner**. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. In production environments, do not grant the Owner, Editor, or Viewer roles. Instead, grant a [predefined role](https://docs.cloud.google.com/iam/docs/understanding-roles#predefined_roles) or [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) that meets your needs. 
     7. Click **Continue**. 
     8. Click **Done** to finish creating the service account. 

  13. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  14. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  15. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  16. Grant the [App Lifecycle Manager service account](https://docs.cloud.google.com/app-lifecycle-manager/overview#app-lifecycle-manager-sa) the required permissions: 
     1. Navigate to **App Lifecycle Manager** > **Overview** **Get started**.  


[Go to Get started with App Lifecycle Manager](https://console.cloud.google.com/saas/overview/get-started)

     2. In the banner with the message **The required permissions for App Lifecycle Manager account haven't been granted** , click **Grant permissions**.



## Model your Cloud SQL offering using a composite template

In this section, you'll use App Lifecycle Manager to model a composite template (`sql-quickstart-template`) consisting of a Cloud SQL instance using Application Design Center.

  1. In Google Cloud console, go to **App Lifecycle Manager** > **App offering**.

[Go to App offering](https://console.cloud.google.com/saas/saasOfferings)

  2. Click **Create**.

  3. In the **Name of the App offering** field, type: `my-sql-quickstart-saas-offering`.

  4. In the **Region** drop-down, select the regions:

     * `us-central1`
     * `us-east1`
     * `us-east5`

Click **Ok**.

  5. Click **Create**. It may take a few minutes to create `my-sql-quickstart-saas-offering`.

The **App offering details** page opens.

  6. On the **App offering details** page, click **Create new template**.

  7. On the **Create a new composite template** page:

     1. In the **Template ID** box, enter `sql-quickstart-template`.
     2. Click **Create template**. App Lifecycle Manager will take a few minutes to create the composite template.

When App Lifecycle Manager has created the template successfully, you'll see its details in the **Connected application template** section of the **App offering details** page.

  8. In the **Connected application template** section, go to **Manage template** > **Configure in canvas**.

App Design Center opens in the Google Cloud console window.

  9. In the **Components** area, find and click the **Cloud SQL (My SQL)** template.

A **Cloud SQL (My SQL)** component is added to the canvas.

  10. Click **Continue** > **Deploy at scale with App Lifecycle Manager**.

App Lifecycle Manager opens in the Google Cloud console window.

  11. In the **Connected application template** section, click **Update template revision**.

  12. On the **Update template revision** page, select `r-2` in the **Revision** drop-down.

  13. Click **Update**. The **Connected application template** section displays **Importing Application Template**.

It may take a few minutes for App Lifecycle Manager to import the template revision. When the revision has finished importing, you'll see the list of unit kinds populated in the **Unit kinds** tab.




## Provision a Cloud SQL instance using App Lifecycle Manager

In this section, you'll create and provision a unit (`my-sql-quickstart-unit`) with a Cloud SQL instance in the `us-central1` region.

  1. On the **App offering details** page of `my-sql-quickstart-saas-offering`, click **Provision**.

A **Provision** page opens.

  2. On the **Provision** page, select `us-central1` in the **Region** drop-down.

Click **Add** to add a unit to your App offering.

  3. On the **Add unit to provision** panel:

     1. In the **Unit name** box, type `my-sql-quickstart-unit-1`.
     2. In the **Unit kind** drop-down, select the `sql-quickstart-template` unit kind.
     3. In the **Release** drop-down, select (`r-3`).
     4. In the **Service account** drop-down, select the service account you created in the Before you begin section.
  4. Click **Add tenant project variables**.

     1. Select your project to provision your resources.
  5. In the **Other input variables** section of the **Add unit to provision** panel:

     1. Click the `sql-my-sql-1_database_version` drop-down.

        * In the **Variable value** box, type `MYSQL_8_0`.

Click **Done**.

     2. Click the `sql-my-sql-1_name` drop-down.

        * In the **Variable value** box, type `my-sql-db-1`.

Click **Done**.

     3. Click the `sql-my-sql-1_project_id` drop-down.

        * In the **Variable value** box, type your project ID.

Click **Done**.

     4. Click the `sql-my-sql-1_region` drop-down.

        * In the **Variable value** box, type `us-central1`.

Click **Done**.

Click **Add**. You'll see `my-sql-quickstart-unit-1` in the **Units to be provisioned** table.

  6. Click **Provision** to provision the `my-sql-quickstart-unit-1` which will create a live Cloud SQL instance in your App offering.

It may take a few minutes for App Lifecycle Manager to provision `my-sql-quickstart-unit-1`.

**Note:** You can repeat this process for each of the regions you selected when creating the App offering to deploy the Cloud SQL instance in multiple regions.



## View the deployed Cloud SQL instance

You have now used App Lifecycle Manager to deploy a Cloud SQL instance.

To view the Cloud SQL instance that you deployed in this quickstart:

  1. In Google Cloud console, go to the **App Lifecycle Manager** > **Units** > **Unit details** page.

[Go to Units](https://console.cloud.google.com/saas/units)

  2. Click the name of your unit: `my-sql-quickstart-unit-1`.

  3. On the **Unit details** page:

     1. See that the **State** is:

        * **Ready** if the Cloud SQL instance is provisioned.
        * **Provisioning** if the operation is still in progress.



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

### Delete the project

If you deployed the Cloud SQL instance in a new Google Cloud project, and if you no longer need the project, then delete it by completing the following steps:

**Caution:** If you delete a project, all the resources in the project are permanently deleted.

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. At the prompt, type the project ID, and then click **Shut down**. 



## What's next

  * To understand more about App Lifecycle Manager, see [App Lifecycle Manager overview](https://docs.cloud.google.com/app-lifecycle-manager/overview).
  * To get started with App Lifecycle Manager, begin with [Create an App offering](https://docs.cloud.google.com/app-lifecycle-manager/create-saas-offering).
  * To understand how service accounts are used and how to grant the required permissions for these accounts, see [App Lifecycle Manager service accounts](https://docs.cloud.google.com/app-lifecycle-manager/overview#alm-service-accounts).
  * For the steps to update the release, see [Rollout a release](https://docs.cloud.google.com/app-lifecycle-manager/update-saas-offering).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
