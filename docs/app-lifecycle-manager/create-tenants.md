---
url: https://docs.cloud.google.com/app-lifecycle-manager/create-tenants/
title: Set up tenant projects and resources \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:51.572996+00:00
---

# Set up tenant projects and resources  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/create-tenants/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Guides ](https://docs.cloud.google.com/app-lifecycle-manager/overview)



Send feedback 

#  Set up tenant projects and resources Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This guide explains how to use App Lifecycle Manager tenants to organize your deployed units and how to deploy resources into separate _tenant projects_ to isolate and manage your resources.

For an overview of tenants and tenant projects, see [Tenants and tenant projects](https://docs.cloud.google.com/app-lifecycle-manager/tenants).

## Before you begin

Before you create tenant projects or resources:

  1. Create a Terraform configuration, an Artifact Registry repository, and create an artifact containing your SaaS application in your producer project. See [deploy a service instance with App Lifecycle Manager](https://docs.cloud.google.com/app-lifecycle-manager/deploy-sql) to learn how to set up an App offering.
  2. Enable the APIs required by App Lifecycle Manager.

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=saasservicemgmt.googleapis.com,artifactregistry.googleapis.com,config.googleapis.com,developerconnect.googleapis.com,cloudbuild.googleapis.com,storage.googleapis.com)

  3. Verify that you have the necessary service accounts and Identity and Access Management roles granted _within the producer project_. This includes the user-created service account and the permissions granted to the `service-PROJECT-NUMBER@gcp-sa-saasservicemgmt.iam.gserviceaccount.com` account on the producer project.




## Set up a tenant project

When you provision your tenant's resources into separate projects, your resources, IAM policies, quotas, and network configurations are separated for each of your tenants, making it less likely for breaches or misconfigurations with one tenant to affect your others.

You'll need:

  * one producer project, and
  * one tenant project for each of your tenants.




### Console

To set up tenant and producer projects using Google Cloud console:

  1. [Create a producer project, and a tenant project for each of your tenants](https://console.cloud.google.com/home/dashboard).
  2. [Enable billing on your tenant and producer projects](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).
  3. Enable the APIs required by App Lifecycle Manager in your tenant projects. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=saasservicemgmt.googleapis.com,artifactregistry.googleapis.com,config.googleapis.com,developerconnect.googleapis.com,cloudbuild.googleapis.com,storage.googleapis.com)

  4. Verify that your tenant projects have actuation service accounts with the required permissions. 

For details, see [App Lifecycle Manager service accounts](https://docs.cloud.google.com/app-lifecycle-manager/overview#actuation-sa).




You've successfully set up your tenant and producer projects. Once you've created and enabled billing for your producer and tenant projects, you can create tenant resources and associate units with tenants.

### gcloud

To set up a producer and tenant projects using Google Cloud CLI:

  1. Create your producer project, and a tenant project for each of your tenants:
         
         gcloud projects create PRODUCER_PROJECT_ID --name="SaaS producer project" [--folder=folder-id]
         gcloud projects create TENANT_PROJECT_ID --name="SaaS tenant A project" [--folder=folder-id]
         

Replace:

     * `PRODUCER_PROJECT_ID`: A string identifier representing the producer project ID.
     * `TENANT_PROJECT_ID`: A string identifier representing the tenant project ID.
  2. Enable billing for your tenant and producer projects:
         
         gcloud beta billing projects link PRODUCER_PROJECT_ID --billing-account=BILLING_ACCOUNT_ID
          gcloud beta billing projects link TENANT_PROJECT_ID --billing-account=BILLING_ACCOUNT_ID
         

Replace:

     * `PRODUCER_PROJECT_ID`: A string identifier representing the producer project ID.
     * `TENANT_PROJECT_ID`: A string identifier representing the tenant project ID.
     * `BILLING_ACCOUNT_ID`: The ID of the billing account you want to associate with the specified project.
**Note:** You need to link each tenant project with a `gcloud beta billing projects link` command.
  3. Grant the actuation service account the necessary Identity and Access Management roles for each tenant project:
         
         gcloud projects add-iam-policy-binding TENANT_PROJECT_ID \
          --member='serviceAccount:SERVICE_ACCOUNT@PRODUCER_PROJECT_ID.iam.gserviceaccount.com' \
          --role=ROLE
         

Replace:

     * `TENANT_PROJECT_ID`: A string identifier representing the tenant project ID.
     * `PRODUCER_PROJECT_ID`: A string identifier representing the producer project ID.
     * `SERVICE_ACCOUNT`: The service account you want to grant roles to within the specified project.
     * `ROLE`: The Identity and Access Management role to grant. 

You'll need to run `gcloud projects add-iam-policy-binding` for each role you want to grant to the specified service account (`--role='roles/compute.admin'`, for example).




You've successfully set-up your tenant and producer projects. Once you've created and enabled billing for your producer and tenant projects, you can create tenant resources and associate units with tenants.

## Create a tenant resource

Create a _tenant_ resource in your App offering to represent your customer:

  1. In Google Cloud console, go to to **App Lifecycle Manager** > **Tenants**.

[Go to Tenants](https://console.cloud.google.com/saas/tenants)

  2. Click **Create**.

  3. In the **Tenant name** box, enter a name for your tenant resource.

  4. Optional: In the **Customer resource** box, provide a consumer resource with consumer-defined settings for integration. 

  5. In the **App offering** box, select the App offering you want to associate your tenant with.

  6. In the **Region** drop-down, select a region where tenant metadata will be stored.

  7. Optional: Click **Add label** to add a key-value pair label to your tenant.

  8. Click **Create** to create your tenant resource.




You have successfully created a tenant resource.

## Associate a unit with a tenant

After you create a tenant and deploy a unit, you can link them to each other. This association primarily serves as an organizational tag that helps you organize which units belong to which tenant.

For more information about deploying units, see [Deploy a MySQL instance with App Lifecycle Manager](https://docs.cloud.google.com/app-lifecycle-manager/deploy-sql).

To associate a unit with a tenant:

  1. In Google Cloud console, go to **App Lifecycle Manager** > **Tenants**.

[Go to Tenants](https://console.cloud.google.com/saas/tenants)

  2. Click the name of the tenant you want to associate to a unit.

  3. Click **Edit**.

  4. In the **Associated units** section, click **Add Unit**.

  5. Select the units you want to associate with this tenant.

  6. Click **Done**.

  7. Click **Save**.




The selected units are associated with the indicated tenant.

## Provision a new unit with tenant project variables

When you provision a unit associated with a tenant, you must provide the `tenant_project_id` variable.

  1. Navigate to **App Lifecycle Manager** > **Units** in the Google Cloud console.

[Go to Units](https://console.cloud.google.com/saas/units)

  2. Create a new unit associated with your unit kind.

  3. Click **Provision**.

  4. Select the **Release** to provision to your tenant unit.

  5. Select the **Actuation service account** you granted permissions to in your tenant project. You should follow the principle of least privilege and grant only the necessary roles for the resources being managed.

  6. In the **Input Variables** section:

     1. Verify that the `tenant_project_id` variable listed as you defined it in your Terraform configuration `variables.tf` file.
     2. In the **Tenant Project ID** box, provide the name of your tenant project.
     3. Provide input variables defined in your Terraform configuration. If you haven't defined other variables in your Terraform configuration, skip this step.
  7. Click **Provision**.




App Lifecycle Manager triggers Infrastructure Manager using the specified actuation service account. Infrastructure Manager reads the `tenant_project_id` variable and creates the VM _inside that tenant project_.

**Note:** If provisioning fails, verify the required APIs are enabled and your permissions are correctly configured.

## Re-provision a unit with a new release

When you re-provision an existing unit with a new release, you must provide the `tenant_project_id` variable.

  1. Navigate to **App Lifecycle Manager** > **Units** in the Google Cloud console.

[Go to Units](https://console.cloud.google.com/saas/units)

  2. Select the unit associated with your unit kind.

  3. Click **Edit Provisioning**.

  4. Select the **Release** you created with the updated Terraform configuration.

  5. Select the **Actuation service account** you granted permissions to in your tenant project. You should follow the principle of least privilege and grant only the necessary roles for the resources being managed.

  6. In the **Input Variables** section:

     1. Verify that the `tenant_project_id` variable listed as you defined it in your Terraform configuration `variables.tf` file.
     2. In the **Tenant Project ID** box, provide the name of your tenant project.
     3. Provide input variables defined in your Terraform configuration. If you haven't defined other variables in your Terraform configuration, skip this step.
  7. Click **Update**.




App Lifecycle Manager triggers Infrastructure Manager using the specified actuation service account. Infrastructure Manager reads the `tenant_project_id` variable and creates the VM _inside that tenant project_. 

**Note:** If provisioning fails, verify that the required APIs are enabled and your permissions are correctly configured.

## What's next

  * Explore [managing dependencies between units](https://docs.cloud.google.com/app-lifecycle-manager/dependencies).
  * Learn more about [using variables and variable mapping](https://docs.cloud.google.com/app-lifecycle-manager/variables).
  * Review [permissions required for service accounts](https://docs.cloud.google.com/app-lifecycle-manager/overview#actuation-sa).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
