---
url: https://docs.cloud.google.com/endpoint-verification/docs/view-inventory/
title: Monitor device inventory \u00a0|\u00a0 Endpoint Verification \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:00.981836+00:00
---

# Monitor device inventory  |  Endpoint Verification  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoint-verification/docs/view-inventory/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Endpoint Verification ](https://docs.cloud.google.com/endpoint-verification/docs)
  * [ Guides ](https://docs.cloud.google.com/endpoint-verification/docs/overview)



Send feedback 

#  Monitor device inventory Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how administrators can monitor device inventory from the Google Admin console.

## Before you begin

Log in to the **Google Admin console** by using your Google Workspace administrator account.

[Log in to Google Admin console](https://admin.google.com/ac/devices/list)

## View the device inventory

  1. In the Admin console, go to the **Devices** page. 

[Go to Devices](https://admin.google.com/u/1/ac/dm)

  2. Click **Endpoints**. 

The list of devices in your organization is displayed.

  3. To get more information about a specific device, click the device. The device information is displayed for that specific device. 

![](https://docs.cloud.google.com/static/endpoint-verification/images/device-list.png)![](https://docs.cloud.google.com/static/endpoint-verification/images/device-list.png)

  4. To find specific devices, enter a search term in the search bar and click **Search search**.

![](https://docs.cloud.google.com/static/endpoint-verification/images/search.png)![](https://docs.cloud.google.com/static/endpoint-verification/images/search.png)

  5. To get a report of activities on a device, click **More more_vert** and then select **View audit info**.

![](https://docs.cloud.google.com/static/endpoint-verification/images/view-audit.png)![](https://docs.cloud.google.com/static/endpoint-verification/images/view-audit.png)




## View the company-owned device inventory

  1. In the Google Workspace Admin console, go to the **Devices** page.

[Go to Devices](https://admin.google.com/ac/devices/list)

  2. In the navigation menu, click **Mobile & endpoints > Company owned inventory**.
  3. To find specific devices, enter a search term in the search bar and click **Search search**.

![](https://docs.cloud.google.com/static/endpoint-verification/images/search.png)![](https://docs.cloud.google.com/static/endpoint-verification/images/search.png)

  4. To get more information about a specific device, click the device.

![](https://docs.cloud.google.com/static/endpoint-verification/images/company-dev-info.png)![](https://docs.cloud.google.com/static/endpoint-verification/images/company-dev-info.png)

  5. To get a report of activities on a device, select the device and click **View audit info**.




## Find devices that meet specific criteria

You can find devices by various criteria, such as device model and last sync date. You can also combine criteria for detailed searches, such as finding devices of a certain model running a specific type of the operating system.

  1. In the Google Workspace Admin console, go to the **Devices** page.

[Go to Devices](https://admin.google.com/ac/devices/list)

  2. Click **Endpoints**.
  3. Click **add Add a filter**.

![](https://docs.cloud.google.com/static/endpoint-verification/images/filter.png)![](https://docs.cloud.google.com/static/endpoint-verification/images/filter.png)

  4. From the list of filters, select the required filters, and click **Apply**.




A list of devices that meet the specified criteria is displayed.

## Find devices without Endpoint Verification

You can find devices that do not have Endpoint Verification installed by retrieving a list of users who don't have Endpoint Verification installed on their devices. After retrieving the list, as an administrator, you can notify the users to install the Endpoint Verification extension.

  1. In the Google Workspace Admin console, go to the **Devices** page.

[Go to Devices](https://admin.google.com/ac/devices/list)

  2. Click **Endpoints**.

  3. Click **add Add a filter**.

![](https://docs.cloud.google.com/static/endpoint-verification/images/filter.png)![](https://docs.cloud.google.com/static/endpoint-verification/images/filter.png)

  4. Select **Exclude: Endpoint Verification**.

A list of users and their devices that do not have Endpoint Verification installed is displayed.

  5. Notify users to install the Endpoint Verification extension:

     1. Select the required employees, click **mail Email Users**. A new email window opens with the users that you selected in the **To** field.

     2. Compose your email and click **Send**.




## What's next

  * [Create device-based access levels](https://docs.cloud.google.com/endpoint-verification/docs/creating-device-access-level)
  * [Delete devices](https://docs.cloud.google.com/endpoint-verification/docs/delete-device)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
