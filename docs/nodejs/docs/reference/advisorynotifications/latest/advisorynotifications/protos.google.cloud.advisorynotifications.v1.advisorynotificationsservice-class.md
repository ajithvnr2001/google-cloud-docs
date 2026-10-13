---
url: https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.cloud.advisorynotifications.v1.advisorynotificationsservice-class
title: Class protos.google.cloud.advisorynotifications.v1.AdvisoryNotificationsService (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:23:56.263557+00:00
---

# Class protos.google.cloud.advisorynotifications.v1.AdvisoryNotificationsService (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.cloud.advisorynotifications.v1.advisorynotificationsservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.advisorynotifications.v1.AdvisoryNotificationsService (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  1.1.0  0.2.1  0.1.0 

Represents an AdvisoryNotificationsService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.advisorynotifications.v1.AdvisoryNotificationsService

## Package

[@google-cloud/advisorynotifications](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new AdvisoryNotificationsService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): AdvisoryNotificationsService;

Creates new AdvisoryNotificationsService service using the specified rpc implementation.

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
`[AdvisoryNotificationsService](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.cloud.advisorynotifications.v1.advisorynotificationsservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### getNotification(request, callback)
    
    
    public getNotification(request: google.cloud.advisorynotifications.v1.IGetNotificationRequest, callback: google.cloud.advisorynotifications.v1.AdvisoryNotificationsService.GetNotificationCallback): void;

Calls GetNotification.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetNotificationRequest](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.cloud.advisorynotifications.v1.igetnotificationrequest)`   
GetNotificationRequest message or plain object  
`callback` |  `[GetNotificationCallback](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/overview.html)`   
Node-style callback called with the error, if any, and Notification  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getNotification(request)
    
    
    public getNotification(request: google.cloud.advisorynotifications.v1.IGetNotificationRequest): Promise<google.cloud.advisorynotifications.v1.Notification>;

Calls GetNotification.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetNotificationRequest](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.cloud.advisorynotifications.v1.igetnotificationrequest)`   
GetNotificationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.advisorynotifications.v1.Notification](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.cloud.advisorynotifications.v1.notification)>` | Promise  
  
### getSettings(request, callback)
    
    
    public getSettings(request: google.cloud.advisorynotifications.v1.IGetSettingsRequest, callback: google.cloud.advisorynotifications.v1.AdvisoryNotificationsService.GetSettingsCallback): void;

Calls GetSettings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.cloud.advisorynotifications.v1.igetsettingsrequest)`   
GetSettingsRequest message or plain object  
`callback` |  `[GetSettingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/overview.html)`   
Node-style callback called with the error, if any, and Settings  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSettings(request)
    
    
    public getSettings(request: google.cloud.advisorynotifications.v1.IGetSettingsRequest): Promise<google.cloud.advisorynotifications.v1.Settings>;

Calls GetSettings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.cloud.advisorynotifications.v1.igetsettingsrequest)`   
GetSettingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.advisorynotifications.v1.Settings](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.cloud.advisorynotifications.v1.settings)>` | Promise  
  
### listNotifications(request, callback)
    
    
    public listNotifications(request: google.cloud.advisorynotifications.v1.IListNotificationsRequest, callback: google.cloud.advisorynotifications.v1.AdvisoryNotificationsService.ListNotificationsCallback): void;

Calls ListNotifications.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListNotificationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.cloud.advisorynotifications.v1.ilistnotificationsrequest)`   
ListNotificationsRequest message or plain object  
`callback` |  `[ListNotificationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/overview.html)`   
Node-style callback called with the error, if any, and ListNotificationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listNotifications(request)
    
    
    public listNotifications(request: google.cloud.advisorynotifications.v1.IListNotificationsRequest): Promise<google.cloud.advisorynotifications.v1.ListNotificationsResponse>;

Calls ListNotifications.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListNotificationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.cloud.advisorynotifications.v1.ilistnotificationsrequest)`   
ListNotificationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.advisorynotifications.v1.ListNotificationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.cloud.advisorynotifications.v1.listnotificationsresponse)>` | Promise  
  
### updateSettings(request, callback)
    
    
    public updateSettings(request: google.cloud.advisorynotifications.v1.IUpdateSettingsRequest, callback: google.cloud.advisorynotifications.v1.AdvisoryNotificationsService.UpdateSettingsCallback): void;

Calls UpdateSettings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.cloud.advisorynotifications.v1.iupdatesettingsrequest)`   
UpdateSettingsRequest message or plain object  
`callback` |  `[UpdateSettingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/overview.html)`   
Node-style callback called with the error, if any, and Settings  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateSettings(request)
    
    
    public updateSettings(request: google.cloud.advisorynotifications.v1.IUpdateSettingsRequest): Promise<google.cloud.advisorynotifications.v1.Settings>;

Calls UpdateSettings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.cloud.advisorynotifications.v1.iupdatesettingsrequest)`   
UpdateSettingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.advisorynotifications.v1.Settings](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.cloud.advisorynotifications.v1.settings)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
