---
url: https://docs.cloud.google.com/service-catalog/docs/view-and-launch/
title: Viewing and launching solutions \u00a0|\u00a0 Service Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:08:17.618919+00:00
---

# Viewing and launching solutions  |  Service Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-catalog/docs/view-and-launch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Service Catalog ](https://docs.cloud.google.com/service-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/service-catalog/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Viewing and launching solutions

In this document, you learn how to view and launch solutions from Service Catalog.

## Before you begin

**Note:** Starting April 29, 2024, Cloud Build uses Compute Engine service accounts by default, instead of Cloud Build service accounts. This doesn't affect any existing Google Cloud projects where Cloud Build is already enabled. If you enable Cloud Build for a project on or after April 29th, 2024, you or your organization administrator must update your organization policies or your Compute Engine service accounts to prevent issues. For more details, see [Cloud Build Service Account Change](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates#what_do_you_need_to_do).

  * To launch a solution using Service Catalog, you must have either the [Identity and Access Management (IAM) role](https://docs.cloud.google.com/iam/docs/understanding-roles) of [Catalog Consumer](https://docs.cloud.google.com/service-catalog/docs/access-control#catalog_consumer_roles) _OR_ [IAM Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) for the Google Cloud project where the solution has been shared with you. If you don't have either role for the Google Cloud project, to request access, contact your Organization Administrator.
  * If you're deploying a Terraform configuration, you need the following roles for the Google Cloud project where you want to deploy the Terraform configuration. If you don't have these roles, to request access, contact the Project Owner, or someone who has the `setIAMpolicy` permission for the project.

    * [Cloud Build Editor](https://docs.cloud.google.com/build/docs/iam-roles-permissions#predefined_roles)
    * [Storage Admin](https://docs.cloud.google.com/service-catalog/docs/access-control#catalog_consumer_roles)
    * [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic)

If you plan to use your own service account, you must also have the [Service Account User](https://docs.cloud.google.com/iam/docs/roles-permissions/iam) role for the Google Cloud project that contains the service account that you plan to use.

  * If you're deploying a Terraform configuration, and you choose to use your own service account, your service account must have the following [IAM roles](https://docs.cloud.google.com/iam/docs/understanding-roles) for the project where you want to create your solution:

    * [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage). If your Terraform config is in a different project, your service account must also have the role [Storage Object Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage) for the project containing the Terraform config.
    * [Logs Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging).
    * Any additional IAM roles required to run your Terraform config.
  * If you're deploying a solution using Cloud Deployment Manager, the [Deployment Manager Editor](https://docs.cloud.google.com/deployment-manager/docs/access-control#roles) role for the project where you're deploying the solution. If you don't have this role, contact the Project Owner _OR_ someone who has the [`setIAMpolicy`](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy) permission for the project to request access.



  * If you're launching a Terraform configuration, you must set up Cloud Build:

    1. Enable the Cloud Build API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild)

    2. In Google Cloud console, go to the [Cloud Build](https://console.cloud.google.com/project/_/cloud-build/builds) page.
    3. Select the **Settings** tab.
    4. Use the service account listed under **Service account email:**.
    5. If you aren't using your own service account, grant the following Identity and Access Management (IAM) roles to the Cloud Build service account. For example, in the sample Terraform configuration file provided in [Creating a Terraform configuration](https://docs.cloud.google.com/service-catalog/docs/terraform-configuration), **Compute Engine** is one of the resources, and the role **Compute Instance Admin (v1)** (`roles/compute.instanceAdmin.v1`) has been enabled for the service account.

**Note:** If you don't provide your own service account, Service Catalog uses the default Cloud Build service account settings. For more information, see [Cloud Build Service Account Change](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates).
    6. Grant the [Project Editor](https://docs.cloud.google.com/resource-manager/docs/access-control-proj#using_basic_roles) role to the service account for the project where you're deploying the Terraform configuration.

    7. To manage all of your Terraform state files in Service Catalog, grant the Storage Admin role to your Cloud Build service account for the project where the configuration is shared and the project where you're deploying it. For steps to grant access, see [Configuring access for Cloud Build Service Account](https://docs.cloud.google.com/build/docs/securing-builds/configure-access-for-cloud-build-service-account).




## View Service Catalog solutions

In Service Catalog, you see a union of solutions from all the catalogs you have access to in your Google Cloud hierarchy.

To view available solutions, go to the Google Cloud console [Service Catalog](https://console.cloud.google.com/project/_/catalog) page. Solutions that have been shared with you appear in the main panel.

## Launch a link-based solution

To launch a reference link-based solution:

  1. Go to the Google Cloud console [Service Catalog](https://console.cloud.google.com/project/_/catalog) page.

[Go to the Service Catalog page](https://console.cloud.google.com/project/_/catalog)

  2. Under **TYPE** , filter by **Link** and click a solution.

  3. Click **Go to link**.

This takes you to a link outside of the Google domain where you can download a solution.




## Launch a Deployment Manager (DM)-based solution

To launch a DM-based solution:

  1. Go to the Google Cloud console [Service Catalog](https://console.cloud.google.com/catalog) page.

[Go to the Service Catalog page](https://console.cloud.google.com/project/_/catalog)

  2. Under **TYPE** , filter by **DM Template** and click a solution.

  3. Click **Launch on Compute Engine**.

  4. If prompted, enable the Deployment Manager API and the Service Catalog API.

Enabling the APIs takes several minutes to complete, but you only need to do it once per Google Cloud project (not per solution).

  5. Complete the deployment form.

You must enter the **zone** parameter manually by specifying the Compute Engine [region and zone](https://docs.cloud.google.com/compute/docs/regions-zones) you prefer. Enter the **region** followed by a dash and then the **zone** (without spaces): `region-zone`. For example, `us-central1-a` where `us-central1` is the **region** and `a` is the **zone**.

**Note:** If you use the **network** parameter in your template and specify `default`, the **subnetwork** must also be set to `default`.
  6. Click **Deploy**.




The solution is deployed.

## Launch a Terraform configuration

To launch a Terraform configuration:

  1. Go to the Google Cloud console [Service Catalog](https://console.cloud.google.com/catalog) page.

[Go to the Service Catalog page](https://console.cloud.google.com/project/_/catalog)

  2. Under **TYPE** , filter by **Terraform** and click a solution.

  3. Click **Deploy**.

  4. If prompted, in the window that appears, click **Start a new deployment**.

  5. If prompted, enable the Cloud Build API.

Enabling the APIs takes several minutes to complete, but you only need to do it once per Google Cloud project (not per solution).

  6. Create a name for your deployment.

  7. Optionally, you can provide your own service account by clicking the checkbox next to **Select or enter your own service account**. If your service account is located in the same Google Cloud project where you're creating your solution, select **Select a service account from the current project** , and select your service account from the drop-down menu. If your service account is located in a different Google Cloud project from your solution, select **Enter a service account email from any project** , and enter the email of your service account.

**Note:** If you don't provide your own service account, Service Catalog uses the default Cloud Build service account settings. For more information, see [Cloud Build Service Account Change](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates).
  8. Fill in the parameters.

**Note:** For some fields, you must use [HashiCorp Configuration Language (HCL)](https://www.terraform.io/docs/configuration/syntax.html) syntax.
  9. Click **Preview and deploy**.

  10. Review the deployment and click **Deploy**.




The solution is deployed.

### Update a Terraform deployment

For an existing deployment of a Terraform solution, you can update deployment details, including parameters. If there is a new version of the Terraform configuration available for the solution, you can update your deployment to the latest version of the configuration.

To update an existing deployment:

  1. Go to the **Deployments** page in Service Catalog.

[Go to the Deployments page](https://console.cloud.google.com/project/_/catalog/deployments)

  2. In the table of deployments, click the name of the deployment that you want to update.

  3. On the **Deployment Details** page, click **Update deployment**.

  4. Update the deployment details.

  5. Optionally, you can provide your own service account by clicking the checkbox next to **Select or enter your own service account**. If your service account is located in the same Google Cloud project where you're creating your solution, select **Select a service account from the current project** , and select your service account from the drop-down menu. If your service account is located in a different Google Cloud project from your solution, select **Enter a service account email from any project** , and enter the email of your service account.

**Note:** If you don't provide your own service account, Service Catalog uses the default Cloud Build service account settings. For more information, see [Cloud Build Service Account Change](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates).
  6. Click **Preview and deploy**.

  7. Review the deployment and click **Deploy**.




#### View and apply the latest version of a configuration

When you manage your Terraform deployments, you can view if the associated solution has released a newer version of the Terraform configuration and update the deployment to the latest configuration.

To view if a deployment has available updates and apply the latest version of the configuration:

  1. Go to the **Deployments** page in Service Catalog.

[Go to the Deployments page](https://console.cloud.google.com/project/_/catalog/deployments)

  2. Click **View deployments with updates** to filter the table of deployments. In the table, find the deployment that you want to update and click **New Version Available**.

  3. On the **Deployment Details** page, click **Update deployment**.

  4. Under **Select version** , select **Update to the latest version**.

  5. Optionally, you can provide your own service account by clicking the checkbox next to **Select or enter your own service account**. If your service account is located in the same Google Cloud project where you're creating your solution, select **Select a service account from the current project** , and select your service account from the drop-down menu. If your service account is located in a different Google Cloud project from your solution, select **Enter a service account email from any project** , and enter the email of your service account.

**Note:** If you don't provide your own service account, Service Catalog uses the default Cloud Build service account settings. For more information, see [Cloud Build Service Account Change](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates).
  6. If prompted, enter values for any additional parameters.

  7. Click **Preview and deploy**.

  8. Review the deployment and click **Deploy**.




### Deprovision a Terraform deployment

You deprovision a Terraform deployment to permanently delete all of its resources.

To deprovision a deployment:

  1. Go to the Google Cloud console [Service Catalog](https://console.cloud.google.com/catalog) page.

[Go to the Service Catalog page](https://console.cloud.google.com/project/_/catalog)

  2. Click **Terraform deployments**.

  3. In the table, find the deployment you want to deprovision.

  4. Click the **more actions** menu (displayed as three dots arranged vertically) more_vert.

  5. Optionally, you can provide your own service account by clicking the checkbox next to **Select or enter your own service account**. If your service account is located in the same Google Cloud project where you're creating your solution, select **Select a service account from the current project** , and select your service account from the drop-down menu. If your service account is located in a different Google Cloud project from your solution, select **Enter a service account email from any project** , and enter the email of your service account.

**Note:** If you don't provide your own service account, Service Catalog uses the default Cloud Build service account settings. For more information, see [Cloud Build Service Account Change](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates).
  6. Click **Deprovision**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
