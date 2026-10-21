---
url: https://docs.cloud.google.com/resource-manager/docs/standalone-organization-overview/
title: Set up standalone organizations \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:20:26.233635+00:00
---

# Set up standalone organizations  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/standalone-organization-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Set up standalone organizations Stay organized with collections  Save and categorize content based on your preferences. 

This guide provides information about obtaining and managing a standalone organization within Google Cloud.

The organization resource serves as the root node of your Google Cloud resource hierarchy. In most circumstances, creating an organization requires you to be a Cloud Identity super administrator and connect the Google Cloud organization to a DNS domain.

With standalone organizations, you don't require Cloud Identity. When you sign up for Google Cloud and provide a Google email address, the standalone organization is automatically created for you. Being the account owner, you also acquire the Organization Owner role. You can then use the **Organization details** page to manage ownership access for other users.

Standalone organizations offer the following benefits:

  * Ability to add users with federated identities as organization owners.
  * Ability to support multiple organizations to test different features.
  * Ability to support multiple organization owners to avoid single points of failure if an employee leaves.



## Before you begin

Before you begin, review the following:

  * Understand the [organization resource](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations).
  * Learn how to [decide a resource hierarchy for your Google Cloud landing zone](https://cloud.google.com/architecture/landing-zones/decide-resource-hierarchy).



## Identify your organization

Your standalone organization is identified by an organization name and an organization ID.

**Organization name**

The default organization name is created by combining the username with `-org`. Any special characters in the username are replaced with a dash. For example, if the username is `lara_brown`, the organization name will be `lara-brown-org`. This name is not used by any Google APIs. You can edit the organization name at any time after organization creation.

Ensure the names meet the following criteria:

  * Contain only letters, numbers, or hyphens.
  * Don't use a domain name. Domain names are reserved for Cloud Identity and Google Workspace organizations only.
  * Don't contain common words such as 'Google Cloud'.



**Organization ID**

The organization ID is a globally unique identifier for your organization. The Google Cloud console generates this number to differentiate your organization from all others in Google Cloud. Organization IDs are formatted as whole numbers and can't have leading zeros.

Don't include sensitive information such as personally identifiable information (PII) or security data in your organization name or other resource names. The organization ID is used in the name of many other Google Cloud resources. Any reference to the organization or related resources exposes the organization ID and resource name.

## Get a standalone organization resource

Standalone organizations are available for all new [Free Trial](https://docs.cloud.google.com/free/docs/free-cloud-features) Google Cloud customers. After you create your Google Cloud account, your organization resource is automatically created. This occurs when you sign in to the Google Cloud console and accept the terms. Standalone organizations aren't available for existing Google Cloud accounts.

Only one organization is created per user account. However, you can invite a single user to own and administer multiple organizations.

When the organization resource is created, the system assigns the following roles to the account owner:

  * `roles/cloudowner.admin` (Organization Owner)
  * `roles/resourcemanager.organizationAdmin` (Organization Administrator)



The Organization Owner role is managed outside of IAM, and grants permissions to manage organization owners and administrators from the **Organization details** page. For information on adding more owners and administrators to your organization, see Set up your standalone organization.

## Get your organization ID

To get the organization ID of your standalone organization, you can use the Google Cloud console, the Google Cloud CLI, or the Resource Manager API.

###  Console 

  * In the Google Cloud console, go to the **My organizations** page.

[Go to My organizations](https://console.cloud.google.com/organizations/list)

The table lists your organizations and their organization IDs.




###  gcloud 

To find your organization resource ID, run the following command:
    
    
    gcloud organizations list
    

This command lists all the organization resources to which you belong to, and their corresponding organization resource IDs.

###  API 

To find your organization resource ID using the Cloud Resource Manager API, use the [`organizations.search()`](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations/search) method, including a query for your domain. For example:
    
    
    GET https://cloudresourcemanager.googleapis.com/v3/organizations:search{query=domain:altostrat.com}
    

The response contains the metadata of the organization resource that belongs to `altostrat.com`, which includes the organization resource ID.

## Set up your standalone organization

When you create a Google Cloud account, you automatically get a standalone organization resource. In this section, you learn about the initial setup, the essential roles, and how to manage these permissions within your organization.

The account creator is the first user with access to the organization resource. Other users in the organization can view the resource but can only modify it after appropriate permissions are set.

The Organization Owner and Organization Administrator are key roles for setting up and controlling the lifecycle of the organization resource. These two roles are typically assigned to different users or groups, depending on your organization's structure and needs.

### Organization Owner responsibilities

The Organization Owner role lets you perform the following actions:

  * Assign the Organization Administrator role to other users.
  * Serve as the point of contact in case of recovery issues.
  * Control the lifecycle of the standalone organization resource, as explained in [Delete, restore, and rename standalone organizations](https://docs.cloud.google.com/resource-manager/docs/delete-standalone-org).



Organization owners can be individuals or principals within a workforce pool. Each standalone organization must always have at least one active Google Account as the organization owner. Service accounts can't be invited to become organization owners.

### Organization Administrator responsibilities

The Organization Administrator role lets you perform the following actions:

  * Define allow and deny policies.
  * Grant Identity and Access Management roles to other users in Google Cloud.
  * View the resource hierarchy.



Following the principle of least privilege, this role prevents you from performing other actions, such as creating folders or projects. To get these permissions, an Organization Administrator must assign additional roles to your account.

### Grant the Organization Owner role to individuals

  1. Sign in to the Google Cloud console as an organization owner.
  2. In the Google Cloud console, go to the **Organization details** page.

[Go to Organization details](https://console.cloud.google.com/organizations/details)

  3. Under **Organization Owner** , click **Add organization Owner**.

  4. Enter the email address of the principal you want to add as an owner. The system sends an email to the principal inviting them to become an owner of the organization. The principal must accept the invitation within 30 days to become an organization owner.




### Grant the Organization Owner role to users in a workforce identity pool

This step assumes that you have already configured [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) for your organization. Additionally, ensure that Essential Contacts are configured on your account.

  1. Sign in to the Google Cloud console as an organization owner.
  2. In the Google Cloud console, go to the **Organization details** page.

[Go to Organization details](https://console.cloud.google.com/organizations/details)

  3. Under **Organization Owner** , click **Add organization Owner**.

  4. Enter the principal identifier of the user in the format `principal://iam.googleapis.com/locations/LOCATION/workforcePools/POOL_ID/subject/SUBJECT_ATTRIBUTE_VALUE`.

  5. Click **Next**.

  6. Enter the email address to which to send the owner invitation link. Google Cloud sends an email to the user inviting them to become an owner of the organization. To become an organization owner, the user must accept the invitation within 30 days. When the user accepts the invitation, they are automatically granted the role of an Organization Administrator.




### Grant the Organization Administrator role

The Organization Owner can grant the Organization Administrator role to other users from the **Organization details** page. This is useful if you have inadvertently removed Organization Administrator permissions from all users who can set IAM policies on the organization, and need to restore access.

To grant users the Organization Administrator role, follow these steps:

  1. Sign in to the Google Cloud console as an organization owner.
  2. In the Google Cloud console, go to the **Organization details** page.

[Go to Organization details](https://console.cloud.google.com/organizations/details)

  3. View the list of organization owners in the **Organization owners** table.

  4. Select the principal that you want to assign the Organization Administrator role to.

  5. In the final column of the table, under **Actions** , click **More actions** next to the principal.

  6. Click **Grant Organization Administrator role**. The principal is granted the Organization Administrator role (`roles/resourcemanager.organizationAdmin`) on the organization resource.




### Remove an organization owner

To remove users with the Organization Owner role, follow these steps:

  1. Sign in to the Google Cloud console as an organization owner.
  2. In the Google Cloud console, go to the **Organization details** page.

[Go to Organization details](https://console.cloud.google.com/organizations/details)

  3. Under **Organization Owners** , select the principal that you want to remove.

  4. In the final column of the table, under **Actions** , click **More actions** next to the principal.

  5. In the dialog that appears, click **Remove**.




### Remove an organization administrator

To remove users with the Organization Administrator role, follow these steps:

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam?supportedpurview=project)

  2. Under **IAM Allow** , go to **View by principals**.

  3. Locate the row that contains the principal that you granted roles to and click **Edit principal** edit in that row.

  4. In the **Edit permissions** pane, click the delete icon next to the Organization Administrator role.

  5. Click **Save**.




## What's next

  * [Delete, restore, and rename standalone organizations](https://docs.cloud.google.com/resource-manager/docs/delete-standalone-org)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
