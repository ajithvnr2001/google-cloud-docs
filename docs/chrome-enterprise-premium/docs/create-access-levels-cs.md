---
url: https://docs.cloud.google.com/chrome-enterprise-premium/docs/create-access-levels-cs/
title: Create and assign custom access levels using Falcon ZTA data \u00a0|\u00a0 Chrome Enterprise Premium \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:50.399075+00:00
---

# Create and assign custom access levels using Falcon ZTA data  |  Chrome Enterprise Premium  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chrome-enterprise-premium/docs/create-access-levels-cs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Chrome Enterprise Premium ](https://docs.cloud.google.com/chrome-enterprise-premium/docs)
  * [ Guides ](https://docs.cloud.google.com/chrome-enterprise-premium/docs/overview)



Send feedback 

#  Create and assign custom access levels using Falcon ZTA data Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to create device-based custom access levels using Falcon ZTA data and assign those access levels to your organizational resources.

## Before you begin

  * [Set up Chrome Enterprise Premium and Falcon ZTA integration](https://docs.cloud.google.com/chrome-enterprise-premium/docs/setting-up-cs). 
  * Upgrade to Chrome Enterprise Premium, which is the paid subscription of Chrome Enterprise Premium. To upgrade, [contact our sales team](https://go.chronicle.security/beyondcorp-enterprise-upgrade).
  * Ensure that you have one of the following Identity and Access Management roles: 
    * Access Context Manager Admin (`roles/accesscontextmanager.policyAdmin`)
    * Access Context Manager Editor (`roles/accesscontextmanager.policyEditor`)
  * Understand the objects and attributes that are used to build the [Common Expression Language (CEL)](https://opensource.google.com/projects/cel) expressions for custom access levels. For details, see [Custom access level specification](https://docs.cloud.google.com/access-context-manager/docs/custom-access-level-spec). 



## Create custom access levels

You can create access levels with one or more conditions. If you want the users' devices to satisfy multiple conditions (a logical AND of conditions), create an access level that contains all the required conditions.

To create a new custom access level using the data provided by Falcon ZTA, do the following:

  1. Go to the **Access Context Manager** page in the Google Cloud console.

[Go to Access Context Manager](https://console.cloud.google.com/security/access-level)
  2. If you are prompted, select your organization.
  3. On the **Access Context Manager** page, click **New**.
  4. In the **New Access Level** pane, enter the following: 
     1. In the **Access level title** field, enter a title for the access level. The title must be at most 50 characters, start with a letter, and can contain only numbers, letters, underscores, and spaces.
     2. In the **Create Conditions in** section, select **Advanced Mode**.
     3. In the **Conditions** section, enter the expressions for your custom access level. The condition must resolve to a single boolean value. 

To find the available CrowdStrike fields for your CEL expression, you can review the [Falcon ZTA data](https://docs.cloud.google.com/chrome-enterprise-premium/docs/setting-up-cs#verify-client-data) collected for your devices.

**Examples**

The following CEL expression creates a rule that allows access only from Falcon ZTA-managed devices with an OS assessment score higher than 50:
            
            device.vendors["CrowdStrike"].is_managed_device == true && device.vendors["CrowdStrike"].data["assessment.os"] > 50.0

The following CEL expression creates a rule that allows access only from devices that Falcon ZTA assessed in the last two days. The `iat` (issued at) field is provided as part of the Falcon ZTA's zero trust assessment. 
            
            request.time - timestamp(device.vendors["CrowdStrike"].data["iat"]) < duration("48h")
                  

**Note:** We recommend setting a value more than 90 minutes for `duration` because Chrome Enterprise Premium has an innate delay of 90 minutes for getting any new assessment by Falcon ZTA. 

The following CEL expression creates a rule that allows access only from devices whose Falcon ZTA's assessment is not expired. The `exp` field (expiry) field is provided as part of the Falcon ZTA's zero trust assessment.
            
            timestamp(device.vendors["CrowdStrike"].data["exp"]) - request.time > duration("0m")
                   

For examples and more information about Common Expression Language (CEL) support and custom access levels, see the [Custom access level specification](https://docs.cloud.google.com/access-context-manager/docs/custom-access-level-spec).

     4. Click **Save**.



## Assign custom access levels

You can assign custom access levels to control access to applications. These applications include [Google Workspace](https://workspace.google.com/) apps and the applications that are protected by [Identity-Aware Proxy](https://docs.cloud.google.com/iap/docs/concepts-overview) on Google Cloud (also known as IAP-secured resource). You can assign one or more access levels for the apps. If you select multiple access levels, users' devices only need to satisfy the conditions in **one** of the access levels to be granted access to the app.

**Note:** If you want user devices to satisfy conditions in more than one access level (a logical AND of access levels), create an access level with all the required conditions. 

### Assign custom access levels for Google Workspace applications

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



### Assign custom access levels for IAP-secured resources

To assign access levels for IAP-secured resources from the Google Cloud console, follow the instructions in [Apply an access level for IAP-secured resources](https://docs.cloud.google.com/chrome-enterprise-premium/docs/access-levels#applying_an_access_level). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
