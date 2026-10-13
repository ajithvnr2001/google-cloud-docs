---
url: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.conversationprofiles-class
title: Class protos.google.cloud.dialogflow.v2.ConversationProfiles (8.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:59:38.508376+00:00
---

# Class protos.google.cloud.dialogflow.v2.ConversationProfiles (8.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.conversationprofiles-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dialogflow.v2.ConversationProfiles (8.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

8.2.0 (latest)  8.1.1  7.9.0  7.8.0  7.7.0  7.5.0  7.4.0  7.1.0  7.0.1  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.8.0  6.6.0  6.4.0  6.3.1  6.2.0  6.0.0  5.7.1  5.6.0  5.5.1  5.3.0  5.2.1  4.7.0  4.6.0  4.5.0  4.4.0  4.3.1  4.2.0  4.1.4  3.5.0  3.3.0 

Represents a ConversationProfiles

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.dialogflow.v2.ConversationProfiles

## Package

[@google-cloud/dialogflow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new ConversationProfiles service.

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

### clearSuggestionFeatureConfig(request, callback)
    
    
    public clearSuggestionFeatureConfig(request: google.cloud.dialogflow.v2.IClearSuggestionFeatureConfigRequest, callback: google.cloud.dialogflow.v2.ConversationProfiles.ClearSuggestionFeatureConfigCallback): void;

Calls ClearSuggestionFeatureConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IClearSuggestionFeatureConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.iclearsuggestionfeatureconfigrequest)`   
ClearSuggestionFeatureConfigRequest message or plain object  
`callback` |  `[ClearSuggestionFeatureConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### clearSuggestionFeatureConfig(request)
    
    
    public clearSuggestionFeatureConfig(request: google.cloud.dialogflow.v2.IClearSuggestionFeatureConfigRequest): Promise<google.longrunning.Operation>;

Calls ClearSuggestionFeatureConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IClearSuggestionFeatureConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.iclearsuggestionfeatureconfigrequest)`   
ClearSuggestionFeatureConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.longrunning.operation)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): ConversationProfiles;

Creates new ConversationProfiles service using the specified rpc implementation.

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
`[ConversationProfiles](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.conversationprofiles-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createConversationProfile(request, callback)
    
    
    public createConversationProfile(request: google.cloud.dialogflow.v2.ICreateConversationProfileRequest, callback: google.cloud.dialogflow.v2.ConversationProfiles.CreateConversationProfileCallback): void;

Calls CreateConversationProfile.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConversationProfileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.icreateconversationprofilerequest)`   
CreateConversationProfileRequest message or plain object  
`callback` |  `[CreateConversationProfileCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and ConversationProfile  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createConversationProfile(request)
    
    
    public createConversationProfile(request: google.cloud.dialogflow.v2.ICreateConversationProfileRequest): Promise<google.cloud.dialogflow.v2.ConversationProfile>;

Calls CreateConversationProfile.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateConversationProfileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.icreateconversationprofilerequest)`   
CreateConversationProfileRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.ConversationProfile](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.conversationprofile)>` | Promise  
  
### deleteConversationProfile(request, callback)
    
    
    public deleteConversationProfile(request: google.cloud.dialogflow.v2.IDeleteConversationProfileRequest, callback: google.cloud.dialogflow.v2.ConversationProfiles.DeleteConversationProfileCallback): void;

Calls DeleteConversationProfile.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConversationProfileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ideleteconversationprofilerequest)`   
DeleteConversationProfileRequest message or plain object  
`callback` |  `[DeleteConversationProfileCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteConversationProfile(request)
    
    
    public deleteConversationProfile(request: google.cloud.dialogflow.v2.IDeleteConversationProfileRequest): Promise<google.protobuf.Empty>;

Calls DeleteConversationProfile.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConversationProfileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ideleteconversationprofilerequest)`   
DeleteConversationProfileRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.protobuf.empty)>` | Promise  
  
### getConversationProfile(request, callback)
    
    
    public getConversationProfile(request: google.cloud.dialogflow.v2.IGetConversationProfileRequest, callback: google.cloud.dialogflow.v2.ConversationProfiles.GetConversationProfileCallback): void;

Calls GetConversationProfile.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConversationProfileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.igetconversationprofilerequest)`   
GetConversationProfileRequest message or plain object  
`callback` |  `[GetConversationProfileCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and ConversationProfile  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConversationProfile(request)
    
    
    public getConversationProfile(request: google.cloud.dialogflow.v2.IGetConversationProfileRequest): Promise<google.cloud.dialogflow.v2.ConversationProfile>;

Calls GetConversationProfile.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetConversationProfileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.igetconversationprofilerequest)`   
GetConversationProfileRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.ConversationProfile](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.conversationprofile)>` | Promise  
  
### listConversationProfiles(request, callback)
    
    
    public listConversationProfiles(request: google.cloud.dialogflow.v2.IListConversationProfilesRequest, callback: google.cloud.dialogflow.v2.ConversationProfiles.ListConversationProfilesCallback): void;

Calls ListConversationProfiles.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConversationProfilesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ilistconversationprofilesrequest)`   
ListConversationProfilesRequest message or plain object  
`callback` |  `[ListConversationProfilesCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and ListConversationProfilesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listConversationProfiles(request)
    
    
    public listConversationProfiles(request: google.cloud.dialogflow.v2.IListConversationProfilesRequest): Promise<google.cloud.dialogflow.v2.ListConversationProfilesResponse>;

Calls ListConversationProfiles.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListConversationProfilesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ilistconversationprofilesrequest)`   
ListConversationProfilesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.ListConversationProfilesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.listconversationprofilesresponse)>` | Promise  
  
### setSuggestionFeatureConfig(request, callback)
    
    
    public setSuggestionFeatureConfig(request: google.cloud.dialogflow.v2.ISetSuggestionFeatureConfigRequest, callback: google.cloud.dialogflow.v2.ConversationProfiles.SetSuggestionFeatureConfigCallback): void;

Calls SetSuggestionFeatureConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetSuggestionFeatureConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.isetsuggestionfeatureconfigrequest)`   
SetSuggestionFeatureConfigRequest message or plain object  
`callback` |  `[SetSuggestionFeatureConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setSuggestionFeatureConfig(request)
    
    
    public setSuggestionFeatureConfig(request: google.cloud.dialogflow.v2.ISetSuggestionFeatureConfigRequest): Promise<google.longrunning.Operation>;

Calls SetSuggestionFeatureConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetSuggestionFeatureConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.isetsuggestionfeatureconfigrequest)`   
SetSuggestionFeatureConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.longrunning.operation)>` | Promise  
  
### updateConversationProfile(request, callback)
    
    
    public updateConversationProfile(request: google.cloud.dialogflow.v2.IUpdateConversationProfileRequest, callback: google.cloud.dialogflow.v2.ConversationProfiles.UpdateConversationProfileCallback): void;

Calls UpdateConversationProfile.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConversationProfileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.iupdateconversationprofilerequest)`   
UpdateConversationProfileRequest message or plain object  
`callback` |  `[UpdateConversationProfileCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and ConversationProfile  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateConversationProfile(request)
    
    
    public updateConversationProfile(request: google.cloud.dialogflow.v2.IUpdateConversationProfileRequest): Promise<google.cloud.dialogflow.v2.ConversationProfile>;

Calls UpdateConversationProfile.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConversationProfileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.iupdateconversationprofilerequest)`   
UpdateConversationProfileRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.ConversationProfile](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.conversationprofile)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
