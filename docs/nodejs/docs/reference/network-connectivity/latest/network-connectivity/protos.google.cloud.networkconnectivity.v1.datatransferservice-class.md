---
url: https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.datatransferservice-class
title: Class protos.google.cloud.networkconnectivity.v1.DataTransferService (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:12:27.542545+00:00
---

# Class protos.google.cloud.networkconnectivity.v1.DataTransferService (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.datatransferservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.networkconnectivity.v1.DataTransferService (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.6.0  4.2.0  3.6.0  3.2.0  2.3.3  2.2.0  2.1.2  1.5.0  1.4.2  1.3.0  1.2.1  1.1.6 

Represents a DataTransferService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.networkconnectivity.v1.DataTransferService

## Package

[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new DataTransferService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): DataTransferService;

Creates new DataTransferService service using the specified rpc implementation.

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
`[DataTransferService](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.datatransferservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createDestination(request, callback)
    
    
    public createDestination(request: google.cloud.networkconnectivity.v1.ICreateDestinationRequest, callback: google.cloud.networkconnectivity.v1.DataTransferService.CreateDestinationCallback): void;

Calls CreateDestination.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDestinationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.icreatedestinationrequest)`   
CreateDestinationRequest message or plain object  
`callback` |  `[CreateDestinationCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDestination(request)
    
    
    public createDestination(request: google.cloud.networkconnectivity.v1.ICreateDestinationRequest): Promise<google.longrunning.Operation>;

Calls CreateDestination.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDestinationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.icreatedestinationrequest)`   
CreateDestinationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.operation)>` | Promise  
  
### createMulticloudDataTransferConfig(request, callback)
    
    
    public createMulticloudDataTransferConfig(request: google.cloud.networkconnectivity.v1.ICreateMulticloudDataTransferConfigRequest, callback: google.cloud.networkconnectivity.v1.DataTransferService.CreateMulticloudDataTransferConfigCallback): void;

Calls CreateMulticloudDataTransferConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.icreatemulticlouddatatransferconfigrequest)`   
CreateMulticloudDataTransferConfigRequest message or plain object  
`callback` |  `[CreateMulticloudDataTransferConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createMulticloudDataTransferConfig(request)
    
    
    public createMulticloudDataTransferConfig(request: google.cloud.networkconnectivity.v1.ICreateMulticloudDataTransferConfigRequest): Promise<google.longrunning.Operation>;

Calls CreateMulticloudDataTransferConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.icreatemulticlouddatatransferconfigrequest)`   
CreateMulticloudDataTransferConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.operation)>` | Promise  
  
### deleteDestination(request, callback)
    
    
    public deleteDestination(request: google.cloud.networkconnectivity.v1.IDeleteDestinationRequest, callback: google.cloud.networkconnectivity.v1.DataTransferService.DeleteDestinationCallback): void;

Calls DeleteDestination.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDestinationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.ideletedestinationrequest)`   
DeleteDestinationRequest message or plain object  
`callback` |  `[DeleteDestinationCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDestination(request)
    
    
    public deleteDestination(request: google.cloud.networkconnectivity.v1.IDeleteDestinationRequest): Promise<google.longrunning.Operation>;

Calls DeleteDestination.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDestinationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.ideletedestinationrequest)`   
DeleteDestinationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.operation)>` | Promise  
  
### deleteMulticloudDataTransferConfig(request, callback)
    
    
    public deleteMulticloudDataTransferConfig(request: google.cloud.networkconnectivity.v1.IDeleteMulticloudDataTransferConfigRequest, callback: google.cloud.networkconnectivity.v1.DataTransferService.DeleteMulticloudDataTransferConfigCallback): void;

Calls DeleteMulticloudDataTransferConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.ideletemulticlouddatatransferconfigrequest)`   
DeleteMulticloudDataTransferConfigRequest message or plain object  
`callback` |  `[DeleteMulticloudDataTransferConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteMulticloudDataTransferConfig(request)
    
    
    public deleteMulticloudDataTransferConfig(request: google.cloud.networkconnectivity.v1.IDeleteMulticloudDataTransferConfigRequest): Promise<google.longrunning.Operation>;

Calls DeleteMulticloudDataTransferConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.ideletemulticlouddatatransferconfigrequest)`   
DeleteMulticloudDataTransferConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.operation)>` | Promise  
  
### getDestination(request, callback)
    
    
    public getDestination(request: google.cloud.networkconnectivity.v1.IGetDestinationRequest, callback: google.cloud.networkconnectivity.v1.DataTransferService.GetDestinationCallback): void;

Calls GetDestination.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDestinationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.igetdestinationrequest)`   
GetDestinationRequest message or plain object  
`callback` |  `[GetDestinationCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and Destination  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDestination(request)
    
    
    public getDestination(request: google.cloud.networkconnectivity.v1.IGetDestinationRequest): Promise<google.cloud.networkconnectivity.v1.Destination>;

Calls GetDestination.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDestinationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.igetdestinationrequest)`   
GetDestinationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.networkconnectivity.v1.Destination](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.destination-class)>` | Promise  
  
### getMulticloudDataTransferConfig(request, callback)
    
    
    public getMulticloudDataTransferConfig(request: google.cloud.networkconnectivity.v1.IGetMulticloudDataTransferConfigRequest, callback: google.cloud.networkconnectivity.v1.DataTransferService.GetMulticloudDataTransferConfigCallback): void;

Calls GetMulticloudDataTransferConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.igetmulticlouddatatransferconfigrequest)`   
GetMulticloudDataTransferConfigRequest message or plain object  
`callback` |  `[GetMulticloudDataTransferConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and MulticloudDataTransferConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMulticloudDataTransferConfig(request)
    
    
    public getMulticloudDataTransferConfig(request: google.cloud.networkconnectivity.v1.IGetMulticloudDataTransferConfigRequest): Promise<google.cloud.networkconnectivity.v1.MulticloudDataTransferConfig>;

Calls GetMulticloudDataTransferConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.igetmulticlouddatatransferconfigrequest)`   
GetMulticloudDataTransferConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.networkconnectivity.v1.MulticloudDataTransferConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.multiclouddatatransferconfig)>` | Promise  
  
### getMulticloudDataTransferSupportedService(request, callback)
    
    
    public getMulticloudDataTransferSupportedService(request: google.cloud.networkconnectivity.v1.IGetMulticloudDataTransferSupportedServiceRequest, callback: google.cloud.networkconnectivity.v1.DataTransferService.GetMulticloudDataTransferSupportedServiceCallback): void;

Calls GetMulticloudDataTransferSupportedService.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMulticloudDataTransferSupportedServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.igetmulticlouddatatransfersupportedservicerequest)`   
GetMulticloudDataTransferSupportedServiceRequest message or plain object  
`callback` |  `[GetMulticloudDataTransferSupportedServiceCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and MulticloudDataTransferSupportedService  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMulticloudDataTransferSupportedService(request)
    
    
    public getMulticloudDataTransferSupportedService(request: google.cloud.networkconnectivity.v1.IGetMulticloudDataTransferSupportedServiceRequest): Promise<google.cloud.networkconnectivity.v1.MulticloudDataTransferSupportedService>;

Calls GetMulticloudDataTransferSupportedService.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetMulticloudDataTransferSupportedServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.igetmulticlouddatatransfersupportedservicerequest)`   
GetMulticloudDataTransferSupportedServiceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.networkconnectivity.v1.MulticloudDataTransferSupportedService](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.multiclouddatatransfersupportedservice)>` | Promise  
  
### listDestinations(request, callback)
    
    
    public listDestinations(request: google.cloud.networkconnectivity.v1.IListDestinationsRequest, callback: google.cloud.networkconnectivity.v1.DataTransferService.ListDestinationsCallback): void;

Calls ListDestinations.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDestinationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.ilistdestinationsrequest)`   
ListDestinationsRequest message or plain object  
`callback` |  `[ListDestinationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDestinationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDestinations(request)
    
    
    public listDestinations(request: google.cloud.networkconnectivity.v1.IListDestinationsRequest): Promise<google.cloud.networkconnectivity.v1.ListDestinationsResponse>;

Calls ListDestinations.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDestinationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.ilistdestinationsrequest)`   
ListDestinationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.networkconnectivity.v1.ListDestinationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.listdestinationsresponse)>` | Promise  
  
### listMulticloudDataTransferConfigs(request, callback)
    
    
    public listMulticloudDataTransferConfigs(request: google.cloud.networkconnectivity.v1.IListMulticloudDataTransferConfigsRequest, callback: google.cloud.networkconnectivity.v1.DataTransferService.ListMulticloudDataTransferConfigsCallback): void;

Calls ListMulticloudDataTransferConfigs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMulticloudDataTransferConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.ilistmulticlouddatatransferconfigsrequest)`   
ListMulticloudDataTransferConfigsRequest message or plain object  
`callback` |  `[ListMulticloudDataTransferConfigsCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and ListMulticloudDataTransferConfigsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMulticloudDataTransferConfigs(request)
    
    
    public listMulticloudDataTransferConfigs(request: google.cloud.networkconnectivity.v1.IListMulticloudDataTransferConfigsRequest): Promise<google.cloud.networkconnectivity.v1.ListMulticloudDataTransferConfigsResponse>;

Calls ListMulticloudDataTransferConfigs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListMulticloudDataTransferConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.ilistmulticlouddatatransferconfigsrequest)`   
ListMulticloudDataTransferConfigsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.networkconnectivity.v1.ListMulticloudDataTransferConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.listmulticlouddatatransferconfigsresponse)>` | Promise  
  
### listMulticloudDataTransferSupportedServices(request, callback)
    
    
    public listMulticloudDataTransferSupportedServices(request: google.cloud.networkconnectivity.v1.IListMulticloudDataTransferSupportedServicesRequest, callback: google.cloud.networkconnectivity.v1.DataTransferService.ListMulticloudDataTransferSupportedServicesCallback): void;

Calls ListMulticloudDataTransferSupportedServices.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMulticloudDataTransferSupportedServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.ilistmulticlouddatatransfersupportedservicesrequest)`   
ListMulticloudDataTransferSupportedServicesRequest message or plain object  
`callback` |  `[ListMulticloudDataTransferSupportedServicesCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and ListMulticloudDataTransferSupportedServicesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMulticloudDataTransferSupportedServices(request)
    
    
    public listMulticloudDataTransferSupportedServices(request: google.cloud.networkconnectivity.v1.IListMulticloudDataTransferSupportedServicesRequest): Promise<google.cloud.networkconnectivity.v1.ListMulticloudDataTransferSupportedServicesResponse>;

Calls ListMulticloudDataTransferSupportedServices.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListMulticloudDataTransferSupportedServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.ilistmulticlouddatatransfersupportedservicesrequest)`   
ListMulticloudDataTransferSupportedServicesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.networkconnectivity.v1.ListMulticloudDataTransferSupportedServicesResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.listmulticlouddatatransfersupportedservicesresponse)>` | Promise  
  
### updateDestination(request, callback)
    
    
    public updateDestination(request: google.cloud.networkconnectivity.v1.IUpdateDestinationRequest, callback: google.cloud.networkconnectivity.v1.DataTransferService.UpdateDestinationCallback): void;

Calls UpdateDestination.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDestinationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.iupdatedestinationrequest)`   
UpdateDestinationRequest message or plain object  
`callback` |  `[UpdateDestinationCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDestination(request)
    
    
    public updateDestination(request: google.cloud.networkconnectivity.v1.IUpdateDestinationRequest): Promise<google.longrunning.Operation>;

Calls UpdateDestination.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDestinationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.iupdatedestinationrequest)`   
UpdateDestinationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.operation)>` | Promise  
  
### updateMulticloudDataTransferConfig(request, callback)
    
    
    public updateMulticloudDataTransferConfig(request: google.cloud.networkconnectivity.v1.IUpdateMulticloudDataTransferConfigRequest, callback: google.cloud.networkconnectivity.v1.DataTransferService.UpdateMulticloudDataTransferConfigCallback): void;

Calls UpdateMulticloudDataTransferConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.iupdatemulticlouddatatransferconfigrequest)`   
UpdateMulticloudDataTransferConfigRequest message or plain object  
`callback` |  `[UpdateMulticloudDataTransferConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateMulticloudDataTransferConfig(request)
    
    
    public updateMulticloudDataTransferConfig(request: google.cloud.networkconnectivity.v1.IUpdateMulticloudDataTransferConfigRequest): Promise<google.longrunning.Operation>;

Calls UpdateMulticloudDataTransferConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.iupdatemulticlouddatatransferconfigrequest)`   
UpdateMulticloudDataTransferConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
