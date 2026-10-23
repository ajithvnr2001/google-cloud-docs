---
url: https://docs.cloud.google.com/firewall/docs/configure-security-profile-groups/
title: Create security profile groups \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:14.393580+00:00
---

# Create security profile groups  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/configure-security-profile-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Create security profile groups Stay organized with collections  Save and categorize content based on your preferences. 

Security profile groups are containers for security profiles. They let you bundle security profile types together for easier management and application to firewall rules. You can create these groups at either the organization or project level.

Each security profile group can contain up to one security profile of each of the following types:

  * `THREAT_PREVENTION`
  * `WILDFIRE_ANALYSIS` ([Preview](https://cloud.google.com/products#product-launch-stages))
  * `URL_FILTERING`



To apply consistent network security policies across your Google Cloud environment, you can use security profile groups to combine and apply threat prevention, Advanced malware sandbox (WildFire), and URL filtering profiles. By grouping these profiles, you can enforce multiple security checks such as threat prevention, Advanced malware sandbox, and URL filtering on network traffic through a single firewall policy rule, ensuring consistent policy enforcement and simplified management.

This document is intended for network administrators and security engineers who configure network security and firewall policies.

Before you begin, review the concepts in the [Security profile groups overview](https://docs.cloud.google.com/firewall/docs/about-security-profile-groups).

**Note:** To check the progress of the operations listed on this page, make sure that your user role has the following [Compute Network User role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`roles/compute.networkUser`) permissions: 

  * `networksecurity.operations.get`
  * `networksecurity.operations.list`



## Before you begin

  * You must [enable](https://console.cloud.google.com/apis/library/networksecurity.googleapis.com) the [Network Security API](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest) in your project.

  * To run the `gcloud` command-line examples in this guide, install the [gcloud CLI](https://docs.cloud.google.com/sdk/docs).

  * Create the security profiles that you need to add to the security profile group.




### Roles

To get the permissions that you need to create security profile groups, ask your administrator to grant you the necessary [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/firewall/docs/about-security-profile-groups#iam-roles) on your organization or project. For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Create a security profile group

Create a security profile group to bundle one or more security profiles into one resource for easier management and application to firewall rules.

Each security profile group can contain up to one security profile of each of the following types:

  * `THREAT_PREVENTION`
  * `WILDFIRE_ANALYSIS` ([Preview](https://cloud.google.com/products#product-launch-stages))
  * `URL_FILTERING`



#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization or project.

**Permissions**

  * `networksecurity.securityProfileGroups.create`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`)
  * Security Profile Admin (`roles/networksecurity.securityProfileAdmin`) granted at the organization level for organization-level security profile groups, and at either the project level or the organization level for project-level security profile groups 



###  Console 

**Note:** If your Google Cloud project is in a data residency zone (DRZ) in the Kingdom of Saudi Arabia (KSA) or India, you can't view, list, create, update, or delete project-level security profiles or security profile groups by using the Google Cloud console. To manage project-level security profiles and security profile groups in KSA and India, use the gcloud CLI or the API. 

  1. In the Google Cloud console, go to the **Security profiles** page.

[Go to Security profiles](https://console.cloud.google.com/net-security/security-profiles/profiles/list)

  2. Click **Open project picker** and select your organization.

  3. Select the **Security profile groups** tab.

  4. Click **Create profile group**.

  5. Enter a name in the **Name** field.

Avoid sensitive information, such as personally identifiable information (PII) or security data, in the security profile group name.
  6. Optional: Enter a description in the **Description** field.

  7. To create a security profile group for Cloud Next Generation Firewall Enterprise, in the **Purpose** section, select **Cloud NGFW Enterprise**.

  8. Add one or more security profiles to the group:

     * To add a threat prevention profile, select **Threat prevention profile**.
     * To add an Advanced malware sandbox profile, select **Advanced malware sandbox (WildFire) profile** ([Preview](https://cloud.google.com/products#product-launch-stages)).
     * To add a URL filtering profile, select the **URL filtering profile**.
  9. Click **Create**.




###  gcloud 

To create a security profile group, use the [`gcloud network-security security-profile-groups create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/create):
    
    
    gcloud network-security security-profile-groups create NAME \
        --organization ORGANIZATION_ID | --project PROJECT_ID \
        [--billing-project QUOTA_PROJECT_ID] \
        --threat-prevention-profile THREAT_SECURITY_PROFILE_URL \
        --url-filtering-profile URL_SECURITY_PROFILE_URL \
        --location global
    

Replace the following:

  * `NAME`: the name of the security profile group.

If you don't specify the name in [the unique URL identifier format](https://docs.cloud.google.com/firewall/docs/about-security-profile-groups#specifications), you must specify the organization or the project name, and the location.

Don't include sensitive information such as personally identifiable information or security data in the security profile group name.
  * `ORGANIZATION_ID`: the organization ID. Use this flag for an organization-level security profile group.

  * `PROJECT_ID`: the project ID. Use this flag for a project-level security profile group.

  * `QUOTA_PROJECT_ID`: the quota project ID. Use this flag only for organization-level security profile groups.

  * `THREAT_SECURITY_PROFILE_URL`: a unique URL identifier for a security profile of `THREAT_PREVENTION` type.

  * `URL_SECURITY_PROFILE_URL`: a unique URL identifier for a security profile of `URL_FILTERING` type.




To create a security profile group for Advanced malware sandbox, use the [`gcloud beta network-security security-profile-groups create` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profile-groups/create) ([Preview](https://cloud.google.com/products#product-launch-stages)):
    
    
    gcloud beta network-security security-profile-groups create NAME \
       --organization ORGANIZATION_ID | --project PROJECT_ID \
       --location global \
       --billing-project QUOTA_PROJECT_ID \
       --threat-prevention-profile THREAT_SECURITY_PROFILE_URL \
       --wildfire-analysis-profile WILDFIRE_SECURITY_PROFILE_URL \
       --url-filtering-profile URL_SECURITY_PROFILE_URL \
       --description DESCRIPTION
    

Replace the following:

  * `NAME`: the name of the security profile group.

Avoid sensitive information, such as PII or security data, in the security profile group name.
  * `ORGANIZATION_ID`: the organization ID. Use this flag for an organization-level security profile group.

  * `PROJECT_ID`: the project ID. Use this flag for a project-level security profile group.

  * `QUOTA_PROJECT_ID`: the quota project ID. Use this flag only for organization-level security profile groups.

  * `THREAT_SECURITY_PROFILE_URL`: a unique URL identifier for a security profile of `THREAT_PREVENTION` type.

  * `WILDFIRE_SECURITY_PROFILE_URL`: a unique URL identifier for a security profile of `WILDFIRE_ANALYSIS` type.

  * `URL_SECURITY_PROFILE_URL`: a unique URL identifier for a security profile of `URL_FILTERING` type.




## What's next

  * [Manage security profile groups](https://docs.cloud.google.com/firewall/docs/manage-security-profile-groups)
  * [Create firewall endpoints and endpoint associations](https://docs.cloud.google.com/firewall/docs/configure-firewall-endpoints)
  * [Manage firewall endpoints and endpoint associations](https://docs.cloud.google.com/firewall/docs/manage-firewall-endpoints)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
