---
url: https://docs.cloud.google.com/access-context-manager/docs/use-mobile-devices/
title: Use mobile devices with access levels \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:07.347771+00:00
---

# Use mobile devices with access levels  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/use-mobile-devices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/access-context-manager/docs/create-access-level)



Send feedback 

#  Use mobile devices with access levels Stay organized with collections  Save and categorize content based on your preferences. 

This page provides information about using mobile devices with access levels.

  * Overview

  * Limitations

  * Get started




## Overview

Access Context Manager supports using [Google basic mobile management](https://support.google.com/a/answer/1734200) and [advanced mobile management](https://support.google.com/a/answer/7396025) to create access levels that check for certain characteristics of mobile devices.

For iOS and Android devices, Access Context Manager can accept or reject requests based on the following:

  * Whether screen lock is enabled.

  * Whether storage on the device is encrypted.

**Note:** For iOS devices, encryption is enabled only if screen lock is also enabled.
  * Whether the device is owned by your enterprise.

  * Whether the device has been approved by an administrator.

  * Whether the OS version running on the device is compatible.




Because Access Context Manager relies on MDM, the [minimum device requirements](https://support.google.com/a/answer/7582673) for basic and advanced management apply.

## Limitations

This section describes the limitations of mobile device support in Access Context Manager.

### Request origin

Access levels that check mobile device attributes permit access only if the following applies:

  * The request originates from Safari or Google Chrome.

  * The request comes from a user account in your organization.




If a request from a mobile device doesn't meet the preceding criteria, Access Context Manager denies the request, even if it meets the other requirements of the access level.

### Enforcement delays

When you change settings for your managed mobile devices, [it can take time for those changes to propagate](https://support.google.com/a/answer/7514107). For example, if you modify your basic management settings to include a screen lock requirement, it can take up to 24 hours to propagate that change.

Although changes to access levels typically take effect within a few minutes, mobile device attributes might take longer to enforce while changes to your managed mobile device settings propagate.

## Get started

To start using access levels to check mobile device attributes, do the following:

  1. [Set up basic mobile management](https://support.google.com/a/answer/7400753) or [advanced mobile management](https://support.google.com/a/answer/7396025) for your organization.

This step requires access to the [Google Admin console](https://admin.google.com). To limit access to the console, you can grant [administrator privileges](https://support.google.com/a/answer/1219251) specifically for [mobile device management](https://support.google.com/a/answer/1219251#mobile).

  2. On your devices, [sign in to Chrome using a corporate account](https://support.google.com/chrome/answer/185277).

  3. For devices that should be permitted access to protected services, ensure requests originate from Safari or Chrome.

  4. [Create an access level](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level) that includes [device policy attributes](https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes#device-policy-attributes) for your organization's mobile devices.




## What's next

  * [Troubleshoot mobile devices with access levels](https://docs.cloud.google.com/access-context-manager/docs/troubleshooting#mobile-device-issues)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
