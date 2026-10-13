---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient
title: Class CloudChannelServiceClient (3.103.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:26:54.791813+00:00
---

# Class CloudChannelServiceClient (3.103.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CloudChannelServiceClient (3.103.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.103.0 (latest)  3.99.0  3.98.0  3.97.0  3.95.0  3.92.0  3.91.0  3.89.0  3.87.0  3.86.0  3.85.0  3.84.0  3.82.0  3.80.0  3.79.0  3.78.0  3.77.0  3.76.0  3.74.0  3.72.0  3.71.0  3.68.0  3.67.0  3.66.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.6  3.6.1  3.5.1  3.3.1 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-channel/google-cloud-channel/src/main/java/com/google/cloud/channel/v1/CloudChannelServiceClient.java)| [Product Reference](https://cloud.google.com/channel/docs)| [REST Documentation](https://cloud.google.com/channel/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/channel/docs/reference/rpc)  
---|---|---|---  
  
Service Description: CloudChannelService lets Google cloud resellers and distributors manage their customers, channel partners, entitlements, and reports.

Using this service: 1. Resellers and distributors can manage a customer entity. 2. Distributors can register an authorized reseller in their channel and provide them with delegated admin access. 3. Resellers and distributors can manage customer entitlements.

CloudChannelService exposes the following resources: - Customers: An entity-usually an enterprise-managed by a reseller or distributor.

\- Entitlements: An entity that provides a customer with the means to use a service. Entitlements are created or updated as a result of a successful fulfillment.

\- ChannelPartnerLinks: An entity that identifies links between distributors and their indirect resellers in a channel.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       CustomerName name = CustomerName.of("[ACCOUNT]", "[CUSTOMER]");
       Customer response = cloudChannelServiceClient.getCustomer(name);
     }
     

Note: close() needs to be called on the CloudChannelServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListCustomers |  List Customers.  Possible error codes: 

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 

Return value: List of Customers, or an empty list if there are no customers. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listCustomers(ListCustomersRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listCustomersPagedCallable() 
  * listCustomersCallable() 

  
GetCustomer |  Returns the requested Customer resource.  Possible error codes: 

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: The customer resource doesn't exist. Usually the result of an invalid name parameter. 

Return value: The Customer resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getCustomer(GetCustomerRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getCustomer(CustomerName name) 
  * getCustomer(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCustomerCallable() 

  
CheckCloudIdentityAccountsExist |  Confirms the existence of Cloud Identity accounts based on the domain and if the Cloud Identity accounts are owned by the reseller.  Possible error codes: 

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * INVALID_VALUE: Invalid domain value in the request. 

Return value: A list of CloudIdentityCustomerAccount resources for the domain (may be empty)  Note: in the v1alpha1 version of the API, a NOT_FOUND error returns if no CloudIdentityCustomerAccount resources match the domain. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * checkCloudIdentityAccountsExist(CheckCloudIdentityAccountsExistRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * checkCloudIdentityAccountsExistCallable() 

  
CreateCustomer |  Creates a new Customer resource under the reseller or distributor account.  Possible error codes: 

  * PERMISSION_DENIED: * The reseller account making the request is different from the reseller account in the API request. * You are not authorized to create a customer. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT: * Required request parameters are missing or invalid. * Domain field value doesn't match the primary email domain. 

Return value: The newly created Customer resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createCustomer(CreateCustomerRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createCustomerCallable() 

  
UpdateCustomer |  Updates an existing Customer resource for the reseller or distributor.  Possible error codes: 

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: No Customer resource found for the name in the request. 

Return value: The updated Customer resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateCustomer(UpdateCustomerRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateCustomerCallable() 

  
DeleteCustomer |  Deletes the given Customer permanently.  Possible error codes: 

  * PERMISSION_DENIED: The account making the request does not own this customer. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * FAILED_PRECONDITION: The customer has existing entitlements. 
  * NOT_FOUND: No Customer resource found for the name in the request. 

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteCustomer(DeleteCustomerRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteCustomer(CustomerName name) 
  * deleteCustomer(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteCustomerCallable() 

  
ImportCustomer |  Imports a Customer from the Cloud Identity associated with the provided Cloud Identity ID or domain before a TransferEntitlements call. If a linked Customer already exists and overwrite_if_exists is true, it will update that Customer's data.  Possible error codes: 

  * PERMISSION_DENIED: * The reseller account making the request is different from the reseller account in the API request. * You are not authorized to import the customer. See <https://support.google.com/channelservices/answer/9759265>
  * NOT_FOUND: Cloud Identity doesn't exist or was deleted. 
  * INVALID_ARGUMENT: Required parameters are missing, or the auth_token is expired or invalid. 
  * ALREADY_EXISTS: A customer already exists and has conflicting critical fields. Requires an overwrite. 

Return value: The Customer. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * importCustomer(ImportCustomerRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * importCustomerCallable() 

  
ProvisionCloudIdentity |  Creates a Cloud Identity for the given customer using the customer's information, or the information provided here.  Possible error codes: 

  * PERMISSION_DENIED: * The customer doesn't belong to the reseller. * You are not authorized to provision cloud identity id. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: The customer was not found. 
  * ALREADY_EXISTS: The customer's primary email already exists. Retry after changing the customer's primary contact email. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 

Return value: The ID of a long-running operation.  To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata contains an instance of OperationMetadata. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * provisionCloudIdentityAsync(ProvisionCloudIdentityRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * provisionCloudIdentityOperationCallable() 
  * provisionCloudIdentityCallable() 

  
ListEntitlements |  Lists Entitlements belonging to a customer.  Possible error codes: 

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 

Return value: A list of the customer's Entitlements. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listEntitlements(ListEntitlementsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listEntitlementsPagedCallable() 
  * listEntitlementsCallable() 

  
ListTransferableSkus |  List TransferableSkus of a customer based on the Cloud Identity ID or Customer Name in the request.  Use this method to list the entitlements information of an unowned customer. You should provide the customer's Cloud Identity ID or Customer Name.  Possible error codes: 

  * PERMISSION_DENIED: * The customer doesn't belong to the reseller and has no auth token. * The supplied auth token is invalid. * The reseller account making the request is different from the reseller account in the query. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 

Return value: A list of the customer's TransferableSku. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listTransferableSkus(ListTransferableSkusRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listTransferableSkusPagedCallable() 
  * listTransferableSkusCallable() 

  
ListTransferableOffers |  List TransferableOffers of a customer based on Cloud Identity ID or Customer Name in the request.  Use this method when a reseller gets the entitlement information of an unowned customer. The reseller should provide the customer's Cloud Identity ID or Customer Name.  Possible error codes: 

  * PERMISSION_DENIED: * The customer doesn't belong to the reseller and has no auth token. * The customer provided incorrect reseller information when generating auth token. * The reseller account making the request is different from the reseller account in the query. * The reseller is not authorized to transact on this Product. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 

Return value: List of TransferableOffer for the given customer and SKU. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listTransferableOffers(ListTransferableOffersRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listTransferableOffersPagedCallable() 
  * listTransferableOffersCallable() 

  
GetEntitlement |  Returns the requested Entitlement resource.  Possible error codes: 

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: The customer entitlement was not found. 

Return value: The requested Entitlement resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getEntitlement(GetEntitlementRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getEntitlementCallable() 

  
CreateEntitlement |  Creates an entitlement for a customer.  Possible error codes: 

  * PERMISSION_DENIED: * The customer doesn't belong to the reseller. * The reseller is not authorized to transact on this Product. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT: * Required request parameters are missing or invalid. * There is already a customer entitlement for a SKU from the same product family. 
  * INVALID_VALUE: Make sure the OfferId is valid. If it is, contact Google Channel support for further troubleshooting. 
  * NOT_FOUND: The customer or offer resource was not found. 
  * ALREADY_EXISTS: * The SKU was already purchased for the customer. * The customer's primary email already exists. Retry after changing the customer's primary contact email. 
  * CONDITION_NOT_MET or FAILED_PRECONDITION: * The domain required for purchasing a SKU has not been verified. * A pre-requisite SKU required to purchase an Add-On SKU is missing. For example, Google Workspace Business Starter is required to purchase Vault or Drive. * (Developer accounts only) Reseller and resold domain must meet the following naming requirements: * Domain names must start with goog-test. * Domain names must include the reseller domain. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 

Return value: The ID of a long-running operation.  To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createEntitlementAsync(CreateEntitlementRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createEntitlementOperationCallable() 
  * createEntitlementCallable() 

  
ChangeParameters |  Change parameters of the entitlement.  An entitlement update is a long-running operation and it updates the entitlement as a result of fulfillment.  Possible error codes: 

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. For example, the number of seats being changed is greater than the allowed number of max seats, or decreasing seats for a commitment based plan. 
  * NOT_FOUND: Entitlement resource not found. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 

Return value: The ID of a long-running operation.  To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * changeParametersAsync(ChangeParametersRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * changeParametersOperationCallable() 
  * changeParametersCallable() 

  
ChangeRenewalSettings |  Updates the renewal settings for an existing customer entitlement.  An entitlement update is a long-running operation and it updates the entitlement as a result of fulfillment.  Possible error codes: 

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: Entitlement resource not found. 
  * NOT_COMMITMENT_PLAN: Renewal Settings are only applicable for a commitment plan. Can't enable or disable renewals for non-commitment plans. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 

Return value: The ID of a long-running operation.  To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * changeRenewalSettingsAsync(ChangeRenewalSettingsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * changeRenewalSettingsOperationCallable() 
  * changeRenewalSettingsCallable() 

  
ChangeOffer |  Updates the Offer for an existing customer entitlement.  An entitlement update is a long-running operation and it updates the entitlement as a result of fulfillment.  Possible error codes: 

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: Offer or Entitlement resource not found. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 

Return value: The ID of a long-running operation.  To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * changeOfferAsync(ChangeOfferRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * changeOfferOperationCallable() 
  * changeOfferCallable() 

  
StartPaidService |  Starts paid service for a trial entitlement.  Starts paid service for a trial entitlement immediately. This method is only applicable if a plan is set up for a trial entitlement but has some trial days remaining.  Possible error codes: 

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: Entitlement resource not found. 
  * FAILED_PRECONDITION/NOT_IN_TRIAL: This method only works for entitlement on trial plans. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 

Return value: The ID of a long-running operation.  To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * startPaidServiceAsync(StartPaidServiceRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * startPaidServiceOperationCallable() 
  * startPaidServiceCallable() 

  
SuspendEntitlement |  Suspends a previously fulfilled entitlement.  An entitlement suspension is a long-running operation.  Possible error codes: 

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: Entitlement resource not found. 
  * NOT_ACTIVE: Entitlement is not active. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 

Return value: The ID of a long-running operation.  To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * suspendEntitlementAsync(SuspendEntitlementRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * suspendEntitlementOperationCallable() 
  * suspendEntitlementCallable() 

  
CancelEntitlement |  Cancels a previously fulfilled entitlement.  An entitlement cancellation is a long-running operation.  Possible error codes: 

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * FAILED_PRECONDITION: There are Google Cloud projects linked to the Google Cloud entitlement's Cloud Billing subaccount. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: Entitlement resource not found. 
  * DELETION_TYPE_NOT_ALLOWED: Cancel is only allowed for Google Workspace add-ons, or entitlements for Google Cloud's development platform. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 

Return value: The ID of a long-running operation.  To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The response will contain google.protobuf.Empty on success. The Operation metadata will contain an instance of OperationMetadata. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * cancelEntitlementAsync(CancelEntitlementRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * cancelEntitlementOperationCallable() 
  * cancelEntitlementCallable() 

  
ActivateEntitlement |  Activates a previously suspended entitlement. Entitlements suspended for pending ToS acceptance can't be activated using this method.  An entitlement activation is a long-running operation and it updates the state of the customer entitlement.  Possible error codes: 

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: Entitlement resource not found. 
  * SUSPENSION_NOT_RESELLER_INITIATED: Can only activate reseller-initiated suspensions and entitlements that have accepted the TOS. 
  * NOT_SUSPENDED: Can only activate suspended entitlements not in an ACTIVE state. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 

Return value: The ID of a long-running operation.  To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * activateEntitlementAsync(ActivateEntitlementRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * activateEntitlementOperationCallable() 
  * activateEntitlementCallable() 

  
TransferEntitlements |  Transfers customer entitlements to new reseller.  Possible error codes: 

  * PERMISSION_DENIED: * The customer doesn't belong to the reseller. * The reseller is not authorized to transact on this Product. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: The customer or offer resource was not found. 
  * ALREADY_EXISTS: The SKU was already transferred for the customer. 
  * CONDITION_NOT_MET or FAILED_PRECONDITION: * The SKU requires domain verification to transfer, but the domain is not verified. * An Add-On SKU (example, Vault or Drive) is missing the pre-requisite SKU (example, G Suite Basic). * (Developer accounts only) Reseller and resold domain must meet the following naming requirements: * Domain names must start with goog-test. * Domain names must include the reseller domain. * Specify all transferring entitlements. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 

Return value: The ID of a long-running operation.  To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * transferEntitlementsAsync(TransferEntitlementsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * transferEntitlementsOperationCallable() 
  * transferEntitlementsCallable() 

  
TransferEntitlementsToGoogle |  Transfers customer entitlements from their current reseller to Google.  Possible error codes: 

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: The customer or offer resource was not found. 
  * ALREADY_EXISTS: The SKU was already transferred for the customer. 
  * CONDITION_NOT_MET or FAILED_PRECONDITION: * The SKU requires domain verification to transfer, but the domain is not verified. * An Add-On SKU (example, Vault or Drive) is missing the pre-requisite SKU (example, G Suite Basic). * (Developer accounts only) Reseller and resold domain must meet the following naming requirements: * Domain names must start with goog-test. * Domain names must include the reseller domain. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 

Return value: The ID of a long-running operation.  To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The response will contain google.protobuf.Empty on success. The Operation metadata will contain an instance of OperationMetadata. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * transferEntitlementsToGoogleAsync(TransferEntitlementsToGoogleRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * transferEntitlementsToGoogleOperationCallable() 
  * transferEntitlementsToGoogleCallable() 

  
ListChannelPartnerLinks |  List ChannelPartnerLinks belonging to a distributor. You must be a distributor to call this method.  Possible error codes: 

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 

Return value: The list of the distributor account's ChannelPartnerLink resources. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listChannelPartnerLinks(ListChannelPartnerLinksRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listChannelPartnerLinksPagedCallable() 
  * listChannelPartnerLinksCallable() 

  
GetChannelPartnerLink |  Returns the requested ChannelPartnerLink resource. You must be a distributor to call this method.  Possible error codes: 

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: ChannelPartnerLink resource not found because of an invalid channel partner link name. 

Return value: The ChannelPartnerLink resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getChannelPartnerLink(GetChannelPartnerLinkRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getChannelPartnerLinkCallable() 

  
CreateChannelPartnerLink |  Initiates a channel partner link between a distributor and a reseller, or between resellers in an n-tier reseller channel. Invited partners need to follow the invite_link_uri provided in the response to accept. After accepting the invitation, a link is set up between the two parties. You must be a distributor to call this method.  Possible error codes: 

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * ALREADY_EXISTS: The ChannelPartnerLink sent in the request already exists. 
  * NOT_FOUND: No Cloud Identity customer exists for provided domain. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 

Return value: The new ChannelPartnerLink resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createChannelPartnerLink(CreateChannelPartnerLinkRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createChannelPartnerLinkCallable() 

  
UpdateChannelPartnerLink |  Updates a channel partner link. Distributors call this method to change a link's status. For example, to suspend a partner link. You must be a distributor to call this method.  Possible error codes: 

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * INVALID_ARGUMENT: * Required request parameters are missing or invalid. * Link state cannot change from invited to active or suspended. * Cannot send reseller_cloud_identity_id, invite_url, or name in update mask. 
  * NOT_FOUND: ChannelPartnerLink resource not found. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 

Return value: The updated ChannelPartnerLink resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateChannelPartnerLink(UpdateChannelPartnerLinkRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateChannelPartnerLinkCallable() 

  
GetCustomerRepricingConfig |  Gets information about how a Reseller modifies their bill before sending it to a Customer.  Possible Error Codes: 

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * NOT_FOUND: The CustomerRepricingConfig was not found. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 

Return Value: If successful, the CustomerRepricingConfig resource, otherwise returns an error. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getCustomerRepricingConfig(GetCustomerRepricingConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getCustomerRepricingConfig(CustomerRepricingConfigName name) 
  * getCustomerRepricingConfig(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCustomerRepricingConfigCallable() 

  
ListCustomerRepricingConfigs |  Lists information about how a Reseller modifies their bill before sending it to a Customer.  Possible Error Codes: 

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * NOT_FOUND: The CustomerRepricingConfig specified does not exist or is not associated with the given account. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 

Return Value: If successful, the CustomerRepricingConfig resources. The data for each resource is displayed in the ascending order of: 

  * Customer ID 
  * RepricingConfig.EntitlementGranularity.entitlement
  * RepricingConfig.effective_invoice_month
  * CustomerRepricingConfig.update_time

If unsuccessful, returns an error. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listCustomerRepricingConfigs(ListCustomerRepricingConfigsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listCustomerRepricingConfigs(CustomerName parent) 
  * listCustomerRepricingConfigs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listCustomerRepricingConfigsPagedCallable() 
  * listCustomerRepricingConfigsCallable() 

  
CreateCustomerRepricingConfig |  Creates a CustomerRepricingConfig. Call this method to set modifications for a specific customer's bill. You can only create configs if the RepricingConfig.effective_invoice_month is a future month. If needed, you can create a config for the current month, with some restrictions.  When creating a config for a future month, make sure there are no existing configs for that RepricingConfig.effective_invoice_month.  The following restrictions are for creating configs in the current month. 

  * This functionality is reserved for recovering from an erroneous config, and should not be used for regular business cases. 
  * The new config will not modify exports used with other configs. Changes to the config may be immediate, but may take up to 24 hours. 
  * There is a limit of ten configs for any RepricingConfig.EntitlementGranularity.entitlement, for any RepricingConfig.effective_invoice_month. 
  * The contained CustomerRepricingConfig.repricing_config value must be different from the value used in the current config for a RepricingConfig.EntitlementGranularity.entitlement. 

Possible Error Codes: 

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * INVALID_ARGUMENT: Missing or invalid required parameters in the request. Also displays if the updated config is for the current month or past months. 
  * NOT_FOUND: The CustomerRepricingConfig specified does not exist or is not associated with the given account. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 

Return Value: If successful, the updated CustomerRepricingConfig resource, otherwise returns an error. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createCustomerRepricingConfig(CreateCustomerRepricingConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createCustomerRepricingConfig(CustomerName parent, CustomerRepricingConfig customerRepricingConfig) 
  * createCustomerRepricingConfig(String parent, CustomerRepricingConfig customerRepricingConfig) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createCustomerRepricingConfigCallable() 

  
UpdateCustomerRepricingConfig |  Updates a CustomerRepricingConfig. Call this method to set modifications for a specific customer's bill. This method overwrites the existing CustomerRepricingConfig.  You can only update configs if the RepricingConfig.effective_invoice_month is a future month. To make changes to configs for the current month, use CreateCustomerRepricingConfig, taking note of its restrictions. You cannot update the RepricingConfig.effective_invoice_month.  When updating a config in the future: 

  * This config must already exist. 

Possible Error Codes: 

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * INVALID_ARGUMENT: Missing or invalid required parameters in the request. Also displays if the updated config is for the current month or past months. 
  * NOT_FOUND: The CustomerRepricingConfig specified does not exist or is not associated with the given account. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 

Return Value: If successful, the updated CustomerRepricingConfig resource, otherwise returns an error. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateCustomerRepricingConfig(UpdateCustomerRepricingConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateCustomerRepricingConfig(CustomerRepricingConfig customerRepricingConfig) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateCustomerRepricingConfigCallable() 

  
DeleteCustomerRepricingConfig |  Deletes the given CustomerRepricingConfig permanently. You can only delete configs if their RepricingConfig.effective_invoice_month is set to a date after the current month.  Possible error codes: 

  * PERMISSION_DENIED: The account making the request does not own this customer. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * FAILED_PRECONDITION: The CustomerRepricingConfig is active or in the past. 
  * NOT_FOUND: No CustomerRepricingConfig found for the name in the request. 

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteCustomerRepricingConfig(DeleteCustomerRepricingConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteCustomerRepricingConfig(CustomerRepricingConfigName name) 
  * deleteCustomerRepricingConfig(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteCustomerRepricingConfigCallable() 

  
GetChannelPartnerRepricingConfig |  Gets information about how a Distributor modifies their bill before sending it to a ChannelPartner.  Possible Error Codes: 

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * NOT_FOUND: The ChannelPartnerRepricingConfig was not found. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 

Return Value: If successful, the ChannelPartnerRepricingConfig resource, otherwise returns an error. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getChannelPartnerRepricingConfig(GetChannelPartnerRepricingConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getChannelPartnerRepricingConfig(ChannelPartnerRepricingConfigName name) 
  * getChannelPartnerRepricingConfig(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getChannelPartnerRepricingConfigCallable() 

  
ListChannelPartnerRepricingConfigs |  Lists information about how a Reseller modifies their bill before sending it to a ChannelPartner.  Possible Error Codes: 

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * NOT_FOUND: The ChannelPartnerRepricingConfig specified does not exist or is not associated with the given account. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 

Return Value: If successful, the ChannelPartnerRepricingConfig resources. The data for each resource is displayed in the ascending order of: 

  * Channel Partner ID 
  * RepricingConfig.effective_invoice_month
  * ChannelPartnerRepricingConfig.update_time

If unsuccessful, returns an error. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listChannelPartnerRepricingConfigs(ListChannelPartnerRepricingConfigsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listChannelPartnerRepricingConfigs(ChannelPartnerLinkName parent) 
  * listChannelPartnerRepricingConfigs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listChannelPartnerRepricingConfigsPagedCallable() 
  * listChannelPartnerRepricingConfigsCallable() 

  
CreateChannelPartnerRepricingConfig |  Creates a ChannelPartnerRepricingConfig. Call this method to set modifications for a specific ChannelPartner's bill. You can only create configs if the RepricingConfig.effective_invoice_month is a future month. If needed, you can create a config for the current month, with some restrictions.  When creating a config for a future month, make sure there are no existing configs for that RepricingConfig.effective_invoice_month.  The following restrictions are for creating configs in the current month. 

  * This functionality is reserved for recovering from an erroneous config, and should not be used for regular business cases. 
  * The new config will not modify exports used with other configs. Changes to the config may be immediate, but may take up to 24 hours. 
  * There is a limit of ten configs for any ChannelPartner or RepricingConfig.EntitlementGranularity.entitlement, for any RepricingConfig.effective_invoice_month. 
  * The contained ChannelPartnerRepricingConfig.repricing_config value must be different from the value used in the current config for a ChannelPartner. 

Possible Error Codes: 

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * INVALID_ARGUMENT: Missing or invalid required parameters in the request. Also displays if the updated config is for the current month or past months. 
  * NOT_FOUND: The ChannelPartnerRepricingConfig specified does not exist or is not associated with the given account. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 

Return Value: If successful, the updated ChannelPartnerRepricingConfig resource, otherwise returns an error. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createChannelPartnerRepricingConfig(CreateChannelPartnerRepricingConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createChannelPartnerRepricingConfig(ChannelPartnerLinkName parent, ChannelPartnerRepricingConfig channelPartnerRepricingConfig) 
  * createChannelPartnerRepricingConfig(String parent, ChannelPartnerRepricingConfig channelPartnerRepricingConfig) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createChannelPartnerRepricingConfigCallable() 

  
UpdateChannelPartnerRepricingConfig |  Updates a ChannelPartnerRepricingConfig. Call this method to set modifications for a specific ChannelPartner's bill. This method overwrites the existing CustomerRepricingConfig.  You can only update configs if the RepricingConfig.effective_invoice_month is a future month. To make changes to configs for the current month, use CreateChannelPartnerRepricingConfig, taking note of its restrictions. You cannot update the RepricingConfig.effective_invoice_month.  When updating a config in the future: 

  * This config must already exist. 

Possible Error Codes: 

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * INVALID_ARGUMENT: Missing or invalid required parameters in the request. Also displays if the updated config is for the current month or past months. 
  * NOT_FOUND: The ChannelPartnerRepricingConfig specified does not exist or is not associated with the given account. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 

Return Value: If successful, the updated ChannelPartnerRepricingConfig resource, otherwise returns an error. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateChannelPartnerRepricingConfig(UpdateChannelPartnerRepricingConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateChannelPartnerRepricingConfig(ChannelPartnerRepricingConfig channelPartnerRepricingConfig) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateChannelPartnerRepricingConfigCallable() 

  
DeleteChannelPartnerRepricingConfig |  Deletes the given ChannelPartnerRepricingConfig permanently. You can only delete configs if their RepricingConfig.effective_invoice_month is set to a date after the current month.  Possible error codes: 

  * PERMISSION_DENIED: The account making the request does not own this customer. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * FAILED_PRECONDITION: The ChannelPartnerRepricingConfig is active or in the past. 
  * NOT_FOUND: No ChannelPartnerRepricingConfig found for the name in the request. 

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteChannelPartnerRepricingConfig(DeleteChannelPartnerRepricingConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteChannelPartnerRepricingConfig(ChannelPartnerRepricingConfigName name) 
  * deleteChannelPartnerRepricingConfig(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteChannelPartnerRepricingConfigCallable() 

  
ListSkuGroups |  Lists the Rebilling supported SKU groups the account is authorized to sell. Reference: <https://cloud.google.com/skus/sku-groups> Possible Error Codes: 

  * PERMISSION_DENIED: If the account making the request and the account being queried are different, or the account doesn't exist. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 

Return Value: If successful, the SkuGroup resources. The data for each resource is displayed in the alphabetical order of SKU group display name. The data for each resource is displayed in the ascending order of SkuGroup.display_name If unsuccessful, returns an error. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSkuGroups(ListSkuGroupsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listSkuGroups(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSkuGroupsPagedCallable() 
  * listSkuGroupsCallable() 

  
ListSkuGroupBillableSkus |  Lists the Billable SKUs in a given SKU group.  Possible error codes: PERMISSION_DENIED: If the account making the request and the account being queried for are different, or the account doesn't exist. INVALID_ARGUMENT: Missing or invalid required parameters in the request. INTERNAL: Any non-user error related to technical issue in the backend. In this case, contact cloud channel support.  Return Value: If successful, the BillableSku resources. The data for each resource is displayed in the ascending order of: 

  * BillableSku.service_display_name
  * BillableSku.sku_display_name

If unsuccessful, returns an error. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSkuGroupBillableSkus(ListSkuGroupBillableSkusRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listSkuGroupBillableSkus(SkuGroupName parent) 
  * listSkuGroupBillableSkus(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSkuGroupBillableSkusPagedCallable() 
  * listSkuGroupBillableSkusCallable() 

  
LookupOffer |  Returns the requested Offer resource.  Possible error codes: 

  * PERMISSION_DENIED: The entitlement doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: Entitlement or offer was not found. 

Return value: The Offer resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * lookupOffer(LookupOfferRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * lookupOfferCallable() 

  
ListProducts |  Lists the Products the reseller is authorized to sell.  Possible error codes: 

  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listProducts(ListProductsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listProductsPagedCallable() 
  * listProductsCallable() 

  
ListSkus |  Lists the SKUs for a product the reseller is authorized to sell.  Possible error codes: 

  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSkus(ListSkusRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSkusPagedCallable() 
  * listSkusCallable() 

  
ListOffers |  Lists the Offers the reseller can sell.  Possible error codes: 

  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listOffers(ListOffersRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listOffersPagedCallable() 
  * listOffersCallable() 

  
ListPurchasableSkus |  Lists the following: 

  * SKUs that you can purchase for a customer 
  * SKUs that you can upgrade or downgrade for an entitlement. 

Possible error codes: 

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPurchasableSkus(ListPurchasableSkusRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPurchasableSkusPagedCallable() 
  * listPurchasableSkusCallable() 

  
ListPurchasableOffers |  Lists the following: 

  * Offers that you can purchase for a customer. 
  * Offers that you can change for an entitlement. 

Possible error codes: 

  * PERMISSION_DENIED: * The customer doesn't belong to the reseller * The reseller is not authorized to transact on this Product. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPurchasableOffers(ListPurchasableOffersRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPurchasableOffersPagedCallable() 
  * listPurchasableOffersCallable() 

  
QueryEligibleBillingAccounts |  Lists the billing accounts that are eligible to purchase particular SKUs for a given customer.  Possible error codes: 

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 

Return value: Based on the provided list of SKUs, returns a list of SKU groups that must be purchased using the same billing account and the billing accounts eligible to purchase each SKU group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * queryEligibleBillingAccounts(QueryEligibleBillingAccountsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * queryEligibleBillingAccountsCallable() 

  
RegisterSubscriber |  Registers a service account with subscriber privileges on the Pub/Sub topic for this Channel Services account or integrator. After you create a subscriber, you get the events through SubscriberEvent Possible error codes: 

  * PERMISSION_DENIED: The reseller account making the request and the provided reseller account are different, or the impersonated user is not a super admin. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 

Return value: The topic name with the registered service email address. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * registerSubscriber(RegisterSubscriberRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * registerSubscriberCallable() 

  
UnregisterSubscriber |  Unregisters a service account with subscriber privileges on the Pub/Sub topic created for this Channel Services account or integrator. If there are no service accounts left with subscriber privileges, this deletes the topic. You can call ListSubscribers to check for these accounts.  Possible error codes: 

  * PERMISSION_DENIED: The reseller account making the request and the provided reseller account are different, or the impersonated user is not a super admin. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: The topic resource doesn't exist. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 

Return value: The topic name that unregistered the service email address. Returns a success response if the service email address wasn't registered with the topic. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * unregisterSubscriber(UnregisterSubscriberRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * unregisterSubscriberCallable() 

  
ListSubscribers |  Lists service accounts with subscriber privileges on the Pub/Sub topic created for this Channel Services account or integrator.  Possible error codes: 

  * PERMISSION_DENIED: The reseller account making the request and the provided reseller account are different, or the impersonated user is not a super admin. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: The topic resource doesn't exist. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 

Return value: A list of service email addresses. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSubscribers(ListSubscribersRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSubscribersPagedCallable() 
  * listSubscribersCallable() 

  
ListEntitlementChanges |  List entitlement history.  Possible error codes: 

  * PERMISSION_DENIED: The reseller account making the request and the provided reseller account are different. 
  * INVALID_ARGUMENT: Missing or invalid required fields in the request. 
  * NOT_FOUND: The parent resource doesn't exist. Usually the result of an invalid name parameter. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. In this case, contact CloudChannel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. In this case, contact Cloud Channel support. 

Return value: List of EntitlementChanges. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listEntitlementChanges(ListEntitlementChangesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listEntitlementChanges(EntitlementName parent) 
  * listEntitlementChanges(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listEntitlementChangesPagedCallable() 
  * listEntitlementChangesCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of CloudChannelServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CloudChannelServiceSettings cloudChannelServiceSettings =
         CloudChannelServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     CloudChannelServiceClient cloudChannelServiceClient =
         CloudChannelServiceClient.create(cloudChannelServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CloudChannelServiceSettings cloudChannelServiceSettings =
         CloudChannelServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     CloudChannelServiceClient cloudChannelServiceClient =
         CloudChannelServiceClient.create(cloudChannelServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CloudChannelServiceSettings cloudChannelServiceSettings =
         CloudChannelServiceSettings.newHttpJsonBuilder().build();
     CloudChannelServiceClient cloudChannelServiceClient =
         CloudChannelServiceClient.create(cloudChannelServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CloudChannelServiceClient

## Static Methods 

### create()
    
    
    public static final CloudChannelServiceClient create()

Constructs an instance of CloudChannelServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CloudChannelServiceSettings settings)
    
    
    public static final CloudChannelServiceClient create(CloudChannelServiceSettings settings)

Constructs an instance of CloudChannelServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CloudChannelServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CloudChannelServiceStub stub)
    
    
    public static final CloudChannelServiceClient create(CloudChannelServiceStub stub)

Constructs an instance of CloudChannelServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(CloudChannelServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CloudChannelServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.stub.CloudChannelServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient)` |   
  
## Constructors 

### CloudChannelServiceClient(CloudChannelServiceSettings settings)
    
    
    protected CloudChannelServiceClient(CloudChannelServiceSettings settings)

Constructs an instance of CloudChannelServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CloudChannelServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceSettings)`  
  
  
### CloudChannelServiceClient(CloudChannelServiceStub stub)
    
    
    protected CloudChannelServiceClient(CloudChannelServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CloudChannelServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.stub.CloudChannelServiceStub)`  
  
  
## Methods 

### activateEntitlementAsync(ActivateEntitlementRequest request)
    
    
    public final OperationFuture<Entitlement,OperationMetadata> activateEntitlementAsync(ActivateEntitlementRequest request)

Activates a previously suspended entitlement. Entitlements suspended for pending ToS acceptance can't be activated using this method.

An entitlement activation is a long-running operation and it updates the state of the customer entitlement.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: Entitlement resource not found. 
  * SUSPENSION_NOT_RESELLER_INITIATED: Can only activate reseller-initiated suspensions and entitlements that have accepted the TOS. 
  * NOT_SUSPENDED: Can only activate suspended entitlements not in an ACTIVE state. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ActivateEntitlementRequest request =
           ActivateEntitlementRequest.newBuilder()
               .setName("name3373707")
               .setRequestId("requestId693933066")
               .build();
       Entitlement response = cloudChannelServiceClient.activateEntitlementAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ActivateEntitlementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ActivateEntitlementRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Entitlement](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Entitlement),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### activateEntitlementCallable()
    
    
    public final UnaryCallable<ActivateEntitlementRequest,Operation> activateEntitlementCallable()

Activates a previously suspended entitlement. Entitlements suspended for pending ToS acceptance can't be activated using this method.

An entitlement activation is a long-running operation and it updates the state of the customer entitlement.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: Entitlement resource not found. 
  * SUSPENSION_NOT_RESELLER_INITIATED: Can only activate reseller-initiated suspensions and entitlements that have accepted the TOS. 
  * NOT_SUSPENDED: Can only activate suspended entitlements not in an ACTIVE state. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ActivateEntitlementRequest request =
           ActivateEntitlementRequest.newBuilder()
               .setName("name3373707")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           cloudChannelServiceClient.activateEntitlementCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ActivateEntitlementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ActivateEntitlementRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### activateEntitlementOperationCallable()
    
    
    public final OperationCallable<ActivateEntitlementRequest,Entitlement,OperationMetadata> activateEntitlementOperationCallable()

Activates a previously suspended entitlement. Entitlements suspended for pending ToS acceptance can't be activated using this method.

An entitlement activation is a long-running operation and it updates the state of the customer entitlement.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: Entitlement resource not found. 
  * SUSPENSION_NOT_RESELLER_INITIATED: Can only activate reseller-initiated suspensions and entitlements that have accepted the TOS. 
  * NOT_SUSPENDED: Can only activate suspended entitlements not in an ACTIVE state. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ActivateEntitlementRequest request =
           ActivateEntitlementRequest.newBuilder()
               .setName("name3373707")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Entitlement, OperationMetadata> future =
           cloudChannelServiceClient.activateEntitlementOperationCallable().futureCall(request);
       // Do something.
       Entitlement response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ActivateEntitlementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ActivateEntitlementRequest),[Entitlement](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Entitlement),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### awaitTermination(long duration, TimeUnit unit)
    
    
    public boolean awaitTermination(long duration, TimeUnit unit)

**Parameters**  
---  
**Name** | **Description**  
`duration` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`unit` | `[TimeUnit](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InterruptedException](https://docs.oracle.com/javase/8/docs/api/java/lang/InterruptedException.html)` |   
  
### cancelEntitlementAsync(CancelEntitlementRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> cancelEntitlementAsync(CancelEntitlementRequest request)

Cancels a previously fulfilled entitlement.

An entitlement cancellation is a long-running operation.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * FAILED_PRECONDITION: There are Google Cloud projects linked to the Google Cloud entitlement's Cloud Billing subaccount. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: Entitlement resource not found. 
  * DELETION_TYPE_NOT_ALLOWED: Cancel is only allowed for Google Workspace add-ons, or entitlements for Google Cloud's development platform. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The response will contain google.protobuf.Empty on success. The Operation metadata will contain an instance of OperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       CancelEntitlementRequest request =
           CancelEntitlementRequest.newBuilder()
               .setName("name3373707")
               .setRequestId("requestId693933066")
               .build();
       cloudChannelServiceClient.cancelEntitlementAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CancelEntitlementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CancelEntitlementRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### cancelEntitlementCallable()
    
    
    public final UnaryCallable<CancelEntitlementRequest,Operation> cancelEntitlementCallable()

Cancels a previously fulfilled entitlement.

An entitlement cancellation is a long-running operation.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * FAILED_PRECONDITION: There are Google Cloud projects linked to the Google Cloud entitlement's Cloud Billing subaccount. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: Entitlement resource not found. 
  * DELETION_TYPE_NOT_ALLOWED: Cancel is only allowed for Google Workspace add-ons, or entitlements for Google Cloud's development platform. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The response will contain google.protobuf.Empty on success. The Operation metadata will contain an instance of OperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       CancelEntitlementRequest request =
           CancelEntitlementRequest.newBuilder()
               .setName("name3373707")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           cloudChannelServiceClient.cancelEntitlementCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CancelEntitlementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CancelEntitlementRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### cancelEntitlementOperationCallable()
    
    
    public final OperationCallable<CancelEntitlementRequest,Empty,OperationMetadata> cancelEntitlementOperationCallable()

Cancels a previously fulfilled entitlement.

An entitlement cancellation is a long-running operation.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * FAILED_PRECONDITION: There are Google Cloud projects linked to the Google Cloud entitlement's Cloud Billing subaccount. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: Entitlement resource not found. 
  * DELETION_TYPE_NOT_ALLOWED: Cancel is only allowed for Google Workspace add-ons, or entitlements for Google Cloud's development platform. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The response will contain google.protobuf.Empty on success. The Operation metadata will contain an instance of OperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       CancelEntitlementRequest request =
           CancelEntitlementRequest.newBuilder()
               .setName("name3373707")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           cloudChannelServiceClient.cancelEntitlementOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CancelEntitlementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CancelEntitlementRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### changeOfferAsync(ChangeOfferRequest request)
    
    
    public final OperationFuture<Entitlement,OperationMetadata> changeOfferAsync(ChangeOfferRequest request)

Updates the Offer for an existing customer entitlement.

An entitlement update is a long-running operation and it updates the entitlement as a result of fulfillment.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: Offer or Entitlement resource not found. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ChangeOfferRequest request =
           ChangeOfferRequest.newBuilder()
               .setName("name3373707")
               .setOffer(OfferName.of("[ACCOUNT]", "[OFFER]").toString())
               .addAllParameters(new ArrayList<Parameter>())
               .setPurchaseOrderId("purchaseOrderId2029917384")
               .setRequestId("requestId693933066")
               .setBillingAccount("billingAccount708726578")
               .setPriceReferenceId("priceReferenceId-5103427")
               .build();
       Entitlement response = cloudChannelServiceClient.changeOfferAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ChangeOfferRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChangeOfferRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Entitlement](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Entitlement),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### changeOfferCallable()
    
    
    public final UnaryCallable<ChangeOfferRequest,Operation> changeOfferCallable()

Updates the Offer for an existing customer entitlement.

An entitlement update is a long-running operation and it updates the entitlement as a result of fulfillment.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: Offer or Entitlement resource not found. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ChangeOfferRequest request =
           ChangeOfferRequest.newBuilder()
               .setName("name3373707")
               .setOffer(OfferName.of("[ACCOUNT]", "[OFFER]").toString())
               .addAllParameters(new ArrayList<Parameter>())
               .setPurchaseOrderId("purchaseOrderId2029917384")
               .setRequestId("requestId693933066")
               .setBillingAccount("billingAccount708726578")
               .setPriceReferenceId("priceReferenceId-5103427")
               .build();
       ApiFuture<Operation> future =
           cloudChannelServiceClient.changeOfferCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ChangeOfferRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChangeOfferRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### changeOfferOperationCallable()
    
    
    public final OperationCallable<ChangeOfferRequest,Entitlement,OperationMetadata> changeOfferOperationCallable()

Updates the Offer for an existing customer entitlement.

An entitlement update is a long-running operation and it updates the entitlement as a result of fulfillment.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: Offer or Entitlement resource not found. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ChangeOfferRequest request =
           ChangeOfferRequest.newBuilder()
               .setName("name3373707")
               .setOffer(OfferName.of("[ACCOUNT]", "[OFFER]").toString())
               .addAllParameters(new ArrayList<Parameter>())
               .setPurchaseOrderId("purchaseOrderId2029917384")
               .setRequestId("requestId693933066")
               .setBillingAccount("billingAccount708726578")
               .setPriceReferenceId("priceReferenceId-5103427")
               .build();
       OperationFuture<Entitlement, OperationMetadata> future =
           cloudChannelServiceClient.changeOfferOperationCallable().futureCall(request);
       // Do something.
       Entitlement response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ChangeOfferRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChangeOfferRequest),[Entitlement](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Entitlement),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### changeParametersAsync(ChangeParametersRequest request)
    
    
    public final OperationFuture<Entitlement,OperationMetadata> changeParametersAsync(ChangeParametersRequest request)

Change parameters of the entitlement.

An entitlement update is a long-running operation and it updates the entitlement as a result of fulfillment.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. For example, the number of seats being changed is greater than the allowed number of max seats, or decreasing seats for a commitment based plan. 
  * NOT_FOUND: Entitlement resource not found. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ChangeParametersRequest request =
           ChangeParametersRequest.newBuilder()
               .setName("name3373707")
               .addAllParameters(new ArrayList<Parameter>())
               .setRequestId("requestId693933066")
               .setPurchaseOrderId("purchaseOrderId2029917384")
               .build();
       Entitlement response = cloudChannelServiceClient.changeParametersAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ChangeParametersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChangeParametersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Entitlement](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Entitlement),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### changeParametersCallable()
    
    
    public final UnaryCallable<ChangeParametersRequest,Operation> changeParametersCallable()

Change parameters of the entitlement.

An entitlement update is a long-running operation and it updates the entitlement as a result of fulfillment.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. For example, the number of seats being changed is greater than the allowed number of max seats, or decreasing seats for a commitment based plan. 
  * NOT_FOUND: Entitlement resource not found. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ChangeParametersRequest request =
           ChangeParametersRequest.newBuilder()
               .setName("name3373707")
               .addAllParameters(new ArrayList<Parameter>())
               .setRequestId("requestId693933066")
               .setPurchaseOrderId("purchaseOrderId2029917384")
               .build();
       ApiFuture<Operation> future =
           cloudChannelServiceClient.changeParametersCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ChangeParametersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChangeParametersRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### changeParametersOperationCallable()
    
    
    public final OperationCallable<ChangeParametersRequest,Entitlement,OperationMetadata> changeParametersOperationCallable()

Change parameters of the entitlement.

An entitlement update is a long-running operation and it updates the entitlement as a result of fulfillment.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. For example, the number of seats being changed is greater than the allowed number of max seats, or decreasing seats for a commitment based plan. 
  * NOT_FOUND: Entitlement resource not found. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ChangeParametersRequest request =
           ChangeParametersRequest.newBuilder()
               .setName("name3373707")
               .addAllParameters(new ArrayList<Parameter>())
               .setRequestId("requestId693933066")
               .setPurchaseOrderId("purchaseOrderId2029917384")
               .build();
       OperationFuture<Entitlement, OperationMetadata> future =
           cloudChannelServiceClient.changeParametersOperationCallable().futureCall(request);
       // Do something.
       Entitlement response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ChangeParametersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChangeParametersRequest),[Entitlement](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Entitlement),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### changeRenewalSettingsAsync(ChangeRenewalSettingsRequest request)
    
    
    public final OperationFuture<Entitlement,OperationMetadata> changeRenewalSettingsAsync(ChangeRenewalSettingsRequest request)

Updates the renewal settings for an existing customer entitlement.

An entitlement update is a long-running operation and it updates the entitlement as a result of fulfillment.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: Entitlement resource not found. 
  * NOT_COMMITMENT_PLAN: Renewal Settings are only applicable for a commitment plan. Can't enable or disable renewals for non-commitment plans. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ChangeRenewalSettingsRequest request =
           ChangeRenewalSettingsRequest.newBuilder()
               .setName("name3373707")
               .setRenewalSettings(RenewalSettings.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Entitlement response = cloudChannelServiceClient.changeRenewalSettingsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ChangeRenewalSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChangeRenewalSettingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Entitlement](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Entitlement),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### changeRenewalSettingsCallable()
    
    
    public final UnaryCallable<ChangeRenewalSettingsRequest,Operation> changeRenewalSettingsCallable()

Updates the renewal settings for an existing customer entitlement.

An entitlement update is a long-running operation and it updates the entitlement as a result of fulfillment.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: Entitlement resource not found. 
  * NOT_COMMITMENT_PLAN: Renewal Settings are only applicable for a commitment plan. Can't enable or disable renewals for non-commitment plans. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ChangeRenewalSettingsRequest request =
           ChangeRenewalSettingsRequest.newBuilder()
               .setName("name3373707")
               .setRenewalSettings(RenewalSettings.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           cloudChannelServiceClient.changeRenewalSettingsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ChangeRenewalSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChangeRenewalSettingsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### changeRenewalSettingsOperationCallable()
    
    
    public final OperationCallable<ChangeRenewalSettingsRequest,Entitlement,OperationMetadata> changeRenewalSettingsOperationCallable()

Updates the renewal settings for an existing customer entitlement.

An entitlement update is a long-running operation and it updates the entitlement as a result of fulfillment.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: Entitlement resource not found. 
  * NOT_COMMITMENT_PLAN: Renewal Settings are only applicable for a commitment plan. Can't enable or disable renewals for non-commitment plans. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ChangeRenewalSettingsRequest request =
           ChangeRenewalSettingsRequest.newBuilder()
               .setName("name3373707")
               .setRenewalSettings(RenewalSettings.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Entitlement, OperationMetadata> future =
           cloudChannelServiceClient.changeRenewalSettingsOperationCallable().futureCall(request);
       // Do something.
       Entitlement response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ChangeRenewalSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChangeRenewalSettingsRequest),[Entitlement](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Entitlement),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### checkCloudIdentityAccountsExist(CheckCloudIdentityAccountsExistRequest request)
    
    
    public final CheckCloudIdentityAccountsExistResponse checkCloudIdentityAccountsExist(CheckCloudIdentityAccountsExistRequest request)

Confirms the existence of Cloud Identity accounts based on the domain and if the Cloud Identity accounts are owned by the reseller.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * INVALID_VALUE: Invalid domain value in the request. 



Return value: A list of CloudIdentityCustomerAccount resources for the domain (may be empty)

Note: in the v1alpha1 version of the API, a NOT_FOUND error returns if no CloudIdentityCustomerAccount resources match the domain.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       CheckCloudIdentityAccountsExistRequest request =
           CheckCloudIdentityAccountsExistRequest.newBuilder()
               .setParent("parent-995424086")
               .setDomain("domain-1326197564")
               .setPrimaryAdminEmail("primaryAdminEmail-1896816337")
               .build();
       CheckCloudIdentityAccountsExistResponse response =
           cloudChannelServiceClient.checkCloudIdentityAccountsExist(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CheckCloudIdentityAccountsExistRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CheckCloudIdentityAccountsExistRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CheckCloudIdentityAccountsExistResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CheckCloudIdentityAccountsExistResponse)` |   
  
### checkCloudIdentityAccountsExistCallable()
    
    
    public final UnaryCallable<CheckCloudIdentityAccountsExistRequest,CheckCloudIdentityAccountsExistResponse> checkCloudIdentityAccountsExistCallable()

Confirms the existence of Cloud Identity accounts based on the domain and if the Cloud Identity accounts are owned by the reseller.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * INVALID_VALUE: Invalid domain value in the request. 



Return value: A list of CloudIdentityCustomerAccount resources for the domain (may be empty)

Note: in the v1alpha1 version of the API, a NOT_FOUND error returns if no CloudIdentityCustomerAccount resources match the domain.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       CheckCloudIdentityAccountsExistRequest request =
           CheckCloudIdentityAccountsExistRequest.newBuilder()
               .setParent("parent-995424086")
               .setDomain("domain-1326197564")
               .setPrimaryAdminEmail("primaryAdminEmail-1896816337")
               .build();
       ApiFuture<CheckCloudIdentityAccountsExistResponse> future =
           cloudChannelServiceClient.checkCloudIdentityAccountsExistCallable().futureCall(request);
       // Do something.
       CheckCloudIdentityAccountsExistResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CheckCloudIdentityAccountsExistRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CheckCloudIdentityAccountsExistRequest),[CheckCloudIdentityAccountsExistResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CheckCloudIdentityAccountsExistResponse)>` |   
  
### close()
    
    
    public final void close()

### createChannelPartnerLink(CreateChannelPartnerLinkRequest request)
    
    
    public final ChannelPartnerLink createChannelPartnerLink(CreateChannelPartnerLinkRequest request)

Initiates a channel partner link between a distributor and a reseller, or between resellers in an n-tier reseller channel. Invited partners need to follow the invite_link_uri provided in the response to accept. After accepting the invitation, a link is set up between the two parties. You must be a distributor to call this method.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * ALREADY_EXISTS: The ChannelPartnerLink sent in the request already exists. 
  * NOT_FOUND: No Cloud Identity customer exists for provided domain. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The new ChannelPartnerLink resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       CreateChannelPartnerLinkRequest request =
           CreateChannelPartnerLinkRequest.newBuilder()
               .setParent("parent-995424086")
               .setChannelPartnerLink(ChannelPartnerLink.newBuilder().build())
               .build();
       ChannelPartnerLink response = cloudChannelServiceClient.createChannelPartnerLink(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateChannelPartnerLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CreateChannelPartnerLinkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ChannelPartnerLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerLink)` |   
  
### createChannelPartnerLinkCallable()
    
    
    public final UnaryCallable<CreateChannelPartnerLinkRequest,ChannelPartnerLink> createChannelPartnerLinkCallable()

Initiates a channel partner link between a distributor and a reseller, or between resellers in an n-tier reseller channel. Invited partners need to follow the invite_link_uri provided in the response to accept. After accepting the invitation, a link is set up between the two parties. You must be a distributor to call this method.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * ALREADY_EXISTS: The ChannelPartnerLink sent in the request already exists. 
  * NOT_FOUND: No Cloud Identity customer exists for provided domain. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The new ChannelPartnerLink resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       CreateChannelPartnerLinkRequest request =
           CreateChannelPartnerLinkRequest.newBuilder()
               .setParent("parent-995424086")
               .setChannelPartnerLink(ChannelPartnerLink.newBuilder().build())
               .build();
       ApiFuture<ChannelPartnerLink> future =
           cloudChannelServiceClient.createChannelPartnerLinkCallable().futureCall(request);
       // Do something.
       ChannelPartnerLink response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateChannelPartnerLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CreateChannelPartnerLinkRequest),[ChannelPartnerLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerLink)>` |   
  
### createChannelPartnerRepricingConfig(@Nullable ChannelPartnerLinkName parent, ChannelPartnerRepricingConfig channelPartnerRepricingConfig)
    
    
    public final ChannelPartnerRepricingConfig createChannelPartnerRepricingConfig(@Nullable ChannelPartnerLinkName parent, ChannelPartnerRepricingConfig channelPartnerRepricingConfig)

Creates a ChannelPartnerRepricingConfig. Call this method to set modifications for a specific ChannelPartner's bill. You can only create configs if the RepricingConfig.effective_invoice_month is a future month. If needed, you can create a config for the current month, with some restrictions.

When creating a config for a future month, make sure there are no existing configs for that RepricingConfig.effective_invoice_month.

The following restrictions are for creating configs in the current month.

  * This functionality is reserved for recovering from an erroneous config, and should not be used for regular business cases. 
  * The new config will not modify exports used with other configs. Changes to the config may be immediate, but may take up to 24 hours. 
  * There is a limit of ten configs for any ChannelPartner or RepricingConfig.EntitlementGranularity.entitlement, for any RepricingConfig.effective_invoice_month. 
  * The contained ChannelPartnerRepricingConfig.repricing_config value must be different from the value used in the current config for a ChannelPartner. 



Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * INVALID_ARGUMENT: Missing or invalid required parameters in the request. Also displays if the updated config is for the current month or past months. 
  * NOT_FOUND: The ChannelPartnerRepricingConfig specified does not exist or is not associated with the given account. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the updated ChannelPartnerRepricingConfig resource, otherwise returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ChannelPartnerLinkName parent =
           ChannelPartnerLinkName.of("[ACCOUNT]", "[CHANNEL_PARTNER_LINK]");
       ChannelPartnerRepricingConfig channelPartnerRepricingConfig =
           ChannelPartnerRepricingConfig.newBuilder().build();
       ChannelPartnerRepricingConfig response =
           cloudChannelServiceClient.createChannelPartnerRepricingConfig(
               parent, channelPartnerRepricingConfig);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.channel.v1.ChannelPartnerLinkName`  
Required. The resource name of the ChannelPartner that will receive the repricing config. Parent uses the format: accounts/{account_id}/channelPartnerLinks/{channel_partner_id}  
`channelPartnerRepricingConfig` | `[ChannelPartnerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerRepricingConfig)`  
Required. The ChannelPartnerRepricingConfig object to update.  
**Returns**  
---  
**Type** | **Description**  
`[ChannelPartnerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerRepricingConfig)` |   
  
### createChannelPartnerRepricingConfig(CreateChannelPartnerRepricingConfigRequest request)
    
    
    public final ChannelPartnerRepricingConfig createChannelPartnerRepricingConfig(CreateChannelPartnerRepricingConfigRequest request)

Creates a ChannelPartnerRepricingConfig. Call this method to set modifications for a specific ChannelPartner's bill. You can only create configs if the RepricingConfig.effective_invoice_month is a future month. If needed, you can create a config for the current month, with some restrictions.

When creating a config for a future month, make sure there are no existing configs for that RepricingConfig.effective_invoice_month.

The following restrictions are for creating configs in the current month.

  * This functionality is reserved for recovering from an erroneous config, and should not be used for regular business cases. 
  * The new config will not modify exports used with other configs. Changes to the config may be immediate, but may take up to 24 hours. 
  * There is a limit of ten configs for any ChannelPartner or RepricingConfig.EntitlementGranularity.entitlement, for any RepricingConfig.effective_invoice_month. 
  * The contained ChannelPartnerRepricingConfig.repricing_config value must be different from the value used in the current config for a ChannelPartner. 



Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * INVALID_ARGUMENT: Missing or invalid required parameters in the request. Also displays if the updated config is for the current month or past months. 
  * NOT_FOUND: The ChannelPartnerRepricingConfig specified does not exist or is not associated with the given account. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the updated ChannelPartnerRepricingConfig resource, otherwise returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       CreateChannelPartnerRepricingConfigRequest request =
           CreateChannelPartnerRepricingConfigRequest.newBuilder()
               .setParent(
                   ChannelPartnerLinkName.of("[ACCOUNT]", "[CHANNEL_PARTNER_LINK]").toString())
               .setChannelPartnerRepricingConfig(ChannelPartnerRepricingConfig.newBuilder().build())
               .build();
       ChannelPartnerRepricingConfig response =
           cloudChannelServiceClient.createChannelPartnerRepricingConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CreateChannelPartnerRepricingConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ChannelPartnerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerRepricingConfig)` |   
  
### createChannelPartnerRepricingConfig(String parent, ChannelPartnerRepricingConfig channelPartnerRepricingConfig)
    
    
    public final ChannelPartnerRepricingConfig createChannelPartnerRepricingConfig(String parent, ChannelPartnerRepricingConfig channelPartnerRepricingConfig)

Creates a ChannelPartnerRepricingConfig. Call this method to set modifications for a specific ChannelPartner's bill. You can only create configs if the RepricingConfig.effective_invoice_month is a future month. If needed, you can create a config for the current month, with some restrictions.

When creating a config for a future month, make sure there are no existing configs for that RepricingConfig.effective_invoice_month.

The following restrictions are for creating configs in the current month.

  * This functionality is reserved for recovering from an erroneous config, and should not be used for regular business cases. 
  * The new config will not modify exports used with other configs. Changes to the config may be immediate, but may take up to 24 hours. 
  * There is a limit of ten configs for any ChannelPartner or RepricingConfig.EntitlementGranularity.entitlement, for any RepricingConfig.effective_invoice_month. 
  * The contained ChannelPartnerRepricingConfig.repricing_config value must be different from the value used in the current config for a ChannelPartner. 



Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * INVALID_ARGUMENT: Missing or invalid required parameters in the request. Also displays if the updated config is for the current month or past months. 
  * NOT_FOUND: The ChannelPartnerRepricingConfig specified does not exist or is not associated with the given account. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the updated ChannelPartnerRepricingConfig resource, otherwise returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       String parent = ChannelPartnerLinkName.of("[ACCOUNT]", "[CHANNEL_PARTNER_LINK]").toString();
       ChannelPartnerRepricingConfig channelPartnerRepricingConfig =
           ChannelPartnerRepricingConfig.newBuilder().build();
       ChannelPartnerRepricingConfig response =
           cloudChannelServiceClient.createChannelPartnerRepricingConfig(
               parent, channelPartnerRepricingConfig);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the ChannelPartner that will receive the repricing config. Parent uses the format: accounts/{account_id}/channelPartnerLinks/{channel_partner_id}  
`channelPartnerRepricingConfig` | `[ChannelPartnerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerRepricingConfig)`  
Required. The ChannelPartnerRepricingConfig object to update.  
**Returns**  
---  
**Type** | **Description**  
`[ChannelPartnerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerRepricingConfig)` |   
  
### createChannelPartnerRepricingConfigCallable()
    
    
    public final UnaryCallable<CreateChannelPartnerRepricingConfigRequest,ChannelPartnerRepricingConfig> createChannelPartnerRepricingConfigCallable()

Creates a ChannelPartnerRepricingConfig. Call this method to set modifications for a specific ChannelPartner's bill. You can only create configs if the RepricingConfig.effective_invoice_month is a future month. If needed, you can create a config for the current month, with some restrictions.

When creating a config for a future month, make sure there are no existing configs for that RepricingConfig.effective_invoice_month.

The following restrictions are for creating configs in the current month.

  * This functionality is reserved for recovering from an erroneous config, and should not be used for regular business cases. 
  * The new config will not modify exports used with other configs. Changes to the config may be immediate, but may take up to 24 hours. 
  * There is a limit of ten configs for any ChannelPartner or RepricingConfig.EntitlementGranularity.entitlement, for any RepricingConfig.effective_invoice_month. 
  * The contained ChannelPartnerRepricingConfig.repricing_config value must be different from the value used in the current config for a ChannelPartner. 



Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * INVALID_ARGUMENT: Missing or invalid required parameters in the request. Also displays if the updated config is for the current month or past months. 
  * NOT_FOUND: The ChannelPartnerRepricingConfig specified does not exist or is not associated with the given account. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the updated ChannelPartnerRepricingConfig resource, otherwise returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       CreateChannelPartnerRepricingConfigRequest request =
           CreateChannelPartnerRepricingConfigRequest.newBuilder()
               .setParent(
                   ChannelPartnerLinkName.of("[ACCOUNT]", "[CHANNEL_PARTNER_LINK]").toString())
               .setChannelPartnerRepricingConfig(ChannelPartnerRepricingConfig.newBuilder().build())
               .build();
       ApiFuture<ChannelPartnerRepricingConfig> future =
           cloudChannelServiceClient
               .createChannelPartnerRepricingConfigCallable()
               .futureCall(request);
       // Do something.
       ChannelPartnerRepricingConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CreateChannelPartnerRepricingConfigRequest),[ChannelPartnerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerRepricingConfig)>` |   
  
### createCustomer(CreateCustomerRequest request)
    
    
    public final Customer createCustomer(CreateCustomerRequest request)

Creates a new Customer resource under the reseller or distributor account.

Possible error codes:

  * PERMISSION_DENIED: * The reseller account making the request is different from the reseller account in the API request. * You are not authorized to create a customer. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT: * Required request parameters are missing or invalid. * Domain field value doesn't match the primary email domain. 



Return value: The newly created Customer resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       CreateCustomerRequest request =
           CreateCustomerRequest.newBuilder()
               .setParent("parent-995424086")
               .setCustomer(Customer.newBuilder().build())
               .build();
       Customer response = cloudChannelServiceClient.createCustomer(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateCustomerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CreateCustomerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Customer](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Customer)` |   
  
### createCustomerCallable()
    
    
    public final UnaryCallable<CreateCustomerRequest,Customer> createCustomerCallable()

Creates a new Customer resource under the reseller or distributor account.

Possible error codes:

  * PERMISSION_DENIED: * The reseller account making the request is different from the reseller account in the API request. * You are not authorized to create a customer. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT: * Required request parameters are missing or invalid. * Domain field value doesn't match the primary email domain. 



Return value: The newly created Customer resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       CreateCustomerRequest request =
           CreateCustomerRequest.newBuilder()
               .setParent("parent-995424086")
               .setCustomer(Customer.newBuilder().build())
               .build();
       ApiFuture<Customer> future =
           cloudChannelServiceClient.createCustomerCallable().futureCall(request);
       // Do something.
       Customer response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateCustomerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CreateCustomerRequest),[Customer](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Customer)>` |   
  
### createCustomerRepricingConfig(@Nullable CustomerName parent, CustomerRepricingConfig customerRepricingConfig)
    
    
    public final CustomerRepricingConfig createCustomerRepricingConfig(@Nullable CustomerName parent, CustomerRepricingConfig customerRepricingConfig)

Creates a CustomerRepricingConfig. Call this method to set modifications for a specific customer's bill. You can only create configs if the RepricingConfig.effective_invoice_month is a future month. If needed, you can create a config for the current month, with some restrictions.

When creating a config for a future month, make sure there are no existing configs for that RepricingConfig.effective_invoice_month.

The following restrictions are for creating configs in the current month.

  * This functionality is reserved for recovering from an erroneous config, and should not be used for regular business cases. 
  * The new config will not modify exports used with other configs. Changes to the config may be immediate, but may take up to 24 hours. 
  * There is a limit of ten configs for any RepricingConfig.EntitlementGranularity.entitlement, for any RepricingConfig.effective_invoice_month. 
  * The contained CustomerRepricingConfig.repricing_config value must be different from the value used in the current config for a RepricingConfig.EntitlementGranularity.entitlement. 



Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * INVALID_ARGUMENT: Missing or invalid required parameters in the request. Also displays if the updated config is for the current month or past months. 
  * NOT_FOUND: The CustomerRepricingConfig specified does not exist or is not associated with the given account. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the updated CustomerRepricingConfig resource, otherwise returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       CustomerName parent = CustomerName.of("[ACCOUNT]", "[CUSTOMER]");
       CustomerRepricingConfig customerRepricingConfig =
           CustomerRepricingConfig.newBuilder().build();
       CustomerRepricingConfig response =
           cloudChannelServiceClient.createCustomerRepricingConfig(parent, customerRepricingConfig);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.channel.v1.CustomerName`  
Required. The resource name of the customer that will receive this repricing config. Parent uses the format: accounts/{account_id}/customers/{customer_id}  
`customerRepricingConfig` | `[CustomerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CustomerRepricingConfig)`  
Required. The CustomerRepricingConfig object to update.  
**Returns**  
---  
**Type** | **Description**  
`[CustomerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CustomerRepricingConfig)` |   
  
### createCustomerRepricingConfig(CreateCustomerRepricingConfigRequest request)
    
    
    public final CustomerRepricingConfig createCustomerRepricingConfig(CreateCustomerRepricingConfigRequest request)

Creates a CustomerRepricingConfig. Call this method to set modifications for a specific customer's bill. You can only create configs if the RepricingConfig.effective_invoice_month is a future month. If needed, you can create a config for the current month, with some restrictions.

When creating a config for a future month, make sure there are no existing configs for that RepricingConfig.effective_invoice_month.

The following restrictions are for creating configs in the current month.

  * This functionality is reserved for recovering from an erroneous config, and should not be used for regular business cases. 
  * The new config will not modify exports used with other configs. Changes to the config may be immediate, but may take up to 24 hours. 
  * There is a limit of ten configs for any RepricingConfig.EntitlementGranularity.entitlement, for any RepricingConfig.effective_invoice_month. 
  * The contained CustomerRepricingConfig.repricing_config value must be different from the value used in the current config for a RepricingConfig.EntitlementGranularity.entitlement. 



Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * INVALID_ARGUMENT: Missing or invalid required parameters in the request. Also displays if the updated config is for the current month or past months. 
  * NOT_FOUND: The CustomerRepricingConfig specified does not exist or is not associated with the given account. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the updated CustomerRepricingConfig resource, otherwise returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       CreateCustomerRepricingConfigRequest request =
           CreateCustomerRepricingConfigRequest.newBuilder()
               .setParent(CustomerName.of("[ACCOUNT]", "[CUSTOMER]").toString())
               .setCustomerRepricingConfig(CustomerRepricingConfig.newBuilder().build())
               .build();
       CustomerRepricingConfig response =
           cloudChannelServiceClient.createCustomerRepricingConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateCustomerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CreateCustomerRepricingConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CustomerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CustomerRepricingConfig)` |   
  
### createCustomerRepricingConfig(String parent, CustomerRepricingConfig customerRepricingConfig)
    
    
    public final CustomerRepricingConfig createCustomerRepricingConfig(String parent, CustomerRepricingConfig customerRepricingConfig)

Creates a CustomerRepricingConfig. Call this method to set modifications for a specific customer's bill. You can only create configs if the RepricingConfig.effective_invoice_month is a future month. If needed, you can create a config for the current month, with some restrictions.

When creating a config for a future month, make sure there are no existing configs for that RepricingConfig.effective_invoice_month.

The following restrictions are for creating configs in the current month.

  * This functionality is reserved for recovering from an erroneous config, and should not be used for regular business cases. 
  * The new config will not modify exports used with other configs. Changes to the config may be immediate, but may take up to 24 hours. 
  * There is a limit of ten configs for any RepricingConfig.EntitlementGranularity.entitlement, for any RepricingConfig.effective_invoice_month. 
  * The contained CustomerRepricingConfig.repricing_config value must be different from the value used in the current config for a RepricingConfig.EntitlementGranularity.entitlement. 



Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * INVALID_ARGUMENT: Missing or invalid required parameters in the request. Also displays if the updated config is for the current month or past months. 
  * NOT_FOUND: The CustomerRepricingConfig specified does not exist or is not associated with the given account. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the updated CustomerRepricingConfig resource, otherwise returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       String parent = CustomerName.of("[ACCOUNT]", "[CUSTOMER]").toString();
       CustomerRepricingConfig customerRepricingConfig =
           CustomerRepricingConfig.newBuilder().build();
       CustomerRepricingConfig response =
           cloudChannelServiceClient.createCustomerRepricingConfig(parent, customerRepricingConfig);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the customer that will receive this repricing config. Parent uses the format: accounts/{account_id}/customers/{customer_id}  
`customerRepricingConfig` | `[CustomerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CustomerRepricingConfig)`  
Required. The CustomerRepricingConfig object to update.  
**Returns**  
---  
**Type** | **Description**  
`[CustomerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CustomerRepricingConfig)` |   
  
### createCustomerRepricingConfigCallable()
    
    
    public final UnaryCallable<CreateCustomerRepricingConfigRequest,CustomerRepricingConfig> createCustomerRepricingConfigCallable()

Creates a CustomerRepricingConfig. Call this method to set modifications for a specific customer's bill. You can only create configs if the RepricingConfig.effective_invoice_month is a future month. If needed, you can create a config for the current month, with some restrictions.

When creating a config for a future month, make sure there are no existing configs for that RepricingConfig.effective_invoice_month.

The following restrictions are for creating configs in the current month.

  * This functionality is reserved for recovering from an erroneous config, and should not be used for regular business cases. 
  * The new config will not modify exports used with other configs. Changes to the config may be immediate, but may take up to 24 hours. 
  * There is a limit of ten configs for any RepricingConfig.EntitlementGranularity.entitlement, for any RepricingConfig.effective_invoice_month. 
  * The contained CustomerRepricingConfig.repricing_config value must be different from the value used in the current config for a RepricingConfig.EntitlementGranularity.entitlement. 



Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * INVALID_ARGUMENT: Missing or invalid required parameters in the request. Also displays if the updated config is for the current month or past months. 
  * NOT_FOUND: The CustomerRepricingConfig specified does not exist or is not associated with the given account. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the updated CustomerRepricingConfig resource, otherwise returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       CreateCustomerRepricingConfigRequest request =
           CreateCustomerRepricingConfigRequest.newBuilder()
               .setParent(CustomerName.of("[ACCOUNT]", "[CUSTOMER]").toString())
               .setCustomerRepricingConfig(CustomerRepricingConfig.newBuilder().build())
               .build();
       ApiFuture<CustomerRepricingConfig> future =
           cloudChannelServiceClient.createCustomerRepricingConfigCallable().futureCall(request);
       // Do something.
       CustomerRepricingConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateCustomerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CreateCustomerRepricingConfigRequest),[CustomerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CustomerRepricingConfig)>` |   
  
### createEntitlementAsync(CreateEntitlementRequest request)
    
    
    public final OperationFuture<Entitlement,OperationMetadata> createEntitlementAsync(CreateEntitlementRequest request)

Creates an entitlement for a customer.

Possible error codes:

  * PERMISSION_DENIED: * The customer doesn't belong to the reseller. * The reseller is not authorized to transact on this Product. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT: * Required request parameters are missing or invalid. * There is already a customer entitlement for a SKU from the same product family. 
  * INVALID_VALUE: Make sure the OfferId is valid. If it is, contact Google Channel support for further troubleshooting. 
  * NOT_FOUND: The customer or offer resource was not found. 
  * ALREADY_EXISTS: * The SKU was already purchased for the customer. * The customer's primary email already exists. Retry after changing the customer's primary contact email. 
  * CONDITION_NOT_MET or FAILED_PRECONDITION: * The domain required for purchasing a SKU has not been verified. * A pre-requisite SKU required to purchase an Add-On SKU is missing. For example, Google Workspace Business Starter is required to purchase Vault or Drive. * (Developer accounts only) Reseller and resold domain must meet the following naming requirements: * Domain names must start with goog-test. * Domain names must include the reseller domain. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       CreateEntitlementRequest request =
           CreateEntitlementRequest.newBuilder()
               .setParent(CustomerName.of("[ACCOUNT]", "[CUSTOMER]").toString())
               .setEntitlement(Entitlement.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Entitlement response = cloudChannelServiceClient.createEntitlementAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateEntitlementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CreateEntitlementRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Entitlement](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Entitlement),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### createEntitlementCallable()
    
    
    public final UnaryCallable<CreateEntitlementRequest,Operation> createEntitlementCallable()

Creates an entitlement for a customer.

Possible error codes:

  * PERMISSION_DENIED: * The customer doesn't belong to the reseller. * The reseller is not authorized to transact on this Product. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT: * Required request parameters are missing or invalid. * There is already a customer entitlement for a SKU from the same product family. 
  * INVALID_VALUE: Make sure the OfferId is valid. If it is, contact Google Channel support for further troubleshooting. 
  * NOT_FOUND: The customer or offer resource was not found. 
  * ALREADY_EXISTS: * The SKU was already purchased for the customer. * The customer's primary email already exists. Retry after changing the customer's primary contact email. 
  * CONDITION_NOT_MET or FAILED_PRECONDITION: * The domain required for purchasing a SKU has not been verified. * A pre-requisite SKU required to purchase an Add-On SKU is missing. For example, Google Workspace Business Starter is required to purchase Vault or Drive. * (Developer accounts only) Reseller and resold domain must meet the following naming requirements: * Domain names must start with goog-test. * Domain names must include the reseller domain. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       CreateEntitlementRequest request =
           CreateEntitlementRequest.newBuilder()
               .setParent(CustomerName.of("[ACCOUNT]", "[CUSTOMER]").toString())
               .setEntitlement(Entitlement.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           cloudChannelServiceClient.createEntitlementCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateEntitlementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CreateEntitlementRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createEntitlementOperationCallable()
    
    
    public final OperationCallable<CreateEntitlementRequest,Entitlement,OperationMetadata> createEntitlementOperationCallable()

Creates an entitlement for a customer.

Possible error codes:

  * PERMISSION_DENIED: * The customer doesn't belong to the reseller. * The reseller is not authorized to transact on this Product. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT: * Required request parameters are missing or invalid. * There is already a customer entitlement for a SKU from the same product family. 
  * INVALID_VALUE: Make sure the OfferId is valid. If it is, contact Google Channel support for further troubleshooting. 
  * NOT_FOUND: The customer or offer resource was not found. 
  * ALREADY_EXISTS: * The SKU was already purchased for the customer. * The customer's primary email already exists. Retry after changing the customer's primary contact email. 
  * CONDITION_NOT_MET or FAILED_PRECONDITION: * The domain required for purchasing a SKU has not been verified. * A pre-requisite SKU required to purchase an Add-On SKU is missing. For example, Google Workspace Business Starter is required to purchase Vault or Drive. * (Developer accounts only) Reseller and resold domain must meet the following naming requirements: * Domain names must start with goog-test. * Domain names must include the reseller domain. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       CreateEntitlementRequest request =
           CreateEntitlementRequest.newBuilder()
               .setParent(CustomerName.of("[ACCOUNT]", "[CUSTOMER]").toString())
               .setEntitlement(Entitlement.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Entitlement, OperationMetadata> future =
           cloudChannelServiceClient.createEntitlementOperationCallable().futureCall(request);
       // Do something.
       Entitlement response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateEntitlementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CreateEntitlementRequest),[Entitlement](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Entitlement),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### deleteChannelPartnerRepricingConfig(@Nullable ChannelPartnerRepricingConfigName name)
    
    
    public final void deleteChannelPartnerRepricingConfig(@Nullable ChannelPartnerRepricingConfigName name)

Deletes the given ChannelPartnerRepricingConfig permanently. You can only delete configs if their RepricingConfig.effective_invoice_month is set to a date after the current month.

Possible error codes:

  * PERMISSION_DENIED: The account making the request does not own this customer. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * FAILED_PRECONDITION: The ChannelPartnerRepricingConfig is active or in the past. 
  * NOT_FOUND: No ChannelPartnerRepricingConfig found for the name in the request. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ChannelPartnerRepricingConfigName name =
           ChannelPartnerRepricingConfigName.of(
               "[ACCOUNT]", "[CHANNEL_PARTNER]", "[CHANNEL_PARTNER_REPRICING_CONFIG]");
       cloudChannelServiceClient.deleteChannelPartnerRepricingConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.channel.v1.ChannelPartnerRepricingConfigName`  
Required. The resource name of the channel partner repricing config rule to delete.  
  
### deleteChannelPartnerRepricingConfig(DeleteChannelPartnerRepricingConfigRequest request)
    
    
    public final void deleteChannelPartnerRepricingConfig(DeleteChannelPartnerRepricingConfigRequest request)

Deletes the given ChannelPartnerRepricingConfig permanently. You can only delete configs if their RepricingConfig.effective_invoice_month is set to a date after the current month.

Possible error codes:

  * PERMISSION_DENIED: The account making the request does not own this customer. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * FAILED_PRECONDITION: The ChannelPartnerRepricingConfig is active or in the past. 
  * NOT_FOUND: No ChannelPartnerRepricingConfig found for the name in the request. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       DeleteChannelPartnerRepricingConfigRequest request =
           DeleteChannelPartnerRepricingConfigRequest.newBuilder()
               .setName(
                   ChannelPartnerRepricingConfigName.of(
                           "[ACCOUNT]", "[CHANNEL_PARTNER]", "[CHANNEL_PARTNER_REPRICING_CONFIG]")
                       .toString())
               .build();
       cloudChannelServiceClient.deleteChannelPartnerRepricingConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.DeleteChannelPartnerRepricingConfigRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteChannelPartnerRepricingConfig(String name)
    
    
    public final void deleteChannelPartnerRepricingConfig(String name)

Deletes the given ChannelPartnerRepricingConfig permanently. You can only delete configs if their RepricingConfig.effective_invoice_month is set to a date after the current month.

Possible error codes:

  * PERMISSION_DENIED: The account making the request does not own this customer. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * FAILED_PRECONDITION: The ChannelPartnerRepricingConfig is active or in the past. 
  * NOT_FOUND: No ChannelPartnerRepricingConfig found for the name in the request. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       String name =
           ChannelPartnerRepricingConfigName.of(
                   "[ACCOUNT]", "[CHANNEL_PARTNER]", "[CHANNEL_PARTNER_REPRICING_CONFIG]")
               .toString();
       cloudChannelServiceClient.deleteChannelPartnerRepricingConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the channel partner repricing config rule to delete.  
  
### deleteChannelPartnerRepricingConfigCallable()
    
    
    public final UnaryCallable<DeleteChannelPartnerRepricingConfigRequest,Empty> deleteChannelPartnerRepricingConfigCallable()

Deletes the given ChannelPartnerRepricingConfig permanently. You can only delete configs if their RepricingConfig.effective_invoice_month is set to a date after the current month.

Possible error codes:

  * PERMISSION_DENIED: The account making the request does not own this customer. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * FAILED_PRECONDITION: The ChannelPartnerRepricingConfig is active or in the past. 
  * NOT_FOUND: No ChannelPartnerRepricingConfig found for the name in the request. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       DeleteChannelPartnerRepricingConfigRequest request =
           DeleteChannelPartnerRepricingConfigRequest.newBuilder()
               .setName(
                   ChannelPartnerRepricingConfigName.of(
                           "[ACCOUNT]", "[CHANNEL_PARTNER]", "[CHANNEL_PARTNER_REPRICING_CONFIG]")
                       .toString())
               .build();
       ApiFuture<Empty> future =
           cloudChannelServiceClient
               .deleteChannelPartnerRepricingConfigCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.DeleteChannelPartnerRepricingConfigRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteCustomer(@Nullable CustomerName name)
    
    
    public final void deleteCustomer(@Nullable CustomerName name)

Deletes the given Customer permanently.

Possible error codes:

  * PERMISSION_DENIED: The account making the request does not own this customer. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * FAILED_PRECONDITION: The customer has existing entitlements. 
  * NOT_FOUND: No Customer resource found for the name in the request. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       CustomerName name = CustomerName.of("[ACCOUNT]", "[CUSTOMER]");
       cloudChannelServiceClient.deleteCustomer(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.channel.v1.CustomerName`  
Required. The resource name of the customer to delete.  
  
### deleteCustomer(DeleteCustomerRequest request)
    
    
    public final void deleteCustomer(DeleteCustomerRequest request)

Deletes the given Customer permanently.

Possible error codes:

  * PERMISSION_DENIED: The account making the request does not own this customer. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * FAILED_PRECONDITION: The customer has existing entitlements. 
  * NOT_FOUND: No Customer resource found for the name in the request. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       DeleteCustomerRequest request =
           DeleteCustomerRequest.newBuilder()
               .setName(CustomerName.of("[ACCOUNT]", "[CUSTOMER]").toString())
               .build();
       cloudChannelServiceClient.deleteCustomer(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteCustomerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.DeleteCustomerRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteCustomer(String name)
    
    
    public final void deleteCustomer(String name)

Deletes the given Customer permanently.

Possible error codes:

  * PERMISSION_DENIED: The account making the request does not own this customer. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * FAILED_PRECONDITION: The customer has existing entitlements. 
  * NOT_FOUND: No Customer resource found for the name in the request. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       String name = CustomerName.of("[ACCOUNT]", "[CUSTOMER]").toString();
       cloudChannelServiceClient.deleteCustomer(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the customer to delete.  
  
### deleteCustomerCallable()
    
    
    public final UnaryCallable<DeleteCustomerRequest,Empty> deleteCustomerCallable()

Deletes the given Customer permanently.

Possible error codes:

  * PERMISSION_DENIED: The account making the request does not own this customer. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * FAILED_PRECONDITION: The customer has existing entitlements. 
  * NOT_FOUND: No Customer resource found for the name in the request. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       DeleteCustomerRequest request =
           DeleteCustomerRequest.newBuilder()
               .setName(CustomerName.of("[ACCOUNT]", "[CUSTOMER]").toString())
               .build();
       ApiFuture<Empty> future =
           cloudChannelServiceClient.deleteCustomerCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteCustomerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.DeleteCustomerRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteCustomerRepricingConfig(@Nullable CustomerRepricingConfigName name)
    
    
    public final void deleteCustomerRepricingConfig(@Nullable CustomerRepricingConfigName name)

Deletes the given CustomerRepricingConfig permanently. You can only delete configs if their RepricingConfig.effective_invoice_month is set to a date after the current month.

Possible error codes:

  * PERMISSION_DENIED: The account making the request does not own this customer. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * FAILED_PRECONDITION: The CustomerRepricingConfig is active or in the past. 
  * NOT_FOUND: No CustomerRepricingConfig found for the name in the request. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       CustomerRepricingConfigName name =
           CustomerRepricingConfigName.of("[ACCOUNT]", "[CUSTOMER]", "[CUSTOMER_REPRICING_CONFIG]");
       cloudChannelServiceClient.deleteCustomerRepricingConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.channel.v1.CustomerRepricingConfigName`  
Required. The resource name of the customer repricing config rule to delete. Format: accounts/{account_id}/customers/{customer_id}/customerRepricingConfigs/{id}.  
  
### deleteCustomerRepricingConfig(DeleteCustomerRepricingConfigRequest request)
    
    
    public final void deleteCustomerRepricingConfig(DeleteCustomerRepricingConfigRequest request)

Deletes the given CustomerRepricingConfig permanently. You can only delete configs if their RepricingConfig.effective_invoice_month is set to a date after the current month.

Possible error codes:

  * PERMISSION_DENIED: The account making the request does not own this customer. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * FAILED_PRECONDITION: The CustomerRepricingConfig is active or in the past. 
  * NOT_FOUND: No CustomerRepricingConfig found for the name in the request. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       DeleteCustomerRepricingConfigRequest request =
           DeleteCustomerRepricingConfigRequest.newBuilder()
               .setName(
                   CustomerRepricingConfigName.of(
                           "[ACCOUNT]", "[CUSTOMER]", "[CUSTOMER_REPRICING_CONFIG]")
                       .toString())
               .build();
       cloudChannelServiceClient.deleteCustomerRepricingConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteCustomerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.DeleteCustomerRepricingConfigRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteCustomerRepricingConfig(String name)
    
    
    public final void deleteCustomerRepricingConfig(String name)

Deletes the given CustomerRepricingConfig permanently. You can only delete configs if their RepricingConfig.effective_invoice_month is set to a date after the current month.

Possible error codes:

  * PERMISSION_DENIED: The account making the request does not own this customer. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * FAILED_PRECONDITION: The CustomerRepricingConfig is active or in the past. 
  * NOT_FOUND: No CustomerRepricingConfig found for the name in the request. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       String name =
           CustomerRepricingConfigName.of("[ACCOUNT]", "[CUSTOMER]", "[CUSTOMER_REPRICING_CONFIG]")
               .toString();
       cloudChannelServiceClient.deleteCustomerRepricingConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the customer repricing config rule to delete. Format: accounts/{account_id}/customers/{customer_id}/customerRepricingConfigs/{id}.  
  
### deleteCustomerRepricingConfigCallable()
    
    
    public final UnaryCallable<DeleteCustomerRepricingConfigRequest,Empty> deleteCustomerRepricingConfigCallable()

Deletes the given CustomerRepricingConfig permanently. You can only delete configs if their RepricingConfig.effective_invoice_month is set to a date after the current month.

Possible error codes:

  * PERMISSION_DENIED: The account making the request does not own this customer. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * FAILED_PRECONDITION: The CustomerRepricingConfig is active or in the past. 
  * NOT_FOUND: No CustomerRepricingConfig found for the name in the request. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       DeleteCustomerRepricingConfigRequest request =
           DeleteCustomerRepricingConfigRequest.newBuilder()
               .setName(
                   CustomerRepricingConfigName.of(
                           "[ACCOUNT]", "[CUSTOMER]", "[CUSTOMER_REPRICING_CONFIG]")
                       .toString())
               .build();
       ApiFuture<Empty> future =
           cloudChannelServiceClient.deleteCustomerRepricingConfigCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteCustomerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.DeleteCustomerRepricingConfigRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getChannelPartnerLink(GetChannelPartnerLinkRequest request)
    
    
    public final ChannelPartnerLink getChannelPartnerLink(GetChannelPartnerLinkRequest request)

Returns the requested ChannelPartnerLink resource. You must be a distributor to call this method.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: ChannelPartnerLink resource not found because of an invalid channel partner link name. 



Return value: The ChannelPartnerLink resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       GetChannelPartnerLinkRequest request =
           GetChannelPartnerLinkRequest.newBuilder()
               .setName("name3373707")
               .setView(ChannelPartnerLinkView.forNumber(0))
               .build();
       ChannelPartnerLink response = cloudChannelServiceClient.getChannelPartnerLink(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetChannelPartnerLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.GetChannelPartnerLinkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ChannelPartnerLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerLink)` |   
  
### getChannelPartnerLinkCallable()
    
    
    public final UnaryCallable<GetChannelPartnerLinkRequest,ChannelPartnerLink> getChannelPartnerLinkCallable()

Returns the requested ChannelPartnerLink resource. You must be a distributor to call this method.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: ChannelPartnerLink resource not found because of an invalid channel partner link name. 



Return value: The ChannelPartnerLink resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       GetChannelPartnerLinkRequest request =
           GetChannelPartnerLinkRequest.newBuilder()
               .setName("name3373707")
               .setView(ChannelPartnerLinkView.forNumber(0))
               .build();
       ApiFuture<ChannelPartnerLink> future =
           cloudChannelServiceClient.getChannelPartnerLinkCallable().futureCall(request);
       // Do something.
       ChannelPartnerLink response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetChannelPartnerLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.GetChannelPartnerLinkRequest),[ChannelPartnerLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerLink)>` |   
  
### getChannelPartnerRepricingConfig(@Nullable ChannelPartnerRepricingConfigName name)
    
    
    public final ChannelPartnerRepricingConfig getChannelPartnerRepricingConfig(@Nullable ChannelPartnerRepricingConfigName name)

Gets information about how a Distributor modifies their bill before sending it to a ChannelPartner.

Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * NOT_FOUND: The ChannelPartnerRepricingConfig was not found. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the ChannelPartnerRepricingConfig resource, otherwise returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ChannelPartnerRepricingConfigName name =
           ChannelPartnerRepricingConfigName.of(
               "[ACCOUNT]", "[CHANNEL_PARTNER]", "[CHANNEL_PARTNER_REPRICING_CONFIG]");
       ChannelPartnerRepricingConfig response =
           cloudChannelServiceClient.getChannelPartnerRepricingConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.channel.v1.ChannelPartnerRepricingConfigName`  
Required. The resource name of the ChannelPartnerRepricingConfig Format: accounts/{account_id}/channelPartnerLinks/{channel_partner_id}/channelPartnerRepricingConfigs/{id}.  
**Returns**  
---  
**Type** | **Description**  
`[ChannelPartnerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerRepricingConfig)` |   
  
### getChannelPartnerRepricingConfig(GetChannelPartnerRepricingConfigRequest request)
    
    
    public final ChannelPartnerRepricingConfig getChannelPartnerRepricingConfig(GetChannelPartnerRepricingConfigRequest request)

Gets information about how a Distributor modifies their bill before sending it to a ChannelPartner.

Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * NOT_FOUND: The ChannelPartnerRepricingConfig was not found. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the ChannelPartnerRepricingConfig resource, otherwise returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       GetChannelPartnerRepricingConfigRequest request =
           GetChannelPartnerRepricingConfigRequest.newBuilder()
               .setName(
                   ChannelPartnerRepricingConfigName.of(
                           "[ACCOUNT]", "[CHANNEL_PARTNER]", "[CHANNEL_PARTNER_REPRICING_CONFIG]")
                       .toString())
               .build();
       ChannelPartnerRepricingConfig response =
           cloudChannelServiceClient.getChannelPartnerRepricingConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.GetChannelPartnerRepricingConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ChannelPartnerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerRepricingConfig)` |   
  
### getChannelPartnerRepricingConfig(String name)
    
    
    public final ChannelPartnerRepricingConfig getChannelPartnerRepricingConfig(String name)

Gets information about how a Distributor modifies their bill before sending it to a ChannelPartner.

Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * NOT_FOUND: The ChannelPartnerRepricingConfig was not found. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the ChannelPartnerRepricingConfig resource, otherwise returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       String name =
           ChannelPartnerRepricingConfigName.of(
                   "[ACCOUNT]", "[CHANNEL_PARTNER]", "[CHANNEL_PARTNER_REPRICING_CONFIG]")
               .toString();
       ChannelPartnerRepricingConfig response =
           cloudChannelServiceClient.getChannelPartnerRepricingConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the ChannelPartnerRepricingConfig Format: accounts/{account_id}/channelPartnerLinks/{channel_partner_id}/channelPartnerRepricingConfigs/{id}.  
**Returns**  
---  
**Type** | **Description**  
`[ChannelPartnerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerRepricingConfig)` |   
  
### getChannelPartnerRepricingConfigCallable()
    
    
    public final UnaryCallable<GetChannelPartnerRepricingConfigRequest,ChannelPartnerRepricingConfig> getChannelPartnerRepricingConfigCallable()

Gets information about how a Distributor modifies their bill before sending it to a ChannelPartner.

Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * NOT_FOUND: The ChannelPartnerRepricingConfig was not found. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the ChannelPartnerRepricingConfig resource, otherwise returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       GetChannelPartnerRepricingConfigRequest request =
           GetChannelPartnerRepricingConfigRequest.newBuilder()
               .setName(
                   ChannelPartnerRepricingConfigName.of(
                           "[ACCOUNT]", "[CHANNEL_PARTNER]", "[CHANNEL_PARTNER_REPRICING_CONFIG]")
                       .toString())
               .build();
       ApiFuture<ChannelPartnerRepricingConfig> future =
           cloudChannelServiceClient.getChannelPartnerRepricingConfigCallable().futureCall(request);
       // Do something.
       ChannelPartnerRepricingConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.GetChannelPartnerRepricingConfigRequest),[ChannelPartnerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerRepricingConfig)>` |   
  
### getCustomer(@Nullable CustomerName name)
    
    
    public final Customer getCustomer(@Nullable CustomerName name)

Returns the requested Customer resource.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: The customer resource doesn't exist. Usually the result of an invalid name parameter. 



Return value: The Customer resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       CustomerName name = CustomerName.of("[ACCOUNT]", "[CUSTOMER]");
       Customer response = cloudChannelServiceClient.getCustomer(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.channel.v1.CustomerName`  
Required. The resource name of the customer to retrieve. Name uses the format: accounts/{account_id}/customers/{customer_id}  
**Returns**  
---  
**Type** | **Description**  
`[Customer](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Customer)` |   
  
### getCustomer(GetCustomerRequest request)
    
    
    public final Customer getCustomer(GetCustomerRequest request)

Returns the requested Customer resource.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: The customer resource doesn't exist. Usually the result of an invalid name parameter. 



Return value: The Customer resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       GetCustomerRequest request =
           GetCustomerRequest.newBuilder()
               .setName(CustomerName.of("[ACCOUNT]", "[CUSTOMER]").toString())
               .build();
       Customer response = cloudChannelServiceClient.getCustomer(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCustomerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.GetCustomerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Customer](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Customer)` |   
  
### getCustomer(String name)
    
    
    public final Customer getCustomer(String name)

Returns the requested Customer resource.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: The customer resource doesn't exist. Usually the result of an invalid name parameter. 



Return value: The Customer resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       String name = CustomerName.of("[ACCOUNT]", "[CUSTOMER]").toString();
       Customer response = cloudChannelServiceClient.getCustomer(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the customer to retrieve. Name uses the format: accounts/{account_id}/customers/{customer_id}  
**Returns**  
---  
**Type** | **Description**  
`[Customer](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Customer)` |   
  
### getCustomerCallable()
    
    
    public final UnaryCallable<GetCustomerRequest,Customer> getCustomerCallable()

Returns the requested Customer resource.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: The customer resource doesn't exist. Usually the result of an invalid name parameter. 



Return value: The Customer resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       GetCustomerRequest request =
           GetCustomerRequest.newBuilder()
               .setName(CustomerName.of("[ACCOUNT]", "[CUSTOMER]").toString())
               .build();
       ApiFuture<Customer> future =
           cloudChannelServiceClient.getCustomerCallable().futureCall(request);
       // Do something.
       Customer response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetCustomerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.GetCustomerRequest),[Customer](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Customer)>` |   
  
### getCustomerRepricingConfig(@Nullable CustomerRepricingConfigName name)
    
    
    public final CustomerRepricingConfig getCustomerRepricingConfig(@Nullable CustomerRepricingConfigName name)

Gets information about how a Reseller modifies their bill before sending it to a Customer.

Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * NOT_FOUND: The CustomerRepricingConfig was not found. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the CustomerRepricingConfig resource, otherwise returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       CustomerRepricingConfigName name =
           CustomerRepricingConfigName.of("[ACCOUNT]", "[CUSTOMER]", "[CUSTOMER_REPRICING_CONFIG]");
       CustomerRepricingConfig response = cloudChannelServiceClient.getCustomerRepricingConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.channel.v1.CustomerRepricingConfigName`  
Required. The resource name of the CustomerRepricingConfig. Format: accounts/{account_id}/customers/{customer_id}/customerRepricingConfigs/{id}.  
**Returns**  
---  
**Type** | **Description**  
`[CustomerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CustomerRepricingConfig)` |   
  
### getCustomerRepricingConfig(GetCustomerRepricingConfigRequest request)
    
    
    public final CustomerRepricingConfig getCustomerRepricingConfig(GetCustomerRepricingConfigRequest request)

Gets information about how a Reseller modifies their bill before sending it to a Customer.

Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * NOT_FOUND: The CustomerRepricingConfig was not found. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the CustomerRepricingConfig resource, otherwise returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       GetCustomerRepricingConfigRequest request =
           GetCustomerRepricingConfigRequest.newBuilder()
               .setName(
                   CustomerRepricingConfigName.of(
                           "[ACCOUNT]", "[CUSTOMER]", "[CUSTOMER_REPRICING_CONFIG]")
                       .toString())
               .build();
       CustomerRepricingConfig response =
           cloudChannelServiceClient.getCustomerRepricingConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCustomerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.GetCustomerRepricingConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CustomerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CustomerRepricingConfig)` |   
  
### getCustomerRepricingConfig(String name)
    
    
    public final CustomerRepricingConfig getCustomerRepricingConfig(String name)

Gets information about how a Reseller modifies their bill before sending it to a Customer.

Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * NOT_FOUND: The CustomerRepricingConfig was not found. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the CustomerRepricingConfig resource, otherwise returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       String name =
           CustomerRepricingConfigName.of("[ACCOUNT]", "[CUSTOMER]", "[CUSTOMER_REPRICING_CONFIG]")
               .toString();
       CustomerRepricingConfig response = cloudChannelServiceClient.getCustomerRepricingConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the CustomerRepricingConfig. Format: accounts/{account_id}/customers/{customer_id}/customerRepricingConfigs/{id}.  
**Returns**  
---  
**Type** | **Description**  
`[CustomerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CustomerRepricingConfig)` |   
  
### getCustomerRepricingConfigCallable()
    
    
    public final UnaryCallable<GetCustomerRepricingConfigRequest,CustomerRepricingConfig> getCustomerRepricingConfigCallable()

Gets information about how a Reseller modifies their bill before sending it to a Customer.

Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * NOT_FOUND: The CustomerRepricingConfig was not found. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the CustomerRepricingConfig resource, otherwise returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       GetCustomerRepricingConfigRequest request =
           GetCustomerRepricingConfigRequest.newBuilder()
               .setName(
                   CustomerRepricingConfigName.of(
                           "[ACCOUNT]", "[CUSTOMER]", "[CUSTOMER_REPRICING_CONFIG]")
                       .toString())
               .build();
       ApiFuture<CustomerRepricingConfig> future =
           cloudChannelServiceClient.getCustomerRepricingConfigCallable().futureCall(request);
       // Do something.
       CustomerRepricingConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetCustomerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.GetCustomerRepricingConfigRequest),[CustomerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CustomerRepricingConfig)>` |   
  
### getEntitlement(GetEntitlementRequest request)
    
    
    public final Entitlement getEntitlement(GetEntitlementRequest request)

Returns the requested Entitlement resource.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: The customer entitlement was not found. 



Return value: The requested Entitlement resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       GetEntitlementRequest request =
           GetEntitlementRequest.newBuilder()
               .setName(EntitlementName.of("[ACCOUNT]", "[CUSTOMER]", "[ENTITLEMENT]").toString())
               .build();
       Entitlement response = cloudChannelServiceClient.getEntitlement(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetEntitlementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.GetEntitlementRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Entitlement](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Entitlement)` |   
  
### getEntitlementCallable()
    
    
    public final UnaryCallable<GetEntitlementRequest,Entitlement> getEntitlementCallable()

Returns the requested Entitlement resource.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: The customer entitlement was not found. 



Return value: The requested Entitlement resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       GetEntitlementRequest request =
           GetEntitlementRequest.newBuilder()
               .setName(EntitlementName.of("[ACCOUNT]", "[CUSTOMER]", "[ENTITLEMENT]").toString())
               .build();
       ApiFuture<Entitlement> future =
           cloudChannelServiceClient.getEntitlementCallable().futureCall(request);
       // Do something.
       Entitlement response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetEntitlementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.GetEntitlementRequest),[Entitlement](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Entitlement)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable CloudChannelServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.channel.v1.CloudChannelServiceSettings` |   
  
### getStub()
    
    
    public CloudChannelServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.stub.CloudChannelServiceStub)` |   
  
### importCustomer(ImportCustomerRequest request)
    
    
    public final Customer importCustomer(ImportCustomerRequest request)

Imports a Customer from the Cloud Identity associated with the provided Cloud Identity ID or domain before a TransferEntitlements call. If a linked Customer already exists and overwrite_if_exists is true, it will update that Customer's data.

Possible error codes:

  * PERMISSION_DENIED: * The reseller account making the request is different from the reseller account in the API request. * You are not authorized to import the customer. See <https://support.google.com/channelservices/answer/9759265>
  * NOT_FOUND: Cloud Identity doesn't exist or was deleted. 
  * INVALID_ARGUMENT: Required parameters are missing, or the auth_token is expired or invalid. 
  * ALREADY_EXISTS: A customer already exists and has conflicting critical fields. Requires an overwrite. 



Return value: The Customer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ImportCustomerRequest request =
           ImportCustomerRequest.newBuilder()
               .setParent("parent-995424086")
               .setAuthToken("authToken1450587441")
               .setOverwriteIfExists(true)
               .setChannelPartnerId("channelPartnerId-170366400")
               .setCustomer(CustomerName.of("[ACCOUNT]", "[CUSTOMER]").toString())
               .build();
       Customer response = cloudChannelServiceClient.importCustomer(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportCustomerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ImportCustomerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Customer](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Customer)` |   
  
### importCustomerCallable()
    
    
    public final UnaryCallable<ImportCustomerRequest,Customer> importCustomerCallable()

Imports a Customer from the Cloud Identity associated with the provided Cloud Identity ID or domain before a TransferEntitlements call. If a linked Customer already exists and overwrite_if_exists is true, it will update that Customer's data.

Possible error codes:

  * PERMISSION_DENIED: * The reseller account making the request is different from the reseller account in the API request. * You are not authorized to import the customer. See <https://support.google.com/channelservices/answer/9759265>
  * NOT_FOUND: Cloud Identity doesn't exist or was deleted. 
  * INVALID_ARGUMENT: Required parameters are missing, or the auth_token is expired or invalid. 
  * ALREADY_EXISTS: A customer already exists and has conflicting critical fields. Requires an overwrite. 



Return value: The Customer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ImportCustomerRequest request =
           ImportCustomerRequest.newBuilder()
               .setParent("parent-995424086")
               .setAuthToken("authToken1450587441")
               .setOverwriteIfExists(true)
               .setChannelPartnerId("channelPartnerId-170366400")
               .setCustomer(CustomerName.of("[ACCOUNT]", "[CUSTOMER]").toString())
               .build();
       ApiFuture<Customer> future =
           cloudChannelServiceClient.importCustomerCallable().futureCall(request);
       // Do something.
       Customer response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ImportCustomerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ImportCustomerRequest),[Customer](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Customer)>` |   
  
### isShutdown()
    
    
    public boolean isShutdown()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isTerminated()
    
    
    public boolean isTerminated()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### listChannelPartnerLinks(ListChannelPartnerLinksRequest request)
    
    
    public final CloudChannelServiceClient.ListChannelPartnerLinksPagedResponse listChannelPartnerLinks(ListChannelPartnerLinksRequest request)

List ChannelPartnerLinks belonging to a distributor. You must be a distributor to call this method.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 



Return value: The list of the distributor account's ChannelPartnerLink resources.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListChannelPartnerLinksRequest request =
           ListChannelPartnerLinksRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setView(ChannelPartnerLinkView.forNumber(0))
               .build();
       for (ChannelPartnerLink element :
           cloudChannelServiceClient.listChannelPartnerLinks(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListChannelPartnerLinksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListChannelPartnerLinksRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceClient.ListChannelPartnerLinksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListChannelPartnerLinksPagedResponse)` |   
  
### listChannelPartnerLinksCallable()
    
    
    public final UnaryCallable<ListChannelPartnerLinksRequest,ListChannelPartnerLinksResponse> listChannelPartnerLinksCallable()

List ChannelPartnerLinks belonging to a distributor. You must be a distributor to call this method.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 



Return value: The list of the distributor account's ChannelPartnerLink resources.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListChannelPartnerLinksRequest request =
           ListChannelPartnerLinksRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setView(ChannelPartnerLinkView.forNumber(0))
               .build();
       while (true) {
         ListChannelPartnerLinksResponse response =
             cloudChannelServiceClient.listChannelPartnerLinksCallable().call(request);
         for (ChannelPartnerLink element : response.getChannelPartnerLinksList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListChannelPartnerLinksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListChannelPartnerLinksRequest),[ListChannelPartnerLinksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListChannelPartnerLinksResponse)>` |   
  
### listChannelPartnerLinksPagedCallable()
    
    
    public final UnaryCallable<ListChannelPartnerLinksRequest,CloudChannelServiceClient.ListChannelPartnerLinksPagedResponse> listChannelPartnerLinksPagedCallable()

List ChannelPartnerLinks belonging to a distributor. You must be a distributor to call this method.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 



Return value: The list of the distributor account's ChannelPartnerLink resources.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListChannelPartnerLinksRequest request =
           ListChannelPartnerLinksRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setView(ChannelPartnerLinkView.forNumber(0))
               .build();
       ApiFuture<ChannelPartnerLink> future =
           cloudChannelServiceClient.listChannelPartnerLinksPagedCallable().futureCall(request);
       // Do something.
       for (ChannelPartnerLink element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListChannelPartnerLinksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListChannelPartnerLinksRequest),[ListChannelPartnerLinksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListChannelPartnerLinksPagedResponse)>` |   
  
### listChannelPartnerRepricingConfigs(@Nullable ChannelPartnerLinkName parent)
    
    
    public final CloudChannelServiceClient.ListChannelPartnerRepricingConfigsPagedResponse listChannelPartnerRepricingConfigs(@Nullable ChannelPartnerLinkName parent)

Lists information about how a Reseller modifies their bill before sending it to a ChannelPartner.

Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * NOT_FOUND: The ChannelPartnerRepricingConfig specified does not exist or is not associated with the given account. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the ChannelPartnerRepricingConfig resources. The data for each resource is displayed in the ascending order of:

  * Channel Partner ID 
  * RepricingConfig.effective_invoice_month
  * ChannelPartnerRepricingConfig.update_time



If unsuccessful, returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ChannelPartnerLinkName parent =
           ChannelPartnerLinkName.of("[ACCOUNT]", "[CHANNEL_PARTNER_LINK]");
       for (ChannelPartnerRepricingConfig element :
           cloudChannelServiceClient.listChannelPartnerRepricingConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.channel.v1.ChannelPartnerLinkName`  
Required. The resource name of the account's ChannelPartnerLink. Parent uses the format: accounts/{account_id}/channelPartnerLinks/{channel_partner_id}. Supports accounts/{account_id}/channelPartnerLinks/- to retrieve configs for all channel partners.  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceClient.ListChannelPartnerRepricingConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListChannelPartnerRepricingConfigsPagedResponse)` |   
  
### listChannelPartnerRepricingConfigs(ListChannelPartnerRepricingConfigsRequest request)
    
    
    public final CloudChannelServiceClient.ListChannelPartnerRepricingConfigsPagedResponse listChannelPartnerRepricingConfigs(ListChannelPartnerRepricingConfigsRequest request)

Lists information about how a Reseller modifies their bill before sending it to a ChannelPartner.

Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * NOT_FOUND: The ChannelPartnerRepricingConfig specified does not exist or is not associated with the given account. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the ChannelPartnerRepricingConfig resources. The data for each resource is displayed in the ascending order of:

  * Channel Partner ID 
  * RepricingConfig.effective_invoice_month
  * ChannelPartnerRepricingConfig.update_time



If unsuccessful, returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListChannelPartnerRepricingConfigsRequest request =
           ListChannelPartnerRepricingConfigsRequest.newBuilder()
               .setParent(
                   ChannelPartnerLinkName.of("[ACCOUNT]", "[CHANNEL_PARTNER_LINK]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (ChannelPartnerRepricingConfig element :
           cloudChannelServiceClient.listChannelPartnerRepricingConfigs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListChannelPartnerRepricingConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListChannelPartnerRepricingConfigsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceClient.ListChannelPartnerRepricingConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListChannelPartnerRepricingConfigsPagedResponse)` |   
  
### listChannelPartnerRepricingConfigs(String parent)
    
    
    public final CloudChannelServiceClient.ListChannelPartnerRepricingConfigsPagedResponse listChannelPartnerRepricingConfigs(String parent)

Lists information about how a Reseller modifies their bill before sending it to a ChannelPartner.

Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * NOT_FOUND: The ChannelPartnerRepricingConfig specified does not exist or is not associated with the given account. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the ChannelPartnerRepricingConfig resources. The data for each resource is displayed in the ascending order of:

  * Channel Partner ID 
  * RepricingConfig.effective_invoice_month
  * ChannelPartnerRepricingConfig.update_time



If unsuccessful, returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       String parent = ChannelPartnerLinkName.of("[ACCOUNT]", "[CHANNEL_PARTNER_LINK]").toString();
       for (ChannelPartnerRepricingConfig element :
           cloudChannelServiceClient.listChannelPartnerRepricingConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the account's ChannelPartnerLink. Parent uses the format: accounts/{account_id}/channelPartnerLinks/{channel_partner_id}. Supports accounts/{account_id}/channelPartnerLinks/- to retrieve configs for all channel partners.  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceClient.ListChannelPartnerRepricingConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListChannelPartnerRepricingConfigsPagedResponse)` |   
  
### listChannelPartnerRepricingConfigsCallable()
    
    
    public final UnaryCallable<ListChannelPartnerRepricingConfigsRequest,ListChannelPartnerRepricingConfigsResponse> listChannelPartnerRepricingConfigsCallable()

Lists information about how a Reseller modifies their bill before sending it to a ChannelPartner.

Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * NOT_FOUND: The ChannelPartnerRepricingConfig specified does not exist or is not associated with the given account. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the ChannelPartnerRepricingConfig resources. The data for each resource is displayed in the ascending order of:

  * Channel Partner ID 
  * RepricingConfig.effective_invoice_month
  * ChannelPartnerRepricingConfig.update_time



If unsuccessful, returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListChannelPartnerRepricingConfigsRequest request =
           ListChannelPartnerRepricingConfigsRequest.newBuilder()
               .setParent(
                   ChannelPartnerLinkName.of("[ACCOUNT]", "[CHANNEL_PARTNER_LINK]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListChannelPartnerRepricingConfigsResponse response =
             cloudChannelServiceClient.listChannelPartnerRepricingConfigsCallable().call(request);
         for (ChannelPartnerRepricingConfig element :
             response.getChannelPartnerRepricingConfigsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListChannelPartnerRepricingConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListChannelPartnerRepricingConfigsRequest),[ListChannelPartnerRepricingConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListChannelPartnerRepricingConfigsResponse)>` |   
  
### listChannelPartnerRepricingConfigsPagedCallable()
    
    
    public final UnaryCallable<ListChannelPartnerRepricingConfigsRequest,CloudChannelServiceClient.ListChannelPartnerRepricingConfigsPagedResponse> listChannelPartnerRepricingConfigsPagedCallable()

Lists information about how a Reseller modifies their bill before sending it to a ChannelPartner.

Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * NOT_FOUND: The ChannelPartnerRepricingConfig specified does not exist or is not associated with the given account. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the ChannelPartnerRepricingConfig resources. The data for each resource is displayed in the ascending order of:

  * Channel Partner ID 
  * RepricingConfig.effective_invoice_month
  * ChannelPartnerRepricingConfig.update_time



If unsuccessful, returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListChannelPartnerRepricingConfigsRequest request =
           ListChannelPartnerRepricingConfigsRequest.newBuilder()
               .setParent(
                   ChannelPartnerLinkName.of("[ACCOUNT]", "[CHANNEL_PARTNER_LINK]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<ChannelPartnerRepricingConfig> future =
           cloudChannelServiceClient
               .listChannelPartnerRepricingConfigsPagedCallable()
               .futureCall(request);
       // Do something.
       for (ChannelPartnerRepricingConfig element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListChannelPartnerRepricingConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListChannelPartnerRepricingConfigsRequest),[ListChannelPartnerRepricingConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListChannelPartnerRepricingConfigsPagedResponse)>` |   
  
### listCustomerRepricingConfigs(@Nullable CustomerName parent)
    
    
    public final CloudChannelServiceClient.ListCustomerRepricingConfigsPagedResponse listCustomerRepricingConfigs(@Nullable CustomerName parent)

Lists information about how a Reseller modifies their bill before sending it to a Customer.

Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * NOT_FOUND: The CustomerRepricingConfig specified does not exist or is not associated with the given account. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the CustomerRepricingConfig resources. The data for each resource is displayed in the ascending order of:

  * Customer ID 
  * RepricingConfig.EntitlementGranularity.entitlement
  * RepricingConfig.effective_invoice_month
  * CustomerRepricingConfig.update_time



If unsuccessful, returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       CustomerName parent = CustomerName.of("[ACCOUNT]", "[CUSTOMER]");
       for (CustomerRepricingConfig element :
           cloudChannelServiceClient.listCustomerRepricingConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.channel.v1.CustomerName`  
Required. The resource name of the customer. Parent uses the format: accounts/{account_id}/customers/{customer_id}. Supports accounts/{account_id}/customers/- to retrieve configs for all customers.  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceClient.ListCustomerRepricingConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListCustomerRepricingConfigsPagedResponse)` |   
  
### listCustomerRepricingConfigs(ListCustomerRepricingConfigsRequest request)
    
    
    public final CloudChannelServiceClient.ListCustomerRepricingConfigsPagedResponse listCustomerRepricingConfigs(ListCustomerRepricingConfigsRequest request)

Lists information about how a Reseller modifies their bill before sending it to a Customer.

Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * NOT_FOUND: The CustomerRepricingConfig specified does not exist or is not associated with the given account. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the CustomerRepricingConfig resources. The data for each resource is displayed in the ascending order of:

  * Customer ID 
  * RepricingConfig.EntitlementGranularity.entitlement
  * RepricingConfig.effective_invoice_month
  * CustomerRepricingConfig.update_time



If unsuccessful, returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListCustomerRepricingConfigsRequest request =
           ListCustomerRepricingConfigsRequest.newBuilder()
               .setParent(CustomerName.of("[ACCOUNT]", "[CUSTOMER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (CustomerRepricingConfig element :
           cloudChannelServiceClient.listCustomerRepricingConfigs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCustomerRepricingConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListCustomerRepricingConfigsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceClient.ListCustomerRepricingConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListCustomerRepricingConfigsPagedResponse)` |   
  
### listCustomerRepricingConfigs(String parent)
    
    
    public final CloudChannelServiceClient.ListCustomerRepricingConfigsPagedResponse listCustomerRepricingConfigs(String parent)

Lists information about how a Reseller modifies their bill before sending it to a Customer.

Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * NOT_FOUND: The CustomerRepricingConfig specified does not exist or is not associated with the given account. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the CustomerRepricingConfig resources. The data for each resource is displayed in the ascending order of:

  * Customer ID 
  * RepricingConfig.EntitlementGranularity.entitlement
  * RepricingConfig.effective_invoice_month
  * CustomerRepricingConfig.update_time



If unsuccessful, returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       String parent = CustomerName.of("[ACCOUNT]", "[CUSTOMER]").toString();
       for (CustomerRepricingConfig element :
           cloudChannelServiceClient.listCustomerRepricingConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the customer. Parent uses the format: accounts/{account_id}/customers/{customer_id}. Supports accounts/{account_id}/customers/- to retrieve configs for all customers.  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceClient.ListCustomerRepricingConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListCustomerRepricingConfigsPagedResponse)` |   
  
### listCustomerRepricingConfigsCallable()
    
    
    public final UnaryCallable<ListCustomerRepricingConfigsRequest,ListCustomerRepricingConfigsResponse> listCustomerRepricingConfigsCallable()

Lists information about how a Reseller modifies their bill before sending it to a Customer.

Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * NOT_FOUND: The CustomerRepricingConfig specified does not exist or is not associated with the given account. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the CustomerRepricingConfig resources. The data for each resource is displayed in the ascending order of:

  * Customer ID 
  * RepricingConfig.EntitlementGranularity.entitlement
  * RepricingConfig.effective_invoice_month
  * CustomerRepricingConfig.update_time



If unsuccessful, returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListCustomerRepricingConfigsRequest request =
           ListCustomerRepricingConfigsRequest.newBuilder()
               .setParent(CustomerName.of("[ACCOUNT]", "[CUSTOMER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListCustomerRepricingConfigsResponse response =
             cloudChannelServiceClient.listCustomerRepricingConfigsCallable().call(request);
         for (CustomerRepricingConfig element : response.getCustomerRepricingConfigsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCustomerRepricingConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListCustomerRepricingConfigsRequest),[ListCustomerRepricingConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListCustomerRepricingConfigsResponse)>` |   
  
### listCustomerRepricingConfigsPagedCallable()
    
    
    public final UnaryCallable<ListCustomerRepricingConfigsRequest,CloudChannelServiceClient.ListCustomerRepricingConfigsPagedResponse> listCustomerRepricingConfigsPagedCallable()

Lists information about how a Reseller modifies their bill before sending it to a Customer.

Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * NOT_FOUND: The CustomerRepricingConfig specified does not exist or is not associated with the given account. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the CustomerRepricingConfig resources. The data for each resource is displayed in the ascending order of:

  * Customer ID 
  * RepricingConfig.EntitlementGranularity.entitlement
  * RepricingConfig.effective_invoice_month
  * CustomerRepricingConfig.update_time



If unsuccessful, returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListCustomerRepricingConfigsRequest request =
           ListCustomerRepricingConfigsRequest.newBuilder()
               .setParent(CustomerName.of("[ACCOUNT]", "[CUSTOMER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<CustomerRepricingConfig> future =
           cloudChannelServiceClient.listCustomerRepricingConfigsPagedCallable().futureCall(request);
       // Do something.
       for (CustomerRepricingConfig element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCustomerRepricingConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListCustomerRepricingConfigsRequest),[ListCustomerRepricingConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListCustomerRepricingConfigsPagedResponse)>` |   
  
### listCustomers(ListCustomersRequest request)
    
    
    public final CloudChannelServiceClient.ListCustomersPagedResponse listCustomers(ListCustomersRequest request)

List Customers.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 



Return value: List of Customers, or an empty list if there are no customers.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListCustomersRequest request =
           ListCustomersRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (Customer element : cloudChannelServiceClient.listCustomers(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCustomersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListCustomersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceClient.ListCustomersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListCustomersPagedResponse)` |   
  
### listCustomersCallable()
    
    
    public final UnaryCallable<ListCustomersRequest,ListCustomersResponse> listCustomersCallable()

List Customers.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 



Return value: List of Customers, or an empty list if there are no customers.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListCustomersRequest request =
           ListCustomersRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListCustomersResponse response =
             cloudChannelServiceClient.listCustomersCallable().call(request);
         for (Customer element : response.getCustomersList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCustomersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListCustomersRequest),[ListCustomersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListCustomersResponse)>` |   
  
### listCustomersPagedCallable()
    
    
    public final UnaryCallable<ListCustomersRequest,CloudChannelServiceClient.ListCustomersPagedResponse> listCustomersPagedCallable()

List Customers.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 



Return value: List of Customers, or an empty list if there are no customers.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListCustomersRequest request =
           ListCustomersRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<Customer> future =
           cloudChannelServiceClient.listCustomersPagedCallable().futureCall(request);
       // Do something.
       for (Customer element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCustomersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListCustomersRequest),[ListCustomersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListCustomersPagedResponse)>` |   
  
### listEntitlementChanges(@Nullable EntitlementName parent)
    
    
    public final CloudChannelServiceClient.ListEntitlementChangesPagedResponse listEntitlementChanges(@Nullable EntitlementName parent)

List entitlement history.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request and the provided reseller account are different. 
  * INVALID_ARGUMENT: Missing or invalid required fields in the request. 
  * NOT_FOUND: The parent resource doesn't exist. Usually the result of an invalid name parameter. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. In this case, contact CloudChannel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. In this case, contact Cloud Channel support. 



Return value: List of EntitlementChanges.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       EntitlementName parent = EntitlementName.of("[ACCOUNT]", "[CUSTOMER]", "[ENTITLEMENT]");
       for (EntitlementChange element :
           cloudChannelServiceClient.listEntitlementChanges(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.channel.v1.EntitlementName`  
Required. The resource name of the entitlement for which to list entitlement changes. The `-` wildcard may be used to match entitlements across a customer. Formats: * accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id} * accounts/{account_id}/customers/{customer_id}/entitlements/-  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceClient.ListEntitlementChangesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListEntitlementChangesPagedResponse)` |   
  
### listEntitlementChanges(ListEntitlementChangesRequest request)
    
    
    public final CloudChannelServiceClient.ListEntitlementChangesPagedResponse listEntitlementChanges(ListEntitlementChangesRequest request)

List entitlement history.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request and the provided reseller account are different. 
  * INVALID_ARGUMENT: Missing or invalid required fields in the request. 
  * NOT_FOUND: The parent resource doesn't exist. Usually the result of an invalid name parameter. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. In this case, contact CloudChannel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. In this case, contact Cloud Channel support. 



Return value: List of EntitlementChanges.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListEntitlementChangesRequest request =
           ListEntitlementChangesRequest.newBuilder()
               .setParent(EntitlementName.of("[ACCOUNT]", "[CUSTOMER]", "[ENTITLEMENT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (EntitlementChange element :
           cloudChannelServiceClient.listEntitlementChanges(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListEntitlementChangesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListEntitlementChangesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceClient.ListEntitlementChangesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListEntitlementChangesPagedResponse)` |   
  
### listEntitlementChanges(String parent)
    
    
    public final CloudChannelServiceClient.ListEntitlementChangesPagedResponse listEntitlementChanges(String parent)

List entitlement history.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request and the provided reseller account are different. 
  * INVALID_ARGUMENT: Missing or invalid required fields in the request. 
  * NOT_FOUND: The parent resource doesn't exist. Usually the result of an invalid name parameter. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. In this case, contact CloudChannel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. In this case, contact Cloud Channel support. 



Return value: List of EntitlementChanges.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       String parent = EntitlementName.of("[ACCOUNT]", "[CUSTOMER]", "[ENTITLEMENT]").toString();
       for (EntitlementChange element :
           cloudChannelServiceClient.listEntitlementChanges(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the entitlement for which to list entitlement changes. The `-` wildcard may be used to match entitlements across a customer. Formats: * accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id} * accounts/{account_id}/customers/{customer_id}/entitlements/-  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceClient.ListEntitlementChangesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListEntitlementChangesPagedResponse)` |   
  
### listEntitlementChangesCallable()
    
    
    public final UnaryCallable<ListEntitlementChangesRequest,ListEntitlementChangesResponse> listEntitlementChangesCallable()

List entitlement history.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request and the provided reseller account are different. 
  * INVALID_ARGUMENT: Missing or invalid required fields in the request. 
  * NOT_FOUND: The parent resource doesn't exist. Usually the result of an invalid name parameter. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. In this case, contact CloudChannel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. In this case, contact Cloud Channel support. 



Return value: List of EntitlementChanges.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListEntitlementChangesRequest request =
           ListEntitlementChangesRequest.newBuilder()
               .setParent(EntitlementName.of("[ACCOUNT]", "[CUSTOMER]", "[ENTITLEMENT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListEntitlementChangesResponse response =
             cloudChannelServiceClient.listEntitlementChangesCallable().call(request);
         for (EntitlementChange element : response.getEntitlementChangesList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEntitlementChangesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListEntitlementChangesRequest),[ListEntitlementChangesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListEntitlementChangesResponse)>` |   
  
### listEntitlementChangesPagedCallable()
    
    
    public final UnaryCallable<ListEntitlementChangesRequest,CloudChannelServiceClient.ListEntitlementChangesPagedResponse> listEntitlementChangesPagedCallable()

List entitlement history.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request and the provided reseller account are different. 
  * INVALID_ARGUMENT: Missing or invalid required fields in the request. 
  * NOT_FOUND: The parent resource doesn't exist. Usually the result of an invalid name parameter. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. In this case, contact CloudChannel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. In this case, contact Cloud Channel support. 



Return value: List of EntitlementChanges.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListEntitlementChangesRequest request =
           ListEntitlementChangesRequest.newBuilder()
               .setParent(EntitlementName.of("[ACCOUNT]", "[CUSTOMER]", "[ENTITLEMENT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<EntitlementChange> future =
           cloudChannelServiceClient.listEntitlementChangesPagedCallable().futureCall(request);
       // Do something.
       for (EntitlementChange element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEntitlementChangesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListEntitlementChangesRequest),[ListEntitlementChangesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListEntitlementChangesPagedResponse)>` |   
  
### listEntitlements(ListEntitlementsRequest request)
    
    
    public final CloudChannelServiceClient.ListEntitlementsPagedResponse listEntitlements(ListEntitlementsRequest request)

Lists Entitlements belonging to a customer.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 



Return value: A list of the customer's Entitlements.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListEntitlementsRequest request =
           ListEntitlementsRequest.newBuilder()
               .setParent(CustomerName.of("[ACCOUNT]", "[CUSTOMER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Entitlement element : cloudChannelServiceClient.listEntitlements(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListEntitlementsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListEntitlementsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceClient.ListEntitlementsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListEntitlementsPagedResponse)` |   
  
### listEntitlementsCallable()
    
    
    public final UnaryCallable<ListEntitlementsRequest,ListEntitlementsResponse> listEntitlementsCallable()

Lists Entitlements belonging to a customer.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 



Return value: A list of the customer's Entitlements.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListEntitlementsRequest request =
           ListEntitlementsRequest.newBuilder()
               .setParent(CustomerName.of("[ACCOUNT]", "[CUSTOMER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListEntitlementsResponse response =
             cloudChannelServiceClient.listEntitlementsCallable().call(request);
         for (Entitlement element : response.getEntitlementsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEntitlementsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListEntitlementsRequest),[ListEntitlementsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListEntitlementsResponse)>` |   
  
### listEntitlementsPagedCallable()
    
    
    public final UnaryCallable<ListEntitlementsRequest,CloudChannelServiceClient.ListEntitlementsPagedResponse> listEntitlementsPagedCallable()

Lists Entitlements belonging to a customer.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 



Return value: A list of the customer's Entitlements.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListEntitlementsRequest request =
           ListEntitlementsRequest.newBuilder()
               .setParent(CustomerName.of("[ACCOUNT]", "[CUSTOMER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Entitlement> future =
           cloudChannelServiceClient.listEntitlementsPagedCallable().futureCall(request);
       // Do something.
       for (Entitlement element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEntitlementsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListEntitlementsRequest),[ListEntitlementsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListEntitlementsPagedResponse)>` |   
  
### listOffers(ListOffersRequest request)
    
    
    public final CloudChannelServiceClient.ListOffersPagedResponse listOffers(ListOffersRequest request)

Lists the Offers the reseller can sell.

Possible error codes:

  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListOffersRequest request =
           ListOffersRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setLanguageCode("languageCode-2092349083")
               .setShowFutureOffers(true)
               .build();
       for (Offer element : cloudChannelServiceClient.listOffers(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListOffersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListOffersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceClient.ListOffersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListOffersPagedResponse)` |   
  
### listOffersCallable()
    
    
    public final UnaryCallable<ListOffersRequest,ListOffersResponse> listOffersCallable()

Lists the Offers the reseller can sell.

Possible error codes:

  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListOffersRequest request =
           ListOffersRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setLanguageCode("languageCode-2092349083")
               .setShowFutureOffers(true)
               .build();
       while (true) {
         ListOffersResponse response = cloudChannelServiceClient.listOffersCallable().call(request);
         for (Offer element : response.getOffersList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListOffersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListOffersRequest),[ListOffersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListOffersResponse)>` |   
  
### listOffersPagedCallable()
    
    
    public final UnaryCallable<ListOffersRequest,CloudChannelServiceClient.ListOffersPagedResponse> listOffersPagedCallable()

Lists the Offers the reseller can sell.

Possible error codes:

  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListOffersRequest request =
           ListOffersRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setLanguageCode("languageCode-2092349083")
               .setShowFutureOffers(true)
               .build();
       ApiFuture<Offer> future =
           cloudChannelServiceClient.listOffersPagedCallable().futureCall(request);
       // Do something.
       for (Offer element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListOffersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListOffersRequest),[ListOffersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListOffersPagedResponse)>` |   
  
### listProducts(ListProductsRequest request)
    
    
    public final CloudChannelServiceClient.ListProductsPagedResponse listProducts(ListProductsRequest request)

Lists the Products the reseller is authorized to sell.

Possible error codes:

  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListProductsRequest request =
           ListProductsRequest.newBuilder()
               .setAccount("account-1177318867")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setLanguageCode("languageCode-2092349083")
               .build();
       for (Product element : cloudChannelServiceClient.listProducts(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListProductsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceClient.ListProductsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListProductsPagedResponse)` |   
  
### listProductsCallable()
    
    
    public final UnaryCallable<ListProductsRequest,ListProductsResponse> listProductsCallable()

Lists the Products the reseller is authorized to sell.

Possible error codes:

  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListProductsRequest request =
           ListProductsRequest.newBuilder()
               .setAccount("account-1177318867")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setLanguageCode("languageCode-2092349083")
               .build();
       while (true) {
         ListProductsResponse response =
             cloudChannelServiceClient.listProductsCallable().call(request);
         for (Product element : response.getProductsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListProductsRequest),[ListProductsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListProductsResponse)>` |   
  
### listProductsPagedCallable()
    
    
    public final UnaryCallable<ListProductsRequest,CloudChannelServiceClient.ListProductsPagedResponse> listProductsPagedCallable()

Lists the Products the reseller is authorized to sell.

Possible error codes:

  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListProductsRequest request =
           ListProductsRequest.newBuilder()
               .setAccount("account-1177318867")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setLanguageCode("languageCode-2092349083")
               .build();
       ApiFuture<Product> future =
           cloudChannelServiceClient.listProductsPagedCallable().futureCall(request);
       // Do something.
       for (Product element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListProductsRequest),[ListProductsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListProductsPagedResponse)>` |   
  
### listPurchasableOffers(ListPurchasableOffersRequest request)
    
    
    public final CloudChannelServiceClient.ListPurchasableOffersPagedResponse listPurchasableOffers(ListPurchasableOffersRequest request)

Lists the following:

  * Offers that you can purchase for a customer. 
  * Offers that you can change for an entitlement. 



Possible error codes:

  * PERMISSION_DENIED: * The customer doesn't belong to the reseller * The reseller is not authorized to transact on this Product. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListPurchasableOffersRequest request =
           ListPurchasableOffersRequest.newBuilder()
               .setCustomer(CustomerName.of("[ACCOUNT]", "[CUSTOMER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setLanguageCode("languageCode-2092349083")
               .build();
       for (PurchasableOffer element :
           cloudChannelServiceClient.listPurchasableOffers(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPurchasableOffersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListPurchasableOffersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceClient.ListPurchasableOffersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListPurchasableOffersPagedResponse)` |   
  
### listPurchasableOffersCallable()
    
    
    public final UnaryCallable<ListPurchasableOffersRequest,ListPurchasableOffersResponse> listPurchasableOffersCallable()

Lists the following:

  * Offers that you can purchase for a customer. 
  * Offers that you can change for an entitlement. 



Possible error codes:

  * PERMISSION_DENIED: * The customer doesn't belong to the reseller * The reseller is not authorized to transact on this Product. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListPurchasableOffersRequest request =
           ListPurchasableOffersRequest.newBuilder()
               .setCustomer(CustomerName.of("[ACCOUNT]", "[CUSTOMER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setLanguageCode("languageCode-2092349083")
               .build();
       while (true) {
         ListPurchasableOffersResponse response =
             cloudChannelServiceClient.listPurchasableOffersCallable().call(request);
         for (PurchasableOffer element : response.getPurchasableOffersList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPurchasableOffersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListPurchasableOffersRequest),[ListPurchasableOffersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListPurchasableOffersResponse)>` |   
  
### listPurchasableOffersPagedCallable()
    
    
    public final UnaryCallable<ListPurchasableOffersRequest,CloudChannelServiceClient.ListPurchasableOffersPagedResponse> listPurchasableOffersPagedCallable()

Lists the following:

  * Offers that you can purchase for a customer. 
  * Offers that you can change for an entitlement. 



Possible error codes:

  * PERMISSION_DENIED: * The customer doesn't belong to the reseller * The reseller is not authorized to transact on this Product. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListPurchasableOffersRequest request =
           ListPurchasableOffersRequest.newBuilder()
               .setCustomer(CustomerName.of("[ACCOUNT]", "[CUSTOMER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setLanguageCode("languageCode-2092349083")
               .build();
       ApiFuture<PurchasableOffer> future =
           cloudChannelServiceClient.listPurchasableOffersPagedCallable().futureCall(request);
       // Do something.
       for (PurchasableOffer element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPurchasableOffersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListPurchasableOffersRequest),[ListPurchasableOffersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListPurchasableOffersPagedResponse)>` |   
  
### listPurchasableSkus(ListPurchasableSkusRequest request)
    
    
    public final CloudChannelServiceClient.ListPurchasableSkusPagedResponse listPurchasableSkus(ListPurchasableSkusRequest request)

Lists the following:

  * SKUs that you can purchase for a customer 
  * SKUs that you can upgrade or downgrade for an entitlement. 



Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListPurchasableSkusRequest request =
           ListPurchasableSkusRequest.newBuilder()
               .setCustomer(CustomerName.of("[ACCOUNT]", "[CUSTOMER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setLanguageCode("languageCode-2092349083")
               .build();
       for (PurchasableSku element :
           cloudChannelServiceClient.listPurchasableSkus(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPurchasableSkusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListPurchasableSkusRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceClient.ListPurchasableSkusPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListPurchasableSkusPagedResponse)` |   
  
### listPurchasableSkusCallable()
    
    
    public final UnaryCallable<ListPurchasableSkusRequest,ListPurchasableSkusResponse> listPurchasableSkusCallable()

Lists the following:

  * SKUs that you can purchase for a customer 
  * SKUs that you can upgrade or downgrade for an entitlement. 



Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListPurchasableSkusRequest request =
           ListPurchasableSkusRequest.newBuilder()
               .setCustomer(CustomerName.of("[ACCOUNT]", "[CUSTOMER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setLanguageCode("languageCode-2092349083")
               .build();
       while (true) {
         ListPurchasableSkusResponse response =
             cloudChannelServiceClient.listPurchasableSkusCallable().call(request);
         for (PurchasableSku element : response.getPurchasableSkusList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPurchasableSkusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListPurchasableSkusRequest),[ListPurchasableSkusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListPurchasableSkusResponse)>` |   
  
### listPurchasableSkusPagedCallable()
    
    
    public final UnaryCallable<ListPurchasableSkusRequest,CloudChannelServiceClient.ListPurchasableSkusPagedResponse> listPurchasableSkusPagedCallable()

Lists the following:

  * SKUs that you can purchase for a customer 
  * SKUs that you can upgrade or downgrade for an entitlement. 



Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListPurchasableSkusRequest request =
           ListPurchasableSkusRequest.newBuilder()
               .setCustomer(CustomerName.of("[ACCOUNT]", "[CUSTOMER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setLanguageCode("languageCode-2092349083")
               .build();
       ApiFuture<PurchasableSku> future =
           cloudChannelServiceClient.listPurchasableSkusPagedCallable().futureCall(request);
       // Do something.
       for (PurchasableSku element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPurchasableSkusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListPurchasableSkusRequest),[ListPurchasableSkusPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListPurchasableSkusPagedResponse)>` |   
  
### listSkuGroupBillableSkus(@Nullable SkuGroupName parent)
    
    
    public final CloudChannelServiceClient.ListSkuGroupBillableSkusPagedResponse listSkuGroupBillableSkus(@Nullable SkuGroupName parent)

Lists the Billable SKUs in a given SKU group.

Possible error codes: PERMISSION_DENIED: If the account making the request and the account being queried for are different, or the account doesn't exist. INVALID_ARGUMENT: Missing or invalid required parameters in the request. INTERNAL: Any non-user error related to technical issue in the backend. In this case, contact cloud channel support.

Return Value: If successful, the BillableSku resources. The data for each resource is displayed in the ascending order of:

  * BillableSku.service_display_name
  * BillableSku.sku_display_name



If unsuccessful, returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       SkuGroupName parent = SkuGroupName.of("[ACCOUNT]", "[SKU_GROUP]");
       for (BillableSku element :
           cloudChannelServiceClient.listSkuGroupBillableSkus(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.channel.v1.SkuGroupName`  
Required. Resource name of the SKU group. Format: accounts/{account}/skuGroups/{sku_group}.  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceClient.ListSkuGroupBillableSkusPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListSkuGroupBillableSkusPagedResponse)` |   
  
### listSkuGroupBillableSkus(ListSkuGroupBillableSkusRequest request)
    
    
    public final CloudChannelServiceClient.ListSkuGroupBillableSkusPagedResponse listSkuGroupBillableSkus(ListSkuGroupBillableSkusRequest request)

Lists the Billable SKUs in a given SKU group.

Possible error codes: PERMISSION_DENIED: If the account making the request and the account being queried for are different, or the account doesn't exist. INVALID_ARGUMENT: Missing or invalid required parameters in the request. INTERNAL: Any non-user error related to technical issue in the backend. In this case, contact cloud channel support.

Return Value: If successful, the BillableSku resources. The data for each resource is displayed in the ascending order of:

  * BillableSku.service_display_name
  * BillableSku.sku_display_name



If unsuccessful, returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListSkuGroupBillableSkusRequest request =
           ListSkuGroupBillableSkusRequest.newBuilder()
               .setParent(SkuGroupName.of("[ACCOUNT]", "[SKU_GROUP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (BillableSku element :
           cloudChannelServiceClient.listSkuGroupBillableSkus(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSkuGroupBillableSkusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSkuGroupBillableSkusRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceClient.ListSkuGroupBillableSkusPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListSkuGroupBillableSkusPagedResponse)` |   
  
### listSkuGroupBillableSkus(String parent)
    
    
    public final CloudChannelServiceClient.ListSkuGroupBillableSkusPagedResponse listSkuGroupBillableSkus(String parent)

Lists the Billable SKUs in a given SKU group.

Possible error codes: PERMISSION_DENIED: If the account making the request and the account being queried for are different, or the account doesn't exist. INVALID_ARGUMENT: Missing or invalid required parameters in the request. INTERNAL: Any non-user error related to technical issue in the backend. In this case, contact cloud channel support.

Return Value: If successful, the BillableSku resources. The data for each resource is displayed in the ascending order of:

  * BillableSku.service_display_name
  * BillableSku.sku_display_name



If unsuccessful, returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       String parent = SkuGroupName.of("[ACCOUNT]", "[SKU_GROUP]").toString();
       for (BillableSku element :
           cloudChannelServiceClient.listSkuGroupBillableSkus(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the SKU group. Format: accounts/{account}/skuGroups/{sku_group}.  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceClient.ListSkuGroupBillableSkusPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListSkuGroupBillableSkusPagedResponse)` |   
  
### listSkuGroupBillableSkusCallable()
    
    
    public final UnaryCallable<ListSkuGroupBillableSkusRequest,ListSkuGroupBillableSkusResponse> listSkuGroupBillableSkusCallable()

Lists the Billable SKUs in a given SKU group.

Possible error codes: PERMISSION_DENIED: If the account making the request and the account being queried for are different, or the account doesn't exist. INVALID_ARGUMENT: Missing or invalid required parameters in the request. INTERNAL: Any non-user error related to technical issue in the backend. In this case, contact cloud channel support.

Return Value: If successful, the BillableSku resources. The data for each resource is displayed in the ascending order of:

  * BillableSku.service_display_name
  * BillableSku.sku_display_name



If unsuccessful, returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListSkuGroupBillableSkusRequest request =
           ListSkuGroupBillableSkusRequest.newBuilder()
               .setParent(SkuGroupName.of("[ACCOUNT]", "[SKU_GROUP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListSkuGroupBillableSkusResponse response =
             cloudChannelServiceClient.listSkuGroupBillableSkusCallable().call(request);
         for (BillableSku element : response.getBillableSkusList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSkuGroupBillableSkusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSkuGroupBillableSkusRequest),[ListSkuGroupBillableSkusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSkuGroupBillableSkusResponse)>` |   
  
### listSkuGroupBillableSkusPagedCallable()
    
    
    public final UnaryCallable<ListSkuGroupBillableSkusRequest,CloudChannelServiceClient.ListSkuGroupBillableSkusPagedResponse> listSkuGroupBillableSkusPagedCallable()

Lists the Billable SKUs in a given SKU group.

Possible error codes: PERMISSION_DENIED: If the account making the request and the account being queried for are different, or the account doesn't exist. INVALID_ARGUMENT: Missing or invalid required parameters in the request. INTERNAL: Any non-user error related to technical issue in the backend. In this case, contact cloud channel support.

Return Value: If successful, the BillableSku resources. The data for each resource is displayed in the ascending order of:

  * BillableSku.service_display_name
  * BillableSku.sku_display_name



If unsuccessful, returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListSkuGroupBillableSkusRequest request =
           ListSkuGroupBillableSkusRequest.newBuilder()
               .setParent(SkuGroupName.of("[ACCOUNT]", "[SKU_GROUP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<BillableSku> future =
           cloudChannelServiceClient.listSkuGroupBillableSkusPagedCallable().futureCall(request);
       // Do something.
       for (BillableSku element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSkuGroupBillableSkusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSkuGroupBillableSkusRequest),[ListSkuGroupBillableSkusPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListSkuGroupBillableSkusPagedResponse)>` |   
  
### listSkuGroups(ListSkuGroupsRequest request)
    
    
    public final CloudChannelServiceClient.ListSkuGroupsPagedResponse listSkuGroups(ListSkuGroupsRequest request)

Lists the Rebilling supported SKU groups the account is authorized to sell. Reference: <https://cloud.google.com/skus/sku-groups>

Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different, or the account doesn't exist. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the SkuGroup resources. The data for each resource is displayed in the alphabetical order of SKU group display name. The data for each resource is displayed in the ascending order of SkuGroup.display_name

If unsuccessful, returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListSkuGroupsRequest request =
           ListSkuGroupsRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (SkuGroup element : cloudChannelServiceClient.listSkuGroups(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSkuGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSkuGroupsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceClient.ListSkuGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListSkuGroupsPagedResponse)` |   
  
### listSkuGroups(String parent)
    
    
    public final CloudChannelServiceClient.ListSkuGroupsPagedResponse listSkuGroups(String parent)

Lists the Rebilling supported SKU groups the account is authorized to sell. Reference: <https://cloud.google.com/skus/sku-groups>

Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different, or the account doesn't exist. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the SkuGroup resources. The data for each resource is displayed in the alphabetical order of SKU group display name. The data for each resource is displayed in the ascending order of SkuGroup.display_name

If unsuccessful, returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       String parent = "parent-995424086";
       for (SkuGroup element : cloudChannelServiceClient.listSkuGroups(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the account from which to list SKU groups. Parent uses the format: accounts/{account}.  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceClient.ListSkuGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListSkuGroupsPagedResponse)` |   
  
### listSkuGroupsCallable()
    
    
    public final UnaryCallable<ListSkuGroupsRequest,ListSkuGroupsResponse> listSkuGroupsCallable()

Lists the Rebilling supported SKU groups the account is authorized to sell. Reference: <https://cloud.google.com/skus/sku-groups>

Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different, or the account doesn't exist. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the SkuGroup resources. The data for each resource is displayed in the alphabetical order of SKU group display name. The data for each resource is displayed in the ascending order of SkuGroup.display_name

If unsuccessful, returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListSkuGroupsRequest request =
           ListSkuGroupsRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListSkuGroupsResponse response =
             cloudChannelServiceClient.listSkuGroupsCallable().call(request);
         for (SkuGroup element : response.getSkuGroupsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSkuGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSkuGroupsRequest),[ListSkuGroupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSkuGroupsResponse)>` |   
  
### listSkuGroupsPagedCallable()
    
    
    public final UnaryCallable<ListSkuGroupsRequest,CloudChannelServiceClient.ListSkuGroupsPagedResponse> listSkuGroupsPagedCallable()

Lists the Rebilling supported SKU groups the account is authorized to sell. Reference: <https://cloud.google.com/skus/sku-groups>

Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different, or the account doesn't exist. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the SkuGroup resources. The data for each resource is displayed in the alphabetical order of SKU group display name. The data for each resource is displayed in the ascending order of SkuGroup.display_name

If unsuccessful, returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListSkuGroupsRequest request =
           ListSkuGroupsRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<SkuGroup> future =
           cloudChannelServiceClient.listSkuGroupsPagedCallable().futureCall(request);
       // Do something.
       for (SkuGroup element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSkuGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSkuGroupsRequest),[ListSkuGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListSkuGroupsPagedResponse)>` |   
  
### listSkus(ListSkusRequest request)
    
    
    public final CloudChannelServiceClient.ListSkusPagedResponse listSkus(ListSkusRequest request)

Lists the SKUs for a product the reseller is authorized to sell.

Possible error codes:

  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListSkusRequest request =
           ListSkusRequest.newBuilder()
               .setParent(ProductName.of("[PRODUCT]").toString())
               .setAccount("account-1177318867")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setLanguageCode("languageCode-2092349083")
               .build();
       for (Sku element : cloudChannelServiceClient.listSkus(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSkusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSkusRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceClient.ListSkusPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListSkusPagedResponse)` |   
  
### listSkusCallable()
    
    
    public final UnaryCallable<ListSkusRequest,ListSkusResponse> listSkusCallable()

Lists the SKUs for a product the reseller is authorized to sell.

Possible error codes:

  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListSkusRequest request =
           ListSkusRequest.newBuilder()
               .setParent(ProductName.of("[PRODUCT]").toString())
               .setAccount("account-1177318867")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setLanguageCode("languageCode-2092349083")
               .build();
       while (true) {
         ListSkusResponse response = cloudChannelServiceClient.listSkusCallable().call(request);
         for (Sku element : response.getSkusList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSkusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSkusRequest),[ListSkusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSkusResponse)>` |   
  
### listSkusPagedCallable()
    
    
    public final UnaryCallable<ListSkusRequest,CloudChannelServiceClient.ListSkusPagedResponse> listSkusPagedCallable()

Lists the SKUs for a product the reseller is authorized to sell.

Possible error codes:

  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListSkusRequest request =
           ListSkusRequest.newBuilder()
               .setParent(ProductName.of("[PRODUCT]").toString())
               .setAccount("account-1177318867")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setLanguageCode("languageCode-2092349083")
               .build();
       ApiFuture<Sku> future = cloudChannelServiceClient.listSkusPagedCallable().futureCall(request);
       // Do something.
       for (Sku element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSkusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSkusRequest),[ListSkusPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListSkusPagedResponse)>` |   
  
### listSubscribers(ListSubscribersRequest request)
    
    
    public final CloudChannelServiceClient.ListSubscribersPagedResponse listSubscribers(ListSubscribersRequest request)

Lists service accounts with subscriber privileges on the Pub/Sub topic created for this Channel Services account or integrator.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request and the provided reseller account are different, or the impersonated user is not a super admin. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: The topic resource doesn't exist. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: A list of service email addresses.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListSubscribersRequest request =
           ListSubscribersRequest.newBuilder()
               .setAccount(AccountName.of("[ACCOUNT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setIntegrator("integrator-1902360937")
               .build();
       for (String element : cloudChannelServiceClient.listSubscribers(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSubscribersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSubscribersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceClient.ListSubscribersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListSubscribersPagedResponse)` |   
  
### listSubscribersCallable()
    
    
    public final UnaryCallable<ListSubscribersRequest,ListSubscribersResponse> listSubscribersCallable()

Lists service accounts with subscriber privileges on the Pub/Sub topic created for this Channel Services account or integrator.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request and the provided reseller account are different, or the impersonated user is not a super admin. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: The topic resource doesn't exist. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: A list of service email addresses.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListSubscribersRequest request =
           ListSubscribersRequest.newBuilder()
               .setAccount(AccountName.of("[ACCOUNT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setIntegrator("integrator-1902360937")
               .build();
       while (true) {
         ListSubscribersResponse response =
             cloudChannelServiceClient.listSubscribersCallable().call(request);
         for (String element : response.getServiceAccountsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSubscribersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSubscribersRequest),[ListSubscribersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSubscribersResponse)>` |   
  
### listSubscribersPagedCallable()
    
    
    public final UnaryCallable<ListSubscribersRequest,CloudChannelServiceClient.ListSubscribersPagedResponse> listSubscribersPagedCallable()

Lists service accounts with subscriber privileges on the Pub/Sub topic created for this Channel Services account or integrator.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request and the provided reseller account are different, or the impersonated user is not a super admin. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: The topic resource doesn't exist. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: A list of service email addresses.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListSubscribersRequest request =
           ListSubscribersRequest.newBuilder()
               .setAccount(AccountName.of("[ACCOUNT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setIntegrator("integrator-1902360937")
               .build();
       ApiFuture<String> future =
           cloudChannelServiceClient.listSubscribersPagedCallable().futureCall(request);
       // Do something.
       for (String element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSubscribersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSubscribersRequest),[ListSubscribersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListSubscribersPagedResponse)>` |   
  
### listTransferableOffers(ListTransferableOffersRequest request)
    
    
    public final CloudChannelServiceClient.ListTransferableOffersPagedResponse listTransferableOffers(ListTransferableOffersRequest request)

List TransferableOffers of a customer based on Cloud Identity ID or Customer Name in the request.

Use this method when a reseller gets the entitlement information of an unowned customer. The reseller should provide the customer's Cloud Identity ID or Customer Name.

Possible error codes:

  * PERMISSION_DENIED: * The customer doesn't belong to the reseller and has no auth token. * The customer provided incorrect reseller information when generating auth token. * The reseller account making the request is different from the reseller account in the query. * The reseller is not authorized to transact on this Product. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 



Return value: List of TransferableOffer for the given customer and SKU.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListTransferableOffersRequest request =
           ListTransferableOffersRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setSku("sku113949")
               .setLanguageCode("languageCode-2092349083")
               .setBillingAccount("billingAccount708726578")
               .build();
       for (TransferableOffer element :
           cloudChannelServiceClient.listTransferableOffers(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTransferableOffersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListTransferableOffersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceClient.ListTransferableOffersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListTransferableOffersPagedResponse)` |   
  
### listTransferableOffersCallable()
    
    
    public final UnaryCallable<ListTransferableOffersRequest,ListTransferableOffersResponse> listTransferableOffersCallable()

List TransferableOffers of a customer based on Cloud Identity ID or Customer Name in the request.

Use this method when a reseller gets the entitlement information of an unowned customer. The reseller should provide the customer's Cloud Identity ID or Customer Name.

Possible error codes:

  * PERMISSION_DENIED: * The customer doesn't belong to the reseller and has no auth token. * The customer provided incorrect reseller information when generating auth token. * The reseller account making the request is different from the reseller account in the query. * The reseller is not authorized to transact on this Product. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 



Return value: List of TransferableOffer for the given customer and SKU.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListTransferableOffersRequest request =
           ListTransferableOffersRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setSku("sku113949")
               .setLanguageCode("languageCode-2092349083")
               .setBillingAccount("billingAccount708726578")
               .build();
       while (true) {
         ListTransferableOffersResponse response =
             cloudChannelServiceClient.listTransferableOffersCallable().call(request);
         for (TransferableOffer element : response.getTransferableOffersList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTransferableOffersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListTransferableOffersRequest),[ListTransferableOffersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListTransferableOffersResponse)>` |   
  
### listTransferableOffersPagedCallable()
    
    
    public final UnaryCallable<ListTransferableOffersRequest,CloudChannelServiceClient.ListTransferableOffersPagedResponse> listTransferableOffersPagedCallable()

List TransferableOffers of a customer based on Cloud Identity ID or Customer Name in the request.

Use this method when a reseller gets the entitlement information of an unowned customer. The reseller should provide the customer's Cloud Identity ID or Customer Name.

Possible error codes:

  * PERMISSION_DENIED: * The customer doesn't belong to the reseller and has no auth token. * The customer provided incorrect reseller information when generating auth token. * The reseller account making the request is different from the reseller account in the query. * The reseller is not authorized to transact on this Product. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 



Return value: List of TransferableOffer for the given customer and SKU.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListTransferableOffersRequest request =
           ListTransferableOffersRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setSku("sku113949")
               .setLanguageCode("languageCode-2092349083")
               .setBillingAccount("billingAccount708726578")
               .build();
       ApiFuture<TransferableOffer> future =
           cloudChannelServiceClient.listTransferableOffersPagedCallable().futureCall(request);
       // Do something.
       for (TransferableOffer element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTransferableOffersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListTransferableOffersRequest),[ListTransferableOffersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListTransferableOffersPagedResponse)>` |   
  
### listTransferableSkus(ListTransferableSkusRequest request)
    
    
    public final CloudChannelServiceClient.ListTransferableSkusPagedResponse listTransferableSkus(ListTransferableSkusRequest request)

List TransferableSkus of a customer based on the Cloud Identity ID or Customer Name in the request.

Use this method to list the entitlements information of an unowned customer. You should provide the customer's Cloud Identity ID or Customer Name.

Possible error codes:

  * PERMISSION_DENIED: * The customer doesn't belong to the reseller and has no auth token. * The supplied auth token is invalid. * The reseller account making the request is different from the reseller account in the query. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 



Return value: A list of the customer's TransferableSku.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListTransferableSkusRequest request =
           ListTransferableSkusRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setAuthToken("authToken1450587441")
               .setLanguageCode("languageCode-2092349083")
               .build();
       for (TransferableSku element :
           cloudChannelServiceClient.listTransferableSkus(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTransferableSkusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListTransferableSkusRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceClient.ListTransferableSkusPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListTransferableSkusPagedResponse)` |   
  
### listTransferableSkusCallable()
    
    
    public final UnaryCallable<ListTransferableSkusRequest,ListTransferableSkusResponse> listTransferableSkusCallable()

List TransferableSkus of a customer based on the Cloud Identity ID or Customer Name in the request.

Use this method to list the entitlements information of an unowned customer. You should provide the customer's Cloud Identity ID or Customer Name.

Possible error codes:

  * PERMISSION_DENIED: * The customer doesn't belong to the reseller and has no auth token. * The supplied auth token is invalid. * The reseller account making the request is different from the reseller account in the query. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 



Return value: A list of the customer's TransferableSku.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListTransferableSkusRequest request =
           ListTransferableSkusRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setAuthToken("authToken1450587441")
               .setLanguageCode("languageCode-2092349083")
               .build();
       while (true) {
         ListTransferableSkusResponse response =
             cloudChannelServiceClient.listTransferableSkusCallable().call(request);
         for (TransferableSku element : response.getTransferableSkusList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTransferableSkusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListTransferableSkusRequest),[ListTransferableSkusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListTransferableSkusResponse)>` |   
  
### listTransferableSkusPagedCallable()
    
    
    public final UnaryCallable<ListTransferableSkusRequest,CloudChannelServiceClient.ListTransferableSkusPagedResponse> listTransferableSkusPagedCallable()

List TransferableSkus of a customer based on the Cloud Identity ID or Customer Name in the request.

Use this method to list the entitlements information of an unowned customer. You should provide the customer's Cloud Identity ID or Customer Name.

Possible error codes:

  * PERMISSION_DENIED: * The customer doesn't belong to the reseller and has no auth token. * The supplied auth token is invalid. * The reseller account making the request is different from the reseller account in the query. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 



Return value: A list of the customer's TransferableSku.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ListTransferableSkusRequest request =
           ListTransferableSkusRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setAuthToken("authToken1450587441")
               .setLanguageCode("languageCode-2092349083")
               .build();
       ApiFuture<TransferableSku> future =
           cloudChannelServiceClient.listTransferableSkusPagedCallable().futureCall(request);
       // Do something.
       for (TransferableSku element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTransferableSkusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListTransferableSkusRequest),[ListTransferableSkusPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListTransferableSkusPagedResponse)>` |   
  
### lookupOffer(LookupOfferRequest request)
    
    
    public final Offer lookupOffer(LookupOfferRequest request)

Returns the requested Offer resource.

Possible error codes:

  * PERMISSION_DENIED: The entitlement doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: Entitlement or offer was not found. 



Return value: The Offer resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       LookupOfferRequest request =
           LookupOfferRequest.newBuilder()
               .setEntitlement(
                   EntitlementName.of("[ACCOUNT]", "[CUSTOMER]", "[ENTITLEMENT]").toString())
               .build();
       Offer response = cloudChannelServiceClient.lookupOffer(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[LookupOfferRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.LookupOfferRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Offer](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Offer)` |   
  
### lookupOfferCallable()
    
    
    public final UnaryCallable<LookupOfferRequest,Offer> lookupOfferCallable()

Returns the requested Offer resource.

Possible error codes:

  * PERMISSION_DENIED: The entitlement doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: Entitlement or offer was not found. 



Return value: The Offer resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       LookupOfferRequest request =
           LookupOfferRequest.newBuilder()
               .setEntitlement(
                   EntitlementName.of("[ACCOUNT]", "[CUSTOMER]", "[ENTITLEMENT]").toString())
               .build();
       ApiFuture<Offer> future = cloudChannelServiceClient.lookupOfferCallable().futureCall(request);
       // Do something.
       Offer response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[LookupOfferRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.LookupOfferRequest),[Offer](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Offer)>` |   
  
### provisionCloudIdentityAsync(ProvisionCloudIdentityRequest request)
    
    
    public final OperationFuture<Customer,OperationMetadata> provisionCloudIdentityAsync(ProvisionCloudIdentityRequest request)

Creates a Cloud Identity for the given customer using the customer's information, or the information provided here.

Possible error codes:

  * PERMISSION_DENIED: * The customer doesn't belong to the reseller. * You are not authorized to provision cloud identity id. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: The customer was not found. 
  * ALREADY_EXISTS: The customer's primary email already exists. Retry after changing the customer's primary contact email. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata contains an instance of OperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ProvisionCloudIdentityRequest request =
           ProvisionCloudIdentityRequest.newBuilder()
               .setCustomer(CustomerName.of("[ACCOUNT]", "[CUSTOMER]").toString())
               .setCloudIdentityInfo(CloudIdentityInfo.newBuilder().build())
               .setUser(AdminUser.newBuilder().build())
               .setValidateOnly(true)
               .build();
       Customer response = cloudChannelServiceClient.provisionCloudIdentityAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ProvisionCloudIdentityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ProvisionCloudIdentityRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Customer](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Customer),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### provisionCloudIdentityCallable()
    
    
    public final UnaryCallable<ProvisionCloudIdentityRequest,Operation> provisionCloudIdentityCallable()

Creates a Cloud Identity for the given customer using the customer's information, or the information provided here.

Possible error codes:

  * PERMISSION_DENIED: * The customer doesn't belong to the reseller. * You are not authorized to provision cloud identity id. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: The customer was not found. 
  * ALREADY_EXISTS: The customer's primary email already exists. Retry after changing the customer's primary contact email. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata contains an instance of OperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ProvisionCloudIdentityRequest request =
           ProvisionCloudIdentityRequest.newBuilder()
               .setCustomer(CustomerName.of("[ACCOUNT]", "[CUSTOMER]").toString())
               .setCloudIdentityInfo(CloudIdentityInfo.newBuilder().build())
               .setUser(AdminUser.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           cloudChannelServiceClient.provisionCloudIdentityCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ProvisionCloudIdentityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ProvisionCloudIdentityRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### provisionCloudIdentityOperationCallable()
    
    
    public final OperationCallable<ProvisionCloudIdentityRequest,Customer,OperationMetadata> provisionCloudIdentityOperationCallable()

Creates a Cloud Identity for the given customer using the customer's information, or the information provided here.

Possible error codes:

  * PERMISSION_DENIED: * The customer doesn't belong to the reseller. * You are not authorized to provision cloud identity id. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: The customer was not found. 
  * ALREADY_EXISTS: The customer's primary email already exists. Retry after changing the customer's primary contact email. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata contains an instance of OperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ProvisionCloudIdentityRequest request =
           ProvisionCloudIdentityRequest.newBuilder()
               .setCustomer(CustomerName.of("[ACCOUNT]", "[CUSTOMER]").toString())
               .setCloudIdentityInfo(CloudIdentityInfo.newBuilder().build())
               .setUser(AdminUser.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<Customer, OperationMetadata> future =
           cloudChannelServiceClient.provisionCloudIdentityOperationCallable().futureCall(request);
       // Do something.
       Customer response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ProvisionCloudIdentityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ProvisionCloudIdentityRequest),[Customer](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Customer),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### queryEligibleBillingAccounts(QueryEligibleBillingAccountsRequest request)
    
    
    public final QueryEligibleBillingAccountsResponse queryEligibleBillingAccounts(QueryEligibleBillingAccountsRequest request)

Lists the billing accounts that are eligible to purchase particular SKUs for a given customer.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 



Return value: Based on the provided list of SKUs, returns a list of SKU groups that must be purchased using the same billing account and the billing accounts eligible to purchase each SKU group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       QueryEligibleBillingAccountsRequest request =
           QueryEligibleBillingAccountsRequest.newBuilder()
               .setCustomer(CustomerName.of("[ACCOUNT]", "[CUSTOMER]").toString())
               .addAllSkus(new ArrayList<String>())
               .build();
       QueryEligibleBillingAccountsResponse response =
           cloudChannelServiceClient.queryEligibleBillingAccounts(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[QueryEligibleBillingAccountsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.QueryEligibleBillingAccountsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[QueryEligibleBillingAccountsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.QueryEligibleBillingAccountsResponse)` |   
  
### queryEligibleBillingAccountsCallable()
    
    
    public final UnaryCallable<QueryEligibleBillingAccountsRequest,QueryEligibleBillingAccountsResponse> queryEligibleBillingAccountsCallable()

Lists the billing accounts that are eligible to purchase particular SKUs for a given customer.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 



Return value: Based on the provided list of SKUs, returns a list of SKU groups that must be purchased using the same billing account and the billing accounts eligible to purchase each SKU group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       QueryEligibleBillingAccountsRequest request =
           QueryEligibleBillingAccountsRequest.newBuilder()
               .setCustomer(CustomerName.of("[ACCOUNT]", "[CUSTOMER]").toString())
               .addAllSkus(new ArrayList<String>())
               .build();
       ApiFuture<QueryEligibleBillingAccountsResponse> future =
           cloudChannelServiceClient.queryEligibleBillingAccountsCallable().futureCall(request);
       // Do something.
       QueryEligibleBillingAccountsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[QueryEligibleBillingAccountsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.QueryEligibleBillingAccountsRequest),[QueryEligibleBillingAccountsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.QueryEligibleBillingAccountsResponse)>` |   
  
### registerSubscriber(RegisterSubscriberRequest request)
    
    
    public final RegisterSubscriberResponse registerSubscriber(RegisterSubscriberRequest request)

Registers a service account with subscriber privileges on the Pub/Sub topic for this Channel Services account or integrator. After you create a subscriber, you get the events through SubscriberEvent

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request and the provided reseller account are different, or the impersonated user is not a super admin. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The topic name with the registered service email address.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       RegisterSubscriberRequest request =
           RegisterSubscriberRequest.newBuilder()
               .setAccount(AccountName.of("[ACCOUNT]").toString())
               .setServiceAccount("serviceAccount1079137720")
               .setIntegrator("integrator-1902360937")
               .build();
       RegisterSubscriberResponse response = cloudChannelServiceClient.registerSubscriber(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RegisterSubscriberRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.RegisterSubscriberRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RegisterSubscriberResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.RegisterSubscriberResponse)` |   
  
### registerSubscriberCallable()
    
    
    public final UnaryCallable<RegisterSubscriberRequest,RegisterSubscriberResponse> registerSubscriberCallable()

Registers a service account with subscriber privileges on the Pub/Sub topic for this Channel Services account or integrator. After you create a subscriber, you get the events through SubscriberEvent

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request and the provided reseller account are different, or the impersonated user is not a super admin. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The topic name with the registered service email address.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       RegisterSubscriberRequest request =
           RegisterSubscriberRequest.newBuilder()
               .setAccount(AccountName.of("[ACCOUNT]").toString())
               .setServiceAccount("serviceAccount1079137720")
               .setIntegrator("integrator-1902360937")
               .build();
       ApiFuture<RegisterSubscriberResponse> future =
           cloudChannelServiceClient.registerSubscriberCallable().futureCall(request);
       // Do something.
       RegisterSubscriberResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RegisterSubscriberRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.RegisterSubscriberRequest),[RegisterSubscriberResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.RegisterSubscriberResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### startPaidServiceAsync(StartPaidServiceRequest request)
    
    
    public final OperationFuture<Entitlement,OperationMetadata> startPaidServiceAsync(StartPaidServiceRequest request)

Starts paid service for a trial entitlement.

Starts paid service for a trial entitlement immediately. This method is only applicable if a plan is set up for a trial entitlement but has some trial days remaining.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: Entitlement resource not found. 
  * FAILED_PRECONDITION/NOT_IN_TRIAL: This method only works for entitlement on trial plans. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       StartPaidServiceRequest request =
           StartPaidServiceRequest.newBuilder()
               .setName("name3373707")
               .setRequestId("requestId693933066")
               .build();
       Entitlement response = cloudChannelServiceClient.startPaidServiceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[StartPaidServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.StartPaidServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Entitlement](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Entitlement),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### startPaidServiceCallable()
    
    
    public final UnaryCallable<StartPaidServiceRequest,Operation> startPaidServiceCallable()

Starts paid service for a trial entitlement.

Starts paid service for a trial entitlement immediately. This method is only applicable if a plan is set up for a trial entitlement but has some trial days remaining.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: Entitlement resource not found. 
  * FAILED_PRECONDITION/NOT_IN_TRIAL: This method only works for entitlement on trial plans. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       StartPaidServiceRequest request =
           StartPaidServiceRequest.newBuilder()
               .setName("name3373707")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           cloudChannelServiceClient.startPaidServiceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[StartPaidServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.StartPaidServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### startPaidServiceOperationCallable()
    
    
    public final OperationCallable<StartPaidServiceRequest,Entitlement,OperationMetadata> startPaidServiceOperationCallable()

Starts paid service for a trial entitlement.

Starts paid service for a trial entitlement immediately. This method is only applicable if a plan is set up for a trial entitlement but has some trial days remaining.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: Entitlement resource not found. 
  * FAILED_PRECONDITION/NOT_IN_TRIAL: This method only works for entitlement on trial plans. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       StartPaidServiceRequest request =
           StartPaidServiceRequest.newBuilder()
               .setName("name3373707")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Entitlement, OperationMetadata> future =
           cloudChannelServiceClient.startPaidServiceOperationCallable().futureCall(request);
       // Do something.
       Entitlement response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[StartPaidServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.StartPaidServiceRequest),[Entitlement](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Entitlement),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### suspendEntitlementAsync(SuspendEntitlementRequest request)
    
    
    public final OperationFuture<Entitlement,OperationMetadata> suspendEntitlementAsync(SuspendEntitlementRequest request)

Suspends a previously fulfilled entitlement.

An entitlement suspension is a long-running operation.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: Entitlement resource not found. 
  * NOT_ACTIVE: Entitlement is not active. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       SuspendEntitlementRequest request =
           SuspendEntitlementRequest.newBuilder()
               .setName("name3373707")
               .setRequestId("requestId693933066")
               .build();
       Entitlement response = cloudChannelServiceClient.suspendEntitlementAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SuspendEntitlementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.SuspendEntitlementRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Entitlement](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Entitlement),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### suspendEntitlementCallable()
    
    
    public final UnaryCallable<SuspendEntitlementRequest,Operation> suspendEntitlementCallable()

Suspends a previously fulfilled entitlement.

An entitlement suspension is a long-running operation.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: Entitlement resource not found. 
  * NOT_ACTIVE: Entitlement is not active. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       SuspendEntitlementRequest request =
           SuspendEntitlementRequest.newBuilder()
               .setName("name3373707")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           cloudChannelServiceClient.suspendEntitlementCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SuspendEntitlementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.SuspendEntitlementRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### suspendEntitlementOperationCallable()
    
    
    public final OperationCallable<SuspendEntitlementRequest,Entitlement,OperationMetadata> suspendEntitlementOperationCallable()

Suspends a previously fulfilled entitlement.

An entitlement suspension is a long-running operation.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: Entitlement resource not found. 
  * NOT_ACTIVE: Entitlement is not active. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       SuspendEntitlementRequest request =
           SuspendEntitlementRequest.newBuilder()
               .setName("name3373707")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Entitlement, OperationMetadata> future =
           cloudChannelServiceClient.suspendEntitlementOperationCallable().futureCall(request);
       // Do something.
       Entitlement response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SuspendEntitlementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.SuspendEntitlementRequest),[Entitlement](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Entitlement),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### transferEntitlementsAsync(TransferEntitlementsRequest request)
    
    
    public final OperationFuture<TransferEntitlementsResponse,OperationMetadata> transferEntitlementsAsync(TransferEntitlementsRequest request)

Transfers customer entitlements to new reseller.

Possible error codes:

  * PERMISSION_DENIED: * The customer doesn't belong to the reseller. * The reseller is not authorized to transact on this Product. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: The customer or offer resource was not found. 
  * ALREADY_EXISTS: The SKU was already transferred for the customer. 
  * CONDITION_NOT_MET or FAILED_PRECONDITION: * The SKU requires domain verification to transfer, but the domain is not verified. * An Add-On SKU (example, Vault or Drive) is missing the pre-requisite SKU (example, G Suite Basic). * (Developer accounts only) Reseller and resold domain must meet the following naming requirements: * Domain names must start with goog-test. * Domain names must include the reseller domain. * Specify all transferring entitlements. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       TransferEntitlementsRequest request =
           TransferEntitlementsRequest.newBuilder()
               .setParent("parent-995424086")
               .addAllEntitlements(new ArrayList<Entitlement>())
               .setAuthToken("authToken1450587441")
               .setRequestId("requestId693933066")
               .build();
       TransferEntitlementsResponse response =
           cloudChannelServiceClient.transferEntitlementsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TransferEntitlementsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.TransferEntitlementsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[TransferEntitlementsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.TransferEntitlementsResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### transferEntitlementsCallable()
    
    
    public final UnaryCallable<TransferEntitlementsRequest,Operation> transferEntitlementsCallable()

Transfers customer entitlements to new reseller.

Possible error codes:

  * PERMISSION_DENIED: * The customer doesn't belong to the reseller. * The reseller is not authorized to transact on this Product. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: The customer or offer resource was not found. 
  * ALREADY_EXISTS: The SKU was already transferred for the customer. 
  * CONDITION_NOT_MET or FAILED_PRECONDITION: * The SKU requires domain verification to transfer, but the domain is not verified. * An Add-On SKU (example, Vault or Drive) is missing the pre-requisite SKU (example, G Suite Basic). * (Developer accounts only) Reseller and resold domain must meet the following naming requirements: * Domain names must start with goog-test. * Domain names must include the reseller domain. * Specify all transferring entitlements. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       TransferEntitlementsRequest request =
           TransferEntitlementsRequest.newBuilder()
               .setParent("parent-995424086")
               .addAllEntitlements(new ArrayList<Entitlement>())
               .setAuthToken("authToken1450587441")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           cloudChannelServiceClient.transferEntitlementsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TransferEntitlementsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.TransferEntitlementsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### transferEntitlementsOperationCallable()
    
    
    public final OperationCallable<TransferEntitlementsRequest,TransferEntitlementsResponse,OperationMetadata> transferEntitlementsOperationCallable()

Transfers customer entitlements to new reseller.

Possible error codes:

  * PERMISSION_DENIED: * The customer doesn't belong to the reseller. * The reseller is not authorized to transact on this Product. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: The customer or offer resource was not found. 
  * ALREADY_EXISTS: The SKU was already transferred for the customer. 
  * CONDITION_NOT_MET or FAILED_PRECONDITION: * The SKU requires domain verification to transfer, but the domain is not verified. * An Add-On SKU (example, Vault or Drive) is missing the pre-requisite SKU (example, G Suite Basic). * (Developer accounts only) Reseller and resold domain must meet the following naming requirements: * Domain names must start with goog-test. * Domain names must include the reseller domain. * Specify all transferring entitlements. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       TransferEntitlementsRequest request =
           TransferEntitlementsRequest.newBuilder()
               .setParent("parent-995424086")
               .addAllEntitlements(new ArrayList<Entitlement>())
               .setAuthToken("authToken1450587441")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<TransferEntitlementsResponse, OperationMetadata> future =
           cloudChannelServiceClient.transferEntitlementsOperationCallable().futureCall(request);
       // Do something.
       TransferEntitlementsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[TransferEntitlementsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.TransferEntitlementsRequest),[TransferEntitlementsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.TransferEntitlementsResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### transferEntitlementsToGoogleAsync(TransferEntitlementsToGoogleRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> transferEntitlementsToGoogleAsync(TransferEntitlementsToGoogleRequest request)

Transfers customer entitlements from their current reseller to Google.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: The customer or offer resource was not found. 
  * ALREADY_EXISTS: The SKU was already transferred for the customer. 
  * CONDITION_NOT_MET or FAILED_PRECONDITION: * The SKU requires domain verification to transfer, but the domain is not verified. * An Add-On SKU (example, Vault or Drive) is missing the pre-requisite SKU (example, G Suite Basic). * (Developer accounts only) Reseller and resold domain must meet the following naming requirements: * Domain names must start with goog-test. * Domain names must include the reseller domain. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The response will contain google.protobuf.Empty on success. The Operation metadata will contain an instance of OperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       TransferEntitlementsToGoogleRequest request =
           TransferEntitlementsToGoogleRequest.newBuilder()
               .setParent("parent-995424086")
               .addAllEntitlements(new ArrayList<Entitlement>())
               .setRequestId("requestId693933066")
               .build();
       cloudChannelServiceClient.transferEntitlementsToGoogleAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TransferEntitlementsToGoogleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.TransferEntitlementsToGoogleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### transferEntitlementsToGoogleCallable()
    
    
    public final UnaryCallable<TransferEntitlementsToGoogleRequest,Operation> transferEntitlementsToGoogleCallable()

Transfers customer entitlements from their current reseller to Google.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: The customer or offer resource was not found. 
  * ALREADY_EXISTS: The SKU was already transferred for the customer. 
  * CONDITION_NOT_MET or FAILED_PRECONDITION: * The SKU requires domain verification to transfer, but the domain is not verified. * An Add-On SKU (example, Vault or Drive) is missing the pre-requisite SKU (example, G Suite Basic). * (Developer accounts only) Reseller and resold domain must meet the following naming requirements: * Domain names must start with goog-test. * Domain names must include the reseller domain. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The response will contain google.protobuf.Empty on success. The Operation metadata will contain an instance of OperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       TransferEntitlementsToGoogleRequest request =
           TransferEntitlementsToGoogleRequest.newBuilder()
               .setParent("parent-995424086")
               .addAllEntitlements(new ArrayList<Entitlement>())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           cloudChannelServiceClient.transferEntitlementsToGoogleCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TransferEntitlementsToGoogleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.TransferEntitlementsToGoogleRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### transferEntitlementsToGoogleOperationCallable()
    
    
    public final OperationCallable<TransferEntitlementsToGoogleRequest,Empty,OperationMetadata> transferEntitlementsToGoogleOperationCallable()

Transfers customer entitlements from their current reseller to Google.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: The customer or offer resource was not found. 
  * ALREADY_EXISTS: The SKU was already transferred for the customer. 
  * CONDITION_NOT_MET or FAILED_PRECONDITION: * The SKU requires domain verification to transfer, but the domain is not verified. * An Add-On SKU (example, Vault or Drive) is missing the pre-requisite SKU (example, G Suite Basic). * (Developer accounts only) Reseller and resold domain must meet the following naming requirements: * Domain names must start with goog-test. * Domain names must include the reseller domain. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The response will contain google.protobuf.Empty on success. The Operation metadata will contain an instance of OperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       TransferEntitlementsToGoogleRequest request =
           TransferEntitlementsToGoogleRequest.newBuilder()
               .setParent("parent-995424086")
               .addAllEntitlements(new ArrayList<Entitlement>())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           cloudChannelServiceClient
               .transferEntitlementsToGoogleOperationCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[TransferEntitlementsToGoogleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.TransferEntitlementsToGoogleRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### unregisterSubscriber(UnregisterSubscriberRequest request)
    
    
    public final UnregisterSubscriberResponse unregisterSubscriber(UnregisterSubscriberRequest request)

Unregisters a service account with subscriber privileges on the Pub/Sub topic created for this Channel Services account or integrator. If there are no service accounts left with subscriber privileges, this deletes the topic. You can call ListSubscribers to check for these accounts.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request and the provided reseller account are different, or the impersonated user is not a super admin. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: The topic resource doesn't exist. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The topic name that unregistered the service email address. Returns a success response if the service email address wasn't registered with the topic.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       UnregisterSubscriberRequest request =
           UnregisterSubscriberRequest.newBuilder()
               .setAccount(AccountName.of("[ACCOUNT]").toString())
               .setServiceAccount("serviceAccount1079137720")
               .setIntegrator("integrator-1902360937")
               .build();
       UnregisterSubscriberResponse response =
           cloudChannelServiceClient.unregisterSubscriber(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UnregisterSubscriberRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.UnregisterSubscriberRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UnregisterSubscriberResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.UnregisterSubscriberResponse)` |   
  
### unregisterSubscriberCallable()
    
    
    public final UnaryCallable<UnregisterSubscriberRequest,UnregisterSubscriberResponse> unregisterSubscriberCallable()

Unregisters a service account with subscriber privileges on the Pub/Sub topic created for this Channel Services account or integrator. If there are no service accounts left with subscriber privileges, this deletes the topic. You can call ListSubscribers to check for these accounts.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request and the provided reseller account are different, or the impersonated user is not a super admin. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: The topic resource doesn't exist. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The topic name that unregistered the service email address. Returns a success response if the service email address wasn't registered with the topic.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       UnregisterSubscriberRequest request =
           UnregisterSubscriberRequest.newBuilder()
               .setAccount(AccountName.of("[ACCOUNT]").toString())
               .setServiceAccount("serviceAccount1079137720")
               .setIntegrator("integrator-1902360937")
               .build();
       ApiFuture<UnregisterSubscriberResponse> future =
           cloudChannelServiceClient.unregisterSubscriberCallable().futureCall(request);
       // Do something.
       UnregisterSubscriberResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UnregisterSubscriberRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.UnregisterSubscriberRequest),[UnregisterSubscriberResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.UnregisterSubscriberResponse)>` |   
  
### updateChannelPartnerLink(UpdateChannelPartnerLinkRequest request)
    
    
    public final ChannelPartnerLink updateChannelPartnerLink(UpdateChannelPartnerLinkRequest request)

Updates a channel partner link. Distributors call this method to change a link's status. For example, to suspend a partner link. You must be a distributor to call this method.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * INVALID_ARGUMENT: * Required request parameters are missing or invalid. * Link state cannot change from invited to active or suspended. * Cannot send reseller_cloud_identity_id, invite_url, or name in update mask. 
  * NOT_FOUND: ChannelPartnerLink resource not found. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The updated ChannelPartnerLink resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       UpdateChannelPartnerLinkRequest request =
           UpdateChannelPartnerLinkRequest.newBuilder()
               .setName("name3373707")
               .setChannelPartnerLink(ChannelPartnerLink.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ChannelPartnerLink response = cloudChannelServiceClient.updateChannelPartnerLink(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateChannelPartnerLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.UpdateChannelPartnerLinkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ChannelPartnerLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerLink)` |   
  
### updateChannelPartnerLinkCallable()
    
    
    public final UnaryCallable<UpdateChannelPartnerLinkRequest,ChannelPartnerLink> updateChannelPartnerLinkCallable()

Updates a channel partner link. Distributors call this method to change a link's status. For example, to suspend a partner link. You must be a distributor to call this method.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * INVALID_ARGUMENT: * Required request parameters are missing or invalid. * Link state cannot change from invited to active or suspended. * Cannot send reseller_cloud_identity_id, invite_url, or name in update mask. 
  * NOT_FOUND: ChannelPartnerLink resource not found. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The updated ChannelPartnerLink resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       UpdateChannelPartnerLinkRequest request =
           UpdateChannelPartnerLinkRequest.newBuilder()
               .setName("name3373707")
               .setChannelPartnerLink(ChannelPartnerLink.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<ChannelPartnerLink> future =
           cloudChannelServiceClient.updateChannelPartnerLinkCallable().futureCall(request);
       // Do something.
       ChannelPartnerLink response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateChannelPartnerLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.UpdateChannelPartnerLinkRequest),[ChannelPartnerLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerLink)>` |   
  
### updateChannelPartnerRepricingConfig(ChannelPartnerRepricingConfig channelPartnerRepricingConfig)
    
    
    public final ChannelPartnerRepricingConfig updateChannelPartnerRepricingConfig(ChannelPartnerRepricingConfig channelPartnerRepricingConfig)

Updates a ChannelPartnerRepricingConfig. Call this method to set modifications for a specific ChannelPartner's bill. This method overwrites the existing CustomerRepricingConfig.

You can only update configs if the RepricingConfig.effective_invoice_month is a future month. To make changes to configs for the current month, use CreateChannelPartnerRepricingConfig, taking note of its restrictions. You cannot update the RepricingConfig.effective_invoice_month.

When updating a config in the future:

  * This config must already exist. 



Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * INVALID_ARGUMENT: Missing or invalid required parameters in the request. Also displays if the updated config is for the current month or past months. 
  * NOT_FOUND: The ChannelPartnerRepricingConfig specified does not exist or is not associated with the given account. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the updated ChannelPartnerRepricingConfig resource, otherwise returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       ChannelPartnerRepricingConfig channelPartnerRepricingConfig =
           ChannelPartnerRepricingConfig.newBuilder().build();
       ChannelPartnerRepricingConfig response =
           cloudChannelServiceClient.updateChannelPartnerRepricingConfig(
               channelPartnerRepricingConfig);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`channelPartnerRepricingConfig` | `[ChannelPartnerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerRepricingConfig)`  
Required. The ChannelPartnerRepricingConfig object to update.  
**Returns**  
---  
**Type** | **Description**  
`[ChannelPartnerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerRepricingConfig)` |   
  
### updateChannelPartnerRepricingConfig(UpdateChannelPartnerRepricingConfigRequest request)
    
    
    public final ChannelPartnerRepricingConfig updateChannelPartnerRepricingConfig(UpdateChannelPartnerRepricingConfigRequest request)

Updates a ChannelPartnerRepricingConfig. Call this method to set modifications for a specific ChannelPartner's bill. This method overwrites the existing CustomerRepricingConfig.

You can only update configs if the RepricingConfig.effective_invoice_month is a future month. To make changes to configs for the current month, use CreateChannelPartnerRepricingConfig, taking note of its restrictions. You cannot update the RepricingConfig.effective_invoice_month.

When updating a config in the future:

  * This config must already exist. 



Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * INVALID_ARGUMENT: Missing or invalid required parameters in the request. Also displays if the updated config is for the current month or past months. 
  * NOT_FOUND: The ChannelPartnerRepricingConfig specified does not exist or is not associated with the given account. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the updated ChannelPartnerRepricingConfig resource, otherwise returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       UpdateChannelPartnerRepricingConfigRequest request =
           UpdateChannelPartnerRepricingConfigRequest.newBuilder()
               .setChannelPartnerRepricingConfig(ChannelPartnerRepricingConfig.newBuilder().build())
               .build();
       ChannelPartnerRepricingConfig response =
           cloudChannelServiceClient.updateChannelPartnerRepricingConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.UpdateChannelPartnerRepricingConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ChannelPartnerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerRepricingConfig)` |   
  
### updateChannelPartnerRepricingConfigCallable()
    
    
    public final UnaryCallable<UpdateChannelPartnerRepricingConfigRequest,ChannelPartnerRepricingConfig> updateChannelPartnerRepricingConfigCallable()

Updates a ChannelPartnerRepricingConfig. Call this method to set modifications for a specific ChannelPartner's bill. This method overwrites the existing CustomerRepricingConfig.

You can only update configs if the RepricingConfig.effective_invoice_month is a future month. To make changes to configs for the current month, use CreateChannelPartnerRepricingConfig, taking note of its restrictions. You cannot update the RepricingConfig.effective_invoice_month.

When updating a config in the future:

  * This config must already exist. 



Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * INVALID_ARGUMENT: Missing or invalid required parameters in the request. Also displays if the updated config is for the current month or past months. 
  * NOT_FOUND: The ChannelPartnerRepricingConfig specified does not exist or is not associated with the given account. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the updated ChannelPartnerRepricingConfig resource, otherwise returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       UpdateChannelPartnerRepricingConfigRequest request =
           UpdateChannelPartnerRepricingConfigRequest.newBuilder()
               .setChannelPartnerRepricingConfig(ChannelPartnerRepricingConfig.newBuilder().build())
               .build();
       ApiFuture<ChannelPartnerRepricingConfig> future =
           cloudChannelServiceClient
               .updateChannelPartnerRepricingConfigCallable()
               .futureCall(request);
       // Do something.
       ChannelPartnerRepricingConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.UpdateChannelPartnerRepricingConfigRequest),[ChannelPartnerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerRepricingConfig)>` |   
  
### updateCustomer(UpdateCustomerRequest request)
    
    
    public final Customer updateCustomer(UpdateCustomerRequest request)

Updates an existing Customer resource for the reseller or distributor.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: No Customer resource found for the name in the request. 



Return value: The updated Customer resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       UpdateCustomerRequest request =
           UpdateCustomerRequest.newBuilder()
               .setCustomer(Customer.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Customer response = cloudChannelServiceClient.updateCustomer(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateCustomerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.UpdateCustomerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Customer](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Customer)` |   
  
### updateCustomerCallable()
    
    
    public final UnaryCallable<UpdateCustomerRequest,Customer> updateCustomerCallable()

Updates an existing Customer resource for the reseller or distributor.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: No Customer resource found for the name in the request. 



Return value: The updated Customer resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       UpdateCustomerRequest request =
           UpdateCustomerRequest.newBuilder()
               .setCustomer(Customer.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Customer> future =
           cloudChannelServiceClient.updateCustomerCallable().futureCall(request);
       // Do something.
       Customer response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateCustomerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.UpdateCustomerRequest),[Customer](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Customer)>` |   
  
### updateCustomerRepricingConfig(CustomerRepricingConfig customerRepricingConfig)
    
    
    public final CustomerRepricingConfig updateCustomerRepricingConfig(CustomerRepricingConfig customerRepricingConfig)

Updates a CustomerRepricingConfig. Call this method to set modifications for a specific customer's bill. This method overwrites the existing CustomerRepricingConfig.

You can only update configs if the RepricingConfig.effective_invoice_month is a future month. To make changes to configs for the current month, use CreateCustomerRepricingConfig, taking note of its restrictions. You cannot update the RepricingConfig.effective_invoice_month.

When updating a config in the future:

  * This config must already exist. 



Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * INVALID_ARGUMENT: Missing or invalid required parameters in the request. Also displays if the updated config is for the current month or past months. 
  * NOT_FOUND: The CustomerRepricingConfig specified does not exist or is not associated with the given account. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the updated CustomerRepricingConfig resource, otherwise returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       CustomerRepricingConfig customerRepricingConfig =
           CustomerRepricingConfig.newBuilder().build();
       CustomerRepricingConfig response =
           cloudChannelServiceClient.updateCustomerRepricingConfig(customerRepricingConfig);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`customerRepricingConfig` | `[CustomerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CustomerRepricingConfig)`  
Required. The CustomerRepricingConfig object to update.  
**Returns**  
---  
**Type** | **Description**  
`[CustomerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CustomerRepricingConfig)` |   
  
### updateCustomerRepricingConfig(UpdateCustomerRepricingConfigRequest request)
    
    
    public final CustomerRepricingConfig updateCustomerRepricingConfig(UpdateCustomerRepricingConfigRequest request)

Updates a CustomerRepricingConfig. Call this method to set modifications for a specific customer's bill. This method overwrites the existing CustomerRepricingConfig.

You can only update configs if the RepricingConfig.effective_invoice_month is a future month. To make changes to configs for the current month, use CreateCustomerRepricingConfig, taking note of its restrictions. You cannot update the RepricingConfig.effective_invoice_month.

When updating a config in the future:

  * This config must already exist. 



Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * INVALID_ARGUMENT: Missing or invalid required parameters in the request. Also displays if the updated config is for the current month or past months. 
  * NOT_FOUND: The CustomerRepricingConfig specified does not exist or is not associated with the given account. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the updated CustomerRepricingConfig resource, otherwise returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       UpdateCustomerRepricingConfigRequest request =
           UpdateCustomerRepricingConfigRequest.newBuilder()
               .setCustomerRepricingConfig(CustomerRepricingConfig.newBuilder().build())
               .build();
       CustomerRepricingConfig response =
           cloudChannelServiceClient.updateCustomerRepricingConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateCustomerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.UpdateCustomerRepricingConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CustomerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CustomerRepricingConfig)` |   
  
### updateCustomerRepricingConfigCallable()
    
    
    public final UnaryCallable<UpdateCustomerRepricingConfigRequest,CustomerRepricingConfig> updateCustomerRepricingConfigCallable()

Updates a CustomerRepricingConfig. Call this method to set modifications for a specific customer's bill. This method overwrites the existing CustomerRepricingConfig.

You can only update configs if the RepricingConfig.effective_invoice_month is a future month. To make changes to configs for the current month, use CreateCustomerRepricingConfig, taking note of its restrictions. You cannot update the RepricingConfig.effective_invoice_month.

When updating a config in the future:

  * This config must already exist. 



Possible Error Codes:

  * PERMISSION_DENIED: If the account making the request and the account being queried are different. 
  * INVALID_ARGUMENT: Missing or invalid required parameters in the request. Also displays if the updated config is for the current month or past months. 
  * NOT_FOUND: The CustomerRepricingConfig specified does not exist or is not associated with the given account. 
  * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. 



Return Value: If successful, the updated CustomerRepricingConfig resource, otherwise returns an error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelServiceClient cloudChannelServiceClient = CloudChannelServiceClient.create()) {
       UpdateCustomerRepricingConfigRequest request =
           UpdateCustomerRepricingConfigRequest.newBuilder()
               .setCustomerRepricingConfig(CustomerRepricingConfig.newBuilder().build())
               .build();
       ApiFuture<CustomerRepricingConfig> future =
           cloudChannelServiceClient.updateCustomerRepricingConfigCallable().futureCall(request);
       // Do something.
       CustomerRepricingConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateCustomerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.UpdateCustomerRepricingConfigRequest),[CustomerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CustomerRepricingConfig)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
