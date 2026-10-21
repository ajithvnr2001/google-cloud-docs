---
url: https://docs.cloud.google.com/vpc-service-controls/docs/set-up-service-perimeter/
title: Set up a service perimeter by using VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:29:53.151344+00:00
---

# Set up a service perimeter by using VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/set-up-service-perimeter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up a service perimeter by using VPC Service Controls

Learn how to set up a service perimeter using VPC Service Controls in the Google Cloud console.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Access Context Manager API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=accesscontextmanager.googleapis.com)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Access Context Manager API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=accesscontextmanager.googleapis.com)




### Required roles

To get the permissions that you need to complete this quickstart, ask your administrator to grant you the [Access Context Manager Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`) IAM role on your organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to complete this quickstart. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to complete this quickstart:

  * `accesscontextmanager.accessLevels.list`
  * `accesscontextmanager.policies.create`
  * `accesscontextmanager.servicePerimeters.create`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Set up a VPC Service Controls perimeter

In the following sections, you specify the perimeter details, add projects and services to protect, and create the perimeter.

### Add the VPC Service Controls perimeter details

  1. In the Google Cloud console, go to the **VPC Service Controls** page.

[Go to VPC Service Controls](https://console.cloud.google.com/security/service-perimeter)

  2. To create a new perimeter by using the default access policy, select your organization from the project selector menu.

![](https://docs.cloud.google.com/static/vpc-service-controls/images/project_selector.png)

If your organization doesn't have an access policy, follow these steps:

     1. On the **VPC Service Controls** page, click **Manage policies**.

     2. On the **Manage VPC Service Controls** page, click **Create**.

     3. On the **Create access policy** page, in the **Access policy title** field, enter `access_policy_1`.

     4. Click **Create access policy**.

  3. On the **VPC Service Controls** page, click **New perimeter**.

  4. On the **Create a service perimeter** page, in the **Title** field, enter `perimeter_storage_services`.

  5. For **Perimeter type** and **Enforcement mode** , retain the default selections.

  6. Click **Continue**.




### Add projects to the perimeter

  1. To add projects to the perimeter, click **Add projects**.

  2. In the **Add Projects** pane, select the projects that you want to add to the perimeter and then click **Add selected projects**.

![](https://docs.cloud.google.com/static/vpc-service-controls/images/add_projects_to_perimeter.png)

  3. Click **Continue**.


**Warning:** If you add a project to this perimeter, the Google Cloud resources in the project cannot communicate across the perimeter.

### Secure the BigQuery and Cloud Storage services within the perimeter

  1. In the **Restricted services** pane, click **Add services**.

  2. In the **Add services** pane, select the checkboxes for the BigQuery and Cloud Storage APIs.

To locate the services, you can use the filter query.

![](https://docs.cloud.google.com/static/vpc-service-controls/images/select_services_to_restrict.png)

  3. Click **Add selected services**.

  4. Click **Create**.




You just created a perimeter! You can see your perimeter listed on the **VPC Service Controls** page. The perimeter might take up to 30 minutes to propagate and take effect. When the changes have propagated, access to the BigQuery and Cloud Storage services is limited to the projects you added to the perimeter.

Additionally, the Google Cloud console interface for the BigQuery and Cloud Storage services that you protected with the perimeter might become partially or fully inaccessible.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. In the Google Cloud console, go to the **VPC Service Controls** page.

[Go to VPC Service Controls](https://console.cloud.google.com/security/service-perimeter)

  2. On the **VPC Service Controls** page, in the row corresponding to the perimeter that you created, click delete **Delete**.

  3. In the dialog box, click **Delete** to confirm that you want to delete the perimeter.




## What's next

  * Learn more about [creating service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters).
  * Learn about [managing existing service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters).
  * Learn about the [limitations of using specific services with VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#service-limitations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
  *[VPC]: Virtual Private Cloud
