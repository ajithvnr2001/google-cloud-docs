---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/manage-active-directory-policy/
title: Manage Active Directory policies \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:35.435874+00:00
---

# Manage Active Directory policies  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/manage-active-directory-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Manage Active Directory policies Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to edit or delete an Active Directory policy.

## About Active Directory policy settings

You can change Active Directory policy settings depending on the status of the policy.

After you create a volume with an Active Directory policy, the policy status changes to **Ready**. When the policy status is **Ready** , you can modify all settings except for the policy name and region.

When a volume uses an Active Directory policy, the policy status changes to **In use**. When the policy status is **In use** , you can't change the following settings until all volumes using the policy are deleted and the policy status transitions back to **Ready** :

  * Domain name

  * Organizational unit

  * `NetBIOS` name prefix




## Considerations

Changing the `NetBIOS` name prefix is disruptive to existing volumes which use the policy because it changes the hostname of the SMB Universal Naming Convention (UNC) path, which renders existing client mappings stale. Clients must then remap the volumes using the new UNC path.

## Edit an Active Directory policy

Use the following instructions to edit an Active Directory policy using the Google Cloud console or Google Cloud CLI.

### Console

Use the following instructions to update an Active Directory policy in the Google Cloud console:

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Select **Active Directory policies**.

  3. Click the name of the Active Directory policy you want to edit.

  4. Click **Edit**.

  5. Change the required fields.

  6. Click **Save**. The policy list page appears.

  7. Click the policy you edited. The policy details page appears.

  8. [Test the connection to the Active Directory service](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/test-ad-policy-connection).




### gcloud

In the Google Cloud CLI, edit an Active Directory policy:
    
    
     gcloud netapp active-directories update

For more information on additional optional flags, see [Google Cloud SDK documentation on Active Directory update](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/active-directories/update).

## Delete an Active Directory policy

You can only delete an Active Directory policy when the policy status is **Ready**. When an Active Directory policy attaches to a storage pool, the policy status transitions to **In use**. You need to delete all pools using the policy first, before it transitions back to **Ready**.

## What's next

[Connect to Managed Service for Microsoft Active Directory](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/connect-to-managed-service-for-microsoft-ad).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
