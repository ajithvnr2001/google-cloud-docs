---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceGrpc
title: Class CloudChannelServiceGrpc (3.103.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:55:46.338909+00:00
---

# Class CloudChannelServiceGrpc (3.103.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceGrpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CloudChannelServiceGrpc (3.103.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.103.0 (latest)  3.99.0  3.98.0  3.97.0  3.95.0  3.92.0  3.91.0  3.89.0  3.87.0  3.86.0  3.85.0  3.84.0  3.82.0  3.80.0  3.79.0  3.78.0  3.77.0  3.76.0  3.74.0  3.72.0  3.71.0  3.68.0  3.67.0  3.66.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.6  3.6.1  3.5.1  3.3.1 
    
    
    public final class CloudChannelServiceGrpc

CloudChannelService lets Google cloud resellers and distributors manage their customers, channel partners, entitlements, and reports. Using this service:

  1. Resellers and distributors can manage a customer entity.
  2. Distributors can register an authorized reseller in their channel and provide them with delegated admin access.
  3. Resellers and distributors can manage customer entitlements. CloudChannelService exposes the following resources:
  4. Customers: An entity-usually an enterprise-managed by a reseller or distributor.
  5. Entitlements: An entity that provides a customer with the means to use a service. Entitlements are created or updated as a result of a successful fulfillment.
  6. ChannelPartnerLinks: An entity that identifies links between distributors and their indirect resellers in a channel.



## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CloudChannelServiceGrpc

## Inherited Members

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Fields 

### SERVICE_NAME
    
    
    public static final String SERVICE_NAME

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
## Static Methods 

### bindService(CloudChannelServiceGrpc.AsyncService service)
    
    
    public static final ServerServiceDefinition bindService(CloudChannelServiceGrpc.AsyncService service)

**Parameter**  
---  
**Name** | **Description**  
`service` | `[CloudChannelServiceGrpc.AsyncService](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceGrpc.AsyncService)`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServerServiceDefinition` |   
  
### getActivateEntitlementMethod()
    
    
    public static MethodDescriptor<ActivateEntitlementRequest,Operation> getActivateEntitlementMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ActivateEntitlementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ActivateEntitlementRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getCancelEntitlementMethod()
    
    
    public static MethodDescriptor<CancelEntitlementRequest,Operation> getCancelEntitlementMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CancelEntitlementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CancelEntitlementRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getChangeOfferMethod()
    
    
    public static MethodDescriptor<ChangeOfferRequest,Operation> getChangeOfferMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ChangeOfferRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChangeOfferRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getChangeParametersMethod()
    
    
    public static MethodDescriptor<ChangeParametersRequest,Operation> getChangeParametersMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ChangeParametersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChangeParametersRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getChangeRenewalSettingsMethod()
    
    
    public static MethodDescriptor<ChangeRenewalSettingsRequest,Operation> getChangeRenewalSettingsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ChangeRenewalSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChangeRenewalSettingsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getCheckCloudIdentityAccountsExistMethod()
    
    
    public static MethodDescriptor<CheckCloudIdentityAccountsExistRequest,CheckCloudIdentityAccountsExistResponse> getCheckCloudIdentityAccountsExistMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CheckCloudIdentityAccountsExistRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CheckCloudIdentityAccountsExistRequest),[CheckCloudIdentityAccountsExistResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CheckCloudIdentityAccountsExistResponse)>` |   
  
### getCreateChannelPartnerLinkMethod()
    
    
    public static MethodDescriptor<CreateChannelPartnerLinkRequest,ChannelPartnerLink> getCreateChannelPartnerLinkMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateChannelPartnerLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CreateChannelPartnerLinkRequest),[ChannelPartnerLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerLink)>` |   
  
### getCreateChannelPartnerRepricingConfigMethod()
    
    
    public static MethodDescriptor<CreateChannelPartnerRepricingConfigRequest,ChannelPartnerRepricingConfig> getCreateChannelPartnerRepricingConfigMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CreateChannelPartnerRepricingConfigRequest),[ChannelPartnerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerRepricingConfig)>` |   
  
### getCreateCustomerMethod()
    
    
    public static MethodDescriptor<CreateCustomerRequest,Customer> getCreateCustomerMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateCustomerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CreateCustomerRequest),[Customer](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Customer)>` |   
  
### getCreateCustomerRepricingConfigMethod()
    
    
    public static MethodDescriptor<CreateCustomerRepricingConfigRequest,CustomerRepricingConfig> getCreateCustomerRepricingConfigMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateCustomerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CreateCustomerRepricingConfigRequest),[CustomerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CustomerRepricingConfig)>` |   
  
### getCreateEntitlementMethod()
    
    
    public static MethodDescriptor<CreateEntitlementRequest,Operation> getCreateEntitlementMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateEntitlementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CreateEntitlementRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getDeleteChannelPartnerRepricingConfigMethod()
    
    
    public static MethodDescriptor<DeleteChannelPartnerRepricingConfigRequest,Empty> getDeleteChannelPartnerRepricingConfigMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.DeleteChannelPartnerRepricingConfigRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getDeleteCustomerMethod()
    
    
    public static MethodDescriptor<DeleteCustomerRequest,Empty> getDeleteCustomerMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteCustomerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.DeleteCustomerRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getDeleteCustomerRepricingConfigMethod()
    
    
    public static MethodDescriptor<DeleteCustomerRepricingConfigRequest,Empty> getDeleteCustomerRepricingConfigMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteCustomerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.DeleteCustomerRepricingConfigRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getGetChannelPartnerLinkMethod()
    
    
    public static MethodDescriptor<GetChannelPartnerLinkRequest,ChannelPartnerLink> getGetChannelPartnerLinkMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetChannelPartnerLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.GetChannelPartnerLinkRequest),[ChannelPartnerLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerLink)>` |   
  
### getGetChannelPartnerRepricingConfigMethod()
    
    
    public static MethodDescriptor<GetChannelPartnerRepricingConfigRequest,ChannelPartnerRepricingConfig> getGetChannelPartnerRepricingConfigMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.GetChannelPartnerRepricingConfigRequest),[ChannelPartnerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerRepricingConfig)>` |   
  
### getGetCustomerMethod()
    
    
    public static MethodDescriptor<GetCustomerRequest,Customer> getGetCustomerMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetCustomerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.GetCustomerRequest),[Customer](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Customer)>` |   
  
### getGetCustomerRepricingConfigMethod()
    
    
    public static MethodDescriptor<GetCustomerRepricingConfigRequest,CustomerRepricingConfig> getGetCustomerRepricingConfigMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetCustomerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.GetCustomerRepricingConfigRequest),[CustomerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CustomerRepricingConfig)>` |   
  
### getGetEntitlementMethod()
    
    
    public static MethodDescriptor<GetEntitlementRequest,Entitlement> getGetEntitlementMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetEntitlementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.GetEntitlementRequest),[Entitlement](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Entitlement)>` |   
  
### getImportCustomerMethod()
    
    
    public static MethodDescriptor<ImportCustomerRequest,Customer> getImportCustomerMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ImportCustomerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ImportCustomerRequest),[Customer](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Customer)>` |   
  
### getListChannelPartnerLinksMethod()
    
    
    public static MethodDescriptor<ListChannelPartnerLinksRequest,ListChannelPartnerLinksResponse> getListChannelPartnerLinksMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListChannelPartnerLinksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListChannelPartnerLinksRequest),[ListChannelPartnerLinksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListChannelPartnerLinksResponse)>` |   
  
### getListChannelPartnerRepricingConfigsMethod()
    
    
    public static MethodDescriptor<ListChannelPartnerRepricingConfigsRequest,ListChannelPartnerRepricingConfigsResponse> getListChannelPartnerRepricingConfigsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListChannelPartnerRepricingConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListChannelPartnerRepricingConfigsRequest),[ListChannelPartnerRepricingConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListChannelPartnerRepricingConfigsResponse)>` |   
  
### getListCustomerRepricingConfigsMethod()
    
    
    public static MethodDescriptor<ListCustomerRepricingConfigsRequest,ListCustomerRepricingConfigsResponse> getListCustomerRepricingConfigsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListCustomerRepricingConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListCustomerRepricingConfigsRequest),[ListCustomerRepricingConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListCustomerRepricingConfigsResponse)>` |   
  
### getListCustomersMethod()
    
    
    public static MethodDescriptor<ListCustomersRequest,ListCustomersResponse> getListCustomersMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListCustomersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListCustomersRequest),[ListCustomersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListCustomersResponse)>` |   
  
### getListEntitlementChangesMethod()
    
    
    public static MethodDescriptor<ListEntitlementChangesRequest,ListEntitlementChangesResponse> getListEntitlementChangesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListEntitlementChangesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListEntitlementChangesRequest),[ListEntitlementChangesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListEntitlementChangesResponse)>` |   
  
### getListEntitlementsMethod()
    
    
    public static MethodDescriptor<ListEntitlementsRequest,ListEntitlementsResponse> getListEntitlementsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListEntitlementsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListEntitlementsRequest),[ListEntitlementsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListEntitlementsResponse)>` |   
  
### getListOffersMethod()
    
    
    public static MethodDescriptor<ListOffersRequest,ListOffersResponse> getListOffersMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListOffersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListOffersRequest),[ListOffersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListOffersResponse)>` |   
  
### getListProductsMethod()
    
    
    public static MethodDescriptor<ListProductsRequest,ListProductsResponse> getListProductsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListProductsRequest),[ListProductsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListProductsResponse)>` |   
  
### getListPurchasableOffersMethod()
    
    
    public static MethodDescriptor<ListPurchasableOffersRequest,ListPurchasableOffersResponse> getListPurchasableOffersMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListPurchasableOffersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListPurchasableOffersRequest),[ListPurchasableOffersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListPurchasableOffersResponse)>` |   
  
### getListPurchasableSkusMethod()
    
    
    public static MethodDescriptor<ListPurchasableSkusRequest,ListPurchasableSkusResponse> getListPurchasableSkusMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListPurchasableSkusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListPurchasableSkusRequest),[ListPurchasableSkusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListPurchasableSkusResponse)>` |   
  
### getListSkuGroupBillableSkusMethod()
    
    
    public static MethodDescriptor<ListSkuGroupBillableSkusRequest,ListSkuGroupBillableSkusResponse> getListSkuGroupBillableSkusMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListSkuGroupBillableSkusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSkuGroupBillableSkusRequest),[ListSkuGroupBillableSkusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSkuGroupBillableSkusResponse)>` |   
  
### getListSkuGroupsMethod()
    
    
    public static MethodDescriptor<ListSkuGroupsRequest,ListSkuGroupsResponse> getListSkuGroupsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListSkuGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSkuGroupsRequest),[ListSkuGroupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSkuGroupsResponse)>` |   
  
### getListSkusMethod()
    
    
    public static MethodDescriptor<ListSkusRequest,ListSkusResponse> getListSkusMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListSkusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSkusRequest),[ListSkusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSkusResponse)>` |   
  
### getListSubscribersMethod()
    
    
    public static MethodDescriptor<ListSubscribersRequest,ListSubscribersResponse> getListSubscribersMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListSubscribersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSubscribersRequest),[ListSubscribersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSubscribersResponse)>` |   
  
### getListTransferableOffersMethod()
    
    
    public static MethodDescriptor<ListTransferableOffersRequest,ListTransferableOffersResponse> getListTransferableOffersMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListTransferableOffersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListTransferableOffersRequest),[ListTransferableOffersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListTransferableOffersResponse)>` |   
  
### getListTransferableSkusMethod()
    
    
    public static MethodDescriptor<ListTransferableSkusRequest,ListTransferableSkusResponse> getListTransferableSkusMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListTransferableSkusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListTransferableSkusRequest),[ListTransferableSkusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListTransferableSkusResponse)>` |   
  
### getLookupOfferMethod()
    
    
    public static MethodDescriptor<LookupOfferRequest,Offer> getLookupOfferMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[LookupOfferRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.LookupOfferRequest),[Offer](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Offer)>` |   
  
### getProvisionCloudIdentityMethod()
    
    
    public static MethodDescriptor<ProvisionCloudIdentityRequest,Operation> getProvisionCloudIdentityMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ProvisionCloudIdentityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ProvisionCloudIdentityRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getQueryEligibleBillingAccountsMethod()
    
    
    public static MethodDescriptor<QueryEligibleBillingAccountsRequest,QueryEligibleBillingAccountsResponse> getQueryEligibleBillingAccountsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[QueryEligibleBillingAccountsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.QueryEligibleBillingAccountsRequest),[QueryEligibleBillingAccountsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.QueryEligibleBillingAccountsResponse)>` |   
  
### getRegisterSubscriberMethod()
    
    
    public static MethodDescriptor<RegisterSubscriberRequest,RegisterSubscriberResponse> getRegisterSubscriberMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[RegisterSubscriberRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.RegisterSubscriberRequest),[RegisterSubscriberResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.RegisterSubscriberResponse)>` |   
  
### getServiceDescriptor()
    
    
    public static ServiceDescriptor getServiceDescriptor()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServiceDescriptor` |   
  
### getStartPaidServiceMethod()
    
    
    public static MethodDescriptor<StartPaidServiceRequest,Operation> getStartPaidServiceMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[StartPaidServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.StartPaidServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getSuspendEntitlementMethod()
    
    
    public static MethodDescriptor<SuspendEntitlementRequest,Operation> getSuspendEntitlementMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[SuspendEntitlementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.SuspendEntitlementRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getTransferEntitlementsMethod()
    
    
    public static MethodDescriptor<TransferEntitlementsRequest,Operation> getTransferEntitlementsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[TransferEntitlementsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.TransferEntitlementsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getTransferEntitlementsToGoogleMethod()
    
    
    public static MethodDescriptor<TransferEntitlementsToGoogleRequest,Operation> getTransferEntitlementsToGoogleMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[TransferEntitlementsToGoogleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.TransferEntitlementsToGoogleRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getUnregisterSubscriberMethod()
    
    
    public static MethodDescriptor<UnregisterSubscriberRequest,UnregisterSubscriberResponse> getUnregisterSubscriberMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UnregisterSubscriberRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.UnregisterSubscriberRequest),[UnregisterSubscriberResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.UnregisterSubscriberResponse)>` |   
  
### getUpdateChannelPartnerLinkMethod()
    
    
    public static MethodDescriptor<UpdateChannelPartnerLinkRequest,ChannelPartnerLink> getUpdateChannelPartnerLinkMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateChannelPartnerLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.UpdateChannelPartnerLinkRequest),[ChannelPartnerLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerLink)>` |   
  
### getUpdateChannelPartnerRepricingConfigMethod()
    
    
    public static MethodDescriptor<UpdateChannelPartnerRepricingConfigRequest,ChannelPartnerRepricingConfig> getUpdateChannelPartnerRepricingConfigMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.UpdateChannelPartnerRepricingConfigRequest),[ChannelPartnerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerRepricingConfig)>` |   
  
### getUpdateCustomerMethod()
    
    
    public static MethodDescriptor<UpdateCustomerRequest,Customer> getUpdateCustomerMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateCustomerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.UpdateCustomerRequest),[Customer](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Customer)>` |   
  
### getUpdateCustomerRepricingConfigMethod()
    
    
    public static MethodDescriptor<UpdateCustomerRepricingConfigRequest,CustomerRepricingConfig> getUpdateCustomerRepricingConfigMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateCustomerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.UpdateCustomerRepricingConfigRequest),[CustomerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CustomerRepricingConfig)>` |   
  
### newBlockingStub(Channel channel)
    
    
    public static CloudChannelServiceGrpc.CloudChannelServiceBlockingStub newBlockingStub(Channel channel)

Creates a new blocking-style stub that supports unary and streaming output calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceGrpc.CloudChannelServiceBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceGrpc.CloudChannelServiceBlockingStub)` |   
  
### newBlockingV2Stub(Channel channel)
    
    
    public static CloudChannelServiceGrpc.CloudChannelServiceBlockingV2Stub newBlockingV2Stub(Channel channel)

Creates a new blocking-style stub that supports all types of calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceGrpc.CloudChannelServiceBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceGrpc.CloudChannelServiceBlockingV2Stub)` |   
  
### newFutureStub(Channel channel)
    
    
    public static CloudChannelServiceGrpc.CloudChannelServiceFutureStub newFutureStub(Channel channel)

Creates a new ListenableFuture-style stub that supports unary calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceGrpc.CloudChannelServiceFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceGrpc.CloudChannelServiceFutureStub)` |   
  
### newStub(Channel channel)
    
    
    public static CloudChannelServiceGrpc.CloudChannelServiceStub newStub(Channel channel)

Creates a new async stub that supports all call types for the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceGrpc.CloudChannelServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceGrpc.CloudChannelServiceStub)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
