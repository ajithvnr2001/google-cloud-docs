---
url: https://docs.cloud.google.com/chrome-enterprise-premium/docs/setting-up-intune/
title: Set up Chrome Enterprise Premium integration with Microsoft Intune \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:59:52.362959+00:00
---

# Set up Chrome Enterprise Premium integration with Microsoft Intune  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chrome-enterprise-premium/docs/setting-up-intune/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Chrome Enterprise Premium ](https://docs.cloud.google.com/chrome-enterprise-premium/docs)
  * [ Guides ](https://docs.cloud.google.com/chrome-enterprise-premium/docs/overview)



Send feedback 

#  Set up Chrome Enterprise Premium integration with Microsoft Intune Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to set up Chrome Enterprise Premium integration with Microsoft Intune. Setting up this integration involves setting up Intune, setting up Endpoint Verification, setting up Azure workload identity, and enabling Microsoft Intune on your organizational units. 

## Before you begin

  * To set up Intune for Chrome Enterprise Premium, do the following:

    * [Understand the supported configurations](https://docs.microsoft.com/en-us/mem/intune/fundamentals/supported-devices-browsers) and ensure that your environment satisfies the networking requirements.
    * [Sign in to your trial subscription or create a new Intune subscription](https://docs.microsoft.com/en-us/mem/intune/fundamentals/account-sign-up).
    * [Set DNS registration to connect your company's domain name with Intune](https://docs.microsoft.com/en-us/mem/intune/fundamentals/custom-domain-name-configure).
    * [Add users and groups, or connect Active Directory to sync with Intune](https://docs.microsoft.com/en-us/mem/intune/fundamentals/users-add).
    * [Give users permission to use Intune by assigning licenses](https://docs.microsoft.com/en-us/mem/intune/fundamentals/licenses-assign).

For more information, see [Set up Intune](https://docs.microsoft.com/en-us/mem/intune/fundamentals/setup-steps). 

  * Ensure that the devices in your organization run one of the following operating systems:

    * macOS version 10.11 or later
    * Microsoft® Windows 10 or later
  * [Set up Endpoint Verification for your organization](https://docs.cloud.google.com/endpoint-verification/docs/deploying-with-admin-console). 



## Connect to Intune

  1. [Find your Microsoft 365 tenant ID](https://docs.microsoft.com/en-us/onedrive/find-your-office-365-tenant-id). 
  2. [Register your application to obtain an application ID](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app). 
  3. From the Admin console Home page, go to **Devices**.

[Go to Devices](https://admin.google.com/ac/devices/list)
  4. In the navigation menu, click **Mobile & endpoints > Settings > Third-party integrations > Security and MDM partners > Manage**. 
  5. Look for **Microsoft Intune** and click **Open connection**. 
  6. In the **Connect to Intune** dialog, enter the tenant ID in the **Azure directory tenant id** field and application ID in the **Azure application id** field. 

![manual sync](https://docs.cloud.google.com/static/chrome-enterprise-premium/images/connect-intune1.png)![](https://docs.cloud.google.com/static/chrome-enterprise-premium/images/connect-intune1.png)
  7. Depending on whether you want to import only company-owned devices or import all devices, perform the appropriate action: 
     * To import only company-owned devices, click the **Import only company-owned devices** toggle. In the **Device properties to import** section, select the properties that must be stored in Chrome Enterprise Premium.
     * To import all devices, in the **Device properties to import** section, select the properties that must be stored in Chrome Enterprise Premium.

![manual sync](https://docs.cloud.google.com/static/chrome-enterprise-premium/images/connect-intune3.png)![](https://docs.cloud.google.com/static/chrome-enterprise-premium/images/connect-intune3.png)

The mandatory device properties such as `device identifier`, `last sync time`, `serial number`, and `wifi MAC address` are collected by default.

For more information about the device properties that Intune collects, see [Intune device properties](https://docs.microsoft.com/en-us/graph/api/resources/intune-devices-manageddevice?view=graph-rest-1.0#properties).

  8. Click **Continue**.
  9. Copy the **Service account ID**.   
![](https://docs.cloud.google.com/static/chrome-enterprise-premium/images/connect-intune2.png)![](https://docs.cloud.google.com/static/chrome-enterprise-premium/images/connect-intune2.png)
  10. Use the **Service account ID** to authorize Azure workload identity to collect data from the Intune devices: 
     1. [Configure your app to trust an external identity provider](https://docs.microsoft.com/en-us/azure/active-directory/develop/workload-identity-federation-create-trust?tabs=azure-portal#other-identity-providers-example). 

Specify the following values in the corresponding fields:

        * **Name** : Any name for the federated credential.
        * **Subject identifier** : The **Service account ID** that you copied.
        * **Issuer** : `https://accounts.google.com`.
     2. [Grant your app permissions](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-configure-app-access-web-apis#application-permission-to-microsoft-graph): 
        1. Search for `DeviceManagementManagedDevices.Read.All` and `DeviceManagementApps.Read.All` permissions and add these permissions to Microsoft Graph. When requesting the API permissions, select **Application permissions**. 

`DeviceManagementManagedDevices.Read.All` provides read access to all devices and their properties managed by Intune, and `DeviceManagementApps.Read.All` provides read access to the Intune audit logs for device deletion events. 

        2. [Grant admin consent to the permissions configured for your application](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-configure-app-access-web-apis#admin-consent-button).
  11. In the **Connect to Intune** dialog, click **Connect**.



The connection to Intune is set to open.

## Enable Intune for your organizational unit

To collect device information by using Intune, enable Intune for your organizational unit by doing the following:

  1. From the Admin console Home page, go to **Devices**.

[Go to Devices](https://admin.google.com/ac/devices/list)
  2. In the navigation menu, click **Mobile & endpoints > Settings > Third-party integrations > Security and MDM partners**.
  3. From the **Organizational units** pane, select your organization unit.
  4. Select the checkbox for **Microsoft Intune** , and click **Save**.

**Microsoft Intune** is now listed in the **Security and MDM partners** section. Depending on the size of your organization, it might take a few seconds to establish the connection between Endpoint Verification and Intune. After the connection is established, the devices might take a few minutes to an hour to report Intune data.

  
![](https://docs.cloud.google.com/static/chrome-enterprise-premium/images/intune-confirm.png)![](https://docs.cloud.google.com/static/chrome-enterprise-premium/images/intune-confirm.png)



## Verify Intune data on devices 

  1. From the Admin console Home page, go to **Devices**.

[Go to Devices](https://admin.google.com/u/1/ac/dm)
  2. Click **Endpoints**. 
  3. Select any device from your organizational unit for which Intune is enabled.

![Device page](https://docs.cloud.google.com/static/chrome-enterprise-premium/images/device-inventory.png)![](https://docs.cloud.google.com/static/chrome-enterprise-premium/images/device-inventory.png)
  4. Verify that the Microsoft Intune data is listed in the **Third-party services** section.

![Device page2](https://docs.cloud.google.com/static/chrome-enterprise-premium/images/intune-data1.png)![](https://docs.cloud.google.com/static/chrome-enterprise-premium/images/intune-data1.png)
  5. To see the complete details, expand the **Third-party services** section.

The following image shows details of the data collected by Intune:

![Device page2](https://docs.cloud.google.com/static/chrome-enterprise-premium/images/intune-data2.png)![](https://docs.cloud.google.com/static/chrome-enterprise-premium/images/intune-data2.png)



The compliance states reported by Intune are broadly categorized into the following compliance states:

Compliance states on the Google Admin console | Compliance states reported by Intune | `COMPLIANCE_STATE_UNSPECIFIED` | `unknown`, `configManager`  
---|---  
`COMPLIANT` | `compliant`  
`NON_COMPLIANT` | `noncompliant`, `conflict`, `error`, `inGracePeriod`  
  
## What's next

  * [Create and assign custom access levels](https://docs.cloud.google.com/chrome-enterprise-premium/docs/create-access-levels-intune)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
