---
url: https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-custom-security-profiles/
title: Create and manage custom mirroring security profiles \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:04.007883+00:00
---

# Create and manage custom mirroring security profiles  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-custom-security-profiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)



Send feedback 

#  Create and manage custom mirroring security profiles Stay organized with collections  Save and categorize content based on your preferences. 

You can create a custom mirroring security profile only for Packet Mirroring. A custom mirroring security profile is a configuration that mandates the inspection of specified network traffic by a designated network firewall policy rule. Traffic that matches the mirroring rules in the network firewall policy rule is mirrored to the endpoint group referenced by the security profile of that network firewall policy rule.

This page explains how to create and manage custom security profiles by using the Google Cloud CLI.

## Before you begin

  * You must [enable](https://console.cloud.google.com/apis/library/networksecurity.googleapis.com) the [Network Security API](https://docs.cloud.google.com/network-security-integration/docs/reference/rest) in your project.
  * Install the [gcloud CLI](https://docs.cloud.google.com/sdk/docs) if you want to run the `gcloud` command-line examples in this guide.



### Roles

To get the permissions that you need to create, view, update, or delete custom security profiles, ask your administrator to grant you the necessary [IAM roles](https://docs.cloud.google.com/network-security-integration/docs/security-profiles-overview#iam-roles) on your organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

To check the progress of the operations listed on this page, make sure that your user role has the following [Compute Network User](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`roles/compute.networkUser`) permissions:

  * `networksecurity.operations.get`
  * `networksecurity.operations.list`



## Create a custom security profile

You can only create a security profile of type `CUSTOM_MIRRORING`. You can create security profiles at organization or project level.

When you create a custom security profile, you can specify the name of the custom security profile, the location, and the endpoint group where the traffic is directed.

In this section, create a custom security profile for packet mirroring.

### Direct mode of mirroring

Create a custom security profile for the direct mode of packet mirroring.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization or project.

**Permissions**

  * `networksecurity.securityProfiles.create`



**Roles**

  * [Security Profile Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`networksecurity.securityProfileAdmin`) at the organization level for organization-level security profiles, and at either the project or the organization level for project-level security profiles. 



###  Console 

**Note:** If your Google Cloud project is in a data residency zone (DRZ) in the Kingdom of Saudi Arabia (KSA) or India, you can't view, list, create, update, or delete project-level security profiles or security profile groups by using the Google Cloud console. To manage project-level security profiles and security profile groups in KSA and India, use the gcloud CLI or the API. 

  1. In the Google Cloud console, go to the **Security profiles** page.

[Go to Security profiles](https://console.cloud.google.com/net-security/security-profiles/profiles/list)

  2. From the project selector menu, select your organization or the project.

  3. On the **Security profiles** tab, click **Create profile**.

  4. For **Name** , enter a name.

  5. For **Security profile purpose** , select **NSI out-of-band**.

  6. For **Project** , select the project that hosts the mirroring endpoint group.

  7. For **Mirroring endpoint group** , select the mirroring endpoint group.

  8. Click **Create**.




###  gcloud 

To create a custom security profile for the direct mode of packet mirroring, use the [`gcloud network-security security-profiles custom-mirroring create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/custom-mirroring/create):
    
    
    gcloud network-security security-profiles custom-mirroring \
        create CUSTOM_MIRRORING_PROFILE_NAME \
        --organization ORGANIZATION_ID | --project PROJECT_ID \
        --location=global \
        --mirroring-endpoint-group ENDPOINT_GROUP \
        --description DESCRIPTION \
        [--billing-project QUOTA_PROJECT_ID]
    

Replace the following:

  * `CUSTOM_MIRRORING_PROFILE_NAME`: the name of the custom security profile.

If you don't specify the name in [the unique URL identifier format](https://docs.cloud.google.com/network-security-integration/docs/security-profiles-overview#specifications), you must specify the organization or the project name, and the location.

  * `ORGANIZATION_ID`: your organization ID. Use this flag to create an organization-level security profile.

  * `PROJECT_ID`: your project ID. Use this flag to create a project-level security profile.

  * `ENDPOINT_GROUP`: the URL of the mirroring endpoint group—for example, `projects/12345678/locations/global/mirroringEndpointGroups/mirroringEPG`.

  * `DESCRIPTION`: an optional description for the custom mirroring profile.

  * `QUOTA_PROJECT_ID`: your quota project ID. Use this flag only for organization-level security profiles.




###  Terraform 

To create a security profile, you can use a [`google_network_security_security_profile` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/network_security_security_profile).
    
    
    resource "google_network_security_security_profile" "default" {
      name     = "security-profile"
      type     = "CUSTOM_MIRRORING"
      parent   = "organizations/${data.google_organization.default.org_id}"
      location = "global"
    
      custom_mirroring_profile {
        mirroring_endpoint_group = google_network_security_mirroring_endpoint_group.default.id
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

### Broker mode of mirroring

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Create a custom security profile for the broker mode of packet mirroring.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization or project.

**Permissions**

  * `networksecurity.securityProfiles.create`



**Roles**

  * [Security Profile Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`networksecurity.securityProfileAdmin`) at the organization level for organization-level security profiles, and at either the project or the organization level for project-level security profiles ([Preview](https://cloud.google.com/products#product-launch-stages)). 



###  gcloud 

To create a custom security profile for the broker mode of packet mirroring, use the [`gcloud network-security security-profiles custom-mirroring create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/custom-mirroring/create):
    
    
    gcloud beta network-security security-profiles custom-mirroring \
        create CUSTOM_MIRRORING_PROFILE_NAME \
        --organization ORGANIZATION_ID | --project PROJECT_ID \
        --location=global \
        --mirroring-endpoint-group ENDPOINT_GROUP \
        --description DESCRIPTION \
        --mirroring-deployment-groups DEPLOYMENT_GROUP_1,DEPLOYMENT_GROUP_2 \
        [--billing-project QUOTA_PROJECT_ID]
    

Replace the following:

  * `CUSTOM_MIRRORING_PROFILE_NAME`: the name of the custom security profile.

If you don't specify the name in [the unique URL identifier format](https://docs.cloud.google.com/network-security-integration/docs/security-profiles-overview#security-profile-specification), you must specify the organization or the project name, and the location.

  * `ORGANIZATION_ID`: your organization ID. Use this flag to create an organization-level security profile.

  * `PROJECT_ID`: your project ID. Use this flag to create a project-level security profile ([Preview](https://cloud.google.com/products#product-launch-stages)).

The `--project` flag is available in ([Preview](https://cloud.google.com/products#product-launch-stages)). To use this flag, run the [`gcloud beta network-security security-profiles custom-mirroring create` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/custom-mirroring/create).

  * `ENDPOINT_GROUP`: the URL of the mirroring endpoint group—for example, `projects/12345678/locations/global/mirroringEndpointGroups/mirroringEPG`.

  * `DESCRIPTION`: an optional description for the custom mirroring profile.

  * `DEPLOYMENT_GROUP_1, DEPLOYMENT_GROUP_2`: the comma-separated list of mirroring deployment groups. The deployment groups must be a subset of the deployment groups connected to the mirroring endpoint group for the broker mode of packet mirroring.

The deployment group must be specified in the `projects/PROJECT_ID/locations/global/mirroringDeploymentGroups/DEPLOYMENT_GROUP` format.

  * `QUOTA_PROJECT_ID`: your quota project ID. Use this flag only for organization-level security profiles.




###  Terraform 

To create a security profile, you can use a [`google_network_security_security_profile` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/network_security_security_profile).

The following example shows how to create an organization-level security profile:
    
    
    resource "google_network_security_security_profile" "default" {
      name     = "security-profile"
      type     = "CUSTOM_MIRRORING"
      parent   = "organizations/${data.google_organization.default.org_id}"
      location = "global"
    
      custom_mirroring_profile {
        mirroring_endpoint_group = google_network_security_mirroring_endpoint_group.default.id
      }
    }

The following example shows how to create a project-level security profile:
    
    
    resource "google_network_security_security_profile" "default" {
      name     = "security-profile"
      type     = "CUSTOM_MIRRORING"
      parent   = "projects/${data.google_project.default.project_id}"
      location = "global"
    
      custom_mirroring_profile {
        mirroring_endpoint_group = google_network_security_mirroring_endpoint_group.default.id
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

## List and view details of a custom security profile

You can list custom security profiles in an organization or a project, and view the details of a profile, such as its name and endpoint group ID.

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

  3. On the **Security profiles** tab, click the name of the security profile to see its details.




###  gcloud 

To list all custom mirroring security profiles, use the [`gcloud network-security security-profiles custom-mirroring list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/custom-mirroring/list):
    
    
    gcloud network-security security-profiles custom-mirroring list \
        --organization ORGANIZATION_ID | --project PROJECT_ID \
        --location=global \
        [--billing-project QUOTA_PROJECT_ID]
    

To view details of a custom mirroring security profile, use the [`gcloud network-security security-profiles custom-mirroring describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/custom-mirroring/describe):
    
    
    gcloud network-security security-profiles custom-mirroring \
        describe CUSTOM_MIRRORING_PROFILE_NAME \
        --organization ORGANIZATION_ID | --project PROJECT_ID \
        --location=global \
        [--billing-project QUOTA_PROJECT_ID]
    

Replace the following:

  * `CUSTOM_MIRRORING_PROFILE_NAME`: the name of the custom security profile.

If you don't specify the name in [the unique URL identifier format](https://docs.cloud.google.com/network-security-integration/docs/security-profiles-overview#specifications), you must specify the organization or the project name, and the location.

  * `ORGANIZATION_ID`: your organization ID where the security profile exists.

  * `PROJECT_ID`: your project ID where the security profile exists.

  * `QUOTA_PROJECT_ID`: your quota project ID. Use this flag only for organization-level security profiles.




The output is similar to the following:

  * **Organization-level security profiles** : `organizations/ORGANIZATION_ID/locations/global/securityProfiles/CUSTOM_MIRRORING_PROFILE_NAME`
  * **Project-level security profiles** : `projects/PROJECT_ID/locations/global/securityProfiles/CUSTOM_MIRRORING_PROFILE_NAME`



## Delete a custom security profile

You can delete a custom mirroring security profile by specifying its name, location, and organization or project. However, if a custom security profile is referenced by a security profile group, that custom security profile cannot be deleted.

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

  3. On the **Security profiles** tab, select the checkbox of the security profile, and then click **Delete**.

  4. Click **Delete** again to confirm.




###  gcloud 

To delete a custom mirroring security profile, use the [`gcloud network-security security-profiles custom-mirroring delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/custom-mirroring/delete):
    
    
    gcloud network-security security-profiles custom-mirroring \
        delete CUSTOM_MIRRORING_PROFILE_NAME \
        --organization ORGANIZATION_ID | --project PROJECT_ID \
        --location=global \
        [--billing-project QUOTA_PROJECT_ID]
    

Replace the following:

  * `CUSTOM_MIRRORING_PROFILE_NAME`: the name of the custom security profile that you want to delete.

If you don't specify the name in [the unique URL identifier format](https://docs.cloud.google.com/network-security-integration/docs/security-profiles-overview#specifications), you must specify the organization or the project name, and the location.

  * `ORGANIZATION_ID`: your organization ID where the security profile exists.

  * `PROJECT_ID`: your project ID where the security profile exists.

  * `QUOTA_PROJECT_ID`: your quota project ID. Use this flag only for organization-level security profiles.




## What's next

  * [Security profile groups overview](https://docs.cloud.google.com/network-security-integration/docs/security-profile-groups-overview)
  * [Security profiles overview](https://docs.cloud.google.com/network-security-integration/docs/security-profiles-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
