---
url: https://docs.cloud.google.com/firewall/docs/manage-security-profile-groups/
title: Manage security profile groups \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:31.288773+00:00
---

# Manage security profile groups  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/manage-security-profile-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Manage security profile groups Stay organized with collections  Save and categorize content based on your preferences. 

Security profile groups let you apply and control network security policies across your deployments. Each security profile group can contain up to one security profile of each of the following types:

  * `THREAT_PREVENTION`
  * `WILDFIRE_ANALYSIS` ([Preview](https://cloud.google.com/products#product-launch-stages))
  * `URL_FILTERING`



By grouping threat prevention and URL filtering profiles, you can enforce multiple security checks on network traffic through a single firewall policy rule, ensuring consistent policy enforcement and simplified management. This document helps network administrators and security engineers configure and manage organization-level and project-level security profile groups.

Before you begin, review the concepts in the [Security profile groups overview](https://docs.cloud.google.com/firewall/docs/about-security-profile-groups).

## Before you begin

  * You must [enable](https://console.cloud.google.com/apis/library/networksecurity.googleapis.com) the [Network Security API](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest) in your project.
  * Install the [gcloud CLI](https://docs.cloud.google.com/sdk/docs) if you want to run the `gcloud` command-line examples in this guide.

  * You need either a [threat prevention security profile](https://docs.cloud.google.com/firewall/docs/configure-security-profiles), an [Advanced malware sandbox security profile](https://docs.cloud.google.com/firewall/docs/configure-wildfire-security-profiles) ([Preview](https://cloud.google.com/products#product-launch-stages)), or a [URL filtering security profile](https://docs.cloud.google.com/firewall/docs/configure-urlf-security-profiles).




### Roles

To get the permissions that you need to view, update, or delete security profile groups, ask your administrator to grant you the necessary [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/firewall/docs/about-security-profile-groups#iam-roles) on your organization or project. For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

**Note:** To check the progress of the operations listed on this page, make sure that your user role has the following [Compute Network User role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`roles/compute.networkUser`) permissions: 

  * `networksecurity.operations.get`
  * `networksecurity.operations.list`



## List and view details of a security profile group

To list all security profile groups, use the Google Cloud console or the gcloud CLI.

You can view the following key details of a security profile group:

  * The description
  * The type
  * The name
  * The scope (organization-level or project-level)



#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization or project.

**Permissions**

  * `networksecurity.securityProfileGroups.list` to list security profile groups
  * `networksecurity.securityProfileGroups.get` to see details of a group



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`)
  * Compute Network User (`roles/compute.networkUser`)
  * Compute Network Viewer (`roles/compute.networkViewer`)
  * Security Profile Admin (`roles/networksecurity.securityProfileAdmin`) granted at the organization level for organization-level security profile groups, and at either the project level or the organization level for project-level security profile groups 



###  Console 

**Note:** If your Google Cloud project is in a data residency zone (DRZ) in the Kingdom of Saudi Arabia (KSA) or India, you can't view, list, create, update, or delete project-level security profiles or security profile groups by using the Google Cloud console. To manage project-level security profiles and security profile groups in KSA and India, use the gcloud CLI or the API. 

  1. In the Google Cloud console, go to the **Security profiles** page.

[Go to Security profiles](https://console.cloud.google.com/net-security/security-profiles/profiles/list)

  2. From the project picker, select your organization or the project.

  3. Select the **Security profile groups** tab. The tab shows a list of configured security profile groups.

  4. Select the security profile group to view its details.




###  gcloud 

To list security profile groups, use the [`gcloud network-security security-profile-groups list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/list):
    
    
    gcloud network-security security-profile-groups list \
        --organization ORGANIZATION_ID | --project PROJECT_ID \
        [--billing-project QUOTA_PROJECT_ID] \
        --location global
    

To view details of a security profile group, use the [`gcloud network-security security-profile-groups describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/describe):
    
    
    gcloud network-security security-profile-groups describe NAME \
        --organization ORGANIZATION_ID | --project PROJECT_ID \
        [--billing-project QUOTA_PROJECT_ID] \
        --location global
    

Replace the following:

  * `NAME`: the name of the security profile group.

If you don't use the [the unique URL identifier format](https://docs.cloud.google.com/firewall/docs/about-security-profile-groups#specifications) for the name, you must specify the organization or the project name, and the location.

  * `ORGANIZATION_ID`: the organization ID where the security profile group exists. Use this flag for an organization-level security profile group.

  * `PROJECT_ID`: the project ID where the security profile group exists. Use this flag for a project-level security profile group.

  * `QUOTA_PROJECT_ID`: the quota project ID. Use this flag only for organization-level security profile groups.




## Update a security profile group

To update a security profile group, use the Google Cloud console or the gcloud CLI.

You can update the following key details of a security profile group:

  * The billing project (available for organization-level security profile groups only)
  * Change or remove the security profile
  * The labels
  * The description



You can't change any of the following details:

  * The security profile group name
  * The security profile group zone
  * The security profile group organization or project



To change these details, delete the security profile group and create a new one.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization or project.

**Permissions**

  * `networksecurity.securityProfileGroups.update`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`)
  * Security Profile Admin (`roles/networksecurity.securityProfileAdmin`) granted at the organization level for organization-level security profile groups, and at either the project level or the organization level for project-level security profile groups 



###  Console 

**Note:** If your Google Cloud project is in a data residency zone (DRZ) in the Kingdom of Saudi Arabia (KSA) or India, you can't view, list, create, update, or delete project-level security profiles or security profile groups by using the Google Cloud console. To manage project-level security profiles and security profile groups in KSA and India, use the gcloud CLI or the API. 

  1. In the Google Cloud console, go to the **Security profiles** page.

[Go to Security profiles](https://console.cloud.google.com/net-security/security-profiles/profiles/list)

  2. From the project picker, select your organization or the project.

  3. Select the **Security profile groups** tab. The tab shows a list of configured security profile groups.

  4. Select the security profile group, and then click **Edit**.

  5. Update the required fields, and then click **Save**.




###  gcloud 

To update a security profile group, use the [`gcloud network-security security-profile-groups update` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/update):
    
    
    gcloud network-security security-profile-groups update NAME \
        --organization ORGANIZATION_ID | --project PROJECT_ID \
        --clear-threat-prevention-profile | --threat-prevention-profile THREAT_SECURITY_PROFILE_URL \
        --clear-url-filtering-profile | --url-filtering-profile URL_SECURITY_PROFILE_URL \
        [--billing-project QUOTA_PROJECT_ID] \
        --description DESCRIPTION \
        --location global
    

Replace the following:

  * `NAME`: the name of the security profile group.

If you don't use the [the unique URL identifier format](https://docs.cloud.google.com/firewall/docs/about-security-profile-groups#specifications) for the name, you must specify the organization or the project name, and the location.

  * `ORGANIZATION_ID`: the organization ID. Use this flag for an organization-level security profile group.

  * `PROJECT_ID`: the project ID. Use this flag for a project-level security profile group.

  * `THREAT_SECURITY_PROFILE_URL`: a unique URL identifier for a security profile of `THREAT_PREVENTION` type.

To remove a threat prevention security profile, use the `--clear-threat-prevention-profile` flag. To change a threat prevention security profile, use the `--threat-prevention-profile` flag.

  * `URL_SECURITY_PROFILE_URL`: a unique URL identifier for a security profile of `URL_FILTERING` type.

To remove a URL filtering security profile, use the `--clear-url-filtering-profile` flag. To change the URL filtering security profile, use the `--url-filtering-profile` flag.

  * `QUOTA_PROJECT_ID`: the quota project ID. Use this flag only for organization-level security profile groups.

  * `DESCRIPTION`: an optional description for the security profile group.




To update a security profile group for Advanced malware sandbox, use the [`gcloud beta network-security security-profile-groups update` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profile-groups/update) ([Preview](https://cloud.google.com/products#product-launch-stages)):
    
    
    gcloud beta network-security security-profile-groups update NAME \
        --organization ORGANIZATION_ID \
        --location LOCATION \
        --clear-threat-prevention-profile | --threat-prevention-profile THREAT_SECURITY_PROFILE_URL \
        --clear-wildfire-analysis-profile | --wildfire-analysis-profile WILDFIRE_SECURITY_PROFILE_URL \
        --clear-url-filtering-profile | --url-filtering-profile URL_SECURITY_PROFILE_URL \
        --billing-project QUOTA_PROJECT_ID
    

Replace `WILDFIRE_SECURITY_PROFILE_URL`with unique URL identifier for a security profile of `WILDFIRE_ANALYSIS` type.

Specify at most one of these flags:

  * `clear-wildfire-analysis-profile`: clear the wildfire analysis profile field.
  * `wildfire-analysis-profile`: update the wildfire analysis profile field with the unique URL identifier of the security profile of the `WILDFIRE_ANALYSIS` type.
  * `clear-url-filtering-profile`: clear the URL filtering profile field.
  * `url-filtering-profile`: update the URL filtering profile field with the unique URL identifier of the security profile of the `URL_FILTERING` type.



## Delete a security profile group

You can't delete a security profile group that is referenced by a firewall policy rule.

To delete a security profile group, use the Google Cloud console or the gcloud CLI.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization or project.

**Permissions**

  * `networksecurity.securityProfileGroups.delete`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`)
  * Security Profile Admin (`roles/networksecurity.securityProfileAdmin`) granted at the organization level for organization-level security profile groups, and at either the project level or the organization level for project-level security profile groups 



###  Console 

**Note:** If your Google Cloud project is in a data residency zone (DRZ) in the Kingdom of Saudi Arabia (KSA) or India, you can't view, list, create, update, or delete project-level security profiles or security profile groups by using the Google Cloud console. To manage project-level security profiles and security profile groups in KSA and India, use the gcloud CLI or the API. 

  1. In the Google Cloud console, go to the **Security profiles** page.

[Go to Security profiles](https://console.cloud.google.com/net-security/security-profiles/profiles/list)

  2. In the project selector menu, select your organization or the project.

  3. Select the **Security profile groups** tab. The tab shows a list of configured security profile groups.

  4. Select the security profile group, and then click **Delete**.

  5. Click **Delete** again to confirm.




###  gcloud 

To delete a security profile group, use the [`gcloud network-security security-profile-groups delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/delete):
    
    
    gcloud network-security security-profile-groups delete NAME \
        --organization ORGANIZATION_ID | --project PROJECT_ID \
        [--billing-project QUOTA_PROJECT_ID] \
        --location global
    

Replace the following:

  * `NAME`: the name of the security profile group.

If you don't use the [the unique URL identifier format](https://docs.cloud.google.com/firewall/docs/about-security-profile-groups#specifications) for the name, you must specify the organization or the project name, and the location.

  * `ORGANIZATION_ID`: the organization ID. Use this flag for an organization-level security profile group.

  * `PROJECT_ID`: the project ID. Use this flag for a project-level security profile group.

  * `QUOTA_PROJECT_ID`: the quota project ID. Use this flag only for organization-level security profile groups.




## What's next

  * [Create firewall endpoints and endpoint associations](https://docs.cloud.google.com/firewall/docs/configure-firewall-endpoints)
  * [Manage firewall endpoints and endpoint associations](https://docs.cloud.google.com/firewall/docs/manage-firewall-endpoints)
  * [Create security profile groups](https://docs.cloud.google.com/firewall/docs/configure-security-profile-groups)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
