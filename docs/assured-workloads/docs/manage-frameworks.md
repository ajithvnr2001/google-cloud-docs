---
url: https://docs.cloud.google.com/assured-workloads/docs/manage-frameworks/
title: Manage frameworks in Assured Workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:42.671735+00:00
---

# Manage frameworks in Assured Workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/manage-frameworks/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage frameworks in Assured Workloads

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

_Applicable only for[Assured Workloads frameworks](https://docs.cloud.google.com/assured-workloads/docs/frameworks-overview)_

Assured Workloads frameworks consist of [cloud controls](https://docs.cloud.google.com/assured-workloads/docs/manage-cloud-controls) that help you meet the security and regulatory requirements for a folder or project in your cloud environments. Assured Workloads provides many built-in frameworks, such as data boundaries, but you can also modify existing frameworks or create your own. To create your own framework, you start by identifying or creating the cloud controls that align with your business' security and compliance obligations. Then, you deploy a framework that includes those cloud controls to the selected folder or project.

This page helps you complete the following steps:

  1. Assess which built-in framework best aligns with your regulatory and security requirements. You can create your own custom framework, but we recommend starting with a built-in framework.

  2. Determine which built-in cloud controls map to your business requirements. You can [create custom cloud controls](https://docs.cloud.google.com/assured-workloads/docs/manage-cloud-controls) if required.

  3. Determine which folder or project to deploy the framework to. You can deploy frameworks in the following ways:

     * A single resource—whether a folder or a project—can only have one built-in preventative framework such as a data boundary deployed to it.
     * A single resource—whether a folder or a project—can have multiple detective frameworks deployed to it.
     * Multiple resources can have the same preventative or detective framework deployed to them. For example, a parent folder can have the same preventative or detective framework deployed to it as its child projects.
  4. Copy an existing framework and modify it to match your requirements. If required, you can create a custom framework.

  5. Deploy the framework on the selected folder or project.




## Before you begin

  * To get the permissions that you need to apply frameworks, ask your administrator to grant you the following IAM roles on your organization or project: 

    * [Compliance Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsecuritycompliance#cloudsecuritycompliance.admin) (`roles/cloudsecuritycompliance.admin`)
    * To deploy frameworks that include cloud controls that are based on organization policies, one of: 
      * [Organization Policy Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`)
      * [Assured Workloads Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.admin) (`roles/assuredworkloads.admin`)
      * [Assured Workloads Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.editor) (`roles/assuredworkloads.editor`)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




## View frameworks

Complete the following steps to view the configuration for built-in frameworks or other frameworks that you've already created.

  1. In the Google Cloud console, go to the **Frameworks** page.

[Go to Frameworks](https://console.cloud.google.com/compliance/configure/frameworks)

  2. If prompted, select your organization.

  3. The dashboard shows the available frameworks, a brief description, supported platforms and tiers, and the resources that the framework has been assigned to.

  4. To view details about a specific framework, click the framework name.




## Create a framework

After you determine which cloud controls apply to resources within your organization or a specific folder or project, you can create a framework. You can create a custom framework or copy an existing framework and modify it. When you copy a framework, it includes the latest releases of any built-in cloud controls.

  1. In the Google Cloud console, go to the **Frameworks** page.

[Go to Frameworks](https://console.cloud.google.com/compliance/configure/frameworks)

  2. If prompted, select your organization.

  3. Click **Create custom framework**.

  4. Complete one of the following:

     * To use an existing framework, complete the following:

       1. Select **Start from an existing framework**.

       2. Select the framework that you want to copy.

     * To create a custom framework, select **Start new**.

  5. Enter a name, unique identifier, and description for your framework. Click **Continue**.

  6. In the step to **Set a location for your framework** , select a specific region or a multi-region. For more information about available regions, see [Assured Workloads locations](https://docs.cloud.google.com/assured-workloads/docs/locations). Click **Continue**.

If you're copying an existing framework, the list of cloud controls that were part of the existing framework displays.

  7. To add the cloud controls that you require, complete the following:

     * To add an existing cloud control, click **Add Cloud Controls**. Select all the cloud controls that you require and then click **Add**.

When you add a control, verify the control type (detective, preventive, or audit) of the control. Don't include audit-only controls in a framework that you want to use to monitor your environment and detect violations. You can't deploy frameworks that include audit-only controls.

     * To create a custom cloud control, click **Create custom cloud control**. For instructions, see [Create a custom cloud control](https://docs.cloud.google.com/assured-workloads/docs/manage-cloud-controls#create-custom-cloud-control).

  8. Click **Continue**.

  9. Add any additional parameters that the cloud controls require.

For example, you can set your locations for Cloud Logging storage locations, resource locations, and modify allowed service endpoints.

  10. Click **Create**.




## Deploy a framework

**Note:** Before deploying Assured Workloads frameworks, you must be added to an allowlist. Request access to the allowlist by filling out [the sign-up form](https://forms.gle/JsX7kziFjEGsDhcQ8).

Deploy a framework to a folder or project so that you can control and monitor those resources using the framework's cloud controls. You can deploy frameworks in the following ways:

  * A single resource—whether a folder or a project—can only have one built-in preventative framework such as a data boundary deployed to it.
  * A single resource—whether a folder or a project—can have multiple detective frameworks deployed to it.
  * Multiple resources can have the same preventative or detective framework deployed to them. For example, a parent folder can have the same preventative or detective framework deployed to it as its child projects.



Folders and projects inherit frameworks through the Google Cloud [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). Therefore, if you deploy frameworks at the folder level and at a project level, all the cloud controls within both frameworks apply to the resources in the project. If there are any differences in cloud control definitions, the lower-level cloud control is used by the resources in the project. For example, if a cloud control rule is set to Allow at the folder level and to Deny at the project level, the project-level setting of Deny is applied to the resources in the project.

As a best practice, we recommend that you deploy a framework at the folder level that includes the cloud controls that can apply to all of its projects. You can then deploy more stringent frameworks to individual projects that require them.

If you choose to nest your framework deployments, such as by deploying one framework to a parent folder and then different frameworks to its child projects, it's your responsibility to resolve any compliance violations that might occur on the parent and child resources.

  1. In the Google Cloud console, go to the **Frameworks** page.

[Go to Frameworks](https://console.cloud.google.com/compliance/configure/frameworks)

  2. If prompted, select your organization.

  3. For the framework that you want to deploy, click more_vert **More Actions > Apply to resources**.

  4. Choose one of the following options:

     * To monitor for drift only, choose **Monitor**.

     * To monitor for drift and actively prevent violations, choose **Monitor and prevent**.

**Note:** If you choose to prevent violations on existing resources—that is, resources that were created prior to deploying a framework to the resource or the resource's parent—you may encounter unintended violations on those resources. We recommend that you either choose **Monitor** for existing resources, or choose to apply frameworks to new folders or projects and their resources.
  5. Select the resource that you want to deploy the framework to. You can choose an existing folder or project. If you chose to actively prevent violations, you can create a new folder or project and deploy the framework to it. If the framework requires additional details, such as a CMEK project or other configuration details, you must provide them.

  6. Complete one of the following:

     * If you selected **Monitor** , complete the following:

       1. Verify the information.
       2. Click **Monitor**.
     * If you selected **Monitor and prevent** , complete the following:

       1. Click **Next**. Review the cloud controls and modes.
       2. Click **Continue**.
       3. If displayed, verify the additional information that's required for some cloud controls.
       4. Click **Next**.
       5. Review your selections and then click **Enforce**.



After you deploy the framework, you can monitor your environment for any drift from your defined cloud controls. Assured Workloads' Monitoring reports instances of drift as _violations_ that you can review, filter, and resolve. It can take approximately six hours after you deploy a framework for any violations to appear.

## Edit a custom framework

After you create a framework, you can change its name and description, add or remove cloud controls, and update any parameters. You can only edit frameworks that you create; you can't edit built-in frameworks.

  1. In the Google Cloud console, go to the **Frameworks** page.

[Go to Frameworks](https://console.cloud.google.com/compliance/configure/frameworks)

  2. If prompted, select your organization.

  3. Click the framework that you want to edit.

  4. On the **Framework details** page, verify that the framework isn't assigned to a resource. If required, remove the assignments.

  5. Click **Actions > Edit**.

  6. In the **Update framework details** page, change the name and description as required. Click **Continue**.

  7. To change the cloud controls that are included in the framework, complete the following:

     * To add an existing cloud control, click **Add Cloud Controls**. Select all the cloud controls that you require and then click **Add**.

     * To create a custom cloud control, click **Create custom cloud control**. For instructions, see [Create a custom cloud control](https://docs.cloud.google.com/assured-workloads/docs/create-cloud-control).

     * To remove a cloud control, select the cloud control and click **Remove**.

  8. Click **Continue**.

  9. Add any additional parameters that the cloud controls require.

  10. Click **Save**.




## Remove resources from a deployed framework

You can remove the folders or projects that you assigned to a deployed framework. Removing resources means that the framework no longer generates violations for that node of your resource hierarchy.

  1. In the Google Cloud console, go to the **Frameworks** page.

[Go to Frameworks](https://console.cloud.google.com/compliance/configure/frameworks)

  2. If prompted, select your organization.

  3. Click the framework that you want to unassign resources from.

  4. On the **Framework details** page, click **Actions > Manage resource assignments**.

  5. In the **Assigned resources** table, find the resource that you want to remove and click delete **Delete**.

  6. Review the confirmation message and click **Unassign**.




## Update a framework to a newer release

Google publishes regular updates to its built-in frameworks as services deploy new features or as new best practices emerge. You can view the releases of built-in frameworks in the frameworks dashboard in the **Configure** tab or in the framework details page.

Google notifies you in the console and release notes when the following updates occur:

  * Built-in cloud controls are added or removed from a framework
  * Built-in cloud controls are updated



To update a framework, complete the following:

  1. In the Google Cloud console, go to the **Frameworks** page.

[Go to Frameworks](https://console.cloud.google.com/compliance/configure/frameworks)

  2. If prompted, select your organization.

  3. Click the framework that you want to update.

  4. On the **Framework details** page, in the **Assigned resources** table, review the **Update status** for any assignments that are identified as **Update available**.

  5. To apply the changes, complete the following:

     1. Remove the resource assignment.

**Note:** When you remove a resource assignment, Assured Workloads frameworks no longer evaluates that resource using that framework. Any existing violations are deactivated, and no new violations are created.
     2. Redeploy the framework to your resource so that Assured Workloads frameworks can resume monitoring the resource and creating violations.




## Delete a custom framework

Delete a framework when it's no longer required. You can only delete frameworks that you create; you can't delete built-in frameworks.

**Note:** You can't recover a framework after you delete it.

  1. In the Google Cloud console, go to the **Frameworks** page.

[Go to Frameworks](https://console.cloud.google.com/compliance/configure/frameworks)

  2. If prompted, select your organization.

  3. Click the framework that you want to unassign resources from.

  4. On the **Framework details** page, verify that the framework isn't assigned to a resource. If required, remove the assignments.

  5. Click **Actions > Delete**.

  6. In the **Delete** window, review the message. Type `Delete` and click **Confirm**.




## What's next

  * Learn more about [Assured Workloads frameworks](https://docs.cloud.google.com/assured-workloads/docs/frameworks-overview).
  * Learn how to [manage cloud controls](https://docs.cloud.google.com/assured-workloads/docs/manage-cloud-controls).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
