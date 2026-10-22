---
url: https://docs.cloud.google.com/chrome-enterprise-premium/docs/setting-up-cs/
title: Set up Chrome Enterprise Premium and Falcon ZTA integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:02.730647+00:00
---

# Set up Chrome Enterprise Premium and Falcon ZTA integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chrome-enterprise-premium/docs/setting-up-cs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Chrome Enterprise Premium ](https://docs.cloud.google.com/chrome-enterprise-premium/docs)
  * [ Guides ](https://docs.cloud.google.com/chrome-enterprise-premium/docs/overview)



Send feedback 

#  Set up Chrome Enterprise Premium and Falcon ZTA integration Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to set up Chrome Enterprise Premium and CrowdStrike Falcon Zero Trust Assessment (Falcon ZTA) integration. Setting up this integration involves ensuring that your environment satisfies Falcon ZTA's requirements and enabling Falcon ZTA on your organizational units. 

## Before you begin

  * Ensure that your environment satisfies the following Falcon ZTA requirements:

    * CrowdStrike's Falcon sensor is installed on your devices.
    * The `data.zta` file is available in any of your test devices with some content at `%ProgramData%\CrowdStrike\ZeroTrustAssessment\data.zta` or `/Library/Application Support/Crowdstrike/ZeroTrustAssessment/data.zta`.
    * Your CrowdStrike instance (or CID) has access to an Insight subscription.
    * The CID is enabled in order to receive the `data.zta`file. To enable CID, file a support ticket to [support@crowdstrike.com](mailto:support@crowdstrike.com).
  * Ensure that the devices in your organization run one of the following operating systems:

    * macOS version 10.11 or later
    * Microsoft® Windows 10, Server 2016 or 2019, or later
  * [Set up Endpoint Verification for your organization](https://docs.cloud.google.com/endpoint-verification/docs/deploying-with-admin-console). 
  * [Install Endpoint Verification helper app on all the devices in your organization](https://docs.cloud.google.com/endpoint-verification/docs/deploying-with-admin-console#install-native-helper). 



## Connect to Falcon ZTA

  1. From the Admin console Home page, go to **Devices**.

[Go to Devices](https://admin.google.com/ac/devices/list)
  2. In the navigation menu, click **Mobile & endpoints > Settings > Third-party integrations > Security and MDM partners > Manage**. 
  3. Look for **CrowdStrike** and click **Open connection**. 

The **BeyondCorp Alliance partners** page shows that the connection is open.

  4. Close the **BeyondCorp Alliance partners** page.



## Enable Falcon ZTA for your organizational unit

To collect device information by using Falcon ZTA, enable Falcon ZTA for your organizational unit by doing the following:

  1. From the Admin console Home page, go to **Devices**.

[Go to Devices](https://admin.google.com/ac/devices/list)
  2. In the navigation menu, click **Mobile & endpoints > Settings > Third-party integrations > Security and MDM partners**.
  3. From the **Organizational units** pane, select your organization unit.
  4. Select the checkbox for **CrowdStrike** , and click **Save**.

**CrowdStrike** is now listed in the **Security and MDM partners** section. Depending on the size of your organization, it might take a few seconds to establish the connection between Endpoint Verification and Falcon ZTA. After the connection is established, the devices might take a few minutes to an hour to report Falcon ZTA data.

  5. To verify the connection status, do the following: 
     1. From the Chrome browser toolbar, click **Endpoint Verification** extension.
     2. Click **Sync now**.  
![](https://docs.cloud.google.com/static/chrome-enterprise-premium/images/sync.png)![](https://docs.cloud.google.com/static/chrome-enterprise-premium/images/sync.png)

A successful sync indicates that Endpoint Verification is communicating with CrowdStrike's Falcon sensor.




## Sync Falcon ZTA data on devices 

After you set up the Chrome Enterprise Premium and Falcon ZTA integration, Endpoint Verification automatically syncs and reports Falcon ZTA data every hour. However, the report is only updated if there is a more recent change. You can also sync the device data manually, whenever required.

To sync the device data manually, do the following:

  1. From the Chrome browser toolbar, click **Endpoint Verification** extension. 
  2. Click **Sync now**.  
![manual sync](https://docs.cloud.google.com/static/chrome-enterprise-premium/images/sync.png)![](https://docs.cloud.google.com/static/chrome-enterprise-premium/images/sync.png)



## Verify Falcon ZTA data on devices 

  1. From the Admin console Home page, go to **Devices**.

[Go to Devices](https://admin.google.com/u/1/ac/dm)
  2. Click **Endpoints**. 
  3. Select any device from your organizational unit for which Falcon ZTA is enabled.

![Device page](https://docs.cloud.google.com/static/chrome-enterprise-premium/images/device-inventory.png)![](https://docs.cloud.google.com/static/chrome-enterprise-premium/images/device-inventory.png)
  4. Verify that the CrowdStrike data is listed in the **Third-party services** section.

![Device page](https://docs.cloud.google.com/static/chrome-enterprise-premium/images/cs_verify1.png)![](https://docs.cloud.google.com/static/chrome-enterprise-premium/images/cs_verify1.png)
  5. To see the complete details, expand the **Third-party services** section.

The following image shows details of the data collected by Falcon ZTA:

![Device page2](https://docs.cloud.google.com/static/chrome-enterprise-premium/images/cs_verify2.png)![](https://docs.cloud.google.com/static/chrome-enterprise-premium/images/cs_verify2.png)

**Note:** If you experience issues when verifying the Falcon ZTA data, see [Troubleshoot Falcon ZTA data issues](https://docs.cloud.google.com/chrome-enterprise-premium/docs/troubleshooting-cs#cs-data-issues). 

## What's next

  * [Create and assign custom access levels](https://docs.cloud.google.com/chrome-enterprise-premium/docs/create-access-levels-cs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
