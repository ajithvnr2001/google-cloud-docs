---
url: https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization/
title: Set up a Google Cloud organization resource \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:06.832696+00:00
---

# Set up a Google Cloud organization resource  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Set up a Google Cloud organization resource Stay organized with collections  Save and categorize content based on your preferences. 

The organization resource is the root node in the [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/overview#cloud_platform_resource_hierarchy_and_iam_policy_hierarchy) and is the hierarchical super node of projects. This page explains how to acquire and manage an organization resource.

**Note:** To streamline setup, Google Cloud will automatically create an organization resource for new Free Trial customers. Additionally, every organization resource will automatically have a set of organization policies enforced on it. For more information, see [Standalone organizations](https://docs.cloud.google.com/resource-manager/docs/standalone-organization-overview) and [Managing baseline constraints](https://docs.cloud.google.com/organization-policy/manage-baseline-constraints).

## Before you begin

Read an [overview](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations) of the organization resource.

## Get an organization resource

An organization resource is available for Google Workspace and Cloud Identity customers:

  * **Google Workspace:** Sign up for [Google Workspace](https://support.google.com/a/answer/53926). 
  * **Cloud Identity:** Sign up for [Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin). 



Once you have created your Google Workspace or Cloud Identity account and associated it with a domain, your organization resource will be automatically created for you. The resource will be provisioned at different times depending on your account status: 

  * If you are new to Google Cloud and have not created a project yet, the organization resource will be created for you when you log in to the Google Cloud console and accept the terms and conditions. 
  * If you are an existing Google Cloud user, the organization resource will be created for you when you create a new project or billing account (if one doesn't already exist). Any projects you created previously will be listed under "No organization", and this is normal. The organization resource will appear and the new project you created will be linked to it automatically. 

You will need to move any projects you created under "No organization" into your new organization resource. For instructions on how to move your projects, see [Migrating projects into an organization resource](https://docs.cloud.google.com/resource-manager/docs/migrating-projects-billing). 




The organization resource that is created will be linked to your Google Workspace or Cloud Identity account with the project or billing account you created set as a child resource. All projects and billing accounts created under your Google Workspace or Cloud Identity domain will be children of this organization resource. 

  * For information about how to migrate pre-existing projects, see [Migrating existing projects](https://docs.cloud.google.com/resource-manager/docs/migrating-projects-billing). 



Each Google Workspace or Cloud Identity account is associated with exactly one organization resource. An organization resource is associated with exactly one domain, which is set when the organization resource is created. 

**Note:** Trying to register an organization with a domain that already exists will result in a "This domain is already in use" error. To resolve this, follow the steps in [Resolve "This domain is already in use"](https://support.google.com/a/answer/80610#zippy=%2Cthis-domain-is-already-in-use%2Cthis-domain-has-been-registered-and-is-in-the-process-of-ownership-verification). 

**Important:** When the organization resource is created, we communicate its availability to the Google Workspace or Cloud Identity super admins. These _super administrator accounts_ should be used carefully because they have a lot of control over your organization resource and all the resources underneath it. For this reason, we recommend against using Google Workspace or Cloud Identity super administrator accounts for day-to-day management of your organization resource. For more information about using Google Workspace or Cloud Identity super administrator accounts in Google Cloud, see [Super administrator account best practices](https://docs.cloud.google.com/resource-manager/docs/super-admin-best-practices).

To actively adopt the organization resource, the Google Workspace or Cloud Identity super admins need to assign the [Organization Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager) (`roles/resourcemanager.organizationAdmin`) Identity and Access Management (IAM) role to a user or group. For steps on setting up your organization resource, see Set up your organization resource.

  * When the organization resource is created, all users in your domain are automatically granted Project Creator (`roles/resourcemanager.projectCreator`) and Billing Account Creator (`roles/billing.creator`) IAM roles at the organization resource level. This enables users in your domain to continue creating projects with no disruption.
  * The Organization Administrator will decide when they want to start actively using the organization resource. They can then change the default permissions and enforce more restrictive policies as needed.
  * If the organization resource is available and you don't have the IAM permissions to view it, you can still create projects and billing accounts. These are automatically created under the organization resource, even if you can't see it.

**Note:** There is a second way to obtain an organization resource: a standalone organization is automatically created for users when they sign up for a Google Account. For more information, see the [documentation](https://docs.cloud.google.com/resource-manager/docs/standalone-organization-overview) on standalone organizations.

### Google Cloud security baseline

Google Cloud security baseline addresses insecure security postures with a bundle of organization policies that are enforced when an organization resource is created. These constraints are automatically created and enforced on your organization when it is created. For information about viewing and managing these constraints, see [Google Cloud security baseline constraints](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations).

## Get your organization resource ID

The organization resource ID is a unique identifier for an organization resource and is automatically created when your organization resource is created. Organization resource IDs are formatted as decimal numbers, and cannot have leading zeroes.

You can get your organization resource ID using the Google Cloud console, the gcloud CLI, or the Cloud Resource Manager API.

###  console 

To get your organization resource ID using the Google Cloud console, do the following:

  1. Go to the Google Cloud console: 

[Go to the Google Cloud console](https://console.cloud.google.com/)

  2. From the project picker at the top of the page, select your organization resource.
  3. On the right side, click **More** , and then click **Settings**.   
![](https://docs.cloud.google.com/static/resource-manager/img/console-more-settings.png)



The **Settings** page displays your organization resource ID.

###  gcloud 

To find your organization resource ID, run the following command:
    
    
    gcloud organizations list
    

This command lists all the organization resources to which you belong to, and their corresponding organization resource IDs.

###  API 

To find your organization resource ID using the Cloud Resource Manager API, use the [`organizations.search()`](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations/search) method, including a query for your domain. For example:
    
    
    GET https://cloudresourcemanager.googleapis.com/v3/organizations:search{query=domain:altostrat.com}
    

The response contains the metadata of the organization resource that belongs to `altostrat.com`, which includes the organization resource ID.

## Set up your organization resource

If you're a Google Workspace or Cloud Identity customer, an organization resource is provided to you automatically.

The Google Workspace or Cloud Identity super administrators are the first users who can access the organization resource upon creation. All other users or groups will be able to use Google Cloud as before. They'll be able to see the organization resource, but they'll only be able to modify it after the correct permissions are set.

The Google Workspace or Cloud Identity super administrators and the Google Cloud **Organization Administrator** are key roles during the setup process and for lifecycle control for the organization resource.

By default, the Google Workspace or Cloud Identity super administrator account that creates the organization resource is automatically assigned the **Organization Administrator** role. However, to maintain separation of duties, we recommend that the super administrator delegates the **Organization Administrator** role to a different user or group.

Google Workspace or Cloud Identity super administrator responsibilities, in the context of Google Cloud organization resource setup are:

  * Assigning the **Organization Administrator** role to some users
  * Being a point of contact in case of recovery issues
  * Controlling the lifecycle of the Google Workspace or Cloud Identity account and organization resource as explained under [Delete an organization](https://docs.cloud.google.com/resource-manager/docs/delete-org)



The **Organization Administrator** , once assigned, can assign Identity and Access Management roles to other users. The responsibilities of the **Organization Administrator** role are:

  * Defining allow and deny policies and granting roles to other users.
  * Seeing the structure of the [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy)



Following the principle of least privilege, this role does not include the permission to perform other actions, such as creating folders or projects. To get these permissions, an Organization Administrator must assign additional roles to their account.

While the same user can hold both roles, having two distinct roles ensures separation of duties between the Google Workspace or Cloud Identity super administrators and the Google Cloud Organization Administrator. This is often a requirement as the two Google products are typically managed by different departments in the customer's organization.

To actively use the organization resource, follow these steps to add an **Organization Administrator** :

### Add an Organization Administrator

To add an Organization Administrator, you can use the Google Cloud console, the Google Cloud CLI, or the Resource Manager API.

###  Console 

  1. Sign in to the Google Cloud console as a Google Workspace or Cloud Identity super administrator and navigate to the **IAM & Admin** page: 

[Open the IAM & admin page](https://console.cloud.google.com/iam-admin)

  2. Select the organization resource you want to edit:

     1. Click the project drop-down list at the top of the page.

     2. In the **Select from** dialog, click the organization drop-down list, and select the organization resource to which you want to add an Organization Administrator.

     3. On the list that appears, click the organization resource to open its **IAM Permissions** page.

  3. Click **Add** , and then enter the email address of one or more users you want to set as Organization Administrators.

  4. In the **Select a role** drop-down list, select **Resource Manager** > **Organization Administrator** , and then click **Save**.

The Organization Administrator can do the following:

     * Take full control of the organization resource. Separation of responsibilities between Google Workspace or Cloud Identity super administrator and Google Cloud administrator is established.

     * Delegate responsibility over critical functions by assigning the relevant IAM roles.




###  gcloud 

To add an Organization Administrator, run the [`gcloud organizations add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/organizations/add-iam-policy-binding) command:
    
    
    gcloud organizations add-iam-policy-binding ORGANIZATION_ID \
        --member="user:EMAIL_ADDRESS" \
        --role="roles/resourcemanager.organizationAdmin"
    

Replace the following:

  * `ORGANIZATION_ID`: the unique ID of your organization resource.
  * `EMAIL_ADDRESS`: the email address of the user you want to add as an Organization Administrator.



###  API 

To add an Organization Administrator, call the [`setIamPolicy`](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations/setIamPolicy) method on the organization resource.

  1. Get the current IAM policy for the organization resource:
         
         POST https://cloudresourcemanager.googleapis.com/v3/organizations/ORGANIZATION_ID:getIamPolicy
         

  2. Update the returned policy to add the member to the `roles/resourcemanager.organizationAdmin` role.

  3. Set the updated policy:
         
         POST https://cloudresourcemanager.googleapis.com/v3/organizations/ORGANIZATION_ID:setIamPolicy
         {
           "policy": {
             "bindings": [
               {
                 "role": "roles/resourcemanager.organizationAdmin",
                 "members": [
                   "user:EMAIL_ADDRESS"
                 ]
               }
             ],
             "etag": "ETAG_VALUE"
           }
         }
         

Replace the following:

     * `ORGANIZATION_ID`: the unique ID of your organization resource.
     * `EMAIL_ADDRESS`: the email address of the user you want to add as an Organization Administrator.
     * `ETAG_VALUE`: the `etag` value from the policy returned in the first step.



As explained in [getting an organization resource](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#acquiring), upon creation, all users in the domain are granted Project Creator and Billing Account Creator roles at the organization resource level by default. This ensures that no disruption is caused to Google Cloud users when the organization resource is created. As the **Organization Administrator** takes control, they might want to remove these organization-level permissions to start locking down access at a finer granularity (for instance, at the folder or project level). Note that, because allow and deny policies are inherited down the hierarchy, having the Project Creator role assigned to the entire domain (`domain:mycompany.com`) at the organization resource level implies that every user in the domain can create projects anywhere in the hierarchy.

## What's next

  * [Manage projects and billing in your organization](https://docs.cloud.google.com/resource-manager/docs/organization-resource-management)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
