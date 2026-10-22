---
url: https://docs.cloud.google.com/endpoint-verification/docs/quickstart/
title: Set up Endpoint Verification on your devices \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:46.980375+00:00
---

# Set up Endpoint Verification on your devices  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoint-verification/docs/quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Endpoint Verification ](https://docs.cloud.google.com/endpoint-verification/docs)
  * [ Guides ](https://docs.cloud.google.com/endpoint-verification/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up Endpoint Verification on your devices

This quickstart document guides you how to set up Endpoint Verification on your devices to understand the security posture of your devices.

## Before you begin

  1. You must have a Google Workspace administrator account with the [Service Settings](https://support.google.com/a/answer/1219251) privilege.
  2. Log in to the **Google Admin console** by using your Google Workspace administrator account.

[Log in to Google Admin console](https://admin.google.com/ac/devices/list)

  3. You must have an organization unit with at least one device running one of the following operating systems:

     * ChromeOS
     * Apple® Mac® OS X® El Capitan (10.11) or later
     * Microsoft® Windows® 10 and 11
     * Linux® Debian® and Ubuntu®
  4. You must use Chrome 110 or later. While you can install Endpoint Verification on any Chromium-based browser, it's supported only on Chrome browser. 



## Turn on Endpoint Verification 

To collect information about the devices accessing the resources of your organization, Endpoint Verification must be turned on for your organizational unit. By default, Endpoint Verification is turned on.

To confirm that Endpoint Verification is turned on, do the following:

  1. In the Google Workspace Admin console, go to the **Devices** page.

[Go to Devices](https://admin.google.com/ac/devices/list)

  2. In the navigation menu, click **Mobile & endpoints > Settings > Universal**.
  3. In the **Universal settings** pane, click **Data access**.
  4. In the **Data access** pane, click **Device signals**.
  5. Ensure that the **Collect device signals using endpoint verification** checkbox is selected.
  6. To save the settings, click **Save** , otherwise, click **Cancel**.



## Install Endpoint Verification on your devices

  1. In the Google Workspace Admin console, go to the **Devices** page.

[Go to Devices](https://admin.google.com/ac/devices/list)

  2. In the navigation menu, click **Chrome > Apps & extensions > Users & browsers**.
  3. From the **Organizational Units** pane, select your organization unit for which you want to install the Endpoint Verification extension.
  4. Hold the pointer over **Add** , and click **Add from Chrome Web Store**.

![](https://docs.cloud.google.com/static/endpoint-verification/images/add-ev.png)![](https://docs.cloud.google.com/static/endpoint-verification/images/add-ev.png)
  5. In the **Search the store** field, enter **Endpoint Verification**.
  6. Click **Endpoint Verification** and then click **Select**.
  7. In the **Endpoint Verification** dialog, ensure that **Allow access to keys** and **Allow enterprise challenge** are enabled. 
     * **Allow access to keys** : allows the Endpoint Verification extension to access client certificates and keys on ChromeOS.
     * **Allow enterprise challenge** : allows the Endpoint Verification extension to use the Verified Access feature on ChromeOS. For more information, see [Chrome Verified Access Overview](https://developers.google.com/chrome/verified-access/overview).
![](https://docs.cloud.google.com/static/endpoint-verification/images/ev-settings.png)![](https://docs.cloud.google.com/static/endpoint-verification/images/ev-settings.png)
  8. Click the **Installation policy** drop-down for Endpoint Verification, and select **Force install**.

![](https://docs.cloud.google.com/static/endpoint-verification/images/ev-install.png)![](https://docs.cloud.google.com/static/endpoint-verification/images/ev-install.png)
  9. Click **Save**.



## View your devices information

  1. In the Admin console, go to the **Devices** page. 

[Go to Devices](https://admin.google.com/u/1/ac/dm)

  2. Click **Endpoints**. 

The list of devices in your organization is displayed.

  3. To get more information about a specific device, click the device. The device information is displayed for that specific device. 

The device details show that the device is managed by Endpoint Verification.

![](https://docs.cloud.google.com/static/endpoint-verification/images/ev-details.png)![](https://docs.cloud.google.com/static/endpoint-verification/images/ev-details.png)



## Clean up

If you don't want Endpoint Verification to manage your devices, do the following:

  1. In the Google Workspace Admin console, go to the **Devices** page.

[Go to Devices](https://admin.google.com/ac/devices/list)

  2. In the navigation menu, click **Mobile & endpoints > Settings > Universal**.
  3. In the **Universal settings** pane, click **Data access**.
  4. In the **Data access** pane, click **Device signals**.
  5. Clear the **Monitor which devices access organization data** checkbox.
  6. Click **Save**.



## What's next

  * [Endpoint Verification overview](https://docs.cloud.google.com/endpoint-verification/docs/overview)

  * [Device attributes collected by Endpoint Verification](https://docs.cloud.google.com/endpoint-verification/docs/device-information)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
