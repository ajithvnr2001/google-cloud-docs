---
url: https://docs.cloud.google.com/spectrum-access-system/docs/roles-and-permissions/
title: Roles and permissions \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:50:11.738160+00:00
---

# Roles and permissions  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/roles-and-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  Roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

The Google Spectrum Access System (SAS) Portal API [user roles](https://docs.cloud.google.com/spectrum-access-system/docs/roles-and-permissions#user-roles) allow a user to make certain API calls based on their scope. These roles are assigned to the user's Google Account.

## User roles

The roles assigned to a user are [`role_admin`](https://docs.cloud.google.com/spectrum-access-system/docs/roles-and-permissions#admin) and [`role_cpi`](https://docs.cloud.google.com/spectrum-access-system/docs/guides/roles-and-permissions#cpi). Each user can be assigned to one or more roles.

### role_admin

The first user of a SAS customer's organization is the _administrator_. The administrator is automatically added during the sign-up process. The administrators can then add other users and assign them roles, including the administrator role.

The administrator role has full administrative permissions for all of the child [resources](https://docs.cloud.google.com/spectrum-access-system/docs/manage-resources) under the parent resource to which it has been granted access. The administrator sets up the organization's structure within the SAS Portal and manages user access.

### role_cpi

The [CPI](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms) role is for users who are _Certified Professional Installers_. To be assigned this role, users need to have an active CPI certification. To validate if a user has this certification, use the [`ValidateInstaller()` method](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/installer/validate#spectrum.sas.portal.v1alpha1.DeviceManager.ValidateInstaller).

Only users with a validated `role_cpi` role can use the [`SignDevice()` method](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/deployments.devices/signDevice) to submit the installation parameters of CBSDs that require CPI installation.

## Methods

The following table shows which roles can use each type of method.

Methods | Roles  
---|---  
[`GetCustomer()`](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers/get) |  `role_admin`  
`role_cpi`  
[`ListCustomers()`](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers/list) |  `role_admin`  
`role_cpi`  
[`CreateDevice()`](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.devices/create) |  `role_admin`  
`role_cpi`  
[`GetDevice()`](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.devices/get) |  `role_admin`  
`role_cpi`  
[`ListDevices()`](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.devices/list) |  `role_admin`  
`role_cpi`  
[`UpdateDevice()`](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.devices/patch) |  `role_admin`  
`role_cpi`  
[`CreateSignedDevice()`](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.devices/createSigned) |  `role_admin`  
`role_cpi`  
[`UpdateSignedDevice()`](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.devices/updateSigned) |  `role_admin`  
`role_cpi`  
[`GenerateSecret()`](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.devices/generateSecret) | `role_admin`  
`role_cpi`  
[`ValidateInstaller()`](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.devices/validate) | `role_admin`  
`role_cpi`  
[`SignDevice()`](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.devices/signDevice) | `role_cpi` (validated)  
  
## What's next

  * To get an overview of the SAS Portal API, see [Google SAS Portal API overview](https://docs.cloud.google.com/spectrum-access-system/docs/overview-api).
  * For information about each API, see [Customers API](https://docs.cloud.google.com/spectrum-access-system/docs/customers-api) and [Device Manager API](https://docs.cloud.google.com/spectrum-access-system/docs/device-manager-api).
  * For examples of how to use the API, see [API code samples](https://docs.cloud.google.com/spectrum-access-system/docs/samples).
  * For reference documentation, see [APIs and reference](https://docs.cloud.google.com/spectrum-access-system/docs/apis).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
