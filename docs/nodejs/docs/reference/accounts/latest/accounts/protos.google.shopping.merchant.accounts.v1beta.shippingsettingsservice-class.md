---
url: https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.shippingsettingsservice-class
title: Class protos.google.shopping.merchant.accounts.v1beta.ShippingSettingsService (4.0.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:24.734291+00:00
---

# Class protos.google.shopping.merchant.accounts.v1beta.ShippingSettingsService (4.0.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.shippingsettingsservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.shopping.merchant.accounts.v1beta.ShippingSettingsService (4.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.1 (latest)  3.2.0  2.2.0  1.0.0 

Represents a ShippingSettingsService

## Inheritance

$protobuf.rpc.Service > protos.google.shopping.merchant.accounts.v1beta.ShippingSettingsService

## Package

[@google-shopping/accounts](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new ShippingSettingsService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): ShippingSettingsService;

Creates new ShippingSettingsService service using the specified rpc implementation.

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
`[ShippingSettingsService](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.shippingsettingsservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### getShippingSettings(request, callback)
    
    
    public getShippingSettings(request: google.shopping.merchant.accounts.v1beta.IGetShippingSettingsRequest, callback: google.shopping.merchant.accounts.v1beta.ShippingSettingsService.GetShippingSettingsCallback): void;

Calls GetShippingSettings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetShippingSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.igetshippingsettingsrequest)`   
GetShippingSettingsRequest message or plain object  
`callback` |  `[GetShippingSettingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/overview.html)`   
Node-style callback called with the error, if any, and ShippingSettings  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getShippingSettings(request)
    
    
    public getShippingSettings(request: google.shopping.merchant.accounts.v1beta.IGetShippingSettingsRequest): Promise<google.shopping.merchant.accounts.v1beta.ShippingSettings>;

Calls GetShippingSettings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetShippingSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.igetshippingsettingsrequest)`   
GetShippingSettingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.shopping.merchant.accounts.v1beta.ShippingSettings](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.shippingsettings)>` | Promise  
  
### insertShippingSettings(request, callback)
    
    
    public insertShippingSettings(request: google.shopping.merchant.accounts.v1beta.IInsertShippingSettingsRequest, callback: google.shopping.merchant.accounts.v1beta.ShippingSettingsService.InsertShippingSettingsCallback): void;

Calls InsertShippingSettings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInsertShippingSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.iinsertshippingsettingsrequest)`   
InsertShippingSettingsRequest message or plain object  
`callback` |  `[InsertShippingSettingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/overview.html)`   
Node-style callback called with the error, if any, and ShippingSettings  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### insertShippingSettings(request)
    
    
    public insertShippingSettings(request: google.shopping.merchant.accounts.v1beta.IInsertShippingSettingsRequest): Promise<google.shopping.merchant.accounts.v1beta.ShippingSettings>;

Calls InsertShippingSettings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IInsertShippingSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.iinsertshippingsettingsrequest)`   
InsertShippingSettingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.shopping.merchant.accounts.v1beta.ShippingSettings](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.shippingsettings)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
