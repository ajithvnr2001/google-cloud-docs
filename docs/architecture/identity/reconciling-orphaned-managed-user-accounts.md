---
url: https://docs.cloud.google.com/architecture/identity/reconciling-orphaned-managed-user-accounts/
title: Reconcile orphaned managed user accounts \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:33:09.489289+00:00
---

# Reconcile orphaned managed user accounts  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/identity/reconciling-orphaned-managed-user-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Reconcile orphaned managed user accounts Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-07-11 UTC

This document describes how to identify and reconcile orphaned user accounts.

If you use an [external identity provider (IdP)](https://docs.cloud.google.com/architecture/identity/reference-architectures#using_an_external_idp), then the authoritative source for identities is external to [Cloud Identity](https://docs.cloud.google.com/identity) or [Google Workspace](https://gsuite.google.com/). Each identity in Cloud Identity or Google Workspace should therefore have a counterpart in the [external authoritative source](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#external_authoritative_source). It's possible that some of the identities in your Cloud Identity or Google Workspace account lack a counterpart in your external authoritative source—if so, these user accounts are considered _orphaned_. Orphaned accounts can occur under the following circumstances:

  * A Cloud Identity or Google Workspace administrator has manually created a user account that has a non-matching identity.
  * You have [migrated a consumer account](https://docs.cloud.google.com/architecture/identity/migrating-consumer-accounts#surfacing_unmanaged_user_accounts) to Cloud Identity or Google Workspace, but the account uses an identity that does not match any existing identity in the external source.



## Before you begin

To reconcile orphaned managed user accounts, you must meet the following prerequisites:

  * You have [identified a suitable onboarding plan](https://docs.cloud.google.com/architecture/identity/assessing-onboarding-plans) and have completed all prerequisites for consolidating your existing user accounts.
  * You have created a [Cloud Identity or Google Workspace account](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#cloud_identity_or_g_suite_account).



## Process

To reconcile orphaned user accounts, you must first identify which user accounts are orphaned. For each user account, you then have to decide how to best reconcile that account.

### Identify orphaned user accounts

To find orphaned user accounts, you must compare the identities of user accounts in Cloud Identity or Google Workspace against the identities that are recognized by your authoritative source.

To perform a comparison, you can use the export functionality of a Google Workspace or Cloud Identity account to obtain a list of your current user accounts:

  1. In the Admin Console, go to the [**Users**](https://admin.google.com/ac/users) page.
  2. Select **Download users**.
  3. Select **All user info columns and currently selected columns**.
  4. Click **Download**.

After a few minutes, depending on the number of user accounts you have, you see a notification that the user info CSV file is ready to be downloaded.

  5. Click **Download CSV** and save the file to your local disk.

**Note:** The CSV export might contain personally identifiable information (PII). Make sure that you select a storage location that is protected against unauthorized access.



If you use Active Directory or Microsoft Entra ID (formerly Azure Active Directory) as your authoritative source, follow these steps to compare identities:

### Active Directory

  1. Sign on to a workstation that has access to Active Directory.
  2. Open a PowerShell console.
  3. Set a variable to the location of your downloaded file:
         
         $GoogleUsersCsv="GOOGLE_PATH"

Replace `GOOGLE_PATH` with the path to the CSV file that you downloaded before.

  4. Determine the list of user accounts that lack a counterpart in Active Directory:
         
         $GoogleUsers = (Import-Csv -Path $GoogleUsersCsv -Header FirstName,LastName,Email | Select-Object -Skip 1)
         $LdapFilter = "(|{0})" -f (($GoogleUsers | Select-Object @{Name="Clause";Expression={"(userPrincipalName=$($_.Email))"}} | Select-Object -ExpandProperty Clause) -join "")
         
         $GoogleUsersWithMatch = Get-ADUser -LdapFilter $LdapFilter `
             | Select-Object -ExpandProperty UserPrincipalName
         
         $GoogleUsers | Where-Object {$_.Email -NotIn $GoogleUsersWithMatch}
         

The command compares the primary email address of user accounts in Cloud Identity or Google Workspace against the `userPrincipalName` attribute in Active Directory. If you are using a different mapping between Active Directory users and Cloud Identity or Google Workspace user accounts, you might need to adjust the command.

**Note:** If the CSV file contains a large number of users, the `Get-ADUser` command might take several minutes to execute and might cause significant load on the associated domain controller.

The output is similar to this:
         
         FirstName LastName     Email
         --------- --------     -----
         Alice     Admin        admin@example.org
         Olly      Orphaned     olly@example.org
         Matty     Mismatch     matty@wrongsubdomain.example.org
         

Each item listed in the output represents a user account in Cloud Identity or Google Workspace that lacks a counterpart in Active Directory.

An empty result indicates that you don't have any orphaned user accounts in Google Workspace or Cloud Identity.

  5. Delete the CSV file from your local disk.




### Entra ID

  1. In the [Azure Portal](https://portal.azure.com), go to **Azure Active Directory Users**.
  2. Click **Download users**.
  3. Enter a filename and click **Start**.

Wait until a **Click here to download** link appears.

Depending on the number of user accounts you have, it might take a few minutes for the operation to complete.

  4. Click **Click here to download** and save the file to your local disk.

**Note:** The CSV export might contain personally identifiable information (PII). Make sure that you select a storage location that is protected against unauthorized access.
  5. On a workstation that has PowerShell installed, open a PowerShell console.

  6. Set two environment variables:
         
         $GoogleUsersCsv="GOOGLE_PATH"
         $AzureUsersCsv="AZURE_PATH"
         

Replace `GOOGLE_PATH` and `AZURE_PATH` with the file paths to the CSV files that you previously downloaded.

  7. Determine the list of user accounts that lack a counterpart in Active Directory:
         
         $GoogleUsers = (Import-Csv -Path $GoogleUsersCsv
             -Header FirstName,LastName,Email | Select-Object -Skip 1)
         
         $AzureUsers = (Import-Csv -Path $AzureUsersCsv)
         
         $GoogleUsers | Where-Object {$_.Email -NotIn ($AzureUsers | Select-Object -ExpandProperty userPrincipalName)}
         

The command compares the primary email address of user accounts in Cloud Identity or Google Workspace against the `userPrincipalName` attribute in Entra ID. If you are using a different mapping between Entra ID users and the Cloud Identity or Google Workspace user accounts, you might need to adjust the command.

The output is similar to the following:
         
         FirstName  LastName    Email
         ---------  --------    -----
         Alice      Admin       admin@example.org
         Olly       Orphaned    olly@example.org
         Matty      Mismatch    matty@wrongsubdomain.example.org
         

Each item listed in the output represents a user account in Cloud Identity or Google Workspace that lacks a counterpart in Active Directory.

An empty result indicates that you don't have any orphaned user account in Google Workspace or Cloud Identity.

  8. Delete both CSV files from your local disk.




### Reconcile orphaned user accounts

To reconcile orphaned user accounts, you have to analyze each user account to determine why its identity lacks a counterpart in your authoritative source system.

If you think a user account is obsolete, check whether any configuration settings or data associated with the account are worth preserving:

  * To keep existing Google Drive data, [transfer the data](https://support.google.com/a/answer/1247799?hl=en) to a different user.
  * If you don't want to keep any existing configuration settings or data, delete the user account.
  * To temporarily retain the user account, suspend the user account and change its primary email address to an address that is unlikely to ever [cause a collision](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating#make_cloud_identity_or_g_suite_identities_a_subset_of_the_identities_in_your_external_idp). For example, rename `olly.obsolete@example.com` to `obsolete-2019-11-10-olly.obsolete@example.com`.



For each user account that is still valid, try to fix the primary email address so that it matches an identity in your authoritative source. This might require the following:

  * Changing the domain of the primary email address.
  * Swapping the primary email address and an alias address.
  * Fixing casing or spelling of the primary email address (for example, adding or removing dots).

**Note:** Changing the primary email address impacts the owner of the associated user account. Make sure that you notify the owner of the change so that they know which email address to use for subsequent sign-ins.

## Best practices

We recommend the following best practices when you are reconciling managed user accounts:

  * If you migrate consumer accounts to Cloud Identity or Google Workspace, repeat the reconciliation process at least once for every batch of user accounts that you migrate.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-07-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-07-11 UTC."],[],[]] 
