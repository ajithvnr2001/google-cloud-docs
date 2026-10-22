---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/test-ad-policy-connection/
title: Test the Active Directory policy connection \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:42.801514+00:00
---

# Test the Active Directory policy connection  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/test-ad-policy-connection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Test the Active Directory policy connection Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions for how to test your Active Directory policy connection.

## Before you begin

  * Make sure you have entered the parameters of your Active Directory policy correctly.

  * Make sure that you have associated an Active Directory policy with a storage pool of the Standard, Premium, Extreme, or Flex Unified service level. Testing the Active Directory policy connection is in Preview for the Flex Unified service level and isn't supported for the Flex File service level. For the Flex File service level, you can create an SMB volume instead. If connectivity fails, volume creation fails with an error message that describes the problem.

  * For Flex Unified ONTAP-mode, see [Display information about ONTAP SMB discovered servers](https://docs.netapp.com/us-en/ontap/smb-admin/display-discovered-servers-task.html) after you set up SMB access.




Use the following instructions to test if an Active Directory policy is correctly connected to the Active Directory service using the Google Cloud console. The test is optional but recommended for troubleshooting the errors in your Active Directory policy configuration such as the following:

  * DNS IP address is incorrect or not reachable

  * Domain controller lookup fails or site setting is incorrect

  * Domain controller can't be reached

  * Active Directory administrative user permissions are incorrect

  * Incorrect organizational unit for machine account




Make sure that the test only verifies the connection at the point of time the test is run. Many components, like the domain controllers or network setup, are outside of NetApp Volumes control and the service might lose connection if you make changes to your infrastructure, like retiring the specified DNS servers or changing networking or firewall settings.

## Test the Active Directory policy connection

Use the following instructions to test if an Active Directory policy is connected to the Active Directory service using the Google Cloud console.

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Select **Active Directory policies**.

  3. In the list of Active Directory policies, select the name of the Active Directory policy you want to test. The Active Directory details page appears.

  4. If the policy doesn't already have an associated storage pool, in the **Associated storage pools** section, click **Assign**.

  5. Click **Storage pool** drop-down list to select a storage pool. The **Associated storage pools** list appears.

  6. In the **Associated storage pools** list, click **Test Active Directory Connection** for the pool associated with the Active Directory policy you want to test. You can only test one policy at a time. A message appears indicating that the test is in progress.

Based on your test status, perform one of the following steps:

     * If the test fails, click **Edit Active Directory Policy**. Check your configuration, and perform the test again.

     * If the test succeeds, you will receive a success message. You should continue testing the connection to all other associated storage pools.




## What's next

[Manage Active Directory policies](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/manage-active-directory-policy).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
