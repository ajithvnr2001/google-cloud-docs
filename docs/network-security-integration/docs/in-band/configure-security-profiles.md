---
url: https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-security-profiles/
title: Create and manage custom intercept security profiles \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:02.324907+00:00
---

# Create and manage custom intercept security profiles  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-security-profiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)



Send feedback 

#  Create and manage custom intercept security profiles Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create and manage custom intercept security profiles.

## Before you begin

  * [Enable](https://console.cloud.google.com/apis/library/networksecurity.googleapis.com) the [Network Security API](https://docs.cloud.google.com/network-security-integration/docs/reference/rest) in your project.
  * Install the [gcloud CLI](https://docs.cloud.google.com/sdk/docs).



### Roles

To get the permissions that you need to create, view, update, or delete custom intercept security profiles, ask your administrator to grant you the necessary [IAM roles](https://docs.cloud.google.com/network-security-integration/docs/security-profiles-overview#iam-roles) on your organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

To check the progress of the operations listed on this page, make sure that your user role has the following [Compute Network User role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`roles/compute.networkUser`) permissions:

  * `networksecurity.operations.get`
  * `networksecurity.operations.list`



## Create a custom intercept security profile

For in-band integration, you can only create a security profile of type `custom-intercept`. You can create security profiles at organization or project level.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization or project.

**Permissions**

  * `networksecurity.securityProfiles.create`
  * `networksecurity.interceptEndpointGroups.use`



**Roles**

  * [Security Profile Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`networksecurity.securityProfileAdmin`) at the organization level for organization-level security profiles, and at either the project or the organization level for project-level security profiles. 
  * `networksecurity.interceptEndpointAdmin`



###  Console 

**Note:** If your Google Cloud project is in a data residency zone (DRZ) in the Kingdom of Saudi Arabia (KSA) or India, you can't view, list, create, update, or delete project-level security profiles or security profile groups by using the Google Cloud console. To manage project-level security profiles and security profile groups in KSA and India, use the gcloud CLI or the API. 

  1. In the Google Cloud console, go to the **Security profiles** page.

[Go to Security profiles](https://console.cloud.google.com/net-security/security-profiles/profiles/list)

  2. From the project selector menu, select your organization or the project.

  3. In the **Security profiles** tab, click **Create profile**.

  4. For **Name** , enter a name.

  5. For **Security profile purpose** , select **NSI in-band**.

  6. For **Project** , select the project that hosts the intercept endpoint group.

  7. For **Intercept endpoint group** , select the intercept endpoint group.

  8. Click **Create**.




###  gcloud 

To create a custom intercept security profile for in-band integration, use the [`gcloud network-security security-profiles custom-intercept create` command](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/custom-intercept/create):
    
    
    gcloud network-security security-profiles custom-intercept create CUSTOM_INTERCEPT_PROFILE_ID \
        --organization ORGANIZATION_ID | --project PROJECT_ID \
        --location global \
        [--billing-project QUOTA_PROJECT_ID ] \
        --intercept-endpoint-group \
            projects/ENDPOINT_GROUP_PROJECT_ID/locations/global/interceptEndpointGroups/ENDPOINT_GROUP_ID
    

Replace the following:

  * `CUSTOM_INTERCEPT_PROFILE_ID`: the name of the security profile.

If you don't specify the name in [the unique URL identifier format](https://docs.cloud.google.com/network-security-integration/docs/in-band/security-profiles-overview#specifications), you must specify the organization or the project name, and the location.

  * `ORGANIZATION_ID`: your organization ID. Use this flag to create an organization-level security profile.

  * `PROJECT_ID`: your project ID. Use this flag to create a project-level security profile.

  * `QUOTA_PROJECT_ID`: your quota project ID. Use this flag only for organization-level security profile.

  * `ENDPOINT_GROUP_PROJECT_ID`: the project ID where you created the intercept endpoint group.

  * `ENDPOINT_GROUP_ID`: the ID of the endpoint group.




###  Terraform 

To create a security profile, you can use a [`google_network_security_security_profile` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/network_security_security_profile).

The following example shows how to create an organization-level security profile:
    
    
    resource "google_network_security_security_profile" "default" {
      name     = "security-profile"
      type     = "CUSTOM_INTERCEPT"
      parent   = "organizations/${data.google_organization.default.org_id}"
      location = "global"
    
      custom_intercept_profile {
        intercept_endpoint_group = google_network_security_intercept_endpoint_group.default.id
      }
    }

The following example shows how to create a project-level security profile:
    
    
    resource "google_network_security_security_profile" "default" {
      name     = "security-profile"
      type     = "CUSTOM_INTERCEPT"
      parent   = "projects/${data.google_project.default.project_id}"
      location = "global"
    
      custom_intercept_profile {
        intercept_endpoint_group = google_network_security_intercept_endpoint_group.default.id
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

## List and view details of a custom intercept security profile

You can list security profiles in an organization or a project, and view the details of a profile, such as its name and endpoint group ID.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization or project.

**Permissions**

  * `networksecurity.securityProfiles.list` to see the list of security profiles.
  * `networksecurity.securityProfiles.get` to see the details of a security profile.



**Roles**

  * [Security Profile Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`networksecurity.securityProfileAdmin`) at the organization level for organization-level security profiles, and at either the project or the organization level for project-level security profiles. 



###  Console 

**Note:** If your Google Cloud project is in a data residency zone (DRZ) in the Kingdom of Saudi Arabia (KSA) or India, you can't view, list, create, update, or delete project-level security profiles or security profile groups by using the Google Cloud console. To manage project-level security profiles and security profile groups in KSA and India, use the gcloud CLI or the API. 

  1. In the Google Cloud console, go to the **Security profiles** page.

[Go to Security profiles](https://console.cloud.google.com/net-security/security-profiles/profiles/list)

  2. From the project selector menu, select your organization or the project. The tab lists all security profiles.

  3. In the **Security profiles** tab, click the name of the security profile.




###  gcloud 

To list all the custom intercept security profiles, use the [`gcloud network-security security-profiles custom-intercept list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/custom-intercept/list):
    
    
    gcloud network-security security-profiles custom-intercept list \
        --organization ORGANIZATION_ID | --project PROJECT_ID \
        --location global \
        [--billing-project QUOTA_PROJECT_ID]
    

To view details of a custom intercept security profile, use the [`gcloud network-security security-profiles custom-intercept describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/custom-intercept/describe):
    
    
    gcloud network-security security-profiles custom-intercept describe CUSTOM_INTERCEPT_PROFILE_ID \
        --organization ORGANIZATION_ID | --project PROJECT_ID \
        [--billing-project QUOTA_PROJECT_ID] \
        --location global
    

Replace the following:

  * `CUSTOM_INTERCEPT_PROFILE_ID`: the name of the security profile.

If you don't specify the name in [the unique URL identifier format](https://docs.cloud.google.com/network-security-integration/docs/in-band/security-profiles-overview#specifications), you must specify the organization or the project name, and the location.

  * `ORGANIZATION_ID`: your organization ID where the security profile exists.

  * `PROJECT_ID`: your project ID where the security profile exists.

  * `QUOTA_PROJECT_ID`: your quota project ID. Use this flag only for organization-level security profiles.




The output is similar to the following:

  * **Organization-level security profiles** : `organizations/ORGANIZATION_ID/locations/global/securityProfiles/CUSTOM_INTERCEPT_PROFILE_ID`
  * **Project-level security profiles** : `projects/PROJECT_ID/locations/global/securityProfiles/CUSTOM_INTERCEPT_PROFILE_ID`



## Delete a custom intercept security profile

You can delete a custom intercept security profile by specifying its name, location, and organization or project. Before you delete the security profile, make sure that it isn't used by a security profile group.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization or project.

**Permissions**

  * `networksecurity.securityProfiles.delete`



**Roles**

  * [Security Profile Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`networksecurity.securityProfileAdmin`) at the organization level for organization-level security profiles, and at either the project or the organization level for project-level security profiles. 



###  Console 

**Note:** If your Google Cloud project is in a data residency zone (DRZ) in the Kingdom of Saudi Arabia (KSA) or India, you can't view, list, create, update, or delete project-level security profiles or security profile groups by using the Google Cloud console. To manage project-level security profiles and security profile groups in KSA and India, use the gcloud CLI or the API. 

  1. In the Google Cloud console, go to the **Security profiles** page.

[Go to Security profiles](https://console.cloud.google.com/net-security/security-profiles/profiles/list)

  2. From the project selector menu, select your organization or the project.

  3. In the **Security profiles** tab, select the checkbox of the security profile, and then click **Delete**.

  4. Click **Delete** again to confirm.




###  gcloud 

To delete a custom intercept security profile, use the `gcloud network-security security-profiles custom-intercept delete` command:
    
    
    gcloud network-security security-profiles custom-intercept delete CUSTOM_INTERCEPT_PROFILE_ID \
        --organization ORGANIZATION_ID | --project PROJECT_ID \
        [--billing-project QUOTA_PROJECT_ID] \
        --location global
    

Replace the following:

  * `CUSTOM_INTERCEPT_PROFILE_ID`: the ID of the custom intercept security profile that you want to delete.

If you don't specify the name in [the unique URL identifier format](https://docs.cloud.google.com/network-security-integration/docs/in-band/security-profiles-overview#specifications), you must specify the organization or the project name, and the location.

  * `ORGANIZATION_ID`: your organization ID where the security profile exists.

  * `PROJECT_ID`: your project ID where the security profile exists.

  * `QUOTA_PROJECT_ID`: your quota project ID. Use this flag only for organization-level security profiles.




## What's next

  * [Security profile groups overview](https://docs.cloud.google.com/network-security-integration/docs/in-band/security-profile-groups-overview)
  * [Security profiles overview](https://docs.cloud.google.com/network-security-integration/docs/in-band/security-profiles-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
