---
url: https://docs.cloud.google.com/endpoint-verification/docs/setting-up-device-approvals/
title: Set up device approvals \u00a0|\u00a0 Endpoint Verification \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:46:21.192715+00:00
---

# Set up device approvals  |  Endpoint Verification  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoint-verification/docs/setting-up-device-approvals/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Endpoint Verification ](https://docs.cloud.google.com/endpoint-verification/docs)
  * [ Guides ](https://docs.cloud.google.com/endpoint-verification/docs/overview)



Send feedback 

#  Set up device approvals Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how administrators can set up device approvals to control the devices that users can use to access their organization's resources.

**Note:** This feature is available with one of the following Google Workspace editions: 

  * Frontline Starter, Frontline Standard, and Frontline Plus
  * Business Plus; Enterprise Standard and Enterprise Plus
  * Education Standard, Education Plus, and Endpoint Education Upgrade
  * Enterprise Essentials and Enterprise Essentials Plus
  * G Suite Basic and G Suite Business
  * Cloud Identity Premium



For more information, see [Compare Google Workspace editions](https://support.google.com/a/answer/6043385).

To use one of these editions, [contact our sales team](https://workspace.google.com/contact-form/?utm_source=gwsadminhelp&utm_medium=support&utm_campaign=6043385).

As an administrator, you can enforce administrator approval for device access, and approve or block devices from the Google Admin console. By default, all devices are approved when users log in to their devices by using their Google Accounts unless you set up administrator approvals for the devices.

**Note:** Devices that are registered by serial number are approved automatically, even if you set up device approvals.

## Enable administrator approval for device access

If you want to review devices that users use to access their organization's resources, you can enable the **Require admin approval** option. After you enable this option, when users add their corporate account to their device, they see a message that an administrator must review and approve the device.

To enable administrator approval for device access, do the following:

  1. In the Google Workspace Admin console, go to the **Devices** page.

[Go to Devices](https://admin.google.com/ac/devices/list)

  2. In the navigation menu, click **Mobile & endpoints > Settings > Universal settings > Security**.

  3. From the **Organizational Units** pane, select your organization unit. To apply the setting to everyone, select the top organizational unit.

  4. Click **Device approvals** and then select **Require admin approval**.

![](https://docs.cloud.google.com/static/endpoint-verification/images/approval.png)

  5. Enter an email address to get notifications when users enroll their devices. You can use a group email address that includes all administrators who can activate devices.

  6. Click **Save**.


**Note:** You can also enforce device approval settings by [creating an access level](https://docs.cloud.google.com/endpoint-verification/docs/creating-device-access-level) using the access level attribute [**Require admin approval**](https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes).

## Approve or block devices

Approving or blocking a device adds a device status tag, which you can use to create admin approval-based [access levels](https://docs.cloud.google.com/access-context-manager/docs/overview#access-levels). Approving or blocking a device doesn't affect the device's ability to access data.

When a device approval is pending or a device is blocked, the device can still sync data unless you create access levels to block access based on the device status tag.

To approve, block, or unblock devices, do the following:

  1. In the Google Workspace Admin console, go to the **Devices** page.

[Go to Devices](https://admin.google.com/ac/devices/list)

  2. Click **Endpoints**.
  3. Depending on whether you want to approve, block, or unblock devices, perform the appropriate action:

     * To allow devices to access data and to tag them as approved, select the devices, click **More** more_vert and select **Approve devices**.

     * To prevent devices from accessing data and to tag them as blocked, select the devices and click **Block Devices** block.

     * To unblock devices and to tag them as approved, select the devices and click **Unblock Devices** check_circle.




## What's next

  * [Enforce admin approval by using access levels](https://docs.cloud.google.com/endpoint-verification/docs/creating-device-access-level)
  * [Delete devices](https://docs.cloud.google.com/endpoint-verification/docs/delete-device)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
