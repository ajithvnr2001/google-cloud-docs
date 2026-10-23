---
url: https://docs.cloud.google.com/spectrum-access-system/docs/portal/
title: Google SAS Portal overview \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:02.784301+00:00
---

# Google SAS Portal overview  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/portal/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  Google SAS Portal overview Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of the Google Spectrum Access System (SAS) Portal, including the tasks that you can perform in the SAS Portal.

The SAS Portal helps you to create and sign Citizens Broadband Radio Service Devices (CBSDs). You can monitor status, manage access of your network across users, and access CBSD support resources. To sign in to the SAS Portal, go to the [SAS Portal](https://wirelessconnectivity.google.com/sas/welcome).

## CBSD configurations

A [CBSD configuration](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cbsd-config) is a set of registration parameters for a [CBSD](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cbsd). There are two types of configurations:

  * **Active:** the configuration that is currently registered with SAS.

  * **Inactive:** the configuration that reflects any changes made to the active configuration. Inactive configurations are in one of the following states:

    * **Draft:** the registration parameters are incomplete. For example, mandatory fields are missing.
    * **Ready for CPI:** a [Certified Professional Installer (CPI)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cpi) needs to validate and sign the registration parameters.
    * **Pending registration:** a CPI has validated and signed the registration parameters. SAS is waiting for the CBSD to send a registration request.



## CBSD configuration changes in the SAS Portal

SAS always uses the values of the installation parameters sent by the CBSD in the registration request. This overrides any parameters submitted through the SAS Portal or the SAS Portal API. Use the SAS Portal or the SAS Portal API to modify device parameters and remove `cpiSignatureData` from the registration request in your CBSD or [Domain Proxy (DP)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#dp): `cpiSignatureData`.

**Important:** If the data source that the CBSD uses isn't complete, the registration is rejected. Data from the different sources are not merged.

The following table explains the installation parameters that are used in each case.

Parameters | CBSD configurations signed in the SAS Portal (web or API) | CBSD configurations not signed in the SAS Portal (web or API)  
---|---|---  
`cpiSignatureData` in the registration request | Use the information found in `cpiSignatureData` | Use the information found in `cpiSignatureData`  
No `cpiSignatureData` in the registration request | Use the information in the SAS Portal | Registration fails  
  
For more information about how to import and edit CBSD configurations, see [Manage CBSD configurations](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/manage-configurations).

## Register a CBSD that needs CPI validation

You can use the SAS Portal to register a CBSD that needs CPI validation by adding and signing a CBSD and then sending the registration request to SAS. For details, see the following sections.

### Add a CBSD

If you have Editor permissions, you can add a CBSD configuration from the map or table view in the SAS Portal. To add a CBSD configuration, follow these steps:

  1. Go to the [SAS Portal](https://wirelessconnectivity.google.com/sas/).
  2. On the left, click **SAS Portal**.
  3. To add a new site, do one of the following. 
     * To add a new site in map **Map view** : 
       1. Click add_location_alt **New site**.
       2. Click anywhere in the map to add latitude and longitude.
     * To add a new site in table_chart **Table view** , click **Create CBSD**.
  4. On the right, click location_on **Location**.
  5. For **Location** , enter or verify the latitude and longitude.
  6. To add a device to the site, click add**Add**.
  7. To enter the CBSD configuration, click settings_input_antenna **New CBSD**. 
     * If you have all the required fields for your CBSD type, click **Ready for CPI**.
     * If you don't have all the required information, click **Save** to save the configuration as a **Draft**.



### Sign a CBSD (CPI only)

If you're a verified CPI, you can validate the installation parameters of a CBSD when you sign the CBSD configuration in the SAS Portal.

To validate the installation parameters of a CBSD, follow these steps:

  1. Go to the [SAS Portal](https://wirelessconnectivity.google.com/sas/).
  2. Click **View deployments**.
  3. If you have access to multiple deployments, select a deployment from the **Deployments** list, and then click **Open**.
  4. On the right, click settings **Settings** : 
     * In map **Map view** , click compass_calibration **CBSD location marker**.
     * In table_chart **Table view** , click the row of the CBSD.
  5. Review the configuration to make sure that all the required fields are complete and correct.
  6. Click **Sign**. The CBSD configuration changes to **Pending registration**.



If any incorrect configuration is signed, you need to immediately fix the information and sign the new configuration. The new information does not take effect until the CBSD successfully re-registers. After re-registration, make sure that the **Active** configuration reflects the correct information.

**Important:** If you don't fix any incorrect information, you will lose your CPI certification.

You can [create new CBSD configurations in bulk](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/manage-configurations#start-import) when you import CBSD configurations. If you are a CPI, you can directly import signed CBSD configurations; otherwise, they appear in the SAS Portal in **Ready for CPI** status.

### Send a registration request to SAS

To send a registration request, see your CBSD documentation. Some CBSDs send a registration request when they're turned on. The registration request from the CBSD must _not include_ any installation parameters.

SAS uses the signed installation parameters of the CBSD configuration in the SAS Portal. The SAS Portal and CBSD registration request can provide other parameters, such as Effective Isotropic Radiated Power (EIRP) capability or antenna model. If this happens, SAS uses the values that the CBSD sent in the registration request.

## Analyze your network status

With the Device dashboard, you can analyze the state of your network and apply filters to show only the devices that you want to analyze.

To use the device dashboard, follow these steps:

  1. Go to the [SAS Portal](https://wirelessconnectivity.google.com/sas/).
  2. Optional: Click **View deployments**.
  3. Select the deployment, and then click **Open**.
  4. On the left, click dashboard **Dashboard view**.
  5. From the dashboard, you can do the following: 
     * Review your network details.
     * Apply a filter. To apply a filter, select **View devices**.
     * Export data. To export data as a CSV or PNG, click more_vert **Menu** on the right of the graph.



## Integrate with the SAS Portal API

To extend your network management system to manage the spectrum of your CBSDs connected to SAS, you can use the SAS Portal API. The SAS Portal API lets you use the same functionalities as the SAS Portal. [Learn how to use the SAS Portal API](https://docs.cloud.google.com/spectrum-access-system/docs/overview-api).

## What's next

  * Learn about [user roles](https://docs.cloud.google.com/spectrum-access-system/docs/users-sasportal).
  * Learn [how to verify your CPI identity](https://docs.cloud.google.com/spectrum-access-system/docs/validate-cpi-certification).
  * Learn about [Spectrum Access System](https://docs.cloud.google.com/spectrum-access-system/docs/overview).
  * Learn about [key SAS terms](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms).
  * [Troubleshoot SAS issues](https://docs.cloud.google.com/spectrum-access-system/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
