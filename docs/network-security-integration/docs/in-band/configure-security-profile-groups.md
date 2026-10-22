---
url: https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-security-profile-groups/
title: Create and manage security profile groups \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:38.978585+00:00
---

# Create and manage security profile groups  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-security-profile-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)



Send feedback 

#  Create and manage security profile groups Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create and manage [security profile groups](https://docs.cloud.google.com/network-security-integration/docs/in-band/security-profile-groups-overview) with a [custom intercept security profile](https://docs.cloud.google.com/network-security-integration/docs/in-band/security-profiles-overview).

## Before you begin

  * [Enable](https://console.cloud.google.com/apis/library/networksecurity.googleapis.com) the [Network Security API](https://docs.cloud.google.com/network-security-integration/docs/reference/rest) in your project.
  * Install the [gcloud CLI](https://docs.cloud.google.com/sdk/docs).
  * Create a [custom intercept security profile](https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-security-profiles).



### Roles

To get the permissions that you need to create, view, update, or delete security profile groups, ask your administrator to grant you the required [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/network-security-integration/docs/security-profile-groups-overview#iam-roles) on your organization or project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

To check the progress of the operations listed on this page, make sure that your user role has the following [Compute Network User role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`roles/compute.networkUser`) permissions:

  * `networksecurity.operations.get`
  * `networksecurity.operations.list`



## Create a security profile group

You can create security profile groups at organization or project level. We recommend that you create the security profile group in a project owned by your security administrator.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization or project.

**Permissions**

  * `networksecurity.securityProfileGroups.create`



**Roles**

  * [Security Profile Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`networksecurity.securityProfileAdmin`) at the organization level for organization-level security profile groups, and at either the project or the organization level for project-level security profile groups. 



###  Console 

**Note:** If your Google Cloud project is in a data residency zone (DRZ) in the Kingdom of Saudi Arabia (KSA) or India, you can't view, list, create, update, or delete project-level security profiles or security profile groups by using the Google Cloud console. To manage project-level security profiles and security profile groups in KSA and India, use the gcloud CLI or the API. 

  1. In the Google Cloud console, go to the **Security profile groups** page.

[Go to Security profile groups](https://console.cloud.google.com/net-security/security-profiles/profile-groups/list)

  2. From the project selector menu, select your organization or the project.

  3. In the **Security profile groups** tab, click **Create profile group**.

  4. For **Name** , enter the name of the security profile group.

  5. For **Security profile group purpose** , select **NSI in-band**.

  6. For **Custom intercept profile** , select the custom security profile for in-band integration.

  7. Click **Create**.




###  gcloud 

To create a security profile group, use the [`gcloud network-security security-profile-groups create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/create):
    
    
    gcloud network-security security-profile-groups create SECURITY_PROFILE_GROUP_NAME \
        --custom-intercept-profile CUSTOM_INTERCEPT_PROFILE_ID \
        --organization ORGANIZATION_ID | --project PROJECT_ID \
        [--billing-project QUOTA_PROJECT_ID] \
        --location global
    

Replace the following:

  * `SECURITY_PROFILE_GROUP_ID`: the name of the security profile group.

If you don't specify the name in [the unique URL identifier format](https://docs.cloud.google.com/network-security-integration/docs/in-band/security-profile-groups-overview#specifications), you must specify the organization or the project name, and the location.

  * `CUSTOM_INTERCEPT_PROFILE_ID`: the ID of the custom intercept security profile.

  * `ORGANIZATION_ID`: your organization ID. Use this flag to create an organization-level security profile group.

  * `PROJECT_ID`: your project ID. Use this flag to create a project-level security profile group.

  * `QUOTA_PROJECT_ID`: your quota project ID. Use this flag only for organization-level security profile groups.




###  Terraform 

To create a security profile group, you can use a [`google_network_security_security_profile_group` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/network_security_security_profile_group).

The following example shows how to create an organization-level security profile group:
    
    
    resource "google_network_security_security_profile_group" "default" {
      name                     = "security-profile-group"
      parent                   = "organizations/${data.google_organization.default.org_id}"
      location                 = "global"
      custom_intercept_profile = google_network_security_security_profile.default.id
    }

The following example shows how to create a project-level security profile group:
    
    
    resource "google_network_security_security_profile_group" "default" {
      name                     = "security-profile-group"
      parent                   = "projects/${data.google_project.default.project_id}"
      location                 = "global"
      custom_intercept_profile = google_network_security_security_profile.default.id
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

## List and view details of a security profile group

You can list security profile groups in an organization or a project, and view the details of a group, such as its name and custom intercept profile.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization or project.

**Permissions**

  * `networksecurity.securityProfileGroups.list` to see security profile groups.
  * `networksecurity.securityProfileGroups.get` to see the details of a profile group.



**Roles**

  * [Security Profile Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`networksecurity.securityProfileAdmin`) at the organization level for organization-level security profile groups, and at either the project or the organization level for project-level security profile groups. 



###  Console 

**Note:** If your Google Cloud project is in a data residency zone (DRZ) in the Kingdom of Saudi Arabia (KSA) or India, you can't view, list, create, update, or delete project-level security profiles or security profile groups by using the Google Cloud console. To manage project-level security profiles and security profile groups in KSA and India, use the gcloud CLI or the API. 

  1. In the Google Cloud console, go to the **Security profile groups** page.

[Go to Security profile groups](https://console.cloud.google.com/net-security/security-profiles/profile-groups/list)

  2. From the project selector menu, select your organization or the project. The tab lists all security profile groups.

  3. In the **Security profile groups** tab, click the name of the security profile group to see its details.




###  gcloud 

To list security profile groups, use the [`gcloud network-security security-profile-groups list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/list):
    
    
    gcloud network-security security-profile-groups list \
        --organization ORGANIZATION_ID | --project PROJECT_ID \
        --location global \
        [--billing-project QUOTA_PROJECT_ID]
    

To view details of a security profile group, use the [`gcloud network-security security-profile-groups describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/describe):
    
    
    gcloud network-security security-profile-groups describe SECURITY_PROFILE_GROUP_ID \
        --organization ORGANIZATION_ID | --project PROJECT_ID \
        [--billing-project QUOTA_PROJECT_ID] \
        --location global
    

Replace the following:

  * `SECURITY_PROFILE_GROUP_ID`: the name of the security profile group.

If you don't specify the name in [the unique URL identifier format](https://docs.cloud.google.com/network-security-integration/docs/in-band/security-profile-groups-overview#specifications), you must specify the organization or the project name, and the location.

  * `ORGANIZATION_ID`: your organization ID where the security profile group exists.

  * `PROJECT_ID`: your project ID where the security profile group exists.

  * `QUOTA_PROJECT_ID`: your quota project ID. Use this flag only for organization-level security profile groups.




The output displays security profile group names in the following formats:

  * **Organization-level security profile groups** : `organizations/ORGANIZATION_ID/locations/global/securityProfileGroups/SECURITY_PROFILE_GROUP_ID`
  * **Project-level security profile groups** : `projects/PROJECT_ID/locations/global/securityProfileGroups/SECURITY_PROFILE_GROUP_ID`



## Delete a security profile group

Before you delete a security profile group, [delete the custom intercept security profile](https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-security-profiles#delete-intercept-security-profile) that references the security profile group.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization or project.

**Permissions**

  * `networksecurity.securityProfileGroups.delete`



**Roles**

  * [Security Profile Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`networksecurity.securityProfileAdmin`) at the organization level for organization-level security profile groups, and at either the project or the organization level for project-level security profile groups. 



###  Console 

**Note:** If your Google Cloud project is in a data residency zone (DRZ) in the Kingdom of Saudi Arabia (KSA) or India, you can't view, list, create, update, or delete project-level security profiles or security profile groups by using the Google Cloud console. To manage project-level security profiles and security profile groups in KSA and India, use the gcloud CLI or the API. 

  1. In the Google Cloud console, go to the **Security profile groups** page.

[Go to Security profile groups](https://console.cloud.google.com/net-security/security-profiles/profile-groups/list)

  2. From the project selector menu, select your organization or the project.

  3. In the **Security profile groups** tab, select the checkbox of the security profile group and click **Delete**.

  4. Click **Delete** again to confirm.




###  gcloud 

To delete a security profile group, use the [`gcloud network-security security-profile-groups delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/delete):
    
    
    gcloud network-security security-profile-groups delete SECURITY_PROFILE_GROUP_ID \
        --organization ORGANIZATION_ID | --project PROJECT_ID \
        [--billing-project QUOTA_PROJECT_ID] \
        --location global
    

Replace the following:

  * `SECURITY_PROFILE_GROUP_NAME`: the name of the security profile group that you want to delete.

If you don't specify the name in [the unique URL identifier format](https://docs.cloud.google.com/network-security-integration/docs/in-band/security-profile-groups-overview#specifications), you must specify the organization or the project name, and the location.

  * `ORGANIZATION_ID`: your organization ID where the security profile group exists.

  * `PROJECT_ID`: your project ID where the security profile group exists.

  * `QUOTA_PROJECT_ID`: your quota project ID. Use this flag only for organization-level security profile groups.




## What's next

  * [Create and manage intercept endpoint groups](https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-intercept-endpoint-groups)
  * [Security profile groups overview](https://docs.cloud.google.com/network-security-integration/docs/in-band/security-profile-groups-overview)
  * [Create and manage custom intercept security profiles](https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-security-profiles)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
