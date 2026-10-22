---
url: https://docs.cloud.google.com/endpoint-verification/docs/assign-device-based-access-level/
title: Assign device-based access levels \u00a0|\u00a0 Endpoint Verification \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:47.913536+00:00
---

# Assign device-based access levels  |  Endpoint Verification  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoint-verification/docs/assign-device-based-access-level/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Endpoint Verification ](https://docs.cloud.google.com/endpoint-verification/docs)
  * [ Guides ](https://docs.cloud.google.com/endpoint-verification/docs/overview)



Send feedback 

#  Assign device-based access levels Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how administrators can assign the device-based access levels to control access to applications. These applications include [Google Workspace](https://workspace.google.com/) resources and the applications that are protected by [Identity-Aware Proxy](https://docs.cloud.google.com/iap/docs/concepts-overview) on Google Cloud (also known as IAP-secured resources).

## Before you begin

To complete the tasks on this page, you must have one of the following roles:

  * Access Context Manager Admin (`roles/accesscontextmanager.policyAdmin`)
  * Access Context Manager Editor (`roles/accesscontextmanager.policyEditor`)



## Assign device-based access levels on resources

The way you assign device-based access levels depends on whether you are using Google Workspace or Google Cloud resources:

###  Google Workspace 

As an administrator, you can assign one or more access levels for the apps by using Context-Aware Access from the Google Admin console. If you select multiple access levels, devices must satisfy the conditions only in **one** of the access levels to be granted access to the app.

**Note:** If you want user devices to satisfy conditions in more than one access level (a logical AND of access levels), create an access level with all the required conditions.

Assign access levels for Google Workspace applications from the Google Workspace Admin console:

  1. From the Admin console Home page, go to **Security > Context-Aware Access**.

[Go to Context-Aware Access](https://admin.google.com/u/1/ac/security/context-aware)
  2. Click **Assign access levels**.

You see a list of apps.

  3. In the **Organizational units** section, select your organizational unit or group.
  4. Select the app for which you want to assign an access level, and click **Assign**.

![access level assign](https://docs.cloud.google.com/static/chrome-enterprise-premium/images/assign-level1.png)

You see a list of all access levels. Access levels are a shared resource between Google Workspace, Cloud Identity, and Google Cloud so you might see access levels that you didn't create in the list.

  5. Select one or more access levels for the app.
  6. To apply the access levels to users on desktop and mobile apps (and on the browser), select **Apply to Google desktop and mobile apps**. This checkbox applies to built-in apps only.
  7. Click **Save**. The access level name displays in the assigned access levels list next to the app.



###  Google Cloud 

You assign an access level to an IAP-secured resource by updating its IAM policy. For instructions, see [Apply an access level for IAP-secured resources](https://docs.cloud.google.com/chrome-enterprise-premium/docs/access-levels#applying_an_access_level) in the Chrome Enterprise Premium documentation.

## What's next

  * [Manage access levels](https://docs.cloud.google.com/access-context-manager/docs/manage-access-levels)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
