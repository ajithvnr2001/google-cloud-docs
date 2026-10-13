---
url: https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.cloudchannelservice-class
title: Class protos.google.cloud.channel.v1.CloudChannelService (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:15:16.778859+00:00
---

# Class protos.google.cloud.channel.v1.CloudChannelService (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.cloudchannelservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.channel.v1.CloudChannelService (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.2  3.6.0  3.2.1  3.0.0  2.5.1  2.4.1  2.2.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.6 

Represents a CloudChannelService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.channel.v1.CloudChannelService

## Package

[@google-cloud/channel](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new CloudChannelService service.

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

### activateEntitlement(request, callback)
    
    
    public activateEntitlement(request: google.cloud.channel.v1.IActivateEntitlementRequest, callback: google.cloud.channel.v1.CloudChannelService.ActivateEntitlementCallback): void;

Calls ActivateEntitlement.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IActivateEntitlementRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.iactivateentitlementrequest)`   
ActivateEntitlementRequest message or plain object  
`callback` |  `[ActivateEntitlementCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### activateEntitlement(request)
    
    
    public activateEntitlement(request: google.cloud.channel.v1.IActivateEntitlementRequest): Promise<google.longrunning.Operation>;

Calls ActivateEntitlement.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IActivateEntitlementRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.iactivateentitlementrequest)`   
ActivateEntitlementRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.longrunning.operation)>` | Promise  
  
### cancelEntitlement(request, callback)
    
    
    public cancelEntitlement(request: google.cloud.channel.v1.ICancelEntitlementRequest, callback: google.cloud.channel.v1.CloudChannelService.CancelEntitlementCallback): void;

Calls CancelEntitlement.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICancelEntitlementRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.icancelentitlementrequest)`   
CancelEntitlementRequest message or plain object  
`callback` |  `[CancelEntitlementCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cancelEntitlement(request)
    
    
    public cancelEntitlement(request: google.cloud.channel.v1.ICancelEntitlementRequest): Promise<google.longrunning.Operation>;

Calls CancelEntitlement.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICancelEntitlementRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.icancelentitlementrequest)`   
CancelEntitlementRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.longrunning.operation)>` | Promise  
  
### changeOffer(request, callback)
    
    
    public changeOffer(request: google.cloud.channel.v1.IChangeOfferRequest, callback: google.cloud.channel.v1.CloudChannelService.ChangeOfferCallback): void;

Calls ChangeOffer.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IChangeOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ichangeofferrequest)`   
ChangeOfferRequest message or plain object  
`callback` |  `[ChangeOfferCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### changeOffer(request)
    
    
    public changeOffer(request: google.cloud.channel.v1.IChangeOfferRequest): Promise<google.longrunning.Operation>;

Calls ChangeOffer.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IChangeOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ichangeofferrequest)`   
ChangeOfferRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.longrunning.operation)>` | Promise  
  
### changeParameters(request, callback)
    
    
    public changeParameters(request: google.cloud.channel.v1.IChangeParametersRequest, callback: google.cloud.channel.v1.CloudChannelService.ChangeParametersCallback): void;

Calls ChangeParameters.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IChangeParametersRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ichangeparametersrequest)`   
ChangeParametersRequest message or plain object  
`callback` |  `[ChangeParametersCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### changeParameters(request)
    
    
    public changeParameters(request: google.cloud.channel.v1.IChangeParametersRequest): Promise<google.longrunning.Operation>;

Calls ChangeParameters.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IChangeParametersRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ichangeparametersrequest)`   
ChangeParametersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.longrunning.operation)>` | Promise  
  
### changeRenewalSettings(request, callback)
    
    
    public changeRenewalSettings(request: google.cloud.channel.v1.IChangeRenewalSettingsRequest, callback: google.cloud.channel.v1.CloudChannelService.ChangeRenewalSettingsCallback): void;

Calls ChangeRenewalSettings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IChangeRenewalSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ichangerenewalsettingsrequest)`   
ChangeRenewalSettingsRequest message or plain object  
`callback` |  `[ChangeRenewalSettingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### changeRenewalSettings(request)
    
    
    public changeRenewalSettings(request: google.cloud.channel.v1.IChangeRenewalSettingsRequest): Promise<google.longrunning.Operation>;

Calls ChangeRenewalSettings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IChangeRenewalSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ichangerenewalsettingsrequest)`   
ChangeRenewalSettingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.longrunning.operation)>` | Promise  
  
### checkCloudIdentityAccountsExist(request, callback)
    
    
    public checkCloudIdentityAccountsExist(request: google.cloud.channel.v1.ICheckCloudIdentityAccountsExistRequest, callback: google.cloud.channel.v1.CloudChannelService.CheckCloudIdentityAccountsExistCallback): void;

Calls CheckCloudIdentityAccountsExist.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICheckCloudIdentityAccountsExistRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.icheckcloudidentityaccountsexistrequest)`   
CheckCloudIdentityAccountsExistRequest message or plain object  
`callback` |  `[CheckCloudIdentityAccountsExistCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and CheckCloudIdentityAccountsExistResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### checkCloudIdentityAccountsExist(request)
    
    
    public checkCloudIdentityAccountsExist(request: google.cloud.channel.v1.ICheckCloudIdentityAccountsExistRequest): Promise<google.cloud.channel.v1.CheckCloudIdentityAccountsExistResponse>;

Calls CheckCloudIdentityAccountsExist.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICheckCloudIdentityAccountsExistRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.icheckcloudidentityaccountsexistrequest)`   
CheckCloudIdentityAccountsExistRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.CheckCloudIdentityAccountsExistResponse](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.checkcloudidentityaccountsexistresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): CloudChannelService;

Creates new CloudChannelService service using the specified rpc implementation.

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
`[CloudChannelService](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.cloudchannelservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createChannelPartnerLink(request, callback)
    
    
    public createChannelPartnerLink(request: google.cloud.channel.v1.ICreateChannelPartnerLinkRequest, callback: google.cloud.channel.v1.CloudChannelService.CreateChannelPartnerLinkCallback): void;

Calls CreateChannelPartnerLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateChannelPartnerLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.icreatechannelpartnerlinkrequest)`   
CreateChannelPartnerLinkRequest message or plain object  
`callback` |  `[CreateChannelPartnerLinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and ChannelPartnerLink  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createChannelPartnerLink(request)
    
    
    public createChannelPartnerLink(request: google.cloud.channel.v1.ICreateChannelPartnerLinkRequest): Promise<google.cloud.channel.v1.ChannelPartnerLink>;

Calls CreateChannelPartnerLink.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateChannelPartnerLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.icreatechannelpartnerlinkrequest)`   
CreateChannelPartnerLinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.ChannelPartnerLink](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.channelpartnerlink)>` | Promise  
  
### createChannelPartnerRepricingConfig(request, callback)
    
    
    public createChannelPartnerRepricingConfig(request: google.cloud.channel.v1.ICreateChannelPartnerRepricingConfigRequest, callback: google.cloud.channel.v1.CloudChannelService.CreateChannelPartnerRepricingConfigCallback): void;

Calls CreateChannelPartnerRepricingConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.icreatechannelpartnerrepricingconfigrequest)`   
CreateChannelPartnerRepricingConfigRequest message or plain object  
`callback` |  `[CreateChannelPartnerRepricingConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and ChannelPartnerRepricingConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createChannelPartnerRepricingConfig(request)
    
    
    public createChannelPartnerRepricingConfig(request: google.cloud.channel.v1.ICreateChannelPartnerRepricingConfigRequest): Promise<google.cloud.channel.v1.ChannelPartnerRepricingConfig>;

Calls CreateChannelPartnerRepricingConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.icreatechannelpartnerrepricingconfigrequest)`   
CreateChannelPartnerRepricingConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.ChannelPartnerRepricingConfig](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.channelpartnerrepricingconfig)>` | Promise  
  
### createCustomer(request, callback)
    
    
    public createCustomer(request: google.cloud.channel.v1.ICreateCustomerRequest, callback: google.cloud.channel.v1.CloudChannelService.CreateCustomerCallback): void;

Calls CreateCustomer.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCustomerRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.icreatecustomerrequest)`   
CreateCustomerRequest message or plain object  
`callback` |  `[CreateCustomerCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and Customer  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCustomer(request)
    
    
    public createCustomer(request: google.cloud.channel.v1.ICreateCustomerRequest): Promise<google.cloud.channel.v1.Customer>;

Calls CreateCustomer.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateCustomerRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.icreatecustomerrequest)`   
CreateCustomerRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.Customer](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.customer-class)>` | Promise  
  
### createCustomerRepricingConfig(request, callback)
    
    
    public createCustomerRepricingConfig(request: google.cloud.channel.v1.ICreateCustomerRepricingConfigRequest, callback: google.cloud.channel.v1.CloudChannelService.CreateCustomerRepricingConfigCallback): void;

Calls CreateCustomerRepricingConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCustomerRepricingConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.icreatecustomerrepricingconfigrequest)`   
CreateCustomerRepricingConfigRequest message or plain object  
`callback` |  `[CreateCustomerRepricingConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and CustomerRepricingConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCustomerRepricingConfig(request)
    
    
    public createCustomerRepricingConfig(request: google.cloud.channel.v1.ICreateCustomerRepricingConfigRequest): Promise<google.cloud.channel.v1.CustomerRepricingConfig>;

Calls CreateCustomerRepricingConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateCustomerRepricingConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.icreatecustomerrepricingconfigrequest)`   
CreateCustomerRepricingConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.CustomerRepricingConfig](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.customerrepricingconfig)>` | Promise  
  
### createEntitlement(request, callback)
    
    
    public createEntitlement(request: google.cloud.channel.v1.ICreateEntitlementRequest, callback: google.cloud.channel.v1.CloudChannelService.CreateEntitlementCallback): void;

Calls CreateEntitlement.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateEntitlementRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.icreateentitlementrequest)`   
CreateEntitlementRequest message or plain object  
`callback` |  `[CreateEntitlementCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createEntitlement(request)
    
    
    public createEntitlement(request: google.cloud.channel.v1.ICreateEntitlementRequest): Promise<google.longrunning.Operation>;

Calls CreateEntitlement.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateEntitlementRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.icreateentitlementrequest)`   
CreateEntitlementRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.longrunning.operation)>` | Promise  
  
### deleteChannelPartnerRepricingConfig(request, callback)
    
    
    public deleteChannelPartnerRepricingConfig(request: google.cloud.channel.v1.IDeleteChannelPartnerRepricingConfigRequest, callback: google.cloud.channel.v1.CloudChannelService.DeleteChannelPartnerRepricingConfigCallback): void;

Calls DeleteChannelPartnerRepricingConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ideletechannelpartnerrepricingconfigrequest)`   
DeleteChannelPartnerRepricingConfigRequest message or plain object  
`callback` |  `[DeleteChannelPartnerRepricingConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteChannelPartnerRepricingConfig(request)
    
    
    public deleteChannelPartnerRepricingConfig(request: google.cloud.channel.v1.IDeleteChannelPartnerRepricingConfigRequest): Promise<google.protobuf.Empty>;

Calls DeleteChannelPartnerRepricingConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ideletechannelpartnerrepricingconfigrequest)`   
DeleteChannelPartnerRepricingConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.protobuf.empty)>` | Promise  
  
### deleteCustomer(request, callback)
    
    
    public deleteCustomer(request: google.cloud.channel.v1.IDeleteCustomerRequest, callback: google.cloud.channel.v1.CloudChannelService.DeleteCustomerCallback): void;

Calls DeleteCustomer.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCustomerRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ideletecustomerrequest)`   
DeleteCustomerRequest message or plain object  
`callback` |  `[DeleteCustomerCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteCustomer(request)
    
    
    public deleteCustomer(request: google.cloud.channel.v1.IDeleteCustomerRequest): Promise<google.protobuf.Empty>;

Calls DeleteCustomer.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCustomerRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ideletecustomerrequest)`   
DeleteCustomerRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.protobuf.empty)>` | Promise  
  
### deleteCustomerRepricingConfig(request, callback)
    
    
    public deleteCustomerRepricingConfig(request: google.cloud.channel.v1.IDeleteCustomerRepricingConfigRequest, callback: google.cloud.channel.v1.CloudChannelService.DeleteCustomerRepricingConfigCallback): void;

Calls DeleteCustomerRepricingConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCustomerRepricingConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ideletecustomerrepricingconfigrequest)`   
DeleteCustomerRepricingConfigRequest message or plain object  
`callback` |  `[DeleteCustomerRepricingConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteCustomerRepricingConfig(request)
    
    
    public deleteCustomerRepricingConfig(request: google.cloud.channel.v1.IDeleteCustomerRepricingConfigRequest): Promise<google.protobuf.Empty>;

Calls DeleteCustomerRepricingConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCustomerRepricingConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ideletecustomerrepricingconfigrequest)`   
DeleteCustomerRepricingConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.protobuf.empty)>` | Promise  
  
### getChannelPartnerLink(request, callback)
    
    
    public getChannelPartnerLink(request: google.cloud.channel.v1.IGetChannelPartnerLinkRequest, callback: google.cloud.channel.v1.CloudChannelService.GetChannelPartnerLinkCallback): void;

Calls GetChannelPartnerLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetChannelPartnerLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.igetchannelpartnerlinkrequest)`   
GetChannelPartnerLinkRequest message or plain object  
`callback` |  `[GetChannelPartnerLinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and ChannelPartnerLink  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getChannelPartnerLink(request)
    
    
    public getChannelPartnerLink(request: google.cloud.channel.v1.IGetChannelPartnerLinkRequest): Promise<google.cloud.channel.v1.ChannelPartnerLink>;

Calls GetChannelPartnerLink.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetChannelPartnerLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.igetchannelpartnerlinkrequest)`   
GetChannelPartnerLinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.ChannelPartnerLink](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.channelpartnerlink)>` | Promise  
  
### getChannelPartnerRepricingConfig(request, callback)
    
    
    public getChannelPartnerRepricingConfig(request: google.cloud.channel.v1.IGetChannelPartnerRepricingConfigRequest, callback: google.cloud.channel.v1.CloudChannelService.GetChannelPartnerRepricingConfigCallback): void;

Calls GetChannelPartnerRepricingConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.igetchannelpartnerrepricingconfigrequest)`   
GetChannelPartnerRepricingConfigRequest message or plain object  
`callback` |  `[GetChannelPartnerRepricingConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and ChannelPartnerRepricingConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getChannelPartnerRepricingConfig(request)
    
    
    public getChannelPartnerRepricingConfig(request: google.cloud.channel.v1.IGetChannelPartnerRepricingConfigRequest): Promise<google.cloud.channel.v1.ChannelPartnerRepricingConfig>;

Calls GetChannelPartnerRepricingConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.igetchannelpartnerrepricingconfigrequest)`   
GetChannelPartnerRepricingConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.ChannelPartnerRepricingConfig](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.channelpartnerrepricingconfig)>` | Promise  
  
### getCustomer(request, callback)
    
    
    public getCustomer(request: google.cloud.channel.v1.IGetCustomerRequest, callback: google.cloud.channel.v1.CloudChannelService.GetCustomerCallback): void;

Calls GetCustomer.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCustomerRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.igetcustomerrequest)`   
GetCustomerRequest message or plain object  
`callback` |  `[GetCustomerCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and Customer  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCustomer(request)
    
    
    public getCustomer(request: google.cloud.channel.v1.IGetCustomerRequest): Promise<google.cloud.channel.v1.Customer>;

Calls GetCustomer.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetCustomerRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.igetcustomerrequest)`   
GetCustomerRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.Customer](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.customer-class)>` | Promise  
  
### getCustomerRepricingConfig(request, callback)
    
    
    public getCustomerRepricingConfig(request: google.cloud.channel.v1.IGetCustomerRepricingConfigRequest, callback: google.cloud.channel.v1.CloudChannelService.GetCustomerRepricingConfigCallback): void;

Calls GetCustomerRepricingConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCustomerRepricingConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.igetcustomerrepricingconfigrequest)`   
GetCustomerRepricingConfigRequest message or plain object  
`callback` |  `[GetCustomerRepricingConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and CustomerRepricingConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCustomerRepricingConfig(request)
    
    
    public getCustomerRepricingConfig(request: google.cloud.channel.v1.IGetCustomerRepricingConfigRequest): Promise<google.cloud.channel.v1.CustomerRepricingConfig>;

Calls GetCustomerRepricingConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetCustomerRepricingConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.igetcustomerrepricingconfigrequest)`   
GetCustomerRepricingConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.CustomerRepricingConfig](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.customerrepricingconfig)>` | Promise  
  
### getEntitlement(request, callback)
    
    
    public getEntitlement(request: google.cloud.channel.v1.IGetEntitlementRequest, callback: google.cloud.channel.v1.CloudChannelService.GetEntitlementCallback): void;

Calls GetEntitlement.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEntitlementRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.igetentitlementrequest)`   
GetEntitlementRequest message or plain object  
`callback` |  `[GetEntitlementCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and Entitlement  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEntitlement(request)
    
    
    public getEntitlement(request: google.cloud.channel.v1.IGetEntitlementRequest): Promise<google.cloud.channel.v1.Entitlement>;

Calls GetEntitlement.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetEntitlementRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.igetentitlementrequest)`   
GetEntitlementRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.Entitlement](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.entitlement-class)>` | Promise  
  
### importCustomer(request, callback)
    
    
    public importCustomer(request: google.cloud.channel.v1.IImportCustomerRequest, callback: google.cloud.channel.v1.CloudChannelService.ImportCustomerCallback): void;

Calls ImportCustomer.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportCustomerRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.iimportcustomerrequest)`   
ImportCustomerRequest message or plain object  
`callback` |  `[ImportCustomerCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and Customer  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importCustomer(request)
    
    
    public importCustomer(request: google.cloud.channel.v1.IImportCustomerRequest): Promise<google.cloud.channel.v1.Customer>;

Calls ImportCustomer.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IImportCustomerRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.iimportcustomerrequest)`   
ImportCustomerRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.Customer](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.customer-class)>` | Promise  
  
### listChannelPartnerLinks(request, callback)
    
    
    public listChannelPartnerLinks(request: google.cloud.channel.v1.IListChannelPartnerLinksRequest, callback: google.cloud.channel.v1.CloudChannelService.ListChannelPartnerLinksCallback): void;

Calls ListChannelPartnerLinks.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListChannelPartnerLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilistchannelpartnerlinksrequest)`   
ListChannelPartnerLinksRequest message or plain object  
`callback` |  `[ListChannelPartnerLinksCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and ListChannelPartnerLinksResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listChannelPartnerLinks(request)
    
    
    public listChannelPartnerLinks(request: google.cloud.channel.v1.IListChannelPartnerLinksRequest): Promise<google.cloud.channel.v1.ListChannelPartnerLinksResponse>;

Calls ListChannelPartnerLinks.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListChannelPartnerLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilistchannelpartnerlinksrequest)`   
ListChannelPartnerLinksRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.ListChannelPartnerLinksResponse](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.listchannelpartnerlinksresponse)>` | Promise  
  
### listChannelPartnerRepricingConfigs(request, callback)
    
    
    public listChannelPartnerRepricingConfigs(request: google.cloud.channel.v1.IListChannelPartnerRepricingConfigsRequest, callback: google.cloud.channel.v1.CloudChannelService.ListChannelPartnerRepricingConfigsCallback): void;

Calls ListChannelPartnerRepricingConfigs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListChannelPartnerRepricingConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilistchannelpartnerrepricingconfigsrequest)`   
ListChannelPartnerRepricingConfigsRequest message or plain object  
`callback` |  `[ListChannelPartnerRepricingConfigsCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and ListChannelPartnerRepricingConfigsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listChannelPartnerRepricingConfigs(request)
    
    
    public listChannelPartnerRepricingConfigs(request: google.cloud.channel.v1.IListChannelPartnerRepricingConfigsRequest): Promise<google.cloud.channel.v1.ListChannelPartnerRepricingConfigsResponse>;

Calls ListChannelPartnerRepricingConfigs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListChannelPartnerRepricingConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilistchannelpartnerrepricingconfigsrequest)`   
ListChannelPartnerRepricingConfigsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.ListChannelPartnerRepricingConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.listchannelpartnerrepricingconfigsresponse)>` | Promise  
  
### listCustomerRepricingConfigs(request, callback)
    
    
    public listCustomerRepricingConfigs(request: google.cloud.channel.v1.IListCustomerRepricingConfigsRequest, callback: google.cloud.channel.v1.CloudChannelService.ListCustomerRepricingConfigsCallback): void;

Calls ListCustomerRepricingConfigs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCustomerRepricingConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilistcustomerrepricingconfigsrequest)`   
ListCustomerRepricingConfigsRequest message or plain object  
`callback` |  `[ListCustomerRepricingConfigsCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and ListCustomerRepricingConfigsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCustomerRepricingConfigs(request)
    
    
    public listCustomerRepricingConfigs(request: google.cloud.channel.v1.IListCustomerRepricingConfigsRequest): Promise<google.cloud.channel.v1.ListCustomerRepricingConfigsResponse>;

Calls ListCustomerRepricingConfigs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListCustomerRepricingConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilistcustomerrepricingconfigsrequest)`   
ListCustomerRepricingConfigsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.ListCustomerRepricingConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.listcustomerrepricingconfigsresponse)>` | Promise  
  
### listCustomers(request, callback)
    
    
    public listCustomers(request: google.cloud.channel.v1.IListCustomersRequest, callback: google.cloud.channel.v1.CloudChannelService.ListCustomersCallback): void;

Calls ListCustomers.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCustomersRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilistcustomersrequest)`   
ListCustomersRequest message or plain object  
`callback` |  `[ListCustomersCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and ListCustomersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCustomers(request)
    
    
    public listCustomers(request: google.cloud.channel.v1.IListCustomersRequest): Promise<google.cloud.channel.v1.ListCustomersResponse>;

Calls ListCustomers.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListCustomersRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilistcustomersrequest)`   
ListCustomersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.ListCustomersResponse](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.listcustomersresponse)>` | Promise  
  
### listEntitlementChanges(request, callback)
    
    
    public listEntitlementChanges(request: google.cloud.channel.v1.IListEntitlementChangesRequest, callback: google.cloud.channel.v1.CloudChannelService.ListEntitlementChangesCallback): void;

Calls ListEntitlementChanges.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEntitlementChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilistentitlementchangesrequest)`   
ListEntitlementChangesRequest message or plain object  
`callback` |  `[ListEntitlementChangesCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and ListEntitlementChangesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEntitlementChanges(request)
    
    
    public listEntitlementChanges(request: google.cloud.channel.v1.IListEntitlementChangesRequest): Promise<google.cloud.channel.v1.ListEntitlementChangesResponse>;

Calls ListEntitlementChanges.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListEntitlementChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilistentitlementchangesrequest)`   
ListEntitlementChangesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.ListEntitlementChangesResponse](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.listentitlementchangesresponse)>` | Promise  
  
### listEntitlements(request, callback)
    
    
    public listEntitlements(request: google.cloud.channel.v1.IListEntitlementsRequest, callback: google.cloud.channel.v1.CloudChannelService.ListEntitlementsCallback): void;

Calls ListEntitlements.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEntitlementsRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilistentitlementsrequest)`   
ListEntitlementsRequest message or plain object  
`callback` |  `[ListEntitlementsCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and ListEntitlementsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEntitlements(request)
    
    
    public listEntitlements(request: google.cloud.channel.v1.IListEntitlementsRequest): Promise<google.cloud.channel.v1.ListEntitlementsResponse>;

Calls ListEntitlements.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListEntitlementsRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilistentitlementsrequest)`   
ListEntitlementsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.ListEntitlementsResponse](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.listentitlementsresponse)>` | Promise  
  
### listOffers(request, callback)
    
    
    public listOffers(request: google.cloud.channel.v1.IListOffersRequest, callback: google.cloud.channel.v1.CloudChannelService.ListOffersCallback): void;

Calls ListOffers.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilistoffersrequest)`   
ListOffersRequest message or plain object  
`callback` |  `[ListOffersCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and ListOffersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listOffers(request)
    
    
    public listOffers(request: google.cloud.channel.v1.IListOffersRequest): Promise<google.cloud.channel.v1.ListOffersResponse>;

Calls ListOffers.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilistoffersrequest)`   
ListOffersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.ListOffersResponse](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.listoffersresponse)>` | Promise  
  
### listProducts(request, callback)
    
    
    public listProducts(request: google.cloud.channel.v1.IListProductsRequest, callback: google.cloud.channel.v1.CloudChannelService.ListProductsCallback): void;

Calls ListProducts.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilistproductsrequest)`   
ListProductsRequest message or plain object  
`callback` |  `[ListProductsCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and ListProductsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listProducts(request)
    
    
    public listProducts(request: google.cloud.channel.v1.IListProductsRequest): Promise<google.cloud.channel.v1.ListProductsResponse>;

Calls ListProducts.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilistproductsrequest)`   
ListProductsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.ListProductsResponse](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.listproductsresponse)>` | Promise  
  
### listPurchasableOffers(request, callback)
    
    
    public listPurchasableOffers(request: google.cloud.channel.v1.IListPurchasableOffersRequest, callback: google.cloud.channel.v1.CloudChannelService.ListPurchasableOffersCallback): void;

Calls ListPurchasableOffers.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPurchasableOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilistpurchasableoffersrequest)`   
ListPurchasableOffersRequest message or plain object  
`callback` |  `[ListPurchasableOffersCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and ListPurchasableOffersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listPurchasableOffers(request)
    
    
    public listPurchasableOffers(request: google.cloud.channel.v1.IListPurchasableOffersRequest): Promise<google.cloud.channel.v1.ListPurchasableOffersResponse>;

Calls ListPurchasableOffers.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListPurchasableOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilistpurchasableoffersrequest)`   
ListPurchasableOffersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.ListPurchasableOffersResponse](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.listpurchasableoffersresponse)>` | Promise  
  
### listPurchasableSkus(request, callback)
    
    
    public listPurchasableSkus(request: google.cloud.channel.v1.IListPurchasableSkusRequest, callback: google.cloud.channel.v1.CloudChannelService.ListPurchasableSkusCallback): void;

Calls ListPurchasableSkus.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPurchasableSkusRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilistpurchasableskusrequest)`   
ListPurchasableSkusRequest message or plain object  
`callback` |  `[ListPurchasableSkusCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and ListPurchasableSkusResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listPurchasableSkus(request)
    
    
    public listPurchasableSkus(request: google.cloud.channel.v1.IListPurchasableSkusRequest): Promise<google.cloud.channel.v1.ListPurchasableSkusResponse>;

Calls ListPurchasableSkus.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListPurchasableSkusRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilistpurchasableskusrequest)`   
ListPurchasableSkusRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.ListPurchasableSkusResponse](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.listpurchasableskusresponse)>` | Promise  
  
### listSkuGroupBillableSkus(request, callback)
    
    
    public listSkuGroupBillableSkus(request: google.cloud.channel.v1.IListSkuGroupBillableSkusRequest, callback: google.cloud.channel.v1.CloudChannelService.ListSkuGroupBillableSkusCallback): void;

Calls ListSkuGroupBillableSkus.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSkuGroupBillableSkusRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilistskugroupbillableskusrequest)`   
ListSkuGroupBillableSkusRequest message or plain object  
`callback` |  `[ListSkuGroupBillableSkusCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and ListSkuGroupBillableSkusResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSkuGroupBillableSkus(request)
    
    
    public listSkuGroupBillableSkus(request: google.cloud.channel.v1.IListSkuGroupBillableSkusRequest): Promise<google.cloud.channel.v1.ListSkuGroupBillableSkusResponse>;

Calls ListSkuGroupBillableSkus.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListSkuGroupBillableSkusRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilistskugroupbillableskusrequest)`   
ListSkuGroupBillableSkusRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.ListSkuGroupBillableSkusResponse](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.listskugroupbillableskusresponse)>` | Promise  
  
### listSkuGroups(request, callback)
    
    
    public listSkuGroups(request: google.cloud.channel.v1.IListSkuGroupsRequest, callback: google.cloud.channel.v1.CloudChannelService.ListSkuGroupsCallback): void;

Calls ListSkuGroups.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSkuGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilistskugroupsrequest)`   
ListSkuGroupsRequest message or plain object  
`callback` |  `[ListSkuGroupsCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and ListSkuGroupsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSkuGroups(request)
    
    
    public listSkuGroups(request: google.cloud.channel.v1.IListSkuGroupsRequest): Promise<google.cloud.channel.v1.ListSkuGroupsResponse>;

Calls ListSkuGroups.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListSkuGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilistskugroupsrequest)`   
ListSkuGroupsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.ListSkuGroupsResponse](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.listskugroupsresponse)>` | Promise  
  
### listSkus(request, callback)
    
    
    public listSkus(request: google.cloud.channel.v1.IListSkusRequest, callback: google.cloud.channel.v1.CloudChannelService.ListSkusCallback): void;

Calls ListSkus.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSkusRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilistskusrequest)`   
ListSkusRequest message or plain object  
`callback` |  `[ListSkusCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and ListSkusResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSkus(request)
    
    
    public listSkus(request: google.cloud.channel.v1.IListSkusRequest): Promise<google.cloud.channel.v1.ListSkusResponse>;

Calls ListSkus.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListSkusRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilistskusrequest)`   
ListSkusRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.ListSkusResponse](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.listskusresponse)>` | Promise  
  
### listSubscribers(request, callback)
    
    
    public listSubscribers(request: google.cloud.channel.v1.IListSubscribersRequest, callback: google.cloud.channel.v1.CloudChannelService.ListSubscribersCallback): void;

Calls ListSubscribers.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSubscribersRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilistsubscribersrequest)`   
ListSubscribersRequest message or plain object  
`callback` |  `[ListSubscribersCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and ListSubscribersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSubscribers(request)
    
    
    public listSubscribers(request: google.cloud.channel.v1.IListSubscribersRequest): Promise<google.cloud.channel.v1.ListSubscribersResponse>;

Calls ListSubscribers.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListSubscribersRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilistsubscribersrequest)`   
ListSubscribersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.ListSubscribersResponse](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.listsubscribersresponse)>` | Promise  
  
### listTransferableOffers(request, callback)
    
    
    public listTransferableOffers(request: google.cloud.channel.v1.IListTransferableOffersRequest, callback: google.cloud.channel.v1.CloudChannelService.ListTransferableOffersCallback): void;

Calls ListTransferableOffers.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTransferableOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilisttransferableoffersrequest)`   
ListTransferableOffersRequest message or plain object  
`callback` |  `[ListTransferableOffersCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and ListTransferableOffersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTransferableOffers(request)
    
    
    public listTransferableOffers(request: google.cloud.channel.v1.IListTransferableOffersRequest): Promise<google.cloud.channel.v1.ListTransferableOffersResponse>;

Calls ListTransferableOffers.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListTransferableOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilisttransferableoffersrequest)`   
ListTransferableOffersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.ListTransferableOffersResponse](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.listtransferableoffersresponse)>` | Promise  
  
### listTransferableSkus(request, callback)
    
    
    public listTransferableSkus(request: google.cloud.channel.v1.IListTransferableSkusRequest, callback: google.cloud.channel.v1.CloudChannelService.ListTransferableSkusCallback): void;

Calls ListTransferableSkus.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTransferableSkusRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilisttransferableskusrequest)`   
ListTransferableSkusRequest message or plain object  
`callback` |  `[ListTransferableSkusCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and ListTransferableSkusResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTransferableSkus(request)
    
    
    public listTransferableSkus(request: google.cloud.channel.v1.IListTransferableSkusRequest): Promise<google.cloud.channel.v1.ListTransferableSkusResponse>;

Calls ListTransferableSkus.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListTransferableSkusRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilisttransferableskusrequest)`   
ListTransferableSkusRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.ListTransferableSkusResponse](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.listtransferableskusresponse)>` | Promise  
  
### lookupOffer(request, callback)
    
    
    public lookupOffer(request: google.cloud.channel.v1.ILookupOfferRequest, callback: google.cloud.channel.v1.CloudChannelService.LookupOfferCallback): void;

Calls LookupOffer.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILookupOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilookupofferrequest)`   
LookupOfferRequest message or plain object  
`callback` |  `[LookupOfferCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and Offer  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### lookupOffer(request)
    
    
    public lookupOffer(request: google.cloud.channel.v1.ILookupOfferRequest): Promise<google.cloud.channel.v1.Offer>;

Calls LookupOffer.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ILookupOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilookupofferrequest)`   
LookupOfferRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.Offer](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.offer)>` | Promise  
  
### provisionCloudIdentity(request, callback)
    
    
    public provisionCloudIdentity(request: google.cloud.channel.v1.IProvisionCloudIdentityRequest, callback: google.cloud.channel.v1.CloudChannelService.ProvisionCloudIdentityCallback): void;

Calls ProvisionCloudIdentity.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IProvisionCloudIdentityRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.iprovisioncloudidentityrequest)`   
ProvisionCloudIdentityRequest message or plain object  
`callback` |  `[ProvisionCloudIdentityCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### provisionCloudIdentity(request)
    
    
    public provisionCloudIdentity(request: google.cloud.channel.v1.IProvisionCloudIdentityRequest): Promise<google.longrunning.Operation>;

Calls ProvisionCloudIdentity.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IProvisionCloudIdentityRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.iprovisioncloudidentityrequest)`   
ProvisionCloudIdentityRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.longrunning.operation)>` | Promise  
  
### queryEligibleBillingAccounts(request, callback)
    
    
    public queryEligibleBillingAccounts(request: google.cloud.channel.v1.IQueryEligibleBillingAccountsRequest, callback: google.cloud.channel.v1.CloudChannelService.QueryEligibleBillingAccountsCallback): void;

Calls QueryEligibleBillingAccounts.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryEligibleBillingAccountsRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.iqueryeligiblebillingaccountsrequest)`   
QueryEligibleBillingAccountsRequest message or plain object  
`callback` |  `[QueryEligibleBillingAccountsCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and QueryEligibleBillingAccountsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryEligibleBillingAccounts(request)
    
    
    public queryEligibleBillingAccounts(request: google.cloud.channel.v1.IQueryEligibleBillingAccountsRequest): Promise<google.cloud.channel.v1.QueryEligibleBillingAccountsResponse>;

Calls QueryEligibleBillingAccounts.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IQueryEligibleBillingAccountsRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.iqueryeligiblebillingaccountsrequest)`   
QueryEligibleBillingAccountsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.QueryEligibleBillingAccountsResponse](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.queryeligiblebillingaccountsresponse)>` | Promise  
  
### registerSubscriber(request, callback)
    
    
    public registerSubscriber(request: google.cloud.channel.v1.IRegisterSubscriberRequest, callback: google.cloud.channel.v1.CloudChannelService.RegisterSubscriberCallback): void;

Calls RegisterSubscriber.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRegisterSubscriberRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.iregistersubscriberrequest)`   
RegisterSubscriberRequest message or plain object  
`callback` |  `[RegisterSubscriberCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and RegisterSubscriberResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### registerSubscriber(request)
    
    
    public registerSubscriber(request: google.cloud.channel.v1.IRegisterSubscriberRequest): Promise<google.cloud.channel.v1.RegisterSubscriberResponse>;

Calls RegisterSubscriber.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRegisterSubscriberRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.iregistersubscriberrequest)`   
RegisterSubscriberRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.RegisterSubscriberResponse](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.registersubscriberresponse)>` | Promise  
  
### startPaidService(request, callback)
    
    
    public startPaidService(request: google.cloud.channel.v1.IStartPaidServiceRequest, callback: google.cloud.channel.v1.CloudChannelService.StartPaidServiceCallback): void;

Calls StartPaidService.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IStartPaidServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.istartpaidservicerequest)`   
StartPaidServiceRequest message or plain object  
`callback` |  `[StartPaidServiceCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### startPaidService(request)
    
    
    public startPaidService(request: google.cloud.channel.v1.IStartPaidServiceRequest): Promise<google.longrunning.Operation>;

Calls StartPaidService.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IStartPaidServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.istartpaidservicerequest)`   
StartPaidServiceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.longrunning.operation)>` | Promise  
  
### suspendEntitlement(request, callback)
    
    
    public suspendEntitlement(request: google.cloud.channel.v1.ISuspendEntitlementRequest, callback: google.cloud.channel.v1.CloudChannelService.SuspendEntitlementCallback): void;

Calls SuspendEntitlement.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISuspendEntitlementRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.isuspendentitlementrequest)`   
SuspendEntitlementRequest message or plain object  
`callback` |  `[SuspendEntitlementCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### suspendEntitlement(request)
    
    
    public suspendEntitlement(request: google.cloud.channel.v1.ISuspendEntitlementRequest): Promise<google.longrunning.Operation>;

Calls SuspendEntitlement.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISuspendEntitlementRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.isuspendentitlementrequest)`   
SuspendEntitlementRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.longrunning.operation)>` | Promise  
  
### transferEntitlements(request, callback)
    
    
    public transferEntitlements(request: google.cloud.channel.v1.ITransferEntitlementsRequest, callback: google.cloud.channel.v1.CloudChannelService.TransferEntitlementsCallback): void;

Calls TransferEntitlements.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITransferEntitlementsRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.itransferentitlementsrequest)`   
TransferEntitlementsRequest message or plain object  
`callback` |  `[TransferEntitlementsCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### transferEntitlements(request)
    
    
    public transferEntitlements(request: google.cloud.channel.v1.ITransferEntitlementsRequest): Promise<google.longrunning.Operation>;

Calls TransferEntitlements.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ITransferEntitlementsRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.itransferentitlementsrequest)`   
TransferEntitlementsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.longrunning.operation)>` | Promise  
  
### transferEntitlementsToGoogle(request, callback)
    
    
    public transferEntitlementsToGoogle(request: google.cloud.channel.v1.ITransferEntitlementsToGoogleRequest, callback: google.cloud.channel.v1.CloudChannelService.TransferEntitlementsToGoogleCallback): void;

Calls TransferEntitlementsToGoogle.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITransferEntitlementsToGoogleRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.itransferentitlementstogooglerequest)`   
TransferEntitlementsToGoogleRequest message or plain object  
`callback` |  `[TransferEntitlementsToGoogleCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### transferEntitlementsToGoogle(request)
    
    
    public transferEntitlementsToGoogle(request: google.cloud.channel.v1.ITransferEntitlementsToGoogleRequest): Promise<google.longrunning.Operation>;

Calls TransferEntitlementsToGoogle.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ITransferEntitlementsToGoogleRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.itransferentitlementstogooglerequest)`   
TransferEntitlementsToGoogleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.longrunning.operation)>` | Promise  
  
### unregisterSubscriber(request, callback)
    
    
    public unregisterSubscriber(request: google.cloud.channel.v1.IUnregisterSubscriberRequest, callback: google.cloud.channel.v1.CloudChannelService.UnregisterSubscriberCallback): void;

Calls UnregisterSubscriber.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUnregisterSubscriberRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.iunregistersubscriberrequest)`   
UnregisterSubscriberRequest message or plain object  
`callback` |  `[UnregisterSubscriberCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and UnregisterSubscriberResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### unregisterSubscriber(request)
    
    
    public unregisterSubscriber(request: google.cloud.channel.v1.IUnregisterSubscriberRequest): Promise<google.cloud.channel.v1.UnregisterSubscriberResponse>;

Calls UnregisterSubscriber.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUnregisterSubscriberRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.iunregistersubscriberrequest)`   
UnregisterSubscriberRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.UnregisterSubscriberResponse](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.unregistersubscriberresponse)>` | Promise  
  
### updateChannelPartnerLink(request, callback)
    
    
    public updateChannelPartnerLink(request: google.cloud.channel.v1.IUpdateChannelPartnerLinkRequest, callback: google.cloud.channel.v1.CloudChannelService.UpdateChannelPartnerLinkCallback): void;

Calls UpdateChannelPartnerLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateChannelPartnerLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.iupdatechannelpartnerlinkrequest)`   
UpdateChannelPartnerLinkRequest message or plain object  
`callback` |  `[UpdateChannelPartnerLinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and ChannelPartnerLink  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateChannelPartnerLink(request)
    
    
    public updateChannelPartnerLink(request: google.cloud.channel.v1.IUpdateChannelPartnerLinkRequest): Promise<google.cloud.channel.v1.ChannelPartnerLink>;

Calls UpdateChannelPartnerLink.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateChannelPartnerLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.iupdatechannelpartnerlinkrequest)`   
UpdateChannelPartnerLinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.ChannelPartnerLink](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.channelpartnerlink)>` | Promise  
  
### updateChannelPartnerRepricingConfig(request, callback)
    
    
    public updateChannelPartnerRepricingConfig(request: google.cloud.channel.v1.IUpdateChannelPartnerRepricingConfigRequest, callback: google.cloud.channel.v1.CloudChannelService.UpdateChannelPartnerRepricingConfigCallback): void;

Calls UpdateChannelPartnerRepricingConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.iupdatechannelpartnerrepricingconfigrequest)`   
UpdateChannelPartnerRepricingConfigRequest message or plain object  
`callback` |  `[UpdateChannelPartnerRepricingConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and ChannelPartnerRepricingConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateChannelPartnerRepricingConfig(request)
    
    
    public updateChannelPartnerRepricingConfig(request: google.cloud.channel.v1.IUpdateChannelPartnerRepricingConfigRequest): Promise<google.cloud.channel.v1.ChannelPartnerRepricingConfig>;

Calls UpdateChannelPartnerRepricingConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.iupdatechannelpartnerrepricingconfigrequest)`   
UpdateChannelPartnerRepricingConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.ChannelPartnerRepricingConfig](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.channelpartnerrepricingconfig)>` | Promise  
  
### updateCustomer(request, callback)
    
    
    public updateCustomer(request: google.cloud.channel.v1.IUpdateCustomerRequest, callback: google.cloud.channel.v1.CloudChannelService.UpdateCustomerCallback): void;

Calls UpdateCustomer.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCustomerRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.iupdatecustomerrequest)`   
UpdateCustomerRequest message or plain object  
`callback` |  `[UpdateCustomerCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and Customer  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCustomer(request)
    
    
    public updateCustomer(request: google.cloud.channel.v1.IUpdateCustomerRequest): Promise<google.cloud.channel.v1.Customer>;

Calls UpdateCustomer.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCustomerRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.iupdatecustomerrequest)`   
UpdateCustomerRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.Customer](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.customer-class)>` | Promise  
  
### updateCustomerRepricingConfig(request, callback)
    
    
    public updateCustomerRepricingConfig(request: google.cloud.channel.v1.IUpdateCustomerRepricingConfigRequest, callback: google.cloud.channel.v1.CloudChannelService.UpdateCustomerRepricingConfigCallback): void;

Calls UpdateCustomerRepricingConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCustomerRepricingConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.iupdatecustomerrepricingconfigrequest)`   
UpdateCustomerRepricingConfigRequest message or plain object  
`callback` |  `[UpdateCustomerRepricingConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and CustomerRepricingConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCustomerRepricingConfig(request)
    
    
    public updateCustomerRepricingConfig(request: google.cloud.channel.v1.IUpdateCustomerRepricingConfigRequest): Promise<google.cloud.channel.v1.CustomerRepricingConfig>;

Calls UpdateCustomerRepricingConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCustomerRepricingConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.iupdatecustomerrepricingconfigrequest)`   
UpdateCustomerRepricingConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.CustomerRepricingConfig](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.customerrepricingconfig)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
