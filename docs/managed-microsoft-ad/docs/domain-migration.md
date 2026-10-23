---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/domain-migration/
title: Existing domain migration overview \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:41:14.792116+00:00
---

# Existing domain migration overview  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/domain-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Existing domain migration overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Existing domain migration**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page explains how Google Cloud can help you migrate an existing Active Directory domain from on-premises to Managed Service for Microsoft Active Directory while preserving SID history.

## Overview

If you want to use Managed Microsoft AD instead of your on-premises Active Directory environment, you can use the following approaches:

  * Create a Managed Microsoft AD domain and establish a trust relationship with the on-premises domain. However, you must continue maintaining the on-premises Active Directory environment for this approach to work.

  * Create and set up a new Managed Microsoft AD domain that is similar to your on-premises domain. In this approach, you must create and configure all the users, groups, and other AD objects from your on-premises domain again on the new Managed Microsoft AD domain. This approach is time-consuming and requires substantial manual effort.

  * However, if you want to use the same users from your on-premises domain in Managed Microsoft AD, you can use Active Directory Migration Toolkit (ADMT) that helps you automate the migration of AD objects between two trusted domains. For more information about ADMT, see [Active Directory Migration Tool version 3.2](https://www.microsoft.com/en-us/download/details.aspx?id=56570)




## Why preserve SID history during migration

SID history helps you maintain user access to resources without having to modify resource permissions after migrating Active Directory domains. Active Directory migration using ADMT involves creating a trust relationship between on-premises and Managed Microsoft AD domains. After you create the trust, you need to move the AD objects such as groups, users, and servers, one after another in the required sequence. If you don't preserve SID history during this migration, the existing users can't access the resources using the migrated Active Directory domain.

When you create a user account, the system automatically assigns the user a [security identifier (SID)](https://docs.microsoft.com/windows-server/identity/ad-ds/manage/understand-security-identifiers), which is globally unique within the AD forest. After you migrate a domain, the system assigns a new SID to the same user in the new domain. However, the [`sIDHistory` attribute](https://docs.microsoft.com/windows/win32/adschema/a-sidhistory) stores the SID of a user from the previous domain as well. When the user logs on to the new domain and attempts to authenticate against an existing resource, Active Directory grants access to the resource by evaluating the user's permissions based on their current and previous SIDs available in the SID history.

However, you must import the relevant user properties and disable [SID filtering](https://docs.microsoft.com/previous-versions/windows/it-pro/windows-server-2003/cc772633\(v=ws.10\)) to preserve SID history while migrating your domain. We recommend that you disable SID filtering only until you complete the domain migration. After you migrate the domain, you must enable SID filtering because the groups, users, and resources reside in the same domain. For more information about enabling SID filtering, see [Disable permissions on the Managed Microsoft AD domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/manage-migrate-permissions#disable-permissions).

## Security implications

Before you enable the permissions for migrating your on-premises domain, read the following security implications:

  * Users can get the SID of a domain administrator or privileged account by looking at the access control lists (ACLs) on the resources in the trusting domain.
  * Users with domain administrator or equivalent rights can get the harvested or well-known SID values. They can attach these SID values to a user account's object in the trusted domain, specifically to its `sIDHistory` attribute. When this modified user account crosses an existing trust relationship from the trusted domain into the trusting domain, the user account will effectively have all the privileges of the compromised user account. These privileges can elevate all the way up to the domain administrator or enterprise administrator level.



After you complete the migration, to ensure security, you must [disable the permissions](https://docs.cloud.google.com/managed-microsoft-ad/docs/manage-migrate-permissions#disable-permissions) that are provided for migrating the existing domain.

## What's next

  * [Enable permissions for migrating an on-premises domain with SID history](https://docs.cloud.google.com/managed-microsoft-ad/docs/enable-migrate-permissions)
  * [Manage permissions required for migrating an on-premises domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/manage-migrate-permissions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
