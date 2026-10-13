---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceGrpc.AsyncService
title: Interface CloudChannelServiceGrpc.AsyncService (3.103.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:32:40.998131+00:00
---

# Interface CloudChannelServiceGrpc.AsyncService (3.103.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CloudChannelServiceGrpc.AsyncService (3.103.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.103.0 (latest)  3.99.0  3.98.0  3.97.0  3.95.0  3.92.0  3.91.0  3.89.0  3.87.0  3.86.0  3.85.0  3.84.0  3.82.0  3.80.0  3.79.0  3.78.0  3.77.0  3.76.0  3.74.0  3.72.0  3.71.0  3.68.0  3.67.0  3.66.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.6  3.6.1  3.5.1  3.3.1 
    
    
    public static interface CloudChannelServiceGrpc.AsyncService

CloudChannelService lets Google cloud resellers and distributors manage their customers, channel partners, entitlements, and reports. Using this service:

  1. Resellers and distributors can manage a customer entity.
  2. Distributors can register an authorized reseller in their channel and provide them with delegated admin access.
  3. Resellers and distributors can manage customer entitlements. CloudChannelService exposes the following resources:
  4. Customers: An entity-usually an enterprise-managed by a reseller or distributor.
  5. Entitlements: An entity that provides a customer with the means to use a service. Entitlements are created or updated as a result of a successful fulfillment.
  6. ChannelPartnerLinks: An entity that identifies links between distributors and their indirect resellers in a channel.



## Methods 

### activateEntitlement(ActivateEntitlementRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void activateEntitlement(ActivateEntitlementRequest request, StreamObserver<Operation> responseObserver)

Activates a previously suspended entitlement. Entitlements suspended for pending ToS acceptance can't be activated using this method. An entitlement activation is a long-running operation and it updates the state of the customer entitlement. Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * NOT_FOUND: Entitlement resource not found.
  * SUSPENSION_NOT_RESELLER_INITIATED: Can only activate reseller-initiated suspensions and entitlements that have accepted the TOS.
  * NOT_SUSPENDED: Can only activate suspended entitlements not in an ACTIVE state.
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: The ID of a long-running operation. To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ActivateEntitlementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ActivateEntitlementRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### cancelEntitlement(CancelEntitlementRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void cancelEntitlement(CancelEntitlementRequest request, StreamObserver<Operation> responseObserver)

Cancels a previously fulfilled entitlement. An entitlement cancellation is a long-running operation. Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request.
  * FAILED_PRECONDITION: There are Google Cloud projects linked to the Google Cloud entitlement's Cloud Billing subaccount.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * NOT_FOUND: Entitlement resource not found.
  * DELETION_TYPE_NOT_ALLOWED: Cancel is only allowed for Google Workspace add-ons, or entitlements for Google Cloud's development platform.
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: The ID of a long-running operation. To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The response will contain google.protobuf.Empty on success. The Operation metadata will contain an instance of OperationMetadata.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CancelEntitlementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CancelEntitlementRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### changeOffer(ChangeOfferRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void changeOffer(ChangeOfferRequest request, StreamObserver<Operation> responseObserver)

Updates the Offer for an existing customer entitlement. An entitlement update is a long-running operation and it updates the entitlement as a result of fulfillment. Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * NOT_FOUND: Offer or Entitlement resource not found.
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: The ID of a long-running operation. To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ChangeOfferRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChangeOfferRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### changeParameters(ChangeParametersRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void changeParameters(ChangeParametersRequest request, StreamObserver<Operation> responseObserver)

Change parameters of the entitlement. An entitlement update is a long-running operation and it updates the entitlement as a result of fulfillment. Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. For example, the number of seats being changed is greater than the allowed number of max seats, or decreasing seats for a commitment based plan.
  * NOT_FOUND: Entitlement resource not found.
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: The ID of a long-running operation. To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ChangeParametersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChangeParametersRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### changeRenewalSettings(ChangeRenewalSettingsRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void changeRenewalSettings(ChangeRenewalSettingsRequest request, StreamObserver<Operation> responseObserver)

Updates the renewal settings for an existing customer entitlement. An entitlement update is a long-running operation and it updates the entitlement as a result of fulfillment. Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * NOT_FOUND: Entitlement resource not found.
  * NOT_COMMITMENT_PLAN: Renewal Settings are only applicable for a commitment plan. Can't enable or disable renewals for non-commitment plans.
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: The ID of a long-running operation. To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ChangeRenewalSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChangeRenewalSettingsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### checkCloudIdentityAccountsExist(CheckCloudIdentityAccountsExistRequest request, StreamObserver<CheckCloudIdentityAccountsExistResponse> responseObserver)
    
    
    public default void checkCloudIdentityAccountsExist(CheckCloudIdentityAccountsExistRequest request, StreamObserver<CheckCloudIdentityAccountsExistResponse> responseObserver)

Confirms the existence of Cloud Identity accounts based on the domain and if the Cloud Identity accounts are owned by the reseller. Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * INVALID_VALUE: Invalid domain value in the request. Return value: A list of CloudIdentityCustomerAccount resources for the domain (may be empty) Note: in the v1alpha1 version of the API, a NOT_FOUND error returns if no CloudIdentityCustomerAccount resources match the domain.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CheckCloudIdentityAccountsExistRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CheckCloudIdentityAccountsExistRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[CheckCloudIdentityAccountsExistResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CheckCloudIdentityAccountsExistResponse)>`  
  
  
### createChannelPartnerLink(CreateChannelPartnerLinkRequest request, StreamObserver<ChannelPartnerLink> responseObserver)
    
    
    public default void createChannelPartnerLink(CreateChannelPartnerLinkRequest request, StreamObserver<ChannelPartnerLink> responseObserver)

Initiates a channel partner link between a distributor and a reseller, or between resellers in an n-tier reseller channel. Invited partners need to follow the invite_link_uri provided in the response to accept. After accepting the invitation, a link is set up between the two parties. You must be a distributor to call this method. Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * ALREADY_EXISTS: The ChannelPartnerLink sent in the request already exists.
  * NOT_FOUND: No Cloud Identity customer exists for provided domain.
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: The new ChannelPartnerLink resource.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateChannelPartnerLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CreateChannelPartnerLinkRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ChannelPartnerLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerLink)>`  
  
  
### createChannelPartnerRepricingConfig(CreateChannelPartnerRepricingConfigRequest request, StreamObserver<ChannelPartnerRepricingConfig> responseObserver)
    
    
    public default void createChannelPartnerRepricingConfig(CreateChannelPartnerRepricingConfigRequest request, StreamObserver<ChannelPartnerRepricingConfig> responseObserver)

Creates a ChannelPartnerRepricingConfig. Call this method to set modifications for a specific ChannelPartner's bill. You can only create configs if the RepricingConfig.effective_invoice_month is a future month. If needed, you can create a config for the current month, with some restrictions. When creating a config for a future month, make sure there are no existing configs for that RepricingConfig.effective_invoice_month. The following restrictions are for creating configs in the current month.

  * This functionality is reserved for recovering from an erroneous config, and should not be used for regular business cases.
  * The new config will not modify exports used with other configs. Changes to the config may be immediate, but may take up to 24 hours.
  * There is a limit of ten configs for any ChannelPartner or RepricingConfig.EntitlementGranularity.entitlement, for any RepricingConfig.effective_invoice_month.
  * The contained ChannelPartnerRepricingConfig.repricing_config value must be different from the value used in the current config for a ChannelPartner. Possible Error Codes:
  * PERMISSION_DENIED: If the account making the request and the account being queried are different.
  * INVALID_ARGUMENT: Missing or invalid required parameters in the request. Also displays if the updated config is for the current month or past months.
  * NOT_FOUND: The ChannelPartnerRepricingConfig specified does not exist or is not associated with the given account.
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. Return Value: If successful, the updated ChannelPartnerRepricingConfig resource, otherwise returns an error.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CreateChannelPartnerRepricingConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ChannelPartnerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerRepricingConfig)>`  
  
  
### createCustomer(CreateCustomerRequest request, StreamObserver<Customer> responseObserver)
    
    
    public default void createCustomer(CreateCustomerRequest request, StreamObserver<Customer> responseObserver)

Creates a new Customer resource under the reseller or distributor account. Possible error codes:

  * PERMISSION_DENIED:
    * The reseller account making the request is different from the reseller account in the API request.
    * You are not authorized to create a customer. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT:
    * Required request parameters are missing or invalid.
    * Domain field value doesn't match the primary email domain. Return value: The newly created Customer resource.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCustomerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CreateCustomerRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Customer](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Customer)>`  
  
  
### createCustomerRepricingConfig(CreateCustomerRepricingConfigRequest request, StreamObserver<CustomerRepricingConfig> responseObserver)
    
    
    public default void createCustomerRepricingConfig(CreateCustomerRepricingConfigRequest request, StreamObserver<CustomerRepricingConfig> responseObserver)

Creates a CustomerRepricingConfig. Call this method to set modifications for a specific customer's bill. You can only create configs if the RepricingConfig.effective_invoice_month is a future month. If needed, you can create a config for the current month, with some restrictions. When creating a config for a future month, make sure there are no existing configs for that RepricingConfig.effective_invoice_month. The following restrictions are for creating configs in the current month.

  * This functionality is reserved for recovering from an erroneous config, and should not be used for regular business cases.
  * The new config will not modify exports used with other configs. Changes to the config may be immediate, but may take up to 24 hours.
  * There is a limit of ten configs for any RepricingConfig.EntitlementGranularity.entitlement, for any RepricingConfig.effective_invoice_month.
  * The contained CustomerRepricingConfig.repricing_config value must be different from the value used in the current config for a RepricingConfig.EntitlementGranularity.entitlement. Possible Error Codes:
  * PERMISSION_DENIED: If the account making the request and the account being queried are different.
  * INVALID_ARGUMENT: Missing or invalid required parameters in the request. Also displays if the updated config is for the current month or past months.
  * NOT_FOUND: The CustomerRepricingConfig specified does not exist or is not associated with the given account.
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. Return Value: If successful, the updated CustomerRepricingConfig resource, otherwise returns an error.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCustomerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CreateCustomerRepricingConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[CustomerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CustomerRepricingConfig)>`  
  
  
### createEntitlement(CreateEntitlementRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createEntitlement(CreateEntitlementRequest request, StreamObserver<Operation> responseObserver)

Creates an entitlement for a customer. Possible error codes:

  * PERMISSION_DENIED:
    * The customer doesn't belong to the reseller.
    * The reseller is not authorized to transact on this Product. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT:
    * Required request parameters are missing or invalid.
    * There is already a customer entitlement for a SKU from the same product family.
  * INVALID_VALUE: Make sure the OfferId is valid. If it is, contact Google Channel support for further troubleshooting.
  * NOT_FOUND: The customer or offer resource was not found.
  * ALREADY_EXISTS:
    * The SKU was already purchased for the customer.
    * The customer's primary email already exists. Retry after changing the customer's primary contact email.
  * CONDITION_NOT_MET or FAILED_PRECONDITION:
    * The domain required for purchasing a SKU has not been verified.
    * A pre-requisite SKU required to purchase an Add-On SKU is missing. For example, Google Workspace Business Starter is required to purchase Vault or Drive.
    * (Developer accounts only) Reseller and resold domain must meet the following naming requirements:
      * Domain names must start with goog-test.
      * Domain names must include the reseller domain.
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: The ID of a long-running operation. To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateEntitlementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CreateEntitlementRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteChannelPartnerRepricingConfig(DeleteChannelPartnerRepricingConfigRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteChannelPartnerRepricingConfig(DeleteChannelPartnerRepricingConfigRequest request, StreamObserver<Empty> responseObserver)

Deletes the given ChannelPartnerRepricingConfig permanently. You can only delete configs if their RepricingConfig.effective_invoice_month is set to a date after the current month. Possible error codes:

  * PERMISSION_DENIED: The account making the request does not own this customer.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * FAILED_PRECONDITION: The ChannelPartnerRepricingConfig is active or in the past.
  * NOT_FOUND: No ChannelPartnerRepricingConfig found for the name in the request.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.DeleteChannelPartnerRepricingConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### deleteCustomer(DeleteCustomerRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteCustomer(DeleteCustomerRequest request, StreamObserver<Empty> responseObserver)

Deletes the given Customer permanently. Possible error codes:

  * PERMISSION_DENIED: The account making the request does not own this customer.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * FAILED_PRECONDITION: The customer has existing entitlements.
  * NOT_FOUND: No Customer resource found for the name in the request.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteCustomerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.DeleteCustomerRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### deleteCustomerRepricingConfig(DeleteCustomerRepricingConfigRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteCustomerRepricingConfig(DeleteCustomerRepricingConfigRequest request, StreamObserver<Empty> responseObserver)

Deletes the given CustomerRepricingConfig permanently. You can only delete configs if their RepricingConfig.effective_invoice_month is set to a date after the current month. Possible error codes:

  * PERMISSION_DENIED: The account making the request does not own this customer.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * FAILED_PRECONDITION: The CustomerRepricingConfig is active or in the past.
  * NOT_FOUND: No CustomerRepricingConfig found for the name in the request.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteCustomerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.DeleteCustomerRepricingConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### getChannelPartnerLink(GetChannelPartnerLinkRequest request, StreamObserver<ChannelPartnerLink> responseObserver)
    
    
    public default void getChannelPartnerLink(GetChannelPartnerLinkRequest request, StreamObserver<ChannelPartnerLink> responseObserver)

Returns the requested ChannelPartnerLink resource. You must be a distributor to call this method. Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * NOT_FOUND: ChannelPartnerLink resource not found because of an invalid channel partner link name. Return value: The ChannelPartnerLink resource.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetChannelPartnerLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.GetChannelPartnerLinkRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ChannelPartnerLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerLink)>`  
  
  
### getChannelPartnerRepricingConfig(GetChannelPartnerRepricingConfigRequest request, StreamObserver<ChannelPartnerRepricingConfig> responseObserver)
    
    
    public default void getChannelPartnerRepricingConfig(GetChannelPartnerRepricingConfigRequest request, StreamObserver<ChannelPartnerRepricingConfig> responseObserver)

Gets information about how a Distributor modifies their bill before sending it to a ChannelPartner. Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different.
  * NOT_FOUND: The ChannelPartnerRepricingConfig was not found.
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. Return Value: If successful, the ChannelPartnerRepricingConfig resource, otherwise returns an error.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.GetChannelPartnerRepricingConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ChannelPartnerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerRepricingConfig)>`  
  
  
### getCustomer(GetCustomerRequest request, StreamObserver<Customer> responseObserver)
    
    
    public default void getCustomer(GetCustomerRequest request, StreamObserver<Customer> responseObserver)

Returns the requested Customer resource. Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * NOT_FOUND: The customer resource doesn't exist. Usually the result of an invalid name parameter. Return value: The Customer resource.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCustomerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.GetCustomerRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Customer](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Customer)>`  
  
  
### getCustomerRepricingConfig(GetCustomerRepricingConfigRequest request, StreamObserver<CustomerRepricingConfig> responseObserver)
    
    
    public default void getCustomerRepricingConfig(GetCustomerRepricingConfigRequest request, StreamObserver<CustomerRepricingConfig> responseObserver)

Gets information about how a Reseller modifies their bill before sending it to a Customer. Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different.
  * NOT_FOUND: The CustomerRepricingConfig was not found.
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. Return Value: If successful, the CustomerRepricingConfig resource, otherwise returns an error.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCustomerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.GetCustomerRepricingConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[CustomerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CustomerRepricingConfig)>`  
  
  
### getEntitlement(GetEntitlementRequest request, StreamObserver<Entitlement> responseObserver)
    
    
    public default void getEntitlement(GetEntitlementRequest request, StreamObserver<Entitlement> responseObserver)

Returns the requested Entitlement resource. Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * NOT_FOUND: The customer entitlement was not found. Return value: The requested Entitlement resource.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEntitlementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.GetEntitlementRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Entitlement](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Entitlement)>`  
  
  
### importCustomer(ImportCustomerRequest request, StreamObserver<Customer> responseObserver)
    
    
    public default void importCustomer(ImportCustomerRequest request, StreamObserver<Customer> responseObserver)

Imports a Customer from the Cloud Identity associated with the provided Cloud Identity ID or domain before a TransferEntitlements call. If a linked Customer already exists and overwrite_if_exists is true, it will update that Customer's data. Possible error codes:

  * PERMISSION_DENIED:
    * The reseller account making the request is different from the reseller account in the API request.
    * You are not authorized to import the customer. See <https://support.google.com/channelservices/answer/9759265>
  * NOT_FOUND: Cloud Identity doesn't exist or was deleted.
  * INVALID_ARGUMENT: Required parameters are missing, or the auth_token is expired or invalid.
  * ALREADY_EXISTS: A customer already exists and has conflicting critical fields. Requires an overwrite. Return value: The Customer.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportCustomerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ImportCustomerRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Customer](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Customer)>`  
  
  
### listChannelPartnerLinks(ListChannelPartnerLinksRequest request, StreamObserver<ListChannelPartnerLinksResponse> responseObserver)
    
    
    public default void listChannelPartnerLinks(ListChannelPartnerLinksRequest request, StreamObserver<ListChannelPartnerLinksResponse> responseObserver)

List ChannelPartnerLinks belonging to a distributor. You must be a distributor to call this method. Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. Return value: The list of the distributor account's ChannelPartnerLink resources.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListChannelPartnerLinksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListChannelPartnerLinksRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListChannelPartnerLinksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListChannelPartnerLinksResponse)>`  
  
  
### listChannelPartnerRepricingConfigs(ListChannelPartnerRepricingConfigsRequest request, StreamObserver<ListChannelPartnerRepricingConfigsResponse> responseObserver)
    
    
    public default void listChannelPartnerRepricingConfigs(ListChannelPartnerRepricingConfigsRequest request, StreamObserver<ListChannelPartnerRepricingConfigsResponse> responseObserver)

Lists information about how a Reseller modifies their bill before sending it to a ChannelPartner. Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different.
  * NOT_FOUND: The ChannelPartnerRepricingConfig specified does not exist or is not associated with the given account.
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. Return Value: If successful, the ChannelPartnerRepricingConfig resources. The data for each resource is displayed in the ascending order of:
  * Channel Partner ID
  * RepricingConfig.effective_invoice_month
  * ChannelPartnerRepricingConfig.update_time If unsuccessful, returns an error.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListChannelPartnerRepricingConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListChannelPartnerRepricingConfigsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListChannelPartnerRepricingConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListChannelPartnerRepricingConfigsResponse)>`  
  
  
### listCustomerRepricingConfigs(ListCustomerRepricingConfigsRequest request, StreamObserver<ListCustomerRepricingConfigsResponse> responseObserver)
    
    
    public default void listCustomerRepricingConfigs(ListCustomerRepricingConfigsRequest request, StreamObserver<ListCustomerRepricingConfigsResponse> responseObserver)

Lists information about how a Reseller modifies their bill before sending it to a Customer. Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different.
  * NOT_FOUND: The CustomerRepricingConfig specified does not exist or is not associated with the given account.
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. Return Value: If successful, the CustomerRepricingConfig resources. The data for each resource is displayed in the ascending order of:
  * Customer ID
  * RepricingConfig.EntitlementGranularity.entitlement
  * RepricingConfig.effective_invoice_month
  * CustomerRepricingConfig.update_time If unsuccessful, returns an error.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCustomerRepricingConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListCustomerRepricingConfigsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListCustomerRepricingConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListCustomerRepricingConfigsResponse)>`  
  
  
### listCustomers(ListCustomersRequest request, StreamObserver<ListCustomersResponse> responseObserver)
    
    
    public default void listCustomers(ListCustomersRequest request, StreamObserver<ListCustomersResponse> responseObserver)

List Customers. Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. Return value: List of Customers, or an empty list if there are no customers.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCustomersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListCustomersRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListCustomersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListCustomersResponse)>`  
  
  
### listEntitlementChanges(ListEntitlementChangesRequest request, StreamObserver<ListEntitlementChangesResponse> responseObserver)
    
    
    public default void listEntitlementChanges(ListEntitlementChangesRequest request, StreamObserver<ListEntitlementChangesResponse> responseObserver)

List entitlement history. Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request and the provided reseller account are different.
  * INVALID_ARGUMENT: Missing or invalid required fields in the request.
  * NOT_FOUND: The parent resource doesn't exist. Usually the result of an invalid name parameter.
  * INTERNAL: Any non-user error related to a technical issue in the backend. In this case, contact CloudChannel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. In this case, contact Cloud Channel support. Return value: List of EntitlementChanges.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEntitlementChangesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListEntitlementChangesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListEntitlementChangesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListEntitlementChangesResponse)>`  
  
  
### listEntitlements(ListEntitlementsRequest request, StreamObserver<ListEntitlementsResponse> responseObserver)
    
    
    public default void listEntitlements(ListEntitlementsRequest request, StreamObserver<ListEntitlementsResponse> responseObserver)

Lists Entitlements belonging to a customer. Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. Return value: A list of the customer's Entitlements.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEntitlementsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListEntitlementsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListEntitlementsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListEntitlementsResponse)>`  
  
  
### listOffers(ListOffersRequest request, StreamObserver<ListOffersResponse> responseObserver)
    
    
    public default void listOffers(ListOffersRequest request, StreamObserver<ListOffersResponse> responseObserver)

Lists the Offers the reseller can sell. Possible error codes:

  * INVALID_ARGUMENT: Required request parameters are missing or invalid.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListOffersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListOffersRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListOffersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListOffersResponse)>`  
  
  
### listProducts(ListProductsRequest request, StreamObserver<ListProductsResponse> responseObserver)
    
    
    public default void listProducts(ListProductsRequest request, StreamObserver<ListProductsResponse> responseObserver)

Lists the Products the reseller is authorized to sell. Possible error codes:

  * INVALID_ARGUMENT: Required request parameters are missing or invalid.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListProductsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListProductsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListProductsResponse)>`  
  
  
### listPurchasableOffers(ListPurchasableOffersRequest request, StreamObserver<ListPurchasableOffersResponse> responseObserver)
    
    
    public default void listPurchasableOffers(ListPurchasableOffersRequest request, StreamObserver<ListPurchasableOffersResponse> responseObserver)

Lists the following:

  * Offers that you can purchase for a customer.
  * Offers that you can change for an entitlement. Possible error codes:
  * PERMISSION_DENIED:
    * The customer doesn't belong to the reseller
    * The reseller is not authorized to transact on this Product. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPurchasableOffersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListPurchasableOffersRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListPurchasableOffersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListPurchasableOffersResponse)>`  
  
  
### listPurchasableSkus(ListPurchasableSkusRequest request, StreamObserver<ListPurchasableSkusResponse> responseObserver)
    
    
    public default void listPurchasableSkus(ListPurchasableSkusRequest request, StreamObserver<ListPurchasableSkusResponse> responseObserver)

Lists the following:

  * SKUs that you can purchase for a customer
  * SKUs that you can upgrade or downgrade for an entitlement. Possible error codes:
  * PERMISSION_DENIED: The customer doesn't belong to the reseller.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPurchasableSkusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListPurchasableSkusRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListPurchasableSkusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListPurchasableSkusResponse)>`  
  
  
### listSkuGroupBillableSkus(ListSkuGroupBillableSkusRequest request, StreamObserver<ListSkuGroupBillableSkusResponse> responseObserver)
    
    
    public default void listSkuGroupBillableSkus(ListSkuGroupBillableSkusRequest request, StreamObserver<ListSkuGroupBillableSkusResponse> responseObserver)

Lists the Billable SKUs in a given SKU group. Possible error codes: PERMISSION_DENIED: If the account making the request and the account being queried for are different, or the account doesn't exist. INVALID_ARGUMENT: Missing or invalid required parameters in the request. INTERNAL: Any non-user error related to technical issue in the backend. In this case, contact cloud channel support. Return Value: If successful, the BillableSku resources. The data for each resource is displayed in the ascending order of:

  * BillableSku.service_display_name
  * BillableSku.sku_display_name If unsuccessful, returns an error.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSkuGroupBillableSkusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSkuGroupBillableSkusRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListSkuGroupBillableSkusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSkuGroupBillableSkusResponse)>`  
  
  
### listSkuGroups(ListSkuGroupsRequest request, StreamObserver<ListSkuGroupsResponse> responseObserver)
    
    
    public default void listSkuGroups(ListSkuGroupsRequest request, StreamObserver<ListSkuGroupsResponse> responseObserver)

Lists the Rebilling supported SKU groups the account is authorized to sell. Reference: <https://cloud.google.com/skus/sku-groups> Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different, or the account doesn't exist.
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. Return Value: If successful, the SkuGroup resources. The data for each resource is displayed in the alphabetical order of SKU group display name. The data for each resource is displayed in the ascending order of SkuGroup.display_name If unsuccessful, returns an error.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSkuGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSkuGroupsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListSkuGroupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSkuGroupsResponse)>`  
  
  
### listSkus(ListSkusRequest request, StreamObserver<ListSkusResponse> responseObserver)
    
    
    public default void listSkus(ListSkusRequest request, StreamObserver<ListSkusResponse> responseObserver)

Lists the SKUs for a product the reseller is authorized to sell. Possible error codes:

  * INVALID_ARGUMENT: Required request parameters are missing or invalid.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSkusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSkusRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListSkusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSkusResponse)>`  
  
  
### listSubscribers(ListSubscribersRequest request, StreamObserver<ListSubscribersResponse> responseObserver)
    
    
    public default void listSubscribers(ListSubscribersRequest request, StreamObserver<ListSubscribersResponse> responseObserver)

Lists service accounts with subscriber privileges on the Pub/Sub topic created for this Channel Services account or integrator. Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request and the provided reseller account are different, or the impersonated user is not a super admin.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * NOT_FOUND: The topic resource doesn't exist.
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: A list of service email addresses.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSubscribersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSubscribersRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListSubscribersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSubscribersResponse)>`  
  
  
### listTransferableOffers(ListTransferableOffersRequest request, StreamObserver<ListTransferableOffersResponse> responseObserver)
    
    
    public default void listTransferableOffers(ListTransferableOffersRequest request, StreamObserver<ListTransferableOffersResponse> responseObserver)

List TransferableOffers of a customer based on Cloud Identity ID or Customer Name in the request. Use this method when a reseller gets the entitlement information of an unowned customer. The reseller should provide the customer's Cloud Identity ID or Customer Name. Possible error codes:

  * PERMISSION_DENIED:
    * The customer doesn't belong to the reseller and has no auth token.
    * The customer provided incorrect reseller information when generating auth token.
    * The reseller account making the request is different from the reseller account in the query.
    * The reseller is not authorized to transact on this Product. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. Return value: List of TransferableOffer for the given customer and SKU.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTransferableOffersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListTransferableOffersRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListTransferableOffersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListTransferableOffersResponse)>`  
  
  
### listTransferableSkus(ListTransferableSkusRequest request, StreamObserver<ListTransferableSkusResponse> responseObserver)
    
    
    public default void listTransferableSkus(ListTransferableSkusRequest request, StreamObserver<ListTransferableSkusResponse> responseObserver)

List TransferableSkus of a customer based on the Cloud Identity ID or Customer Name in the request. Use this method to list the entitlements information of an unowned customer. You should provide the customer's Cloud Identity ID or Customer Name. Possible error codes:

  * PERMISSION_DENIED:
    * The customer doesn't belong to the reseller and has no auth token.
    * The supplied auth token is invalid.
    * The reseller account making the request is different from the reseller account in the query.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. Return value: A list of the customer's TransferableSku.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTransferableSkusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListTransferableSkusRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListTransferableSkusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListTransferableSkusResponse)>`  
  
  
### lookupOffer(LookupOfferRequest request, StreamObserver<Offer> responseObserver)
    
    
    public default void lookupOffer(LookupOfferRequest request, StreamObserver<Offer> responseObserver)

Returns the requested Offer resource. Possible error codes:

  * PERMISSION_DENIED: The entitlement doesn't belong to the reseller.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * NOT_FOUND: Entitlement or offer was not found. Return value: The Offer resource.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[LookupOfferRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.LookupOfferRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Offer](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Offer)>`  
  
  
### provisionCloudIdentity(ProvisionCloudIdentityRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void provisionCloudIdentity(ProvisionCloudIdentityRequest request, StreamObserver<Operation> responseObserver)

Creates a Cloud Identity for the given customer using the customer's information, or the information provided here. Possible error codes:

  * PERMISSION_DENIED:
    * The customer doesn't belong to the reseller.
    * You are not authorized to provision cloud identity id. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * NOT_FOUND: The customer was not found.
  * ALREADY_EXISTS: The customer's primary email already exists. Retry after changing the customer's primary contact email.
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: The ID of a long-running operation. To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata contains an instance of OperationMetadata.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ProvisionCloudIdentityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ProvisionCloudIdentityRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### queryEligibleBillingAccounts(QueryEligibleBillingAccountsRequest request, StreamObserver<QueryEligibleBillingAccountsResponse> responseObserver)
    
    
    public default void queryEligibleBillingAccounts(QueryEligibleBillingAccountsRequest request, StreamObserver<QueryEligibleBillingAccountsResponse> responseObserver)

Lists the billing accounts that are eligible to purchase particular SKUs for a given customer. Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. Return value: Based on the provided list of SKUs, returns a list of SKU groups that must be purchased using the same billing account and the billing accounts eligible to purchase each SKU group.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryEligibleBillingAccountsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.QueryEligibleBillingAccountsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[QueryEligibleBillingAccountsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.QueryEligibleBillingAccountsResponse)>`  
  
  
### registerSubscriber(RegisterSubscriberRequest request, StreamObserver<RegisterSubscriberResponse> responseObserver)
    
    
    public default void registerSubscriber(RegisterSubscriberRequest request, StreamObserver<RegisterSubscriberResponse> responseObserver)

Registers a service account with subscriber privileges on the Pub/Sub topic for this Channel Services account or integrator. After you create a subscriber, you get the events through SubscriberEvent Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request and the provided reseller account are different, or the impersonated user is not a super admin.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: The topic name with the registered service email address.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[RegisterSubscriberRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.RegisterSubscriberRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[RegisterSubscriberResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.RegisterSubscriberResponse)>`  
  
  
### startPaidService(StartPaidServiceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void startPaidService(StartPaidServiceRequest request, StreamObserver<Operation> responseObserver)

Starts paid service for a trial entitlement. Starts paid service for a trial entitlement immediately. This method is only applicable if a plan is set up for a trial entitlement but has some trial days remaining. Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * NOT_FOUND: Entitlement resource not found.
  * FAILED_PRECONDITION/NOT_IN_TRIAL: This method only works for entitlement on trial plans.
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: The ID of a long-running operation. To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[StartPaidServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.StartPaidServiceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### suspendEntitlement(SuspendEntitlementRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void suspendEntitlement(SuspendEntitlementRequest request, StreamObserver<Operation> responseObserver)

Suspends a previously fulfilled entitlement. An entitlement suspension is a long-running operation. Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * NOT_FOUND: Entitlement resource not found.
  * NOT_ACTIVE: Entitlement is not active.
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: The ID of a long-running operation. To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[SuspendEntitlementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.SuspendEntitlementRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### transferEntitlements(TransferEntitlementsRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void transferEntitlements(TransferEntitlementsRequest request, StreamObserver<Operation> responseObserver)

Transfers customer entitlements to new reseller. Possible error codes:

  * PERMISSION_DENIED:
    * The customer doesn't belong to the reseller.
    * The reseller is not authorized to transact on this Product. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * NOT_FOUND: The customer or offer resource was not found.
  * ALREADY_EXISTS: The SKU was already transferred for the customer.
  * CONDITION_NOT_MET or FAILED_PRECONDITION:
    * The SKU requires domain verification to transfer, but the domain is not verified.
    * An Add-On SKU (example, Vault or Drive) is missing the pre-requisite SKU (example, G Suite Basic).
    * (Developer accounts only) Reseller and resold domain must meet the following naming requirements:
      * Domain names must start with goog-test.
      * Domain names must include the reseller domain.
    * Specify all transferring entitlements.
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: The ID of a long-running operation. To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[TransferEntitlementsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.TransferEntitlementsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### transferEntitlementsToGoogle(TransferEntitlementsToGoogleRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void transferEntitlementsToGoogle(TransferEntitlementsToGoogleRequest request, StreamObserver<Operation> responseObserver)

Transfers customer entitlements from their current reseller to Google. Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * NOT_FOUND: The customer or offer resource was not found.
  * ALREADY_EXISTS: The SKU was already transferred for the customer.
  * CONDITION_NOT_MET or FAILED_PRECONDITION:
    * The SKU requires domain verification to transfer, but the domain is not verified.
    * An Add-On SKU (example, Vault or Drive) is missing the pre-requisite SKU (example, G Suite Basic).
    * (Developer accounts only) Reseller and resold domain must meet the following naming requirements:
      * Domain names must start with goog-test.
      * Domain names must include the reseller domain.
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: The ID of a long-running operation. To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The response will contain google.protobuf.Empty on success. The Operation metadata will contain an instance of OperationMetadata.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[TransferEntitlementsToGoogleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.TransferEntitlementsToGoogleRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### unregisterSubscriber(UnregisterSubscriberRequest request, StreamObserver<UnregisterSubscriberResponse> responseObserver)
    
    
    public default void unregisterSubscriber(UnregisterSubscriberRequest request, StreamObserver<UnregisterSubscriberResponse> responseObserver)

Unregisters a service account with subscriber privileges on the Pub/Sub topic created for this Channel Services account or integrator. If there are no service accounts left with subscriber privileges, this deletes the topic. You can call ListSubscribers to check for these accounts. Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request and the provided reseller account are different, or the impersonated user is not a super admin.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * NOT_FOUND: The topic resource doesn't exist.
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: The topic name that unregistered the service email address. Returns a success response if the service email address wasn't registered with the topic.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[UnregisterSubscriberRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.UnregisterSubscriberRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[UnregisterSubscriberResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.UnregisterSubscriberResponse)>`  
  
  
### updateChannelPartnerLink(UpdateChannelPartnerLinkRequest request, StreamObserver<ChannelPartnerLink> responseObserver)
    
    
    public default void updateChannelPartnerLink(UpdateChannelPartnerLinkRequest request, StreamObserver<ChannelPartnerLink> responseObserver)

Updates a channel partner link. Distributors call this method to change a link's status. For example, to suspend a partner link. You must be a distributor to call this method. Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request.
  * INVALID_ARGUMENT:
    * Required request parameters are missing or invalid.
    * Link state cannot change from invited to active or suspended.
    * Cannot send reseller_cloud_identity_id, invite_url, or name in update mask.
  * NOT_FOUND: ChannelPartnerLink resource not found.
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: The updated ChannelPartnerLink resource.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateChannelPartnerLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.UpdateChannelPartnerLinkRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ChannelPartnerLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerLink)>`  
  
  
### updateChannelPartnerRepricingConfig(UpdateChannelPartnerRepricingConfigRequest request, StreamObserver<ChannelPartnerRepricingConfig> responseObserver)
    
    
    public default void updateChannelPartnerRepricingConfig(UpdateChannelPartnerRepricingConfigRequest request, StreamObserver<ChannelPartnerRepricingConfig> responseObserver)

Updates a ChannelPartnerRepricingConfig. Call this method to set modifications for a specific ChannelPartner's bill. This method overwrites the existing CustomerRepricingConfig. You can only update configs if the RepricingConfig.effective_invoice_month is a future month. To make changes to configs for the current month, use CreateChannelPartnerRepricingConfig, taking note of its restrictions. You cannot update the RepricingConfig.effective_invoice_month. When updating a config in the future:

  * This config must already exist. Possible Error Codes:
  * PERMISSION_DENIED: If the account making the request and the account being queried are different.
  * INVALID_ARGUMENT: Missing or invalid required parameters in the request. Also displays if the updated config is for the current month or past months.
  * NOT_FOUND: The ChannelPartnerRepricingConfig specified does not exist or is not associated with the given account.
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. Return Value: If successful, the updated ChannelPartnerRepricingConfig resource, otherwise returns an error.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.UpdateChannelPartnerRepricingConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ChannelPartnerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerRepricingConfig)>`  
  
  
### updateCustomer(UpdateCustomerRequest request, StreamObserver<Customer> responseObserver)
    
    
    public default void updateCustomer(UpdateCustomerRequest request, StreamObserver<Customer> responseObserver)

Updates an existing Customer resource for the reseller or distributor. Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * NOT_FOUND: No Customer resource found for the name in the request. Return value: The updated Customer resource.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCustomerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.UpdateCustomerRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Customer](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Customer)>`  
  
  
### updateCustomerRepricingConfig(UpdateCustomerRepricingConfigRequest request, StreamObserver<CustomerRepricingConfig> responseObserver)
    
    
    public default void updateCustomerRepricingConfig(UpdateCustomerRepricingConfigRequest request, StreamObserver<CustomerRepricingConfig> responseObserver)

Updates a CustomerRepricingConfig. Call this method to set modifications for a specific customer's bill. This method overwrites the existing CustomerRepricingConfig. You can only update configs if the RepricingConfig.effective_invoice_month is a future month. To make changes to configs for the current month, use CreateCustomerRepricingConfig, taking note of its restrictions. You cannot update the RepricingConfig.effective_invoice_month. When updating a config in the future:

  * This config must already exist. Possible Error Codes:
  * PERMISSION_DENIED: If the account making the request and the account being queried are different.
  * INVALID_ARGUMENT: Missing or invalid required parameters in the request. Also displays if the updated config is for the current month or past months.
  * NOT_FOUND: The CustomerRepricingConfig specified does not exist or is not associated with the given account.
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. Return Value: If successful, the updated CustomerRepricingConfig resource, otherwise returns an error.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCustomerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.UpdateCustomerRepricingConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[CustomerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CustomerRepricingConfig)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
