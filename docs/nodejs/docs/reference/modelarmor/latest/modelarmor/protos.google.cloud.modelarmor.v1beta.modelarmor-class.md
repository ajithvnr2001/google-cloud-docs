---
url: https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1beta.modelarmor-class
title: Class protos.google.cloud.modelarmor.v1beta.ModelArmor (0.9.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:12:00.371773+00:00
---

# Class protos.google.cloud.modelarmor.v1beta.ModelArmor (0.9.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1beta.modelarmor-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.modelarmor.v1beta.ModelArmor (0.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.7.0  0.6.0 

Represents a ModelArmor

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.modelarmor.v1beta.ModelArmor

## Package

[@google-cloud/modelarmor](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new ModelArmor service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): ModelArmor;

Creates new ModelArmor service using the specified rpc implementation.

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
`[ModelArmor](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1beta.modelarmor-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createTemplate(request, callback)
    
    
    public createTemplate(request: google.cloud.modelarmor.v1beta.ICreateTemplateRequest, callback: google.cloud.modelarmor.v1beta.ModelArmor.CreateTemplateCallback): void;

Calls CreateTemplate.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1beta.icreatetemplaterequest)`   
CreateTemplateRequest message or plain object  
`callback` |  `[CreateTemplateCallback](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/overview.html)`   
Node-style callback called with the error, if any, and Template  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createTemplate(request)
    
    
    public createTemplate(request: google.cloud.modelarmor.v1beta.ICreateTemplateRequest): Promise<google.cloud.modelarmor.v1beta.Template>;

Calls CreateTemplate.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1beta.icreatetemplaterequest)`   
CreateTemplateRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.modelarmor.v1beta.Template](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1beta.template-class)>` | Promise  
  
### deleteTemplate(request, callback)
    
    
    public deleteTemplate(request: google.cloud.modelarmor.v1beta.IDeleteTemplateRequest, callback: google.cloud.modelarmor.v1beta.ModelArmor.DeleteTemplateCallback): void;

Calls DeleteTemplate.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1beta.ideletetemplaterequest)`   
DeleteTemplateRequest message or plain object  
`callback` |  `[DeleteTemplateCallback](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteTemplate(request)
    
    
    public deleteTemplate(request: google.cloud.modelarmor.v1beta.IDeleteTemplateRequest): Promise<google.protobuf.Empty>;

Calls DeleteTemplate.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1beta.ideletetemplaterequest)`   
DeleteTemplateRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.protobuf.empty)>` | Promise  
  
### getFloorSetting(request, callback)
    
    
    public getFloorSetting(request: google.cloud.modelarmor.v1beta.IGetFloorSettingRequest, callback: google.cloud.modelarmor.v1beta.ModelArmor.GetFloorSettingCallback): void;

Calls GetFloorSetting.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFloorSettingRequest](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1beta.igetfloorsettingrequest)`   
GetFloorSettingRequest message or plain object  
`callback` |  `[GetFloorSettingCallback](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/overview.html)`   
Node-style callback called with the error, if any, and FloorSetting  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getFloorSetting(request)
    
    
    public getFloorSetting(request: google.cloud.modelarmor.v1beta.IGetFloorSettingRequest): Promise<google.cloud.modelarmor.v1beta.FloorSetting>;

Calls GetFloorSetting.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetFloorSettingRequest](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1beta.igetfloorsettingrequest)`   
GetFloorSettingRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.modelarmor.v1beta.FloorSetting](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1beta.floorsetting-class)>` | Promise  
  
### getTemplate(request, callback)
    
    
    public getTemplate(request: google.cloud.modelarmor.v1beta.IGetTemplateRequest, callback: google.cloud.modelarmor.v1beta.ModelArmor.GetTemplateCallback): void;

Calls GetTemplate.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1beta.igettemplaterequest)`   
GetTemplateRequest message or plain object  
`callback` |  `[GetTemplateCallback](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/overview.html)`   
Node-style callback called with the error, if any, and Template  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getTemplate(request)
    
    
    public getTemplate(request: google.cloud.modelarmor.v1beta.IGetTemplateRequest): Promise<google.cloud.modelarmor.v1beta.Template>;

Calls GetTemplate.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1beta.igettemplaterequest)`   
GetTemplateRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.modelarmor.v1beta.Template](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1beta.template-class)>` | Promise  
  
### listTemplates(request, callback)
    
    
    public listTemplates(request: google.cloud.modelarmor.v1beta.IListTemplatesRequest, callback: google.cloud.modelarmor.v1beta.ModelArmor.ListTemplatesCallback): void;

Calls ListTemplates.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTemplatesRequest](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1beta.ilisttemplatesrequest)`   
ListTemplatesRequest message or plain object  
`callback` |  `[ListTemplatesCallback](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/overview.html)`   
Node-style callback called with the error, if any, and ListTemplatesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTemplates(request)
    
    
    public listTemplates(request: google.cloud.modelarmor.v1beta.IListTemplatesRequest): Promise<google.cloud.modelarmor.v1beta.ListTemplatesResponse>;

Calls ListTemplates.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListTemplatesRequest](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1beta.ilisttemplatesrequest)`   
ListTemplatesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.modelarmor.v1beta.ListTemplatesResponse](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1beta.listtemplatesresponse)>` | Promise  
  
### sanitizeModelResponse(request, callback)
    
    
    public sanitizeModelResponse(request: google.cloud.modelarmor.v1beta.ISanitizeModelResponseRequest, callback: google.cloud.modelarmor.v1beta.ModelArmor.SanitizeModelResponseCallback): void;

Calls SanitizeModelResponse.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISanitizeModelResponseRequest](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1beta.isanitizemodelresponserequest)`   
SanitizeModelResponseRequest message or plain object  
`callback` |  `[SanitizeModelResponseCallback](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/overview.html)`   
Node-style callback called with the error, if any, and SanitizeModelResponseResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### sanitizeModelResponse(request)
    
    
    public sanitizeModelResponse(request: google.cloud.modelarmor.v1beta.ISanitizeModelResponseRequest): Promise<google.cloud.modelarmor.v1beta.SanitizeModelResponseResponse>;

Calls SanitizeModelResponse.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISanitizeModelResponseRequest](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1beta.isanitizemodelresponserequest)`   
SanitizeModelResponseRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.modelarmor.v1beta.SanitizeModelResponseResponse](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1beta.sanitizemodelresponseresponse)>` | Promise  
  
### sanitizeUserPrompt(request, callback)
    
    
    public sanitizeUserPrompt(request: google.cloud.modelarmor.v1beta.ISanitizeUserPromptRequest, callback: google.cloud.modelarmor.v1beta.ModelArmor.SanitizeUserPromptCallback): void;

Calls SanitizeUserPrompt.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISanitizeUserPromptRequest](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1beta.isanitizeuserpromptrequest)`   
SanitizeUserPromptRequest message or plain object  
`callback` |  `[SanitizeUserPromptCallback](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/overview.html)`   
Node-style callback called with the error, if any, and SanitizeUserPromptResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### sanitizeUserPrompt(request)
    
    
    public sanitizeUserPrompt(request: google.cloud.modelarmor.v1beta.ISanitizeUserPromptRequest): Promise<google.cloud.modelarmor.v1beta.SanitizeUserPromptResponse>;

Calls SanitizeUserPrompt.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISanitizeUserPromptRequest](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1beta.isanitizeuserpromptrequest)`   
SanitizeUserPromptRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.modelarmor.v1beta.SanitizeUserPromptResponse](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1beta.sanitizeuserpromptresponse)>` | Promise  
  
### streamSanitizeModelResponse(request, callback)
    
    
    public streamSanitizeModelResponse(request: google.cloud.modelarmor.v1beta.ISanitizeModelResponseRequest, callback: google.cloud.modelarmor.v1beta.ModelArmor.StreamSanitizeModelResponseCallback): void;

Calls StreamSanitizeModelResponse.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISanitizeModelResponseRequest](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1beta.isanitizemodelresponserequest)`   
SanitizeModelResponseRequest message or plain object  
`callback` |  `[StreamSanitizeModelResponseCallback](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/overview.html)`   
Node-style callback called with the error, if any, and SanitizeModelResponseResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### streamSanitizeModelResponse(request)
    
    
    public streamSanitizeModelResponse(request: google.cloud.modelarmor.v1beta.ISanitizeModelResponseRequest): Promise<google.cloud.modelarmor.v1beta.SanitizeModelResponseResponse>;

Calls StreamSanitizeModelResponse.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISanitizeModelResponseRequest](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1beta.isanitizemodelresponserequest)`   
SanitizeModelResponseRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.modelarmor.v1beta.SanitizeModelResponseResponse](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1beta.sanitizemodelresponseresponse)>` | Promise  
  
### streamSanitizeUserPrompt(request, callback)
    
    
    public streamSanitizeUserPrompt(request: google.cloud.modelarmor.v1beta.ISanitizeUserPromptRequest, callback: google.cloud.modelarmor.v1beta.ModelArmor.StreamSanitizeUserPromptCallback): void;

Calls StreamSanitizeUserPrompt.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISanitizeUserPromptRequest](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1beta.isanitizeuserpromptrequest)`   
SanitizeUserPromptRequest message or plain object  
`callback` |  `[StreamSanitizeUserPromptCallback](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/overview.html)`   
Node-style callback called with the error, if any, and SanitizeUserPromptResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### streamSanitizeUserPrompt(request)
    
    
    public streamSanitizeUserPrompt(request: google.cloud.modelarmor.v1beta.ISanitizeUserPromptRequest): Promise<google.cloud.modelarmor.v1beta.SanitizeUserPromptResponse>;

Calls StreamSanitizeUserPrompt.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISanitizeUserPromptRequest](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1beta.isanitizeuserpromptrequest)`   
SanitizeUserPromptRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.modelarmor.v1beta.SanitizeUserPromptResponse](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1beta.sanitizeuserpromptresponse)>` | Promise  
  
### updateFloorSetting(request, callback)
    
    
    public updateFloorSetting(request: google.cloud.modelarmor.v1beta.IUpdateFloorSettingRequest, callback: google.cloud.modelarmor.v1beta.ModelArmor.UpdateFloorSettingCallback): void;

Calls UpdateFloorSetting.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFloorSettingRequest](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1beta.iupdatefloorsettingrequest)`   
UpdateFloorSettingRequest message or plain object  
`callback` |  `[UpdateFloorSettingCallback](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/overview.html)`   
Node-style callback called with the error, if any, and FloorSetting  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateFloorSetting(request)
    
    
    public updateFloorSetting(request: google.cloud.modelarmor.v1beta.IUpdateFloorSettingRequest): Promise<google.cloud.modelarmor.v1beta.FloorSetting>;

Calls UpdateFloorSetting.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFloorSettingRequest](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1beta.iupdatefloorsettingrequest)`   
UpdateFloorSettingRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.modelarmor.v1beta.FloorSetting](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1beta.floorsetting-class)>` | Promise  
  
### updateTemplate(request, callback)
    
    
    public updateTemplate(request: google.cloud.modelarmor.v1beta.IUpdateTemplateRequest, callback: google.cloud.modelarmor.v1beta.ModelArmor.UpdateTemplateCallback): void;

Calls UpdateTemplate.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1beta.iupdatetemplaterequest)`   
UpdateTemplateRequest message or plain object  
`callback` |  `[UpdateTemplateCallback](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/overview.html)`   
Node-style callback called with the error, if any, and Template  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateTemplate(request)
    
    
    public updateTemplate(request: google.cloud.modelarmor.v1beta.IUpdateTemplateRequest): Promise<google.cloud.modelarmor.v1beta.Template>;

Calls UpdateTemplate.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1beta.iupdatetemplaterequest)`   
UpdateTemplateRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.modelarmor.v1beta.Template](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1beta.template-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
