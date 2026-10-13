---
url: https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.licensemanager-class
title: Class protos.google.cloud.licensemanager.v1.LicenseManager (0.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:40.550014+00:00
---

# Class protos.google.cloud.licensemanager.v1.LicenseManager (0.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.licensemanager-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.licensemanager.v1.LicenseManager (0.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a LicenseManager

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.licensemanager.v1.LicenseManager

## Package

[@google-cloud/licensemanager](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new LicenseManager service.

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

### aggregateUsage(request, callback)
    
    
    public aggregateUsage(request: google.cloud.licensemanager.v1.IAggregateUsageRequest, callback: google.cloud.licensemanager.v1.LicenseManager.AggregateUsageCallback): void;

Calls AggregateUsage.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAggregateUsageRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.iaggregateusagerequest)`   
AggregateUsageRequest message or plain object  
`callback` |  `[AggregateUsageCallback](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/overview.html)`   
Node-style callback called with the error, if any, and AggregateUsageResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### aggregateUsage(request)
    
    
    public aggregateUsage(request: google.cloud.licensemanager.v1.IAggregateUsageRequest): Promise<google.cloud.licensemanager.v1.AggregateUsageResponse>;

Calls AggregateUsage.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAggregateUsageRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.iaggregateusagerequest)`   
AggregateUsageRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.licensemanager.v1.AggregateUsageResponse](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.aggregateusageresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): LicenseManager;

Creates new LicenseManager service using the specified rpc implementation.

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
`[LicenseManager](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.licensemanager-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createConfiguration(request, callback)
    
    
    public createConfiguration(request: google.cloud.licensemanager.v1.ICreateConfigurationRequest, callback: google.cloud.licensemanager.v1.LicenseManager.CreateConfigurationCallback): void;

Calls CreateConfiguration.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConfigurationRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.icreateconfigurationrequest)`   
CreateConfigurationRequest message or plain object  
`callback` |  `[CreateConfigurationCallback](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createConfiguration(request)
    
    
    public createConfiguration(request: google.cloud.licensemanager.v1.ICreateConfigurationRequest): Promise<google.longrunning.Operation>;

Calls CreateConfiguration.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateConfigurationRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.icreateconfigurationrequest)`   
CreateConfigurationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.longrunning.operation)>` | Promise  
  
### deactivateConfiguration(request, callback)
    
    
    public deactivateConfiguration(request: google.cloud.licensemanager.v1.IDeactivateConfigurationRequest, callback: google.cloud.licensemanager.v1.LicenseManager.DeactivateConfigurationCallback): void;

Calls DeactivateConfiguration.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeactivateConfigurationRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.ideactivateconfigurationrequest)`   
DeactivateConfigurationRequest message or plain object  
`callback` |  `[DeactivateConfigurationCallback](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deactivateConfiguration(request)
    
    
    public deactivateConfiguration(request: google.cloud.licensemanager.v1.IDeactivateConfigurationRequest): Promise<google.longrunning.Operation>;

Calls DeactivateConfiguration.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeactivateConfigurationRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.ideactivateconfigurationrequest)`   
DeactivateConfigurationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.longrunning.operation)>` | Promise  
  
### deleteConfiguration(request, callback)
    
    
    public deleteConfiguration(request: google.cloud.licensemanager.v1.IDeleteConfigurationRequest, callback: google.cloud.licensemanager.v1.LicenseManager.DeleteConfigurationCallback): void;

Calls DeleteConfiguration.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConfigurationRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.ideleteconfigurationrequest)`   
DeleteConfigurationRequest message or plain object  
`callback` |  `[DeleteConfigurationCallback](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteConfiguration(request)
    
    
    public deleteConfiguration(request: google.cloud.licensemanager.v1.IDeleteConfigurationRequest): Promise<google.longrunning.Operation>;

Calls DeleteConfiguration.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConfigurationRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.ideleteconfigurationrequest)`   
DeleteConfigurationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.longrunning.operation)>` | Promise  
  
### getConfiguration(request, callback)
    
    
    public getConfiguration(request: google.cloud.licensemanager.v1.IGetConfigurationRequest, callback: google.cloud.licensemanager.v1.LicenseManager.GetConfigurationCallback): void;

Calls GetConfiguration.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConfigurationRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.igetconfigurationrequest)`   
GetConfigurationRequest message or plain object  
`callback` |  `[GetConfigurationCallback](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/overview.html)`   
Node-style callback called with the error, if any, and Configuration  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConfiguration(request)
    
    
    public getConfiguration(request: google.cloud.licensemanager.v1.IGetConfigurationRequest): Promise<google.cloud.licensemanager.v1.Configuration>;

Calls GetConfiguration.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetConfigurationRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.igetconfigurationrequest)`   
GetConfigurationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.licensemanager.v1.Configuration](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.configuration-class)>` | Promise  
  
### getInstance(request, callback)
    
    
    public getInstance(request: google.cloud.licensemanager.v1.IGetInstanceRequest, callback: google.cloud.licensemanager.v1.LicenseManager.GetInstanceCallback): void;

Calls GetInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.igetinstancerequest)`   
GetInstanceRequest message or plain object  
`callback` |  `[GetInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/overview.html)`   
Node-style callback called with the error, if any, and Instance  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getInstance(request)
    
    
    public getInstance(request: google.cloud.licensemanager.v1.IGetInstanceRequest): Promise<google.cloud.licensemanager.v1.Instance>;

Calls GetInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.igetinstancerequest)`   
GetInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.licensemanager.v1.Instance](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.instance-class)>` | Promise  
  
### getProduct(request, callback)
    
    
    public getProduct(request: google.cloud.licensemanager.v1.IGetProductRequest, callback: google.cloud.licensemanager.v1.LicenseManager.GetProductCallback): void;

Calls GetProduct.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.igetproductrequest)`   
GetProductRequest message or plain object  
`callback` |  `[GetProductCallback](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/overview.html)`   
Node-style callback called with the error, if any, and Product  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getProduct(request)
    
    
    public getProduct(request: google.cloud.licensemanager.v1.IGetProductRequest): Promise<google.cloud.licensemanager.v1.Product>;

Calls GetProduct.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.igetproductrequest)`   
GetProductRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.licensemanager.v1.Product](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.product-class)>` | Promise  
  
### listConfigurations(request, callback)
    
    
    public listConfigurations(request: google.cloud.licensemanager.v1.IListConfigurationsRequest, callback: google.cloud.licensemanager.v1.LicenseManager.ListConfigurationsCallback): void;

Calls ListConfigurations.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConfigurationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.ilistconfigurationsrequest)`   
ListConfigurationsRequest message or plain object  
`callback` |  `[ListConfigurationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/overview.html)`   
Node-style callback called with the error, if any, and ListConfigurationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listConfigurations(request)
    
    
    public listConfigurations(request: google.cloud.licensemanager.v1.IListConfigurationsRequest): Promise<google.cloud.licensemanager.v1.ListConfigurationsResponse>;

Calls ListConfigurations.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListConfigurationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.ilistconfigurationsrequest)`   
ListConfigurationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.licensemanager.v1.ListConfigurationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.listconfigurationsresponse)>` | Promise  
  
### listInstances(request, callback)
    
    
    public listInstances(request: google.cloud.licensemanager.v1.IListInstancesRequest, callback: google.cloud.licensemanager.v1.LicenseManager.ListInstancesCallback): void;

Calls ListInstances.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListInstancesRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.ilistinstancesrequest)`   
ListInstancesRequest message or plain object  
`callback` |  `[ListInstancesCallback](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/overview.html)`   
Node-style callback called with the error, if any, and ListInstancesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listInstances(request)
    
    
    public listInstances(request: google.cloud.licensemanager.v1.IListInstancesRequest): Promise<google.cloud.licensemanager.v1.ListInstancesResponse>;

Calls ListInstances.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListInstancesRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.ilistinstancesrequest)`   
ListInstancesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.licensemanager.v1.ListInstancesResponse](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.listinstancesresponse)>` | Promise  
  
### listProducts(request, callback)
    
    
    public listProducts(request: google.cloud.licensemanager.v1.IListProductsRequest, callback: google.cloud.licensemanager.v1.LicenseManager.ListProductsCallback): void;

Calls ListProducts.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.ilistproductsrequest)`   
ListProductsRequest message or plain object  
`callback` |  `[ListProductsCallback](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/overview.html)`   
Node-style callback called with the error, if any, and ListProductsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listProducts(request)
    
    
    public listProducts(request: google.cloud.licensemanager.v1.IListProductsRequest): Promise<google.cloud.licensemanager.v1.ListProductsResponse>;

Calls ListProducts.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.ilistproductsrequest)`   
ListProductsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.licensemanager.v1.ListProductsResponse](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.listproductsresponse)>` | Promise  
  
### queryConfigurationLicenseUsage(request, callback)
    
    
    public queryConfigurationLicenseUsage(request: google.cloud.licensemanager.v1.IQueryConfigurationLicenseUsageRequest, callback: google.cloud.licensemanager.v1.LicenseManager.QueryConfigurationLicenseUsageCallback): void;

Calls QueryConfigurationLicenseUsage.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryConfigurationLicenseUsageRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.iqueryconfigurationlicenseusagerequest)`   
QueryConfigurationLicenseUsageRequest message or plain object  
`callback` |  `[QueryConfigurationLicenseUsageCallback](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/overview.html)`   
Node-style callback called with the error, if any, and QueryConfigurationLicenseUsageResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryConfigurationLicenseUsage(request)
    
    
    public queryConfigurationLicenseUsage(request: google.cloud.licensemanager.v1.IQueryConfigurationLicenseUsageRequest): Promise<google.cloud.licensemanager.v1.QueryConfigurationLicenseUsageResponse>;

Calls QueryConfigurationLicenseUsage.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IQueryConfigurationLicenseUsageRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.iqueryconfigurationlicenseusagerequest)`   
QueryConfigurationLicenseUsageRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.licensemanager.v1.QueryConfigurationLicenseUsageResponse](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.queryconfigurationlicenseusageresponse)>` | Promise  
  
### reactivateConfiguration(request, callback)
    
    
    public reactivateConfiguration(request: google.cloud.licensemanager.v1.IReactivateConfigurationRequest, callback: google.cloud.licensemanager.v1.LicenseManager.ReactivateConfigurationCallback): void;

Calls ReactivateConfiguration.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IReactivateConfigurationRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.ireactivateconfigurationrequest)`   
ReactivateConfigurationRequest message or plain object  
`callback` |  `[ReactivateConfigurationCallback](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### reactivateConfiguration(request)
    
    
    public reactivateConfiguration(request: google.cloud.licensemanager.v1.IReactivateConfigurationRequest): Promise<google.longrunning.Operation>;

Calls ReactivateConfiguration.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IReactivateConfigurationRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.ireactivateconfigurationrequest)`   
ReactivateConfigurationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.longrunning.operation)>` | Promise  
  
### updateConfiguration(request, callback)
    
    
    public updateConfiguration(request: google.cloud.licensemanager.v1.IUpdateConfigurationRequest, callback: google.cloud.licensemanager.v1.LicenseManager.UpdateConfigurationCallback): void;

Calls UpdateConfiguration.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConfigurationRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.iupdateconfigurationrequest)`   
UpdateConfigurationRequest message or plain object  
`callback` |  `[UpdateConfigurationCallback](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateConfiguration(request)
    
    
    public updateConfiguration(request: google.cloud.licensemanager.v1.IUpdateConfigurationRequest): Promise<google.longrunning.Operation>;

Calls UpdateConfiguration.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConfigurationRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.iupdateconfigurationrequest)`   
UpdateConfigurationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
