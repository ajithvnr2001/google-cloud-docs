---
url: https://docs.cloud.google.com/saas-runtime/docs/associate-tenants/
title: Quickstart: Associate units with tenants \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:34:29.337777+00:00
---

# Quickstart: Associate units with tenants  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/saas-runtime/docs/associate-tenants/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Associate units with tenants

In this quickstart, you'll modify your app offering to associate the deployed VM unit with a tenant resource, and provision the VM into a dedicated tenant project owned by your tenant.

This approach enhances resource isolation, which lets you to manage resources for each tenant separately and provide better security and compliance for your app offering.

We'll build upon the scenario from the [Deploy a MySQL instance with App Lifecycle Manager quickstart](https://docs.cloud.google.com/app-lifecycle-manager/deploy-sql), modifying it to associate the deployed VM unit with a tenant resource and provision the VM into a dedicated project owned by the tenant: 

  1. Create a tenant resource in App Lifecycle Manager.
  2. Associate a VM with the tenant resource.
  3. Configure App Lifecycle Manager and your Terraform configuration to deploy resources into a separate tenant project.
  4. Address common permission and API enablement issues when deploying cross-project.



By the end of this quickstart, you will create the foundation for an App offering with multiple tenants that lets you set tenant-level configurations and policies by creating tenants and associating them with units.

## Before you begin

Before you create tenants or associate them with units, you should have some knowledge of the fundamentals of the [App Lifecycle Manager ecosystem](https://docs.cloud.google.com/app-lifecycle-manager/overview), and [create an App offering](https://docs.cloud.google.com/app-lifecycle-manager/create-saas-offering).

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

[Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

[Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  2. [Deploy a MySQL instance with App Lifecycle Manager](https://docs.cloud.google.com/app-lifecycle-manager/deploy-sql), including creating Terraform configuration, an Artifact Registry repository, an App offering, unit kind, a unit, and components (including `terraform-files.zip`).

     * Verify that the APIs listed in the [quickstart's **Before you begin**](https://docs.cloud.google.com/app-lifecycle-manager/deploy-sql#before-you-begin) section are enabled in your producer project.
     * Verify that you have the necessary service accounts and IAM roles granted _within the producer project_. This includes the user-created service account and the permissions granted to the `service-PROJECT-NUMBER@gcp-sa-saasservicemgmt.iam.gserviceaccount.com` account on the producer project.
  3. Your _producer project_ and any _tenant projects_ need to be created before you create and associate your tenant resources. For more information, see [Set up a tenant project](https://docs.cloud.google.com/app-lifecycle-manager/create-tenants#set_up_a_tenant_project).




## Create and associate a tenant resource

You can use tenants to group unit resources. Create a _tenant_ resource in your producer project's App offering to represent your customer:

  1. In Google Cloud console, go to to **App Lifecycle Manager** > **Tenants**.

[Go to Tenants](https://console.cloud.google.com/saas/tenants)

  2. Click **Create**.

  3. On the **Create tenant** page, enter `vm-quickstart-tenant` in the **Tenant name** box.

  4. In the **App offering** box, select `vm-quickstart-saas-offering`.

  5. In the **Region** drop-down, select `us-central1`.

  6. Click **Add unit**. A **New unit** section appears.

  7. In the **Unit** drop-down, select the `projects/YOUR-PROJECT-NAME/locations/us-central1/units/vm-quickstart-unit` unit.

  8. Click **Done** to associate your `vm-quickstart-unit` resource with your `vm-quickstart-tenant` resource.

  9. Click **Create** to create your tenant resource. You have successfully created the `vm-quickstart-tenant` resource and associated it with the `vm-quickstart-unit` resource. This association primarily serves as an organizational tag within the Google Cloud console, helping you identify which units belong to which tenant.




## Create a tenant release

  1. In Google Cloud console, go to to **App Lifecycle Manager** > **Releases**.

[Go to Releases](https://console.cloud.google.com/saas/releases)

  2. On the **Releases** page, click **Create**.

  3. On the **Create Release** page, enter `vm-quickstart-tenant-release` in the **Release name** box.

  4. In the **Unit kind** box, select `vm-quickstart-unit-kind`. Click **Next**.

  5. On the **Select Blueprint** step, click the **Select an existing image from Artifact Registry** toggle.

  6. On the **Store Blueprint** step, click **Browse** and select the artifact associated with `vm-quickstart-tenant-blueprint`. Click **Next**.

  7. Click **Create**. You have successfully created the `vm-quickstart-tenant-release` resource.




## Create a tenant project and deploy a unit

In the [Deploy a MySQL instance with App Lifecycle Manager quickstart](https://docs.cloud.google.com/app-lifecycle-manager/deploy-sql), you provision App Lifecycle Manager resources into the same project that contains your App offering configuration.

In this quickstart, you direct the resource provisioning into the _tenant project_ instead of the _producer project_.

You will need to pass a modified variables `tenant_project_id` and `tenant_project_number` during unit provisioning.

  1. Create a tenant project where you will deploy the `terraform-vm.zip` files:
         
         gcloud projects create quickstart-tenant-project --name="SaaS Tenant A Project"
         

  2. Enable APIs and grant IAM roles on tenant project. To deploy units into your tenant project, you need to enable the Compute Engine API and grant IAM roles on your tenant project. 




### Enable APIs in your tenant project

Enable the Compute Engine API in the tenant project using Google Cloud console:

  1. Go to the project selector.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Click **Select a project**.

  3. Select `quickstart-tenant-project`.

  4. Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com)

  5. Make sure that you have the following role or roles on the project: roles/compute.admin 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 



### Provision a unit with tenant project variables

From your producer project, provision a new unit with your tenant project's input variables:

  1. Go to the project selector.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Click **Select a project**.

  3. Select your producer project.

  4. Navigate to **App Lifecycle Manager** > **Units** in the Google Cloud console.

[Go to Units](https://console.cloud.google.com/saas/units)

  5. Select `vm-quickstart-unit` resource.

  6. Click **Provision**.

  7. Select the `vm-quickstart-tenant-release` resource.

  8. Select the **Actuation service account** you granted permissions to in the tenant project.

  9. In the **Input Variables** section:

     * The `tenant_project_id` variable is listed as you defined it in `variables.tf`.
     * In the **Tenant Project ID** box, enter `quickstart-tenant-project`.
  10. Click **Provision**.




App Lifecycle Manager triggers Infrastructure Manager using the specified actuation service account. Infrastructure Manager reads the `tenant_project_id` variable and creates the VM _inside that tenant project_. 

**Note:** If provisioning fails, verify that the required APIs are enabled and your permissions are correctly configured.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

**Caution:** If you delete a project, all the resources in the project are permanently deleted. Only delete the quickstart projects if you deployed your app offering into a new Google Cloud project and you no longer need the project or any of its resources.

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. At the prompt, type the project ID, and then click **Shut down**. 



## What's next

  * Learn more about how to [set up tenant projects and resources](https://docs.cloud.google.com/app-lifecycle-manager/create-tenants).
  * Use [variables and variable mapping](https://docs.cloud.google.com/app-lifecycle-manager/variables) for sophisticated app offering orchestration (including automated resource provisioning).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
