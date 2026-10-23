---
url: https://docs.cloud.google.com/endpoint-verification/docs/deploying-with-admin-console/
title: Deploy Endpoint Verification \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:53.654143+00:00
---

# Deploy Endpoint Verification  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoint-verification/docs/deploying-with-admin-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Endpoint Verification ](https://docs.cloud.google.com/endpoint-verification/docs)
  * [ Guides ](https://docs.cloud.google.com/endpoint-verification/docs/overview)



Send feedback 

#  Deploy Endpoint Verification Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how administrators can deploy Endpoint Verification to their organization to assess and monitor the security posture of the devices in their organization. As an administrator, you deploy Endpoint Verification from the Google Admin console.

For more information about Endpoint Verification, see [Endpoint Verification overview](https://docs.cloud.google.com/endpoint-verification/docs/overview).

To deploy Endpoint Verification, you complete the following process:

  1. Turn on Endpoint Verification.
  2. Install Endpoint Verification on your devices.
  3. If required for your device type, install the Endpoint Verification helper app.



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



## Install the Endpoint Verification helper app

If you want to do any of the following tasks, install the Endpoint Verification helper app on your organizational unit:

  * [Set up Chrome Enterprise Premium and CrowdStrike Falcon Zero Trust Assessment (Falcon ZTA) integration](https://docs.cloud.google.com/chrome-enterprise-premium/docs/setting-up-cs).
  * [Set up certificate-based access for Google Cloud resources](https://docs.cloud.google.com/chrome-enterprise-premium/docs/securing-resources-with-certificate-based-access).
  * Collect device attributes from the devices that are using Chrome version M92 or earlier.



### Deploy the helper app package

Use the device management tool of your choice to deploy the following packages:

  * macOS: [`helper.dmg`](https://dl.google.com/dl/secureconnect/install/mac/EndpointVerification.dmg)
  * Windows: [`EndpointVerification.msi`](https://dl.google.com/dl/secureconnect/install/win/EndpointVerification_admin.msi)



You can use Jamf on Apple Mac devices and Active Directory on Microsoft Windows devices as shown in the following examples.

### Jamf

  1. [Download the `helper.dmg`](https://dl.google.com/dl/secureconnect/install/mac/EndpointVerification.dmg) file.
  2. Mount the `helper.dmg` file and extract `EndpointVerification.pkg`.
  3. To deploy `EndpointVerification.pkg`, follow the instructions in [Deploying Mac Packages](https://docs.jamf.com/jamf-now/documentation/Deploying_Mac_Packages.html). After the app appears in the **Apps** page, it's ready for deployment with Blueprint.
  4. To deploy the app to all devices, follow the instructions in [Deploying an App to All Devices in a Blueprint](https://docs.jamf.com/jamf-now/documentation/Deploying_an_App_to_All_Devices_in_a_Blueprint.html).



### Active Directory

  1. [Download the `EndpointVerification.msi`](https://dl.google.com/dl/secureconnect/install/win/EndpointVerification_admin.msi) file and use this file when creating a distribution point.
  2. Follow the instructions in [Use Group Policy to remotely install software](https://docs.microsoft.com/en-us/troubleshoot/windows-server/group-policy/use-group-policy-to-install-software).



## What's next

  * [Monitor device inventory](https://docs.cloud.google.com/endpoint-verification/docs/view-inventory)
  * [Create device-based access levels](https://docs.cloud.google.com/endpoint-verification/docs/creating-device-access-level)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
