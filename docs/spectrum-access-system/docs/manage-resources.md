---
url: https://docs.cloud.google.com/spectrum-access-system/docs/manage-resources/
title: Manage user IDs and devices \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:51:17.525710+00:00
---

# Manage user IDs and devices  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/manage-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  Manage user IDs and devices Stay organized with collections  Save and categorize content based on your preferences. 

The Google Spectrum Access System (SAS) Portal API lets you create, view, update, and delete user IDs and devices within your Citizens Broadband Radio Service (CBRS) network.

The ability for each user to manage a resource depends on the user role assigned to the resource or parent resource. Permissions are inherited from the parent resource.

## User IDs

A user ID uniquely identifies the operator of a Citizens Broadband Radio Service Device (CBSD). SAS uses user IDs to assign a device to a [customer](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms). Every SAS customer has to provide at least one user ID during customer account setup. You can add additional user IDs later.

## Devices

The SAS Portal API enables multistep registration of CBSDs. For devices that need to be installed by a [Certified Professional Installer (CPI)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms), there are two ways to initiate the multistep registration process:

  * **Option 1.** Initiate the process with a CPI account. The user must be authenticated with the [`role_cpi` role](https://docs.cloud.google.com/spectrum-access-system/docs/roles-and-permissions#cpi). First, the user is verified by using the [`ValidateInstaller()` method](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/installer/validate#spectrum.sas.portal.v1alpha1.DeviceManager.ValidateInstaller), and then they use the [`SignDevice()` method](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/deployments.devices/signDevice) to send the CPI-validated configuration to SAS.

**Note:** The user only needs to validate their CPI identity once.
  * **Option 2.** Initiate the process with any account. Any user can use the [`CreateSigned()` method](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.devices/createSigned) to create an inactive device configuration that is ready for the CBSD to use. This method uses device parameters that are encoded with a CPI's private key.




Regardless of which option you use, this process creates an inactive configuration for the device in the SAS. Then, the CBSD sends a registration request to the SAS. If it is successful, the device status changes to **Registered**.

  * For CBSDs that do not need CPI validation, use the [`CreateDevice()` method](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rpc/spectrum.sas.portal.v1alpha1#spectrum.sas.portal.v1alpha1.DeviceManager.CreateDevice).
  * For single-step registration with CPI-encoded data, use the [SAS-CBSD API](https://winnf.memberclicks.net/assets/CBRS/WINNF-TS-0016.pdf) defined by WInnForum.



## What's next

  * To get an overview of the SAS Portal API, see [Google SAS Portal API overview](https://docs.cloud.google.com/spectrum-access-system/docs/overview-api).
  * For information about each API, see [Customers API](https://docs.cloud.google.com/spectrum-access-system/docs/customers-api) and [Device Manager API](https://docs.cloud.google.com/spectrum-access-system/docs/device-manager-api).
  * For examples of how to use the API, see [API code samples](https://docs.cloud.google.com/spectrum-access-system/docs/samples).
  * For reference documentation, see [APIs and reference](https://docs.cloud.google.com/spectrum-access-system/docs/apis).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
