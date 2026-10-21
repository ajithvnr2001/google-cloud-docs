---
url: https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/register-deregister/
title: Register and deregister a CBSD \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:06:29.608010+00:00
---

# Register and deregister a CBSD  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/register-deregister/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  Register and deregister a CBSD Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to register, deregister, and re-register a Citizens Broadband Radio Service Device (CBSD) by using single-step or multistep registration.

In single-step registration, a [Certified Professional Installer (CPI)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cpi) provides all the device registration information to Spectrum Access System (SAS) from the CBSD. The CBSD uses registration requests to send all the required information.

Some CBSDs don't support single-step registration and must be registered by using multistep registration. For registration instructions specific to your CBSD, see your CBSD vendor documentation.

## Before you begin

You can register only Federal Communications Commission (FCC)-approved CBSDs in compliance with FCC Part 96 with SAS. Most CBSDs require a CPI to verify the CBSD's installation. For information about CBSD categories, see [Register a CBSD that needs CPI validation](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/overview#register-cbsd).

## Register your CBSD

Before a CBSD can transmit, it needs to register with SAS. For more information, see [Send a registration request to SAS](https://docs.cloud.google.com/spectrum-access-system/docs/portal#sending-cbsd-registration).

If your registration request is successful, SAS responds with a CBSD ID. The CBSD is then registered. If your registration request is rejected, SAS responds with an error message. The CBSD needs to correct the error and send another registration request. For more information, see [Register a CBSD that needs CPI validation](https://docs.cloud.google.com/spectrum-access-system/docs/portal#register-cbsd).

To register your CBSD, follow these steps:

  1. In the CBSDs list or CBSD details, click **CBSD Actions** , and then click **Register**.
  2. Check if your CBSD registered successfully.
  3. Make sure that your CBSD appears in the CBSD list.

**Important:** If you select **Grant** , it performs the **Register** action. If that succeeds, then it performs the **Grant** action.

## Deregister your CBSD

If a CBSD needs to be decommissioned or moved, the CBSD should first send a deregistration request to SAS. This indicates that the CBSD no longer wants to be listed in SAS with the parameters that it originally had. Contact your device vendor for documentation or instructions to deregister your CBSD. If a CBSD needs to transmit again, the CBSD can send a registration request with updated parameters.

The Google SAS Portal gives you a way to deregister your CBSD in the situation that a CBSD is no longer able to send a deregistration request. You can deregister a device by using the SAS Portal device panel or table_chart **Table view**.

To deregister the device by using the SAS Portal device panel, follow these steps:

  1. Go to the [SAS Portal](https://wirelessconnectivity.google.com/sas).
  2. Select the CBSD from the **Deployments** list.
  3. Select table_chart **Table view** or map **Map view** , and then click **Device panel**.
  4. On the right, click settings_input_antenna **Device** , and then click **Deregister CBSD**.



To deregister the device by using table_chart **Table view** , follow these steps:

  1. Go to the [SAS Portal](https://wirelessconnectivity.google.com/sas).
  2. Select the CBSD from the **Deployments** list.
  3. Click table_chart **Table view**.
  4. Right-click the row of the CBSD that you want to deregister.
  5. Select **Deregister CBSD**.



## Re-register your CBSD

If you are a CPI, you can update the SAS configuration by creating an inactive configuration. You need to sign the inactive configuration and instruct the CBSD to send a new registration request to SAS. The CBSD loses all current grants.

To re-register a CBSD, follow these steps:

  1. Go to the [SAS Portal](https://wirelessconnectivity.google.com/sas).
  2. Click **View deployments**.
  3. Optional: If you have access to multiple deployments, select a deployment from the **Deployments** list, and then click **Open**.
  4. On the left, click settings **Settings**.
  5. To select the CBSD, do the following: 
     * In map **Map view** , click the CBSD location marker.
     * In table_chart **Table view** , click the row of the CBSD.
  6. Click **Edit**.
  7. Update and review the CBSD configuration, and then do the following: 
     * If you are an Editor, click **Ready for CPI**.
     * If you are a CPI, click **Sign**.



After re-registering, the inactive configuration status changes to **Pending registration**. However, if the CBSD was already registered, the CBSD status doesn't change while the SAS is still using the previous (active) configuration. You can find the changed configuration in the **Pending changes** section.

When the CBSD re-registers with SAS, the inactive configuration becomes the active configuration. The **Pending changes** section disappears, and the CBSD information page updates with the new set of parameters used in the most recent registration.

## Register a CBSD by using vendor-specific registration parameters

You can register a CBSD directly from your device, but if you use a vendor (Baicells or Telrad) device, then you must add vendor-specific registration parameters to the device. For details, see the following sections.

### Baicells registration parameters

Use these instructions if you have a vendor device such as Baicells. To successfully configure your CBSD and upload the CPI certificate, make sure that you fill in the necessary fields in Baicells. All CBSD configurations are performed in the Baicells device user interface (UI) or by using the Baicells Operations Management Console (OMC).

**Important:** This process can vary by vendor. For additional help, contact your vendor.

#### Configure installation parameters directly in the CBSD UI

The CPI certificate is uploaded directly to the CBSD, which signs and encodes all installation parameters. The encoded CPI data is sent to the OMC and Domain Proxy (DP) service, which is then passed to SAS during the registration request. You don't need to add the CBSD in the SAS Portal. SAS settings are configured as follows:

  * For the CBSD UI, set **SAS Registration Type** to **Single-Step**.
  * For the OMC and DP service, select **Single-Step** , and then upload the CPI certificate.



#### Configure installation parameters by using the OMC and DP service

You can enter the installation parameters by using the OMC and DP service, and then the CPI signs them. You don't need to add the CBSD in the SAS Portal. SAS settings are configured as follows:

  * For the CBSD UI, set **SAS Registration Type** to **Single-Step**.
  * For the OMC and DP service, select **Single-Step** , and then upload CPI certificate.



### Telrad registration parameters

To configure installation parameters for the Telrad device, follow these steps:

  1. In **BreezeVIEW** , go to the CBSD list page.
  2. Click **Add CBSD**.
  3. Set the CBSD Device Type: 
     * For **eNB** , enter the Device ID and Cell ID (0, 1).
     * For **UE** , enter the IMSI ID.
  4. Add UE CBSD.
  5. Add a new CBSD.
  6. Use the BreezeVIEW CLI to sign the CPI.
  7. Configure the CBSD. After the new CBSD is added, the details page appears.
  8. Set the CBSD parameters, and then click **Save**.



## What's next

  * [Use deployments to organize CBSDs](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/organize)
  * [Manage CBSD configurations](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/manage-configurations)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
