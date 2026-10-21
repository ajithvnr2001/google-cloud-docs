---
url: https://docs.cloud.google.com/service-catalog/docs/manage-solutions/
title: Managing solutions \u00a0|\u00a0 Service Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:40:15.395911+00:00
---

# Managing solutions  |  Service Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-catalog/docs/manage-solutions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Service Catalog ](https://docs.cloud.google.com/service-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/service-catalog/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Managing solutions

In this guide, you learn how to update and delete solutions in Service Catalog.

If you prefer to remove access to a solution, see [Removing a solution from a catalog](https://docs.cloud.google.com/service-catalog/docs/assign-solutions#remove_solution_from_catalog).

## Before you begin

  * You must have the following [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/iam/docs/understanding-roles):

    * [Catalog Admin](https://docs.cloud.google.com/service-catalog/docs/access-control#instance_admin_role) _OR_ [Catalog Manager](https://docs.cloud.google.com/service-catalog/docs/access-control#catalog_manager_role) for the Google Cloud organization associated with the Google Cloud project which has Service Catalog enabled. If you don't have this role, contact your Organization Administrator to request access.
    * [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage) for the Google Cloud project where you want to create your solution. If your Terraform config is in a different project, you must also have the Storage Admin role for the project that contains your Terraform config.
    * [Cloud Build Editor](https://docs.cloud.google.com/build/docs/iam-roles-permissions#predefined_roles) for the Google Cloud project where you want to create the solution.

If you plan to use your own service account, you must also have the [Service Account User](https://docs.cloud.google.com/iam/docs/roles-permissions/iam) role for the Google Cloud project that contains the service account that you plan to use.

If you don't have these roles, contact your Organization Administrator to request access.

  * If you plan to use your own service account, your service account must have the following [IAM roles](https://docs.cloud.google.com/iam/docs/understanding-roles):

    * [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage) for the Google Cloud project where you want to create your solution. If your Terraform config is in a different project, your service account must also have the role [Storage Object Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage) for the project containing the Terraform config.
    * [Logs Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging) for the Google Cloud project where you want to create your solution.

If you don't have these roles, contact your Organization Administrator to request access.




## Update a solution

When you edit a solution in Service Catalog, you immediately update the solution in any catalogs where it's assigned. Updating a solution doesn't affect existing deployments, and users who access the solution after you update it can only deploy the latest version.

For Terraform solutions, if you update the configuration, a new version appears to users on the user's **Deployments** page in the Google Cloud console. Users can choose to update their deployment to the latest version.

## Edit solution details

To edit and update a solution:

  1. Go to the Service Catalog Admin [**Solutions** page](https://console.cloud.google.com/project/_/catalog/admin/solutions) in the Google Cloud console.   
[Go to the Solutions page](https://console.cloud.google.com/project/_/catalog/admin/solutions)
  2. Click **Select** to choose the Google Cloud project.
  3. In the list of solutions, click the solution name to open the **Solutions Details** page.
  4. In the top menu, click **EDIT**.
  5. Make any needed updates to the solution.
  6. Optionally, you can provide your own service account by clicking the checkbox next to **Select or enter your own service account**. If your service account is located in the same Google Cloud project where you're creating your solution, select **Select a service account from the current project** , and select your service account from the drop-down menu. If your service account is located in a different Google Cloud project from your solution, select **Enter a service account email from any project** , and enter the email of your service account.

**Note:** If you don't provide your own service account, Service Catalog uses the default Cloud Build service account settings. For more information, see [Cloud Build Service Account Change](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates).
  7. Click **UPDATE**.




The updated solution details now appear on the **Solutions Details** page.

## Update a Terraform configuration

Terraform solutions use Cloud Storage's [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning) to manage updates to configuration files. To update the configuration file of a Terraform solution, you have the following options:

  * Use a different Cloud Storage object that contains a new configuration file. To change the Cloud Storage object for a solution, edit the solution details and update the **Link to Terraform config** with the URL path to the new object. After you update the solution details, users can immediately deploy the latest version.

  * Update the solution's current Cloud Storage object with a new version of the configuration. For steps to upload a new configuration file, visit [Uploading objects](https://docs.cloud.google.com/storage/docs/uploading-objects). After you update the solution's Cloud Storage object, you must also view and apply the changes to the solution in Service Catalog.




### View and apply a newer version of a configuration

When Service Catalog detects changes to a Terraform configuration file, you must apply the latest version to update the solution for your users.

To view and apply the latest version of a Terraform configuration:

  1. Go to the Service Catalog Admin **Solutions** page in the Google Cloud console.   
[Go to the Solutions page](https://console.cloud.google.com/project/_/catalog/admin/solutions)

  2. In the table of solutions, go to the solution's **Version status** and click **New version available**.

  3. On the **Solutions Details** page, click **Compare versions** to download and compare the current and latest version of the configuration. After you compare versions, click **Close** to return to the **Solution Details** page.

  4. Click **Apply newer version**.

  5. Under **New version highlights** , add a description to tell users about the updates to the configuration.

  6. Optionally, you can provide your own service account by clicking the checkbox next to **Select or enter your own service account**. If your service account is located in the same Google Cloud project where you're creating your solution, select **Select a service account from the current project** , and select your service account from the drop-down menu. If your service account is located in a different Google Cloud project from your solution, select **Enter a service account email from any project** , and enter the email of your service account.

**Note:** If you don't provide your own service account, Service Catalog uses the default Cloud Build service account settings. For more information, see [Cloud Build Service Account Change](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates).
  7. Click **Update**.




## Delete solutions from Service Catalog

When you delete a solution, you remove the solution from any associated catalogs, and your Service Catalog users can no longer view or launch the solution. For Deployment Manager-based solutions, users can continue to access and use their existing deployments.

If you prefer to keep the solution in Service Catalog, you can [remove the solution from a catalog](https://docs.cloud.google.com/service-catalog/docs/assign-solutions#remove_solution_from_catalog).

To delete one or more solutions:

  1. Go to the Service Catalog Admin **Solutions** page in the Google Cloud console.   
[Go to the Solutions page](https://console.cloud.google.com/project/_/catalog/admin/solutions)
  2. Click **Select** to choose the Google Cloud project.
  3. In the list of solutions, check the box next to each solution you want to delete.
  4. With the solution(s) selected, in the top menu, click **DELETE**.
  5. Click **CONFIRM**.



The solution(s) are deleted from Service Catalog.

## Next steps

  * [Assign the solution to a catalog](https://docs.cloud.google.com/service-catalog/docs/assign-solutions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
