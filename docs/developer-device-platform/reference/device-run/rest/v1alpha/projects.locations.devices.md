---
url: https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices
title: REST Resource: projects.locations.devices \u00a0|\u00a0 Developer Device Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:55.803545+00:00
---

# REST Resource: projects.locations.devices  |  Developer Device Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Device Platform ](https://docs.cloud.google.com/developer-device-platform)
  * [ API Reference ](https://docs.cloud.google.com/developer-device-platform/apis)



Send feedback 

#  REST Resource: projects.locations.devices Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Device
    * JSON representation
  * AndroidDeviceDetails
    * JSON representation
  * IosDeviceDetails
  * Platform
  * HardwareType
  * FormFactor
  * ScreenMetrics
    * JSON representation
  * SupportedProduct
    * JSON representation
  * AutomationSupport
  * DeviceStreamingSupport
    * JSON representation
  * DeviceAvailability
    * JSON representation
  * Capacity
  * Availability
  * LabInfo
    * JSON representation
  * AccessDeniedReason
  * Methods



## Resource: Device

A single routable device configuration in the catalog.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "manufacturer": string,
      "modelCode": string,
      "platform": enum ([Platform](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices#Platform)),
      "hardwareType": enum ([HardwareType](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices#HardwareType)),
      "formFactor": enum ([FormFactor](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices#FormFactor)),
      "osVersion": string,
      "primaryScreen": {
        object ([ScreenMetrics](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices#ScreenMetrics))
      },
      "supportedProducts": [
        {
          object ([SupportedProduct](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices#SupportedProduct))
        }
      ],
      "lifecycle": {
        object ([Lifecycle](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/Lifecycle))
      },
      "labels": {
        string: string,
        ...
      },
      "availability": {
        object ([DeviceAvailability](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices#DeviceAvailability))
      },
      "labInfo": {
        object ([LabInfo](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices#LabInfo))
      },
      "accessDeniedReasons": [
        enum ([AccessDeniedReason](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices#AccessDeniedReason))
      ],
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "androidDetails": {
        object ([AndroidDeviceDetails](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices#AndroidDeviceDetails))
      },
      "iosDetails": {
        object ([IosDeviceDetails](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices#IosDeviceDetails))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Identifier. Identifies the device resource. Format: `projects/{project}/locations/{location}/devices/{device}`. The {device} segment is an opaque, stable string. Clients must not parse it to derive or assume device-specific details.  
`displayName` |  `string` Output only. Provides a human-readable display name, ex. "Pixel 5".  
`manufacturer` |  `string` Output only. Specifies the hardware manufacturer of the device.  
`modelCode` |  `string` Output only. Provides a human-readable model identifier for this device, independent of OS version. May be empty.Platform-dependent: * Android physical: hardware codename (android.os.Build.DEVICE), ex. "shiba". * Android virtual: AVD model identifier, ex. "MediumPhone.arm". * iOS: model identifier, ex. "iphone14pro".  
`platform` |  `enum (`[Platform](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices#Platform)`)` Output only. Specifies the platform of the device.  
`hardwareType` |  `enum (`[HardwareType](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices#HardwareType)`)` Output only. Indicates whether the device is physical or virtual.  
`formFactor` |  `enum (`[FormFactor](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices#FormFactor)`)` Output only. Specifies the form factor of the device.  
`osVersion` |  `string` Output only. Specifies the OS version, ex. "30" (Android API level) or "17.4" (iOS).  
`primaryScreen` |  `object (`[ScreenMetrics](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices#ScreenMetrics)`)` Output only. Measurements of the primary device screen. Informational only. Unset for devices without a screen (ex. some wearables).  
`supportedProducts[]` |  `object (`[SupportedProduct](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices#SupportedProduct)`)` Output only. Products/Services supported by this device.  
`lifecycle` |  `object (`[Lifecycle](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/Lifecycle)`)` Output only. The device lifecycle (maturity stage and removal date).  
`labels` |  `map (key: string, value: string)` Output only. Additional information. Informational only. May change over the lifecycle of a device.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`availability` |  `object (`[DeviceAvailability](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices#DeviceAvailability)`)` Output only. Reports the current fleet availability for this device configuration.  
`labInfo` |  `object (`[LabInfo](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices#LabInfo)`)` Output only. The lab hosting this device.  
`accessDeniedReasons[]` |  `enum (`[AccessDeniedReason](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices#AccessDeniedReason)`)` Output only. Reasons for access denial. This model is accessible/usable if this list is empty, otherwise the model is viewable only.  
Contains platform-specific attributes. The field that is set matches `platform`. It is type-safe, so an iOS device can never carry Android-only fields. Filterable via dot-path, for example `android_details.build_type = "userdebug"`. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`androidDetails` |  `object (`[AndroidDeviceDetails](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices#AndroidDeviceDetails)`)` Output only. Contains Android-specific attributes (set when platform == ANDROID).  
`iosDetails` |  `object (`[IosDeviceDetails](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices#IosDeviceDetails)`)` Output only. Contains iOS-specific attributes (set when platform == IOS).  
End of mutually exclusive fields.  
  
## AndroidDeviceDetails

Android-specific device attributes.

JSON representation  
---  
      
    
    {
      "buildType": string,
      "supportedAbis": [
        string
      ]
    }  
  
Fields  
---  
`buildType` |  `string` Output only. Mirrors the AOSP `ro.build.type` property, ex. "user", "userdebug", "eng". Empty if unknown.  
`supportedAbis[]` |  `string` Output only. Lists ABIs supported by the device (android.os.Build.SUPPORTED_ABIS), most preferred first, ex. "arm64-v8a".  
  
## IosDeviceDetails

This type has no fields.

iOS-specific device attributes. Reserved for future iOS-only fields.

## Platform

The platform of a device.

New values may be added in the future.

Enums  
---  
`PLATFORM_UNSPECIFIED` | Platform not specified.  
`ANDROID` | Android.  
`IOS` | iOS.  
  
## HardwareType

Whether a device is physical or virtual.

New values may be added in the future.

Enums  
---  
`HARDWARE_TYPE_UNSPECIFIED` | Hardware type not specified.  
`PHYSICAL` | Physical hardware device.  
`VIRTUAL` | Virtual device (emulator / simulator).  
  
## FormFactor

The form factor of a device.

New values may be added in the future.

Enums  
---  
`FORM_FACTOR_UNSPECIFIED` | Form factor not specified.  
`PHONE` | Phone.  
`TABLET` | Tablet.  
`WEARABLE` | Wearable (ex. watch).  
`TV` | TV.  
  
## ScreenMetrics

Screen measurements of a device.

JSON representation  
---  
      
    
    {
      "densityDpi": integer,
      "widthPx": integer,
      "heightPx": integer
    }  
  
Fields  
---  
`densityDpi` |  `integer` Output only. Pixel density in dots per inch (dpi).  
`widthPx` |  `integer` Output only. Width in pixels.  
`heightPx` |  `integer` Output only. Height in pixels.  
  
## SupportedProduct

Declares that a device supports a given Device Cloud product, with optional per-product metadata. Discriminated by which product-specific message is set; adding a new product = new oneof arm + new per-product message.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "automation": {
        object ([AutomationSupport](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices#AutomationSupport))
      },
      "deviceStreaming": {
        object ([DeviceStreamingSupport](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices#DeviceStreamingSupport))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Encapsulates the supported product and its per-product metadata. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`automation` |  `object (`[AutomationSupport](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices#AutomationSupport)`)` Output only. Represents Automation, which is DeviceRun-backed automated test execution.  
`deviceStreaming` |  `object (`[DeviceStreamingSupport](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices#DeviceStreamingSupport)`)` Output only. Represents DeviceStreaming, which is interactive remote device streaming.  
End of mutually exclusive fields.  
  
## AutomationSupport

This type has no fields.

Per-product metadata for the Automation (DeviceRun) product.

## DeviceStreamingSupport

Per-product metadata for the DeviceStreaming product.

JSON representation  
---  
      
    
    {
      "minimumAndroidStudioVersion": string
    }  
  
Fields  
---  
`minimumAndroidStudioVersion` |  `string` Output only. Specifies the minimum Android Studio version that supports this device. Optional; only set when the device is known to work only at or above a certain Android Studio version. Expected format "major.minor.micro.patch", ex. "5921.22.2211.8881706".  
  
## DeviceAvailability

Fleet availability for a device configuration.

JSON representation  
---  
      
    
    {
      "capacity": enum ([Capacity](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices#Capacity)),
      "available": enum ([Availability](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices#Availability))
    }  
  
Fields  
---  
`capacity` |  `enum (`[Capacity](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices#Capacity)`)` Output only. Specifies the current capacity bucket for this device configuration.Represents the total number of online devices (idle or in use).  
`available` |  `enum (`[Availability](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices#Availability)`)` Output only. Specifies the current availability bucket (idle, immediately allocatable devices) for this device configuration.This is a best-effort snapshot, refreshed periodically. It fluctuates depending on traffic as other requests allocate devices.  
  
## Capacity

Capacity based on the number of online devices in the lab.

New values may be added in the future.

Enums  
---  
`CAPACITY_UNSPECIFIED` | The value of device capacity is unknown or unset.  
`CAPACITY_NONE` | No online devices of this configuration.These devices are unavailable either temporarily or permanently and should not be requested. If the device is also marked as deprecated, this state is very likely permanent.  
`CAPACITY_LOW` | Devices that are low in capacity (the lab has a small number of these devices).These devices may be used if users need to test on this specific device model and version. Please note that due to low capacity, the tests may take much longer to finish, especially if a large number of tests are invoked at once. These devices are not suitable for test sharding.  
`CAPACITY_MEDIUM` | Devices that are medium in capacity (the lab has a decent number of these devices, though not as many as high capacity devices).These devices are suitable for fewer test runs (ex. fewer than 100 tests) and only for low shard counts (ex. less than 10 shards).  
`CAPACITY_HIGH` | Devices that are high in capacity (the lab has a large number of these devices).These devices are generally suggested for running a large number of simultaneous tests (ex. more than 100 tests).Please note that high capacity devices do not guarantee short wait times due to several factors: 1. Traffic (how heavily they are used at any given moment). 2. High capacity devices are prioritized for certain usages, which may cause user tests to be slower than selecting other similar device types.  
  
## Availability

Describes how many idle devices are available for allocation.

New values may be added in the future.

Enums  
---  
`AVAILABILITY_UNSPECIFIED` | The value of availability is unknown or unset.  
`AVAILABILITY_NONE` | No devices of this configuration are currently idle.A request can still be made, but it will queue until a device frees up. Expect longer wait times, and avoid requesting many devices at once (ex. high shard counts).  
`AVAILABILITY_LOW` | A small number of devices are currently idle.Suitable for a few concurrent requests. Larger bursts (ex. many shards) may queue until devices free up.  
`AVAILABILITY_MEDIUM` | A moderate number of devices are currently idle.Suitable for a moderate number of concurrent requests. Very large bursts may still queue.  
`AVAILABILITY_HIGH` | Many devices are currently idle.Suitable for a large number of concurrent requests with little to no queueing at the moment of observation.  
  
## LabInfo

The lab hosting a device.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "regionCode": string
    }  
  
Fields  
---  
`displayName` |  `string` Output only. Display name of the lab where the device is hosted. If empty, the device is hosted in a Google-owned lab.  
`regionCode` |  `string` Output only. The Unicode country/region code (CLDR) of the lab where the device is hosted, ex. "US" for United States, "KR" for South Korea. Empty when the hosting region is not published.  
  
## AccessDeniedReason

Why a device that the caller can see cannot be used by the caller's project.

New values may be added in the future.

Enums  
---  
`ACCESS_DENIED_REASON_UNSPECIFIED` | Reason not specified.  
`EULA_NOT_ACCEPTED` | The device is hosted in a partner lab whose end user license agreement the project has not accepted.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices/get)`

|  Returns information about a specific device.  
  
### `[list](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices/list)`

|  Lists all devices.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
