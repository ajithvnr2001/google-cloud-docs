---
url: https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices
title: REST Resource: customers.deployments.devices \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:23:46.502206+00:00
---

# REST Resource: customers.deployments.devices  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)



Send feedback 

#  REST Resource: customers.deployments.devices Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Device
    * JSON representation
    * DeviceConfig
      * JSON representation
    * DeviceCategory
    * DeviceModel
      * JSON representation
    * DeviceAirInterface
      * JSON representation
    * RadioTechnology
    * InstallationParams
      * JSON representation
    * HeightType
    * MeasurementCapability
    * State
    * State
    * DeviceGrant
      * JSON representation
    * FrequencyRange
      * JSON representation
    * GrantState
    * ChannelType
    * DpaMoveList
      * JSON representation
    * DeviceMetadata
  * Methods



## Resource: Device

JSON representation  
---  
      
    
    {
      "name": string,
      "fccId": string,
      "serialNumber": string,
      "preloadedConfig": {
        object ([DeviceConfig](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.DeviceConfig))
      },
      "activeConfig": {
        object ([DeviceConfig](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.DeviceConfig))
      },
      "state": enum ([State](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.State_1)),
      "grants": [
        {
          object ([DeviceGrant](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.DeviceGrant))
        }
      ],
      "displayName": string,
      "deviceMetadata": {
        object ([DeviceMetadata](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.DeviceMetadata))
      }
    }  
  
Fields  
---  
`name` |  `string` Output only. The resource path name.  
`fccId` |  `string` The FCC identifier of the device.  
`serialNumber` |  `string` A serial number assigned to the device by the device manufacturer.  
`preloadedConfig` |  `object (`[DeviceConfig](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.DeviceConfig)`)` Configuration of the device, as specified via SAS Portal API.  
`activeConfig` |  `object (`[DeviceConfig](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.DeviceConfig)`)` Output only. Current configuration of the device as registered to the SAS.  
`state` |  `enum (`[State](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.State_1)`)` Output only. Device state.  
`grants[]` |  `object (`[DeviceGrant](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.DeviceGrant)`)` Output only. Grants held by the device.  
`displayName` |  `string` Device display name.  
`deviceMetadata` |  `object (`[DeviceMetadata](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.DeviceMetadata)`)` Device parameters that can be overridden by both SAS Portal and SAS registration requests.  
  
### DeviceConfig

Information about the device configuration.

JSON representation  
---  
      
    
    {
      "category": enum ([DeviceCategory](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.DeviceCategory)),
      "model": {
        object ([DeviceModel](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.DeviceModel))
      },
      "airInterface": {
        object ([DeviceAirInterface](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.DeviceAirInterface))
      },
      "installationParams": {
        object ([InstallationParams](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.InstallationParams))
      },
      "measurementCapabilities": [
        enum ([MeasurementCapability](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.MeasurementCapability))
      ],
      "userId": string,
      "callSign": string,
      "state": enum ([State](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.State)),
      "isSigned": boolean,
      "updateTime": string
    }  
  
Fields  
---  
`category` |  `enum (`[DeviceCategory](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.DeviceCategory)`)` FCC category of the device.  
`model` |  `object (`[DeviceModel](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.DeviceModel)`)` Information about this device model.  
`airInterface` |  `object (`[DeviceAirInterface](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.DeviceAirInterface)`)` Information about this device's air interface.  
`installationParams` |  `object (`[InstallationParams](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.InstallationParams)`)` Installation parameters for the device.  
`measurementCapabilities[]` |  `enum (`[MeasurementCapability](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.MeasurementCapability)`)` Measurement reporting capabilities of the device.  
`userId` |  `string` The identifier of a device user.  
`callSign` |  `string` The call sign of the device operator.  
`state` |  `enum (`[State](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.State)`)` State of the configuration.  
`isSigned` |  `boolean` Output only. Whether the configuration has been signed by a CPI.  
`updateTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The last time the device configuration was edited.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
  
### DeviceCategory

FCC category of the device, as defined by Part 96.

Enums  
---  
`DEVICE_CATEGORY_UNSPECIFIED` | Unspecified device category.  
`DEVICE_CATEGORY_A` | Category A.  
`DEVICE_CATEGORY_B` | Category B.  
  
### DeviceModel

Information about the model of the device.

JSON representation  
---  
      
    
    {
      "vendor": string,
      "name": string,
      "softwareVersion": string,
      "hardwareVersion": string,
      "firmwareVersion": string
    }  
  
Fields  
---  
`vendor` |  `string` The name of the device vendor.  
`name` |  `string` The name of the device model.  
`softwareVersion` |  `string` The software version of the device.  
`hardwareVersion` |  `string` The hardware version of the device.  
`firmwareVersion` |  `string` The firmware version of the device.  
  
### DeviceAirInterface

Information about the device's air interface.

JSON representation  
---  
      
    
    {
      "radioTechnology": enum ([RadioTechnology](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.RadioTechnology)),
      "supportedSpec": string
    }  
  
Fields  
---  
`radioTechnology` |  `enum (`[RadioTechnology](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.RadioTechnology)`)` Conditional. This field specifies the radio access technology that is used for the CBSD.  
`supportedSpec` |  `string` Optional. This field is related to the `radioTechnology` and provides the air interface specification that the CBSD is compliant with at the time of registration.  
  
### RadioTechnology

The approved types of radio access technology.

Enums  
---  
`RADIO_TECHNOLOGY_UNSPECIFIED` |   
`E_UTRA` |   
`CAMBIUM_NETWORKS` |   
`FOUR_G_BBW_SAA_1` |   
`NR` |   
`DOODLE_CBRS` |   
`CW` |   
`REDLINE` |   
`TARANA_WIRELESS` |   
  
### InstallationParams

Information about the device installation parameters.

JSON representation  
---  
      
    
    {
      "latitude": number,
      "longitude": number,
      "height": number,
      "heightType": enum ([HeightType](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.HeightType)),
      "horizontalAccuracy": number,
      "verticalAccuracy": number,
      "indoorDeployment": boolean,
      "antennaAzimuth": integer,
      "antennaDowntilt": integer,
      "antennaGain": integer,
      "eirpCapability": integer,
      "antennaBeamwidth": integer,
      "antennaModel": string,
      "cpeCbsdIndication": boolean
    }  
  
Fields  
---  
`latitude` |  `number` Latitude of the device antenna location in degrees relative to the WGS 84 datum. The allowed range is from -90.000000 to +90.000000. Positive values represent latitudes north of the equator; negative values south of the equator.  
`longitude` |  `number` Longitude of the device antenna location in degrees relative to the WGS 84 datum. The allowed range is from -180.000000 to +180.000000. Positive values represent longitudes east of the prime meridian; negative values west of the prime meridian.  
`height` |  `number` Device antenna height in meters. When the `heightType` parameter value is "AGL", the antenna height should be given relative to ground level. When the `heightType` parameter value is "AMSL", it is given with respect to WGS84 datum.  
`heightType` |  `enum (`[HeightType](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.HeightType)`)` Specifies how the height is measured.  
`horizontalAccuracy` |  `number` A positive number in meters to indicate accuracy of the device antenna horizontal location. This optional parameter should only be present if its value is less than the FCC requirement of 50 meters.  
`verticalAccuracy` |  `number` A positive number in meters to indicate accuracy of the device antenna vertical location. This optional parameter should only be present if its value is less than the FCC requirement of 3 meters.  
`indoorDeployment` |  `boolean` Whether the device antenna is indoor or not. `true`: indoor. `false`: outdoor.  
`antennaAzimuth` |  `integer` Boresight direction of the horizontal plane of the antenna in degrees with respect to true north. The value of this parameter is an integer with a value between 0 and 359 inclusive. A value of 0 degrees means true north; a value of 90 degrees means east. This parameter is optional for Category A devices and conditional for Category B devices.  
`antennaDowntilt` |  `integer` Antenna downtilt in degrees and is an integer with a value between -90 and +90 inclusive; a negative value means the antenna is tilted up (above horizontal). This parameter is optional for Category A devices and conditional for Category B devices.  
`antennaGain` |  `integer` Peak antenna gain in dBi. This parameter is an integer with a value between -127 and +128 (dBi) inclusive.  
`eirpCapability` |  `integer` This parameter is the maximum device EIRP in units of dBm/10MHz and is an integer with a value between -127 and +47 (dBm/10 MHz) inclusive. If not included, SAS interprets it as maximum allowable EIRP in units of dBm/10MHz for device category.  
`antennaBeamwidth` |  `integer` 3-dB antenna beamwidth of the antenna in the horizontal-plane in degrees. This parameter is an unsigned integer having a value between 0 and 360 (degrees) inclusive; it is optional for Category A devices and conditional for Category B devices.  
`antennaModel` |  `string` If an external antenna is used, the antenna model is optionally provided in this field. The string has a maximum length of 128 octets.  
`cpeCbsdIndication` |  `boolean` If present, this parameter specifies whether the CBSD is a CPE-CBSD or not.  
  
### HeightType

Specifies how the height is measured.

Enums  
---  
`HEIGHT_TYPE_UNSPECIFIED` | Unspecified height type.  
`HEIGHT_TYPE_AGL` | AGL height is measured relative to the ground level.  
`HEIGHT_TYPE_AMSL` | AMSL height is measured relative to the mean sea level.  
  
### MeasurementCapability

Device measurement capability. The values are defined by WINNF-SSC-0002.

Enums  
---  
`MEASUREMENT_CAPABILITY_UNSPECIFIED` |   
`MEASUREMENT_CAPABILITY_RECEIVED_POWER_WITH_GRANT` |   
`MEASUREMENT_CAPABILITY_RECEIVED_POWER_WITHOUT_GRANT` |   
  
### State

State of the device config. Only configs in state `[DEVICE_CONFIG_STATE_FINAL](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.State.ENUM_VALUES.FINAL)` can be used during CBSD Registration.

Enums  
---  
`DEVICE_CONFIG_STATE_UNSPECIFIED` |   
`DRAFT` |   
`FINAL` |   
  
### State

State of the device.

Enums  
---  
`DEVICE_STATE_UNSPECIFIED` | Unspecified state.  
`RESERVED` | Device created in the SAS Portal, however, not yet registered with SAS.  
`REGISTERED` | Device registered with SAS.  
`DEREGISTERED` | Device de-registered with SAS.  
  
### DeviceGrant

Device grant. It is an authorization provided by the Spectrum Access System to a device to transmit using specified operating parameters after a successful heartbeat by the device.

JSON representation  
---  
      
    
    {
      "maxEirp": number,
      "frequencyRange": {
        object ([FrequencyRange](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.FrequencyRange))
      },
      "state": enum ([GrantState](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.GrantState)),
      "channelType": enum ([ChannelType](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.ChannelType)),
      "moveList": [
        {
          object ([DpaMoveList](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.DpaMoveList))
        }
      ],
      "expireTime": string,
      "suspensionReason": [
        string
      ],
      "grantId": string
    }  
  
Fields  
---  
`maxEirp` |  `number` Maximum Equivalent Isotropically Radiated Power (EIRP) permitted by the grant. The maximum EIRP is in units of dBm/MHz. The value of `maxEirp` represents the average (RMS) EIRP that would be measured by the procedure defined in FCC part 96.41(e)(3).  
`frequencyRange` |  `object (`[FrequencyRange](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.FrequencyRange)`)` The transmission frequency range.  
`state` |  `enum (`[GrantState](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.GrantState)`)` State of the grant.  
`channelType` |  `enum (`[ChannelType](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.ChannelType)`)` Type of channel used.  
`moveList[]` |  `object (`[DpaMoveList](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.DpaMoveList)`)` The DPA move lists on which this grant appears.  
`expireTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` The expiration time of the grant.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`suspensionReason[]` |  `string` If the grant is suspended, the reason(s) for suspension.  
`grantId` |  `string` Grant Id.  
  
### FrequencyRange

Frequency range from `low_frequency` to `high_frequency`.

JSON representation  
---  
      
    
    {
      "lowFrequencyMhz": number,
      "highFrequencyMhz": number
    }  
  
Fields  
---  
`lowFrequencyMhz` |  `number` The lowest frequency of the frequency range in MHz.  
`highFrequencyMhz` |  `number` The highest frequency of the frequency range in MHz.  
  
### GrantState

The state of the grant.

Enums  
---  
`GRANT_STATE_UNSPECIFIED` |   
`GRANT_STATE_GRANTED` | The grant has been granted but the device is not heartbeating on it.  
`GRANT_STATE_TERMINATED` | The grant has been terminated by the SAS.  
`GRANT_STATE_SUSPENDED` | The grant has been suspended by the SAS.  
`GRANT_STATE_AUTHORIZED` | The device is currently transmitting.  
`GRANT_STATE_EXPIRED` | The grant has expired.  
  
### ChannelType

Enums  
---  
`CHANNEL_TYPE_UNSPECIFIED` |   
`CHANNEL_TYPE_GAA` |   
`CHANNEL_TYPE_PAL` |   
  
### DpaMoveList

An entry in a DPA's move list.

JSON representation  
---  
      
    
    {
      "dpaId": string,
      "frequencyRange": {
        object ([FrequencyRange](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.FrequencyRange))
      }
    }  
  
Fields  
---  
`dpaId` |  `string` The ID of the DPA.  
`frequencyRange` |  `object (`[FrequencyRange](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.FrequencyRange)`)` The frequency range that the move list affects.  
  
### DeviceMetadata

Device data overridable by both SAS Portal and registration requests.

## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices/create)`

|  Creates a `[device](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device)` under a `[node](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.nodes#Node)` or `[customer](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers#Customer)`.  
  
### `[createSigned](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices/createSigned)`

|  Creates a signed `[device](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device)` under a `[node](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.nodes#Node)` or `[customer](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers#Customer)`.  
  
### `[list](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices/list)`

|  Lists `[devices](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device)` under a `[node](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.nodes#Node)` or `[customer](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers#Customer)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
