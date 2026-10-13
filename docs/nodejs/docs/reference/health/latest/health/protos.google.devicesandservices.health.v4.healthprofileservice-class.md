---
url: https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.healthprofileservice-class
title: Class protos.google.devicesandservices.health.v4.HealthProfileService (0.8.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:45:18.681616+00:00
---

# Class protos.google.devicesandservices.health.v4.HealthProfileService (0.8.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.healthprofileservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.devicesandservices.health.v4.HealthProfileService (0.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a HealthProfileService

## Inheritance

$protobuf.rpc.Service > protos.google.devicesandservices.health.v4.HealthProfileService

## Package

[@google-cloud/health](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new HealthProfileService service.

**Parameters**  
---  
**Name** | **Description**  
`rpcImpl` |  `$protobuf.RPCImpl`   
RPC implementation  
`requestDelimited` |  `boolean`   
Whether requests are length-delimited  
`responseDelimited` |  `boolean`   
Whether responses are length-delimited  
  
## Methods 

### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): HealthProfileService;

Creates new HealthProfileService service using the specified rpc implementation.

**Parameters**  
---  
**Name** | **Description**  
`rpcImpl` |  `$protobuf.RPCImpl`   
RPC implementation  
`requestDelimited` |  `boolean`   
Whether requests are length-delimited  
`responseDelimited` |  `boolean`   
Whether responses are length-delimited  
**Returns**  
---  
**Type** | **Description**  
`[HealthProfileService](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.healthprofileservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### getIdentity(request, callback)
    
    
    public getIdentity(request: google.devicesandservices.health.v4.IGetIdentityRequest, callback: google.devicesandservices.health.v4.HealthProfileService.GetIdentityCallback): void;

Calls GetIdentity.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIdentityRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.igetidentityrequest)`   
GetIdentityRequest message or plain object  
`callback` |  `[GetIdentityCallback](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)`   
Node-style callback called with the error, if any, and Identity  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getIdentity(request)
    
    
    public getIdentity(request: google.devicesandservices.health.v4.IGetIdentityRequest): Promise<google.devicesandservices.health.v4.Identity>;

Calls GetIdentity.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetIdentityRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.igetidentityrequest)`   
GetIdentityRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.devicesandservices.health.v4.Identity](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.identity)>` | Promise  
  
### getIrnProfile(request, callback)
    
    
    public getIrnProfile(request: google.devicesandservices.health.v4.IGetIrnProfileRequest, callback: google.devicesandservices.health.v4.HealthProfileService.GetIrnProfileCallback): void;

Calls GetIrnProfile.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIrnProfileRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.igetirnprofilerequest)`   
GetIrnProfileRequest message or plain object  
`callback` |  `[GetIrnProfileCallback](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)`   
Node-style callback called with the error, if any, and IrnProfile  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getIrnProfile(request)
    
    
    public getIrnProfile(request: google.devicesandservices.health.v4.IGetIrnProfileRequest): Promise<google.devicesandservices.health.v4.IrnProfile>;

Calls GetIrnProfile.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetIrnProfileRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.igetirnprofilerequest)`   
GetIrnProfileRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.devicesandservices.health.v4.IrnProfile](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.irnprofile)>` | Promise  
  
### getPairedDevice(request, callback)
    
    
    public getPairedDevice(request: google.devicesandservices.health.v4.IGetPairedDeviceRequest, callback: google.devicesandservices.health.v4.HealthProfileService.GetPairedDeviceCallback): void;

Calls GetPairedDevice.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPairedDeviceRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.igetpaireddevicerequest)`   
GetPairedDeviceRequest message or plain object  
`callback` |  `[GetPairedDeviceCallback](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)`   
Node-style callback called with the error, if any, and PairedDevice  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getPairedDevice(request)
    
    
    public getPairedDevice(request: google.devicesandservices.health.v4.IGetPairedDeviceRequest): Promise<google.devicesandservices.health.v4.PairedDevice>;

Calls GetPairedDevice.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetPairedDeviceRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.igetpaireddevicerequest)`   
GetPairedDeviceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.devicesandservices.health.v4.PairedDevice](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.paireddevice-class)>` | Promise  
  
### getProfile(request, callback)
    
    
    public getProfile(request: google.devicesandservices.health.v4.IGetProfileRequest, callback: google.devicesandservices.health.v4.HealthProfileService.GetProfileCallback): void;

Calls GetProfile.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetProfileRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.igetprofilerequest)`   
GetProfileRequest message or plain object  
`callback` |  `[GetProfileCallback](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)`   
Node-style callback called with the error, if any, and Profile  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getProfile(request)
    
    
    public getProfile(request: google.devicesandservices.health.v4.IGetProfileRequest): Promise<google.devicesandservices.health.v4.Profile>;

Calls GetProfile.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetProfileRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.igetprofilerequest)`   
GetProfileRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.devicesandservices.health.v4.Profile](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.profile)>` | Promise  
  
### getSettings(request, callback)
    
    
    public getSettings(request: google.devicesandservices.health.v4.IGetSettingsRequest, callback: google.devicesandservices.health.v4.HealthProfileService.GetSettingsCallback): void;

Calls GetSettings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.igetsettingsrequest)`   
GetSettingsRequest message or plain object  
`callback` |  `[GetSettingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)`   
Node-style callback called with the error, if any, and Settings  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSettings(request)
    
    
    public getSettings(request: google.devicesandservices.health.v4.IGetSettingsRequest): Promise<google.devicesandservices.health.v4.Settings>;

Calls GetSettings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.igetsettingsrequest)`   
GetSettingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.devicesandservices.health.v4.Settings](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.settings-class)>` | Promise  
  
### listPairedDevices(request, callback)
    
    
    public listPairedDevices(request: google.devicesandservices.health.v4.IListPairedDevicesRequest, callback: google.devicesandservices.health.v4.HealthProfileService.ListPairedDevicesCallback): void;

Calls ListPairedDevices.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPairedDevicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.ilistpaireddevicesrequest)`   
ListPairedDevicesRequest message or plain object  
`callback` |  `[ListPairedDevicesCallback](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)`   
Node-style callback called with the error, if any, and ListPairedDevicesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listPairedDevices(request)
    
    
    public listPairedDevices(request: google.devicesandservices.health.v4.IListPairedDevicesRequest): Promise<google.devicesandservices.health.v4.ListPairedDevicesResponse>;

Calls ListPairedDevices.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListPairedDevicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.ilistpaireddevicesrequest)`   
ListPairedDevicesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.devicesandservices.health.v4.ListPairedDevicesResponse](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.listpaireddevicesresponse)>` | Promise  
  
### updateProfile(request, callback)
    
    
    public updateProfile(request: google.devicesandservices.health.v4.IUpdateProfileRequest, callback: google.devicesandservices.health.v4.HealthProfileService.UpdateProfileCallback): void;

Calls UpdateProfile.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateProfileRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.iupdateprofilerequest)`   
UpdateProfileRequest message or plain object  
`callback` |  `[UpdateProfileCallback](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)`   
Node-style callback called with the error, if any, and Profile  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateProfile(request)
    
    
    public updateProfile(request: google.devicesandservices.health.v4.IUpdateProfileRequest): Promise<google.devicesandservices.health.v4.Profile>;

Calls UpdateProfile.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateProfileRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.iupdateprofilerequest)`   
UpdateProfileRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.devicesandservices.health.v4.Profile](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.profile)>` | Promise  
  
### updateSettings(request, callback)
    
    
    public updateSettings(request: google.devicesandservices.health.v4.IUpdateSettingsRequest, callback: google.devicesandservices.health.v4.HealthProfileService.UpdateSettingsCallback): void;

Calls UpdateSettings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.iupdatesettingsrequest)`   
UpdateSettingsRequest message or plain object  
`callback` |  `[UpdateSettingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)`   
Node-style callback called with the error, if any, and Settings  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateSettings(request)
    
    
    public updateSettings(request: google.devicesandservices.health.v4.IUpdateSettingsRequest): Promise<google.devicesandservices.health.v4.Settings>;

Calls UpdateSettings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.iupdatesettingsrequest)`   
UpdateSettingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.devicesandservices.health.v4.Settings](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.settings-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
