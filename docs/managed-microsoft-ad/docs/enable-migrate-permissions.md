---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/enable-migrate-permissions/
title: Enable permissions for migrating an on-premises domain with SID history \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:38:23.435024+00:00
---

# Enable permissions for migrating an on-premises domain with SID history  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/enable-migrate-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Enable permissions for migrating an on-premises domain with SID history Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Existing domain migration**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page explains how to enable the permissions required for migrating an existing Active Directory domain from on-premises to Managed Service for Microsoft Active Directory while preserving SID history.

## Before you begin

Before you begin, do the following:

  1. [Create a Managed Microsoft AD domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/create-domain).
  2. [Create a trust with the on-premises domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/create-trust).
  3. Make sure that you read the [Existing domain migration overview](https://docs.cloud.google.com/managed-microsoft-ad/docs/domain-migration) and understand these [security implications](https://docs.cloud.google.com/managed-microsoft-ad/docs/domain-migration#security-implications).
  4. Make sure that you have any one of the following Identity and Access Management ( IAM) user roles:

     * Google Cloud Managed Identities Domain Admin (`roles/managedidentities.domainAdmin`)
     * Google Cloud Managed Identities Admin (`roles/managedidentities.admin`)

For more information, see [Cloud Managed Identities roles](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities).




## Enable permissions to migrate a domain with SID history

You can grant the permissions required to migrate a domain along with SID history either to a global group or a single user. However, we recommend that you use a global group to grant the permissions required to migrate a domain along with SID history. Creating a global group makes it easier for you to delegate the permissions to all of the users involved in migrating your domain.

For both these approaches, make sure that the users are part of Managed Microsoft AD and have administrator privileges to the on-premises domain.

### Create a global group

To create a global group and add users, do the following:

  1. Identify users who need to perform the migration activities that include running ADMT.
  2. Ensure that these users are part of Managed Microsoft AD and have administrator privileges to the on-premises domain.
  3. [Create a global group](https://docs.microsoft.com/windows/win32/ad/creating-groups-in-a-domain) in Managed Microsoft AD. For example, `migrate_domain_admins`.

For more information about global group, see [Group Scope](https://docs.microsoft.com/windows/win32/ad/group-objects#group-scope).

  4. [Add the users to the global group](https://docs.microsoft.com/windows/win32/ad/adding-members-to-groups-in-a-domain).




### Enable permissions on the Managed Microsoft AD domain

When you enable the permissions required on Managed Microsoft AD using the gcloud CLI, Managed Microsoft AD creates a delegated group, `Cloud Service Migrate SID Administrators`, under the [`Cloud Service Objects` OU](https://docs.cloud.google.com/managed-microsoft-ad/docs/objects#organizational_units). This delegated group provides the permissions required to migrate an on-premises domain along with SID history.

Name | Type | Description  
---|---|---  
`Cloud Service Migrate SID Administrators` | Domain Local | Members can migrate SID history while migrating Active Directory objects from on-premises to Managed Microsoft AD using ADMT tool. This can include members from trusted domains.  
  
To enable the permissions required for migrating your on-premises domain with SID history, run the following gcloud CLI command:
    
    
    gcloud beta active-directory domains migration enable DOMAIN_NAME \
      --onprem-domains=SOURCE_DOMAIN_NAME \
      --disable-sid-filtering-domains=SID_FILTERING_DOMAIN_NAME
    

Replace the following:

  * DOMAIN_NAME: The name of your Managed Microsoft AD domain. For example, `my-domain.com`.
  * SOURCE_DOMAIN_NAME: The name of your on-premises domain which Managed Microsoft AD trusts. For example, `domain-one.com`.
  * SID_FILTERING_DOMAIN_NAME: The name of your on-premises domain for which you want to disable SID filtering. For example, `domain-one.com`.

**Note:** When you create a trust between on-premises and Managed Microsoft AD domains, it has SID filtering enabled by default. If you want to disable SID filtering until you migrate the domain, you can use the `--disable-sid-filtering-domains` flag.

### Delegate permissions

To delegate the ability to migrate an on-premises domain with SID history, add the global group or the single user to the following groups on Managed Microsoft AD:

  * `Cloud Service Administrators`
  * `Cloud Service Migrate SID Administrators`



Managed Microsoft AD delegates the permissions to users added to the global group or the single user, which in turn lets them migrate SID history from the on-premises domain using ADMT.

To add the global group or the user to the required Managed Microsoft AD groups and delegate the permissions, run the following commands in PowerShell:
    
    
    Add-ADGroupMember -Identity 'Cloud Service Administrators' \
      -Members GROUP_OR_USER
    
    Add-ADGroupMember -Identity 'Cloud Service Migrate SID Administrators' \
      -Members GROUP_OR_USER
    

Replace GROUP_OR_USER with the name of your global group or user. For example, `migrate_domain_admins`, `my_user`.

For more information, see [Add-ADGroupMember](https://docs.microsoft.com/en-us/powershell/module/activedirectory/add-adgroupmember?view=windowsserver2019-ps).

After you complete these steps, you can use ADMT and migrate your existing domain from on-premises to Managed Microsoft AD with SID history.

## What's next

  * [Disable permissions on the Managed Microsoft AD domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/manage-migrate-permissions#disable-permissions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
