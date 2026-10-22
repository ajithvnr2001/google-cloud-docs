---
url: https://docs.cloud.google.com/endpoint-verification/docs/collect-config-attributes/
title: Enable collection of configurable device attributes \u00a0|\u00a0 Endpoint Verification \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:48.259443+00:00
---

# Enable collection of configurable device attributes  |  Endpoint Verification  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoint-verification/docs/collect-config-attributes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Endpoint Verification ](https://docs.cloud.google.com/endpoint-verification/docs)
  * [ Guides ](https://docs.cloud.google.com/endpoint-verification/docs/overview)



Send feedback 

#  Enable collection of configurable device attributes Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how administrators can enable Endpoint Verification to collect granular device attributes called _configurable device attributes_ , such as metadata attributes of files, folders, and binaries; registry entries; and properties in a plist. Administrators can use these configurable device attributes to create access levels.

## Before you begin

  * [Deploy Endpoint Verification](https://docs.cloud.google.com/endpoint-verification/docs/deploying-with-admin-console).

  * [Install the Endpoint Verification helper app (version 2.11 or later)](https://docs.cloud.google.com/endpoint-verification/docs/deploying-with-admin-console#install-native-helper).




## Configure the Endpoint Verification settings

To enable Endpoint Verification to collect the [device configuration attributes](https://docs.cloud.google.com/endpoint-verification/docs/device-information#configuration-attributes), do the following:

  1. Log in to the **Google Admin console** by using your Google Workspace administrator account.

[Log in to Google Admin console](https://admin.google.com/ac/devices/list)

  2. In the navigation menu, click **Devices > Mobile & endpoints > Settings > Universal**.

  3. Expand the **Endpoint Verification configuration** tab.

  4. From the **Organizational Units** pane, select your organization unit.

**Note:** If the organization unit that you selected is a child of a top-level organizational unit, then the settings that you configure will override the settings that were inherited from the top-level organizational unit.
  5. Depending on the type of configurable device attributes you want Endpoint Verification to collect, configure the settings:

     * **To collect metadata attributes of a file, folder, or binary, do the following:**

       1. In the **File or folder configuration** section, click **Add configuration**.
       2. In the **Add configuration** dialog, enter the following details:

          * Name for the configuration.
          * Operating system of the devices.
          * Path to the file, folder, or binary.
**Note:** The size of a file or a binary must be less than or equal to 1 GB.
       3. If you entered the path for a binary, then select **Is executable**.

       4. Click **Add configuration**.

     * **To collect registry or plist configuration attributes, do the following:**

       1. In the **Registry or plist configurations** section, click **Add configuration**.
       2. In the **Add configuration** dialog, enter the following details:

          * Name for the configuration.
          * Operating system of the devices.
          * Path to the registry or plist file.
**Note:** The size of a plist file must be less than or equal to 512 MB.
          * Key (optional for Windows):

            * Windows: a subkey of the registry, for example: `IsClipboardSignalProducingFeatureAvailable`. If you don't enter a value, then the default value is taken.

            * macOS: keys in the plist file, which can be a number, string, or a boolean value. You can also provide nested keys by using `.` as the delimiter.

For example, if there is a dictionary B inside dictionary A and dictionary B contains a string or number with key `key1`, the final key would be `A.B.key1`. Arrays are supported in the following manner: `A.B.key[0]` or `A.B.key[1].C`. Only hard-coded indexes are supported.

       3. Click **Add configuration**.




## What's next

  * [Learn more about the configurable device attributes](https://docs.cloud.google.com/endpoint-verification/docs/device-information#configuration-attributes).
  * [Create device-based access levels](https://docs.cloud.google.com/endpoint-verification/docs/creating-device-access-level).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
