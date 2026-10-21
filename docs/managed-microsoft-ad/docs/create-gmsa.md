---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/create-gmsa/
title: Create a group Managed Service Account \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:38:24.307352+00:00
---

# Create a group Managed Service Account  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/create-gmsa/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Create a group Managed Service Account Stay organized with collections  Save and categorize content based on your preferences. 

This topic shows you how to create a group Managed Service Account (gMSA) in Managed Service for Microsoft Active Directory. You should follow [these standard instructions](https://docs.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/manage-serviceaccounts#create-a-group-managed-service-account) for setting up the account and incorporate the following special considerations for Managed Microsoft AD.

## Do not create KDS root key

Usually, the first time you create a gMSA in a domain, you need to generate a Key Distribution Service (KDS) root key. Managed Microsoft AD generates a KDS root key for you when you create the domain, so you can skip that step from [the standard instructions](https://docs.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/manage-serviceaccounts#create-a-group-managed-service-account).

### View the KDS root key

Before you begin, be sure that the Active Directory Sites and Services tool is installed from [Remote Server Administration Tools (RSAT)](https://support.microsoft.com/en-us/help/2693643/remote-server-administration-tools-rsat-for-windows-operating-systems).

To view the KDS root key, complete the following steps:

  1. In Windows, launch the Active Directory Sites and Services tool. To launch this tool, you can open the **Run** command dialog box, and then enter `dssite.msc`.
  2. In the **Active Directory Sites and Services** tool, select the **View** tab.
  3. In the **View** menu, select **Show Services Node**.
  4. In the left pane, select **Services > Group Key Distribution Service > Master Root Keys**.
  5. The right pane shows a list of keys for your domain. Select a key to view its details.



Note that running the `Get-KdsRootKey` PowerShell cmdlet returns an empty response even though a valid KDS root key exists. You can only see the key when you run the `Get-KdsRootKey` cmdlet as the Domain Admin.

## Create account under `Managed Service Accounts` container

For a Managed Microsoft AD domain, new gMSAs should be created under the `Managed Service Accounts` container. By default, the `New-ADServiceAccount` cmdlet creates new gMSAs in this location. For more information, see [`New-ADServiceAccount`cmdlet](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-adserviceaccount?view=windowsserver2022-ps).

## Delegate administration of `Managed Service Accounts`

You can delegate the administration of the `Managed Service Accounts` container to a user by adding them to `Cloud Service Managed Service Account Administrators` group. For more information about the groups that Managed Microsoft AD creates for you, see [Groups](https://docs.cloud.google.com/managed-microsoft-ad/docs/objects#groups).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
