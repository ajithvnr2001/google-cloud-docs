---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.type
title: Package google.identity.accesscontextmanager.type \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:11.409618+00:00
---

# Package google.identity.accesscontextmanager.type  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.type

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  Package google.identity.accesscontextmanager.type Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[DeviceEncryptionStatus](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.type#google.identity.accesscontextmanager.type.DeviceEncryptionStatus)` (enum)
  * `[DeviceManagementLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.type#google.identity.accesscontextmanager.type.DeviceManagementLevel)` (enum)
  * `[OsType](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.type#google.identity.accesscontextmanager.type.OsType)` (enum)



## DeviceEncryptionStatus

The encryption state of the device.

Enums  
---  
`ENCRYPTION_UNSPECIFIED` | The encryption status of the device is not specified or not known.  
`ENCRYPTION_UNSUPPORTED` | The device does not support encryption.  
`UNENCRYPTED` | The device supports encryption, but is currently unencrypted.  
`ENCRYPTED` | The device is encrypted.  
  
## DeviceManagementLevel

The degree to which the device is managed by the Cloud organization.

Enums  
---  
`MANAGEMENT_UNSPECIFIED` | The device's management level is not specified or not known.  
`NONE` | The device is not managed.  
`BASIC` | Basic management is enabled, which is generally limited to monitoring and wiping the corporate account.  
`COMPLETE` | Complete device management. This includes more thorough monitoring and the ability to directly manage the device (such as remote wiping). This can be enabled through the Android Enterprise Platform.  
  
## OsType

The operating system type of the device.

Enums  
---  
`OS_UNSPECIFIED` | The operating system of the device is not specified or not known.  
`DESKTOP_MAC` | A desktop Mac operating system.  
`DESKTOP_WINDOWS` | A desktop Windows operating system.  
`DESKTOP_LINUX` | A desktop Linux operating system.  
`DESKTOP_CHROME_OS` | A desktop ChromeOS operating system.  
`ANDROID` | An Android operating system.  
`IOS` | An iOS operating system.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-08 UTC."],[],[]] 
