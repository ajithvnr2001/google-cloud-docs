---
url: https://docs.cloud.google.com/spectrum-access-system/docs/users-sasportal/
title: Manage users \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:54:41.409268+00:00
---

# Manage users  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/users-sasportal/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  Manage users Stay organized with collections  Save and categorize content based on your preferences. 

This document provides information about how to use the Google Spectrum Access System (SAS) Portal to manage your users and operational configurations.

## User roles

One of the most important operations that you are responsible for as a network architect or planner is to manage users in SAS. To successfully do so, you must understand the various user roles supported by SAS. The following table explains these roles.

User roles | Permissions  
---|---  
Administrator | 

  * View, create, edit, and delete Citizens Broadband Radio Service Device (CBSD) configurations.
  * Save and mark CBSD configurations as ready for a Certified Professional Installer (CPI) to sign.
  * Add users and assign roles.

  
[Certified Professional Installer (CPI)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cpi) | 

  * View, create, edit, and delete CBSD configurations.
  * Validate and sign CBSD configurations.
  * Verify CPI identity.

  
Viewer | View CBSD configurations.  
Editor | View, create, edit, and delete CBSD configurations.  
**Note:** You can have both the Administrator role and the CPI role assigned to you at the same time.

If you have the Administrator role, you can add, remove, and assign user roles within your organization at the following level:

  * [Customer account](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#customer-acct)
  * [Node](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#node)
  * [Deployment](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#deployment)



The users added at the customer account or node level inherit the same permissions for the nodes and deployments below that level. The newly added user gets an email notification with a link to the SAS Portal.

To be able to perform any user- or configuration-related tasks, you must sign in to the SAS Portal.

## Sign in to the SAS Portal

  1. Go to the [SAS Portal](https://wirelessconnectivity.google.com/sas/).
  2. Sign in with the Google Account that is sent to you by [SAS Support](https://docs.cloud.google.com/spectrum-access-system/docs/getting-support).



## Prevent accidental changes

To prevent accidental changes to user management settings, you can lock the root settings. To lock the root settings, follow these steps:

  1. Go to the [SAS Portal](https://wirelessconnectivity.google.com/sas/).
  2. Optional: Click **View deployments**.
  3. Select the deployment, and then click **Open**.
  4. On the left, click _settings_ **Settings**.
  5. On the right, click _lock_open_ **Lock node**.



## Add a user

To add a user, follow these steps:

  1. Go to the [SAS Portal](https://wirelessconnectivity.google.com/sas/).
  2. Optional: Click **View deployments**.
  3. Select the deployment, and then click **Open**.
  4. On the left, click _settings_ **Settings**.
  5. Optional: To unlock the user management settings, click _lock_ **Unlock node**.
  6. In the **User Management** section, click _add_**Add**.
  7. For **Add user** , select the role and then enter the user's Google Account.
  8. Click **Share**.



## Remove a user

To remove a user, follow these steps:

  1. Go to the [SAS Portal](https://wirelessconnectivity.google.com/sas/welcome).
  2. Optional: Click **View deployments**.
  3. Select the deployment, and then click **Open**.
  4. On the left, click _settings_ **Settings**.
  5. Optional: To unlock the user management settings, click _lock_ **Unlock node**.
  6. In the **User Management** section, select the user that you want to remove, and then click _clear_**Remove**.



## What's next

  * Learn about [Spectrum Access System](https://docs.cloud.google.com/spectrum-access-system/docs/overview).
  * Learn about [key SAS terms](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms).
  * [Troubleshoot SAS issues](https://docs.cloud.google.com/spectrum-access-system/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
