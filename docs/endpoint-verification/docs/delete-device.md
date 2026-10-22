---
url: https://docs.cloud.google.com/endpoint-verification/docs/delete-device/
title: Delete devices \u00a0|\u00a0 Endpoint Verification \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:47.421554+00:00
---

# Delete devices  |  Endpoint Verification  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoint-verification/docs/delete-device/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Endpoint Verification ](https://docs.cloud.google.com/endpoint-verification/docs)
  * [ Guides ](https://docs.cloud.google.com/endpoint-verification/docs/overview)



Send feedback 

#  Delete devices Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how administrators can delete devices from the device inventory when they must temporarily stop syncing user-account data, such as installed extensions, bookmarks, and history to a device.

As an administrator, when you delete a device, the device no longer syncs user-account data, but no information is removed from it. The device is added back to the list after the next sync unless an access level blocks access. In this case, the device might require the administrator approval to sync data again.

**Note:** Deleting a device from the device inventory generally doesn't delete user-account data. To delete all data from a device, you can [wipe the account from the device or wipe the entire device](https://support.google.com/a/answer/173390).

To delete a device, do the following:

  1. In the Google Workspace Admin console, go to the **Devices** page.

[Go to Devices](https://admin.google.com/ac/devices/list)

  2. Click **Endpoints**.
  3. For the device you want to delete, click **More** more_vert and select **Delete device**.
  4. Optional: If you want to delete multiple devices, select all of the required devices, click **More** more_vert, and select **Delete devices**.



## What's next

  * [Approve devices](https://docs.cloud.google.com/endpoint-verification/docs/setting-up-device-approvals#approve-block-devices)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
