---
url: https://docs.cloud.google.com/apigee/docs/apihub/provision/
title: Provision API hub in the Cloud console \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:03:14.596031+00:00
---

# Provision API hub in the Cloud console  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/provision/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Provision API hub in the Cloud console Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

This page explains how to provision API hub using the Apigee UI in Google Cloud console. This is the recommended method for provisioning API hub.

To provision API hub using the command line, see [Provision API hub from the command line](https://docs.cloud.google.com/apigee/docs/apihub/provision-cli). To provision API hub using a Terraform configuration, see [Provision API hub using Terraform](https://docs.cloud.google.com/apigee/docs/apihub/provision-terraform).

## Before you begin

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

  6. Make sure that you have the following role or roles on the project: 

     * `roles/serviceusage.serviceUsageAdmin`
     * `roles/serviceusage.serviceUsageViewer`
     * `roles/cloudkms.admin`
     * `roles/apihub.provisioningAdmin`
     * `roles/resourcemanager.projectIamAdmin`

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
  7. Ensure that your Google Cloud project doesn't have the `Google Cloud Platform - Resource Location Restriction` [organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints) added. **Important:** API hub uses Cloud Scheduler for some of its features. Cloud Scheduler is not available in all Google Cloud locations. If you are provisioning API hub in a location where Cloud Scheduler is not available, it will be provisioned in a fallback location. For a list of these locations and their fallbacks, see [API hub locations](https://docs.cloud.google.com/apigee/docs/apihub/locations). If your organization has a `Resource Location Restriction` policy that prevents resources from being created in the fallback location, provisioning will fail. 
  8. Optional: [Configure VPC Service Controls](https://docs.cloud.google.com/apigee/docs/apihub/vpc-service-control).



## Summary of steps

The provisioning steps are as follows:

  1. Step 1: Enable APIs. API hub requires you to enable a few Google Cloud APIs.
  2. Step 2: Choose a hosting location. Specify the physical location of your API hub.
  3. Step 3: Register a host project. The current Google Cloud project is selected by default.
  4. Step 4. Configure encryption. Select or create a customer-managed encryption key (CMEK) or use a Google-owned and Google-managed encryption key to encrypt and decrypt your API data at rest.
  5. Step 5: Create a service identity. Assign access permissions to a service identity.
  6. Step 6: Submit the provisioning request. Submit the provisioning request to create your API hub instance.
  7. Step 7:(Optional) Attach runtime projects. Attach Apigee runtime projects to your API hub instance.



## Provisioning steps

To launch provisioning for API hub:

  1. Ensure that you have met the prerequisites described in Before you begin. **Caution:** If you have recently deprovisioned API hub, you must wait **7 days** before provisioning a new instance in the same Google Cloud project. This is because deprovisioning moves the associated Apigee organization (if any) to a soft-delete state for **7 days** , API hub can only be reprovisioned after the Apigee org is permanently deleted. 
  2. In the Google Cloud console, go to the Apigee API hub welcome page.

[ Go to Apigee API hub](https://console.cloud.google.com/apigee/api-hub/)

  3. Click **Create instance**. 
     * If API hub is not provisioned in your organization, the UI displays **Step 1** of the provisioning workflow.
     * If API hub has already been provisioned, you are taken to the API resources page.



### Step 1: APIs

To provision API hub, you must enable the following APIs for your Google Cloud project:

API Name | Location | Description  
---|---|---  
[API hub API](https://console.cloud.google.com/apis/library/apihub.googleapis.com) | `apihub.googleapis.com` | This is required to provision API hub.  
[Cloud Key Management Service (KMS)](https://console.cloud.google.com/apis/library/cloudkms.googleapis.com) | `cloudkms.googleapis.com` | This is required if you choose to use a customer-managed encryption key (CMEK) to encrypt your API hub data.  
[Apigee API](https://console.cloud.google.com/apis/library/apigee.googleapis.com) | `apigee.googleapis.com` | This is required to create an Apigee organization in your project. **Important:** Enabling the API hub API also automatically enables the Apigee API (`apigee.googleapis.com`) for your Google Cloud project. This applies to all projects, regardless of whether Apigee has been provisioned or if the Apigee API was previously disabled.  Note that API hub remains a free service. Auto-enablement of the Apigee API during the API hub provisioning process has no pricing or billing implications for your project.   
  
To enable the required APIs, click **Enable APIs**. This step takes seconds to complete.

### Step 2: Location

You need to select two locations: First, the physical location (region) where you'd like to host your Apigee API hub instance, and second, the multi-region in which your Vertex AI search data will be stored: 

  1. From the drop-down list, select the region in which you want your API hub instance to be hosted. For the list of available regions, see [API hub locations](https://docs.cloud.google.com/apigee/docs/apihub/locations). 
  2. If the **Enable Vertex search capability** option is enabled (the default), you must select the [multi-region location](https://docs.cloud.google.com/generative-ai-app-builder/docs/locations) in which to store your Vertex AI-based search data, the data associated with the [Semantic Search](https://docs.cloud.google.com/apigee/docs/apihub/search-apis#semantic-search) feature of API hub. By default, the multi-region that includes the API hub region you set in Step 1 is selected. For example, if you select `us-central1` as the API hub region, the multi-region `us` will be selected by default. However, you are free to change to another multi-region if you wish.

The Vertex search option enables the Vertex AI-powered Semantic Search feature of API hub. If you deselect the **Enable Vertex search capability** option, Semantic Search is disabled, and the multi-region selector is hidden.

**Note:** When selected, the Vertex search option automatically provisions Vertex AI in a Google Cloud region that exists within the same [multi-region](https://docs.cloud.google.com/docs/geography-and-regions) as the region in which API hub is hosted. For example, if you select `us-central1` as your hosting region for API hub, Vertex may be provisioned in any region within the `us` multi-region. For example, Vertex could be provisioned in `us-west1`, `us-west2`, `us-central2`, or another region inside the `US` multi-region.
  3. Click **Set location**.



### Step 3: Register host project

A _host project_ is a Google Cloud project in your Apigee organization that you designate as the consumer project for all API hub resources. A single API hub instance can be provisioned per host project.

To use the Google Cloud project of your Apigee organization as the **host project** for API hub, click **Register**.

### Step 4: Encryption

In this step, you can choose to use a Google-owned and Google-managed encryption key or a Customer Managed Encryption Key (CMEK) defined in the Cloud Key Management Service to encrypt the data stored in your API hub instance. 

To use a Google-owned and Google-managed encryption key, just select the **Google-managed encryption key** option. If you select this option, no further key configuration is required.

**Caution:** If you use CMEK to encrypt your API hub data, ensure the key remains enabled and available. If the key is disabled or becomes unavailable for more than **7 days** , all data in your API hub instance will be permanently deleted and the instance will enter an unrecoverable state. 

To use an existing CMEK: 

  1. In the **Choose a customer-managed encryption key (CMEK)** box, type to filter or scroll to search for your existing key. Alternatively, you can enter the [key's resource id](https://docs.cloud.google.com/kms/docs/resource-hierarchy#retrieve_resource_id) to locate an existing key.
  2. Select your key and click **OK**.
  3. Click **Confirm**.



To create a new CMEK: 

  1. Click **Create key**. The **Create a new key** dialog displays.
  2. In the **Key ring** section you can specify an existing key ring or create a new one. 
     * To use an existing key ring: 
       1. Select an existing key ring from the **Key ring** list.
       2. Click **Continue**.
     * To create a new key ring: 
       1. Click the **Create key ring** toggle or click **Create key ring** in the select box.
       2. In the **Key ring name** field, enter a name for your key ring. 

Key ring names can contain letters, numbers, underscores (_), and hyphens (-). Key rings can't be renamed or deleted.

       3. Select a location from the **Key ring location** list. 

This location is restricted to the hosting location you chose in the previous step to ensure that the key and data remain in the same region.

       4. Click **Continue**.
  3. In the **Key section** : 
     1. Enter a name for your key in the **Key name** field. 

Key names can contain letters, numbers, underscores (_), and hyphens (-). Keys can't be renamed, and you can't reuse the name of a deleted key.

     2. Select a **Protection level** , for example, **Software**.
     3. Click **Continue**.
  4. In the **Review** section, confirm the details you specified for key creation. 

If the information is correct, click **Create**.

  5. Select your newly created key in the **Choose a customer-managed encryption key** box.
  6. Click **Confirm encryption key**.



### Step 5: Service identity

In this step, you create a new service identity and grant it access to your selected customer-managed encryption key. This key is used to encrypt and decrypt your API hub data.

To create the new service identity, click **Create service identity & grant permissions**.

Apigee creates a service account and assigns the `cloudkms.cryptoKeyEncrypterDecrypter`, `apihub.admin`, and `apihub.runtimeProjectServiceAgent` roles to the service account.

### Step 6: Submit the provisioning request

Once you have provided all the required details to provision an API hub instance, click **Submit**.

When you click **Submit** , API hub also checks for an existing Apigee organization in your Google Cloud project. If it doesn't find one, API hub creates a new Apigee organization with a default Cloud runtime type entitlement. However, if a Hybrid runtime type entitlement already exists, that entitlement is used instead. 

The **Finalizing API hub instance** page appears, indicating that the provisioning request is being processed. Finalizing the API hub instance can take a few minutes.

After provisioning and finalization are complete, you'll be taken to the [Get started with API hub](https://docs.cloud.google.com/apigee/docs/apihub/getting-started-apihub) page.

### Step 7: (Optional) Attach runtime projects

See [Auto-register Apigee proxies](https://docs.cloud.google.com/apigee/docs/apihub/auto-register-apigee-proxies).

## Considerations

  * If you have recently deprovisioned API hub, you must wait **7 days** before provisioning a new instance in the same Google Cloud project. This is because deprovisioning moves the associated Apigee organization (if any) to a soft-delete state for **7 days** , and API hub can only be reprovisioned after the Apigee org is permanently deleted. 
  * If a customer-managed encryption key (CMEK) used for an API hub instance is disabled or becomes unavailable for more than **7 days** , all data in the instance is permanently deleted and the instance becomes unusable. 



## What's next

Now, you are ready to begin using API hub:

  * Learn about the [Get started with API hub](https://docs.cloud.google.com/apigee/docs/apihub/getting-started-apihub) page.
  * Review the [roles and permissions](https://docs.cloud.google.com/apigee/docs/apihub/iam-roles) required to use API hub
  * Configure API hub attributes: 
    * [Manage attributes](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes)
    * [Quickstart: Create and edit attributes](https://docs.cloud.google.com/apigee/docs/apihub/quickstart-settings)
  * Register an API resource: 
    * [Manage API resources](https://docs.cloud.google.com/apigee/docs/apihub/manage-apis)
    * [Quickstart: Register an API](https://docs.cloud.google.com/apigee/docs/apihub/quickstart-api)
  * Add an API version: 
    * [Versions overview](https://docs.cloud.google.com/apigee/docs/apihub/versions-intro)
    * [Quickstart: Create an API version](https://docs.cloud.google.com/apigee/docs/apihub/quickstart-version)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
