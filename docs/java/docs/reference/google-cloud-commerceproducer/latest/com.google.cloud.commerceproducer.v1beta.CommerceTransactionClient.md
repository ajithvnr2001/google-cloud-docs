---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionClient
title: Class CommerceTransactionClient (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:20:37.360180+00:00
---

# Class CommerceTransactionClient (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CommerceTransactionClient (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-commerceproducer/google-cloud-commerceproducer/src/main/java/com/google/cloud/commerceproducer/v1beta/CommerceTransactionClient.java)| [Product Reference](https://docs.cloud.google.com/marketplace/)  
---|---  
  
Service Description: APIs related to managing resources that model commercial transactions.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       ServiceName name = ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]");
       Service response = commerceTransactionClient.getService(name);
     }
     

Note: close() needs to be called on the CommerceTransactionClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListServices |  Lists Services in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listServices(ListServicesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listServices(LocationName parent) 
  * listServices(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listServicesPagedCallable() 
  * listServicesCallable() 

  
GetService |  Gets details of a single Service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getService(GetServiceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getService(ServiceName name) 
  * getService(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getServiceCallable() 

  
ListPrivateOffers |  Lists PrivateOffers for the given parent. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPrivateOffers(ListPrivateOffersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listPrivateOffers(LocationName parent) 
  * listPrivateOffers(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPrivateOffersPagedCallable() 
  * listPrivateOffersCallable() 

  
GetPrivateOffer |  Gets details of a single PrivateOffer. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getPrivateOffer(GetPrivateOfferRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getPrivateOffer(PrivateOfferName name) 
  * getPrivateOffer(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getPrivateOfferCallable() 

  
ResolveAmendmentTarget |  Resolves the existing offer that must be amended when creating a new PrivateOffer. Use this method to determine the correct amendment target before creating or publishing an offer. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * resolveAmendmentTarget(ResolveAmendmentTargetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * resolveAmendmentTarget(LocationName parent, BillingAccountName targetBillingAccount, StandardOfferName baseStandardOffer) 
  * resolveAmendmentTarget(LocationName parent, BillingAccountName targetBillingAccount, String baseStandardOffer) 
  * resolveAmendmentTarget(LocationName parent, String targetBillingAccount, StandardOfferName baseStandardOffer) 
  * resolveAmendmentTarget(LocationName parent, String targetBillingAccount, String baseStandardOffer) 
  * resolveAmendmentTarget(String parent, BillingAccountName targetBillingAccount, StandardOfferName baseStandardOffer) 
  * resolveAmendmentTarget(String parent, BillingAccountName targetBillingAccount, String baseStandardOffer) 
  * resolveAmendmentTarget(String parent, String targetBillingAccount, StandardOfferName baseStandardOffer) 
  * resolveAmendmentTarget(String parent, String targetBillingAccount, String baseStandardOffer) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * resolveAmendmentTargetCallable() 

  
CreatePrivateOffer |  Creates a new PrivateOffer in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createPrivateOffer(CreatePrivateOfferRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createPrivateOfferCallable() 

  
UpdatePrivateOffer |  Updates the target PrivateOffer. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updatePrivateOffer(UpdatePrivateOfferRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updatePrivateOffer(PrivateOffer privateOffer, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updatePrivateOfferCallable() 

  
PublishPrivateOffer |  Publishes the target PrivateOffer. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * publishPrivateOffer(PublishPrivateOfferRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * publishPrivateOffer(PrivateOfferName name) 
  * publishPrivateOffer(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * publishPrivateOfferCallable() 

  
CancelPrivateOffer |  Cancels the target PrivateOffer. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * cancelPrivateOffer(CancelPrivateOfferRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * cancelPrivateOffer(PrivateOfferName name) 
  * cancelPrivateOffer(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * cancelPrivateOfferCallable() 

  
DeletePrivateOffer |  Deletes the target PrivateOffer. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deletePrivateOffer(DeletePrivateOfferRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deletePrivateOffer(PrivateOfferName name) 
  * deletePrivateOffer(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deletePrivateOfferCallable() 

  
ListPrivateOfferDocuments |  Lists PrivateOfferDocuments for the given parent. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPrivateOfferDocuments(ListPrivateOfferDocumentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listPrivateOfferDocuments(PrivateOfferName parent) 
  * listPrivateOfferDocuments(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPrivateOfferDocumentsPagedCallable() 
  * listPrivateOfferDocumentsCallable() 

  
GetPrivateOfferDocument |  Gets details of a single PrivateOfferDocument. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getPrivateOfferDocument(GetPrivateOfferDocumentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getPrivateOfferDocument(PrivateOfferDocumentName name) 
  * getPrivateOfferDocument(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getPrivateOfferDocumentCallable() 

  
CreatePrivateOfferDocument |  Creates a new PrivateOfferDocument in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createPrivateOfferDocument(CreatePrivateOfferDocumentRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createPrivateOfferDocumentCallable() 

  
UpdatePrivateOfferDocument |  Updates the target PrivateOfferDocument. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updatePrivateOfferDocument(UpdatePrivateOfferDocumentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updatePrivateOfferDocument(PrivateOfferDocument privateOfferDocument, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updatePrivateOfferDocumentCallable() 

  
DeletePrivateOfferDocument |  Deletes the target PrivateOfferDocument. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deletePrivateOfferDocument(DeletePrivateOfferDocumentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deletePrivateOfferDocument(PrivateOfferDocumentName name) 
  * deletePrivateOfferDocument(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deletePrivateOfferDocumentCallable() 

  
ListStandardOffers |  Lists StandardOffers for the given parent. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listStandardOffers(ListStandardOffersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listStandardOffers(ServiceName parent) 
  * listStandardOffers(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listStandardOffersPagedCallable() 
  * listStandardOffersCallable() 

  
GetStandardOffer |  Gets details of a single StandardOffer. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getStandardOffer(GetStandardOfferRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getStandardOffer(StandardOfferName name) 
  * getStandardOffer(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getStandardOfferCallable() 

  
GetSku |  Gets details of a single Sku. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getSku(GetSkuRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getSku(SkuName name) 
  * getSku(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getSkuCallable() 

  
ListSkus |  Lists Skus for the given parent. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSkus(ListSkusRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listSkus(ServiceName parent) 
  * listSkus(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSkusPagedCallable() 
  * listSkusCallable() 

  
GetSkuGroup |  Gets details of a single SkuGroup. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getSkuGroup(GetSkuGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getSkuGroup(SkuGroupName name) 
  * getSkuGroup(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getSkuGroupCallable() 

  
ListSkuGroups |  Lists SkuGroups for the given parent. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSkuGroups(ListSkuGroupsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listSkuGroups(LocationName parent) 
  * listSkuGroups(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSkuGroupsPagedCallable() 
  * listSkuGroupsCallable() 

  
ListLocations |  Lists information about the supported locations for this service.  This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.  For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLocations(ListLocationsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLocationsPagedCallable() 
  * listLocationsCallable() 

  
GetLocation |  Gets information about a location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLocation(GetLocationRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLocationCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of CommerceTransactionSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CommerceTransactionSettings commerceTransactionSettings =
         CommerceTransactionSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     CommerceTransactionClient commerceTransactionClient =
         CommerceTransactionClient.create(commerceTransactionSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CommerceTransactionSettings commerceTransactionSettings =
         CommerceTransactionSettings.newBuilder().setEndpoint(myEndpoint).build();
     CommerceTransactionClient commerceTransactionClient =
         CommerceTransactionClient.create(commerceTransactionSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CommerceTransactionSettings commerceTransactionSettings =
         CommerceTransactionSettings.newHttpJsonBuilder().build();
     CommerceTransactionClient commerceTransactionClient =
         CommerceTransactionClient.create(commerceTransactionSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CommerceTransactionClient

## Static Methods 

### create()
    
    
    public static final CommerceTransactionClient create()

Constructs an instance of CommerceTransactionClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[CommerceTransactionClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CommerceTransactionSettings settings)
    
    
    public static final CommerceTransactionClient create(CommerceTransactionSettings settings)

Constructs an instance of CommerceTransactionClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CommerceTransactionSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CommerceTransactionClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CommerceTransactionStub stub)
    
    
    public static final CommerceTransactionClient create(CommerceTransactionStub stub)

Constructs an instance of CommerceTransactionClient, using the given stub for making calls. This is for advanced usage - prefer using create(CommerceTransactionSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CommerceTransactionStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.stub.CommerceTransactionStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CommerceTransactionClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionClient)` |   
  
## Constructors 

### CommerceTransactionClient(CommerceTransactionSettings settings)
    
    
    protected CommerceTransactionClient(CommerceTransactionSettings settings)

Constructs an instance of CommerceTransactionClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CommerceTransactionSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionSettings)`  
  
  
### CommerceTransactionClient(CommerceTransactionStub stub)
    
    
    protected CommerceTransactionClient(CommerceTransactionStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CommerceTransactionStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.stub.CommerceTransactionStub)`  
  
  
## Methods 

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
  
### cancelPrivateOffer(@Nullable PrivateOfferName name)
    
    
    public final PrivateOffer cancelPrivateOffer(@Nullable PrivateOfferName name)

Cancels the target PrivateOffer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       PrivateOfferName name = PrivateOfferName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_OFFER]");
       PrivateOffer response = commerceTransactionClient.cancelPrivateOffer(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.commerceproducer.v1beta.PrivateOfferName`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[PrivateOffer](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOffer)` |   
  
### cancelPrivateOffer(CancelPrivateOfferRequest request)
    
    
    public final PrivateOffer cancelPrivateOffer(CancelPrivateOfferRequest request)

Cancels the target PrivateOffer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       CancelPrivateOfferRequest request =
           CancelPrivateOfferRequest.newBuilder()
               .setName(PrivateOfferName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_OFFER]").toString())
               .setCancellationNote("cancellationNote806581141")
               .build();
       PrivateOffer response = commerceTransactionClient.cancelPrivateOffer(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CancelPrivateOfferRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CancelPrivateOfferRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateOffer](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOffer)` |   
  
### cancelPrivateOffer(String name)
    
    
    public final PrivateOffer cancelPrivateOffer(String name)

Cancels the target PrivateOffer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       String name = PrivateOfferName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_OFFER]").toString();
       PrivateOffer response = commerceTransactionClient.cancelPrivateOffer(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[PrivateOffer](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOffer)` |   
  
### cancelPrivateOfferCallable()
    
    
    public final UnaryCallable<CancelPrivateOfferRequest,PrivateOffer> cancelPrivateOfferCallable()

Cancels the target PrivateOffer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       CancelPrivateOfferRequest request =
           CancelPrivateOfferRequest.newBuilder()
               .setName(PrivateOfferName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_OFFER]").toString())
               .setCancellationNote("cancellationNote806581141")
               .build();
       ApiFuture<PrivateOffer> future =
           commerceTransactionClient.cancelPrivateOfferCallable().futureCall(request);
       // Do something.
       PrivateOffer response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CancelPrivateOfferRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CancelPrivateOfferRequest),[PrivateOffer](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOffer)>` |   
  
### close()
    
    
    public final void close()

### createPrivateOffer(CreatePrivateOfferRequest request)
    
    
    public final PrivateOffer createPrivateOffer(CreatePrivateOfferRequest request)

Creates a new PrivateOffer in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       CreatePrivateOfferRequest request =
           CreatePrivateOfferRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPrivateOffer(PrivateOffer.newBuilder().build())
               .build();
       PrivateOffer response = commerceTransactionClient.createPrivateOffer(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreatePrivateOfferRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CreatePrivateOfferRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateOffer](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOffer)` |   
  
### createPrivateOfferCallable()
    
    
    public final UnaryCallable<CreatePrivateOfferRequest,PrivateOffer> createPrivateOfferCallable()

Creates a new PrivateOffer in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       CreatePrivateOfferRequest request =
           CreatePrivateOfferRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPrivateOffer(PrivateOffer.newBuilder().build())
               .build();
       ApiFuture<PrivateOffer> future =
           commerceTransactionClient.createPrivateOfferCallable().futureCall(request);
       // Do something.
       PrivateOffer response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreatePrivateOfferRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CreatePrivateOfferRequest),[PrivateOffer](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOffer)>` |   
  
### createPrivateOfferDocument(CreatePrivateOfferDocumentRequest request)
    
    
    public final PrivateOfferDocument createPrivateOfferDocument(CreatePrivateOfferDocumentRequest request)

Creates a new PrivateOfferDocument in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       CreatePrivateOfferDocumentRequest request =
           CreatePrivateOfferDocumentRequest.newBuilder()
               .setParent(
                   PrivateOfferName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_OFFER]").toString())
               .setPrivateOfferDocument(PrivateOfferDocument.newBuilder().build())
               .build();
       PrivateOfferDocument response = commerceTransactionClient.createPrivateOfferDocument(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreatePrivateOfferDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CreatePrivateOfferDocumentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateOfferDocument](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOfferDocument)` |   
  
### createPrivateOfferDocumentCallable()
    
    
    public final UnaryCallable<CreatePrivateOfferDocumentRequest,PrivateOfferDocument> createPrivateOfferDocumentCallable()

Creates a new PrivateOfferDocument in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       CreatePrivateOfferDocumentRequest request =
           CreatePrivateOfferDocumentRequest.newBuilder()
               .setParent(
                   PrivateOfferName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_OFFER]").toString())
               .setPrivateOfferDocument(PrivateOfferDocument.newBuilder().build())
               .build();
       ApiFuture<PrivateOfferDocument> future =
           commerceTransactionClient.createPrivateOfferDocumentCallable().futureCall(request);
       // Do something.
       PrivateOfferDocument response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreatePrivateOfferDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CreatePrivateOfferDocumentRequest),[PrivateOfferDocument](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOfferDocument)>` |   
  
### deletePrivateOffer(@Nullable PrivateOfferName name)
    
    
    public final void deletePrivateOffer(@Nullable PrivateOfferName name)

Deletes the target PrivateOffer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       PrivateOfferName name = PrivateOfferName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_OFFER]");
       commerceTransactionClient.deletePrivateOffer(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.commerceproducer.v1beta.PrivateOfferName`  
Required. Name of the resource  
  
### deletePrivateOffer(DeletePrivateOfferRequest request)
    
    
    public final void deletePrivateOffer(DeletePrivateOfferRequest request)

Deletes the target PrivateOffer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       DeletePrivateOfferRequest request =
           DeletePrivateOfferRequest.newBuilder()
               .setName(PrivateOfferName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_OFFER]").toString())
               .setForce(true)
               .build();
       commerceTransactionClient.deletePrivateOffer(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeletePrivateOfferRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.DeletePrivateOfferRequest)`  
The request object containing all of the parameters for the API call.  
  
### deletePrivateOffer(String name)
    
    
    public final void deletePrivateOffer(String name)

Deletes the target PrivateOffer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       String name = PrivateOfferName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_OFFER]").toString();
       commerceTransactionClient.deletePrivateOffer(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource  
  
### deletePrivateOfferCallable()
    
    
    public final UnaryCallable<DeletePrivateOfferRequest,Empty> deletePrivateOfferCallable()

Deletes the target PrivateOffer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       DeletePrivateOfferRequest request =
           DeletePrivateOfferRequest.newBuilder()
               .setName(PrivateOfferName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_OFFER]").toString())
               .setForce(true)
               .build();
       ApiFuture<Empty> future =
           commerceTransactionClient.deletePrivateOfferCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeletePrivateOfferRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.DeletePrivateOfferRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deletePrivateOfferDocument(@Nullable PrivateOfferDocumentName name)
    
    
    public final void deletePrivateOfferDocument(@Nullable PrivateOfferDocumentName name)

Deletes the target PrivateOfferDocument.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       PrivateOfferDocumentName name =
           PrivateOfferDocumentName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_OFFER]", "[DOCUMENT]");
       commerceTransactionClient.deletePrivateOfferDocument(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.commerceproducer.v1beta.PrivateOfferDocumentName`  
Required. Name of the resource.  
  
### deletePrivateOfferDocument(DeletePrivateOfferDocumentRequest request)
    
    
    public final void deletePrivateOfferDocument(DeletePrivateOfferDocumentRequest request)

Deletes the target PrivateOfferDocument.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       DeletePrivateOfferDocumentRequest request =
           DeletePrivateOfferDocumentRequest.newBuilder()
               .setName(
                   PrivateOfferDocumentName.of(
                           "[PROJECT]", "[LOCATION]", "[PRIVATE_OFFER]", "[DOCUMENT]")
                       .toString())
               .build();
       commerceTransactionClient.deletePrivateOfferDocument(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeletePrivateOfferDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.DeletePrivateOfferDocumentRequest)`  
The request object containing all of the parameters for the API call.  
  
### deletePrivateOfferDocument(String name)
    
    
    public final void deletePrivateOfferDocument(String name)

Deletes the target PrivateOfferDocument.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       String name =
           PrivateOfferDocumentName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_OFFER]", "[DOCUMENT]")
               .toString();
       commerceTransactionClient.deletePrivateOfferDocument(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource.  
  
### deletePrivateOfferDocumentCallable()
    
    
    public final UnaryCallable<DeletePrivateOfferDocumentRequest,Empty> deletePrivateOfferDocumentCallable()

Deletes the target PrivateOfferDocument.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       DeletePrivateOfferDocumentRequest request =
           DeletePrivateOfferDocumentRequest.newBuilder()
               .setName(
                   PrivateOfferDocumentName.of(
                           "[PROJECT]", "[LOCATION]", "[PRIVATE_OFFER]", "[DOCUMENT]")
                       .toString())
               .build();
       ApiFuture<Empty> future =
           commerceTransactionClient.deletePrivateOfferDocumentCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeletePrivateOfferDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.DeletePrivateOfferDocumentRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = commerceTransactionClient.getLocation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.cloud.location.GetLocationRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.location.Location` |   
  
### getLocationCallable()
    
    
    public final UnaryCallable<GetLocationRequest,Location> getLocationCallable()

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           commerceTransactionClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getPrivateOffer(@Nullable PrivateOfferName name)
    
    
    public final PrivateOffer getPrivateOffer(@Nullable PrivateOfferName name)

Gets details of a single PrivateOffer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       PrivateOfferName name = PrivateOfferName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_OFFER]");
       PrivateOffer response = commerceTransactionClient.getPrivateOffer(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.commerceproducer.v1beta.PrivateOfferName`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[PrivateOffer](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOffer)` |   
  
### getPrivateOffer(GetPrivateOfferRequest request)
    
    
    public final PrivateOffer getPrivateOffer(GetPrivateOfferRequest request)

Gets details of a single PrivateOffer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       GetPrivateOfferRequest request =
           GetPrivateOfferRequest.newBuilder()
               .setName(PrivateOfferName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_OFFER]").toString())
               .setView(PrivateOfferView.forNumber(0))
               .build();
       PrivateOffer response = commerceTransactionClient.getPrivateOffer(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPrivateOfferRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.GetPrivateOfferRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateOffer](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOffer)` |   
  
### getPrivateOffer(String name)
    
    
    public final PrivateOffer getPrivateOffer(String name)

Gets details of a single PrivateOffer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       String name = PrivateOfferName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_OFFER]").toString();
       PrivateOffer response = commerceTransactionClient.getPrivateOffer(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[PrivateOffer](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOffer)` |   
  
### getPrivateOfferCallable()
    
    
    public final UnaryCallable<GetPrivateOfferRequest,PrivateOffer> getPrivateOfferCallable()

Gets details of a single PrivateOffer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       GetPrivateOfferRequest request =
           GetPrivateOfferRequest.newBuilder()
               .setName(PrivateOfferName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_OFFER]").toString())
               .setView(PrivateOfferView.forNumber(0))
               .build();
       ApiFuture<PrivateOffer> future =
           commerceTransactionClient.getPrivateOfferCallable().futureCall(request);
       // Do something.
       PrivateOffer response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetPrivateOfferRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.GetPrivateOfferRequest),[PrivateOffer](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOffer)>` |   
  
### getPrivateOfferDocument(@Nullable PrivateOfferDocumentName name)
    
    
    public final PrivateOfferDocument getPrivateOfferDocument(@Nullable PrivateOfferDocumentName name)

Gets details of a single PrivateOfferDocument.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       PrivateOfferDocumentName name =
           PrivateOfferDocumentName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_OFFER]", "[DOCUMENT]");
       PrivateOfferDocument response = commerceTransactionClient.getPrivateOfferDocument(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.commerceproducer.v1beta.PrivateOfferDocumentName`  
Required. Name of the resource.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateOfferDocument](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOfferDocument)` |   
  
### getPrivateOfferDocument(GetPrivateOfferDocumentRequest request)
    
    
    public final PrivateOfferDocument getPrivateOfferDocument(GetPrivateOfferDocumentRequest request)

Gets details of a single PrivateOfferDocument.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       GetPrivateOfferDocumentRequest request =
           GetPrivateOfferDocumentRequest.newBuilder()
               .setName(
                   PrivateOfferDocumentName.of(
                           "[PROJECT]", "[LOCATION]", "[PRIVATE_OFFER]", "[DOCUMENT]")
                       .toString())
               .build();
       PrivateOfferDocument response = commerceTransactionClient.getPrivateOfferDocument(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPrivateOfferDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.GetPrivateOfferDocumentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateOfferDocument](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOfferDocument)` |   
  
### getPrivateOfferDocument(String name)
    
    
    public final PrivateOfferDocument getPrivateOfferDocument(String name)

Gets details of a single PrivateOfferDocument.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       String name =
           PrivateOfferDocumentName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_OFFER]", "[DOCUMENT]")
               .toString();
       PrivateOfferDocument response = commerceTransactionClient.getPrivateOfferDocument(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateOfferDocument](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOfferDocument)` |   
  
### getPrivateOfferDocumentCallable()
    
    
    public final UnaryCallable<GetPrivateOfferDocumentRequest,PrivateOfferDocument> getPrivateOfferDocumentCallable()

Gets details of a single PrivateOfferDocument.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       GetPrivateOfferDocumentRequest request =
           GetPrivateOfferDocumentRequest.newBuilder()
               .setName(
                   PrivateOfferDocumentName.of(
                           "[PROJECT]", "[LOCATION]", "[PRIVATE_OFFER]", "[DOCUMENT]")
                       .toString())
               .build();
       ApiFuture<PrivateOfferDocument> future =
           commerceTransactionClient.getPrivateOfferDocumentCallable().futureCall(request);
       // Do something.
       PrivateOfferDocument response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetPrivateOfferDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.GetPrivateOfferDocumentRequest),[PrivateOfferDocument](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOfferDocument)>` |   
  
### getService(@Nullable ServiceName name)
    
    
    public final Service getService(@Nullable ServiceName name)

Gets details of a single Service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       ServiceName name = ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]");
       Service response = commerceTransactionClient.getService(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.commerceproducer.v1beta.ServiceName`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.Service)` |   
  
### getService(GetServiceRequest request)
    
    
    public final Service getService(GetServiceRequest request)

Gets details of a single Service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       GetServiceRequest request =
           GetServiceRequest.newBuilder()
               .setName(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setView(ServiceView.forNumber(0))
               .build();
       Service response = commerceTransactionClient.getService(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.GetServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.Service)` |   
  
### getService(String name)
    
    
    public final Service getService(String name)

Gets details of a single Service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       String name = ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString();
       Service response = commerceTransactionClient.getService(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.Service)` |   
  
### getServiceCallable()
    
    
    public final UnaryCallable<GetServiceRequest,Service> getServiceCallable()

Gets details of a single Service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       GetServiceRequest request =
           GetServiceRequest.newBuilder()
               .setName(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setView(ServiceView.forNumber(0))
               .build();
       ApiFuture<Service> future =
           commerceTransactionClient.getServiceCallable().futureCall(request);
       // Do something.
       Service response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.GetServiceRequest),[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.Service)>` |   
  
### getSettings()
    
    
    public final @Nullable CommerceTransactionSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.commerceproducer.v1beta.CommerceTransactionSettings` |   
  
### getSku(@Nullable SkuName name)
    
    
    public final Sku getSku(@Nullable SkuName name)

Gets details of a single Sku.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       SkuName name = SkuName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[SKU]");
       Sku response = commerceTransactionClient.getSku(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.commerceproducer.v1beta.SkuName`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[Sku](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.Sku)` |   
  
### getSku(GetSkuRequest request)
    
    
    public final Sku getSku(GetSkuRequest request)

Gets details of a single Sku.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       GetSkuRequest request =
           GetSkuRequest.newBuilder()
               .setName(SkuName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[SKU]").toString())
               .build();
       Sku response = commerceTransactionClient.getSku(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSkuRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.GetSkuRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Sku](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.Sku)` |   
  
### getSku(String name)
    
    
    public final Sku getSku(String name)

Gets details of a single Sku.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       String name = SkuName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[SKU]").toString();
       Sku response = commerceTransactionClient.getSku(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[Sku](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.Sku)` |   
  
### getSkuCallable()
    
    
    public final UnaryCallable<GetSkuRequest,Sku> getSkuCallable()

Gets details of a single Sku.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       GetSkuRequest request =
           GetSkuRequest.newBuilder()
               .setName(SkuName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[SKU]").toString())
               .build();
       ApiFuture<Sku> future = commerceTransactionClient.getSkuCallable().futureCall(request);
       // Do something.
       Sku response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSkuRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.GetSkuRequest),[Sku](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.Sku)>` |   
  
### getSkuGroup(@Nullable SkuGroupName name)
    
    
    public final SkuGroup getSkuGroup(@Nullable SkuGroupName name)

Gets details of a single SkuGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       SkuGroupName name = SkuGroupName.of("[PROJECT]", "[LOCATION]", "[SKU_GROUP]");
       SkuGroup response = commerceTransactionClient.getSkuGroup(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.commerceproducer.v1beta.SkuGroupName`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[SkuGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.SkuGroup)` |   
  
### getSkuGroup(GetSkuGroupRequest request)
    
    
    public final SkuGroup getSkuGroup(GetSkuGroupRequest request)

Gets details of a single SkuGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       GetSkuGroupRequest request =
           GetSkuGroupRequest.newBuilder()
               .setName(SkuGroupName.of("[PROJECT]", "[LOCATION]", "[SKU_GROUP]").toString())
               .build();
       SkuGroup response = commerceTransactionClient.getSkuGroup(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSkuGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.GetSkuGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SkuGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.SkuGroup)` |   
  
### getSkuGroup(String name)
    
    
    public final SkuGroup getSkuGroup(String name)

Gets details of a single SkuGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       String name = SkuGroupName.of("[PROJECT]", "[LOCATION]", "[SKU_GROUP]").toString();
       SkuGroup response = commerceTransactionClient.getSkuGroup(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[SkuGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.SkuGroup)` |   
  
### getSkuGroupCallable()
    
    
    public final UnaryCallable<GetSkuGroupRequest,SkuGroup> getSkuGroupCallable()

Gets details of a single SkuGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       GetSkuGroupRequest request =
           GetSkuGroupRequest.newBuilder()
               .setName(SkuGroupName.of("[PROJECT]", "[LOCATION]", "[SKU_GROUP]").toString())
               .build();
       ApiFuture<SkuGroup> future =
           commerceTransactionClient.getSkuGroupCallable().futureCall(request);
       // Do something.
       SkuGroup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSkuGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.GetSkuGroupRequest),[SkuGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.SkuGroup)>` |   
  
### getStandardOffer(@Nullable StandardOfferName name)
    
    
    public final StandardOffer getStandardOffer(@Nullable StandardOfferName name)

Gets details of a single StandardOffer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       StandardOfferName name =
           StandardOfferName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[STANDARD_OFFER]");
       StandardOffer response = commerceTransactionClient.getStandardOffer(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.commerceproducer.v1beta.StandardOfferName`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[StandardOffer](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.StandardOffer)` |   
  
### getStandardOffer(GetStandardOfferRequest request)
    
    
    public final StandardOffer getStandardOffer(GetStandardOfferRequest request)

Gets details of a single StandardOffer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       GetStandardOfferRequest request =
           GetStandardOfferRequest.newBuilder()
               .setName(
                   StandardOfferName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[STANDARD_OFFER]")
                       .toString())
               .setView(StandardOfferView.forNumber(0))
               .build();
       StandardOffer response = commerceTransactionClient.getStandardOffer(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetStandardOfferRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.GetStandardOfferRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[StandardOffer](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.StandardOffer)` |   
  
### getStandardOffer(String name)
    
    
    public final StandardOffer getStandardOffer(String name)

Gets details of a single StandardOffer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       String name =
           StandardOfferName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[STANDARD_OFFER]")
               .toString();
       StandardOffer response = commerceTransactionClient.getStandardOffer(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[StandardOffer](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.StandardOffer)` |   
  
### getStandardOfferCallable()
    
    
    public final UnaryCallable<GetStandardOfferRequest,StandardOffer> getStandardOfferCallable()

Gets details of a single StandardOffer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       GetStandardOfferRequest request =
           GetStandardOfferRequest.newBuilder()
               .setName(
                   StandardOfferName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[STANDARD_OFFER]")
                       .toString())
               .setView(StandardOfferView.forNumber(0))
               .build();
       ApiFuture<StandardOffer> future =
           commerceTransactionClient.getStandardOfferCallable().futureCall(request);
       // Do something.
       StandardOffer response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetStandardOfferRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.GetStandardOfferRequest),[StandardOffer](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.StandardOffer)>` |   
  
### getStub()
    
    
    public CommerceTransactionStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[CommerceTransactionStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.stub.CommerceTransactionStub)` |   
  
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
  
### listLocations(ListLocationsRequest request)
    
    
    public final CommerceTransactionClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : commerceTransactionClient.listLocations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.cloud.location.ListLocationsRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CommerceTransactionClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             commerceTransactionClient.listLocationsCallable().call(request);
         for (Location element : response.getLocationsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse>` |   
  
### listLocationsPagedCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,CommerceTransactionClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           commerceTransactionClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionClient.ListLocationsPagedResponse)>` |   
  
### listPrivateOfferDocuments(@Nullable PrivateOfferName parent)
    
    
    public final CommerceTransactionClient.ListPrivateOfferDocumentsPagedResponse listPrivateOfferDocuments(@Nullable PrivateOfferName parent)

Lists PrivateOfferDocuments for the given parent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       PrivateOfferName parent = PrivateOfferName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_OFFER]");
       for (PrivateOfferDocument element :
           commerceTransactionClient.listPrivateOfferDocuments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.commerceproducer.v1beta.PrivateOfferName`  
Required. Parent value for ListPrivateOfferDocumentsRequest.  
**Returns**  
---  
**Type** | **Description**  
`[CommerceTransactionClient.ListPrivateOfferDocumentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionClient.ListPrivateOfferDocumentsPagedResponse)` |   
  
### listPrivateOfferDocuments(ListPrivateOfferDocumentsRequest request)
    
    
    public final CommerceTransactionClient.ListPrivateOfferDocumentsPagedResponse listPrivateOfferDocuments(ListPrivateOfferDocumentsRequest request)

Lists PrivateOfferDocuments for the given parent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       ListPrivateOfferDocumentsRequest request =
           ListPrivateOfferDocumentsRequest.newBuilder()
               .setParent(
                   PrivateOfferName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_OFFER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (PrivateOfferDocument element :
           commerceTransactionClient.listPrivateOfferDocuments(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPrivateOfferDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListPrivateOfferDocumentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CommerceTransactionClient.ListPrivateOfferDocumentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionClient.ListPrivateOfferDocumentsPagedResponse)` |   
  
### listPrivateOfferDocuments(String parent)
    
    
    public final CommerceTransactionClient.ListPrivateOfferDocumentsPagedResponse listPrivateOfferDocuments(String parent)

Lists PrivateOfferDocuments for the given parent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       String parent = PrivateOfferName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_OFFER]").toString();
       for (PrivateOfferDocument element :
           commerceTransactionClient.listPrivateOfferDocuments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for ListPrivateOfferDocumentsRequest.  
**Returns**  
---  
**Type** | **Description**  
`[CommerceTransactionClient.ListPrivateOfferDocumentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionClient.ListPrivateOfferDocumentsPagedResponse)` |   
  
### listPrivateOfferDocumentsCallable()
    
    
    public final UnaryCallable<ListPrivateOfferDocumentsRequest,ListPrivateOfferDocumentsResponse> listPrivateOfferDocumentsCallable()

Lists PrivateOfferDocuments for the given parent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       ListPrivateOfferDocumentsRequest request =
           ListPrivateOfferDocumentsRequest.newBuilder()
               .setParent(
                   PrivateOfferName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_OFFER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListPrivateOfferDocumentsResponse response =
             commerceTransactionClient.listPrivateOfferDocumentsCallable().call(request);
         for (PrivateOfferDocument element : response.getPrivateOfferDocumentsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPrivateOfferDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListPrivateOfferDocumentsRequest),[ListPrivateOfferDocumentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListPrivateOfferDocumentsResponse)>` |   
  
### listPrivateOfferDocumentsPagedCallable()
    
    
    public final UnaryCallable<ListPrivateOfferDocumentsRequest,CommerceTransactionClient.ListPrivateOfferDocumentsPagedResponse> listPrivateOfferDocumentsPagedCallable()

Lists PrivateOfferDocuments for the given parent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       ListPrivateOfferDocumentsRequest request =
           ListPrivateOfferDocumentsRequest.newBuilder()
               .setParent(
                   PrivateOfferName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_OFFER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<PrivateOfferDocument> future =
           commerceTransactionClient.listPrivateOfferDocumentsPagedCallable().futureCall(request);
       // Do something.
       for (PrivateOfferDocument element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPrivateOfferDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListPrivateOfferDocumentsRequest),[ListPrivateOfferDocumentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionClient.ListPrivateOfferDocumentsPagedResponse)>` |   
  
### listPrivateOffers(@Nullable LocationName parent)
    
    
    public final CommerceTransactionClient.ListPrivateOffersPagedResponse listPrivateOffers(@Nullable LocationName parent)

Lists PrivateOffers for the given parent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (PrivateOffer element :
           commerceTransactionClient.listPrivateOffers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.commerceproducer.v1beta.LocationName`  
Required. Parent value for ListPrivateOffersRequest  
**Returns**  
---  
**Type** | **Description**  
`[CommerceTransactionClient.ListPrivateOffersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionClient.ListPrivateOffersPagedResponse)` |   
  
### listPrivateOffers(ListPrivateOffersRequest request)
    
    
    public final CommerceTransactionClient.ListPrivateOffersPagedResponse listPrivateOffers(ListPrivateOffersRequest request)

Lists PrivateOffers for the given parent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       ListPrivateOffersRequest request =
           ListPrivateOffersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (PrivateOffer element :
           commerceTransactionClient.listPrivateOffers(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPrivateOffersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListPrivateOffersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CommerceTransactionClient.ListPrivateOffersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionClient.ListPrivateOffersPagedResponse)` |   
  
### listPrivateOffers(String parent)
    
    
    public final CommerceTransactionClient.ListPrivateOffersPagedResponse listPrivateOffers(String parent)

Lists PrivateOffers for the given parent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (PrivateOffer element :
           commerceTransactionClient.listPrivateOffers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for ListPrivateOffersRequest  
**Returns**  
---  
**Type** | **Description**  
`[CommerceTransactionClient.ListPrivateOffersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionClient.ListPrivateOffersPagedResponse)` |   
  
### listPrivateOffersCallable()
    
    
    public final UnaryCallable<ListPrivateOffersRequest,ListPrivateOffersResponse> listPrivateOffersCallable()

Lists PrivateOffers for the given parent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       ListPrivateOffersRequest request =
           ListPrivateOffersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListPrivateOffersResponse response =
             commerceTransactionClient.listPrivateOffersCallable().call(request);
         for (PrivateOffer element : response.getPrivateOffersList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPrivateOffersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListPrivateOffersRequest),[ListPrivateOffersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListPrivateOffersResponse)>` |   
  
### listPrivateOffersPagedCallable()
    
    
    public final UnaryCallable<ListPrivateOffersRequest,CommerceTransactionClient.ListPrivateOffersPagedResponse> listPrivateOffersPagedCallable()

Lists PrivateOffers for the given parent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       ListPrivateOffersRequest request =
           ListPrivateOffersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<PrivateOffer> future =
           commerceTransactionClient.listPrivateOffersPagedCallable().futureCall(request);
       // Do something.
       for (PrivateOffer element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPrivateOffersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListPrivateOffersRequest),[ListPrivateOffersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionClient.ListPrivateOffersPagedResponse)>` |   
  
### listServices(@Nullable LocationName parent)
    
    
    public final CommerceTransactionClient.ListServicesPagedResponse listServices(@Nullable LocationName parent)

Lists Services in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Service element : commerceTransactionClient.listServices(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.commerceproducer.v1beta.LocationName`  
Required. Parent value for ListServicesRequest  
**Returns**  
---  
**Type** | **Description**  
`[CommerceTransactionClient.ListServicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionClient.ListServicesPagedResponse)` |   
  
### listServices(ListServicesRequest request)
    
    
    public final CommerceTransactionClient.ListServicesPagedResponse listServices(ListServicesRequest request)

Lists Services in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       ListServicesRequest request =
           ListServicesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Service element : commerceTransactionClient.listServices(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListServicesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CommerceTransactionClient.ListServicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionClient.ListServicesPagedResponse)` |   
  
### listServices(String parent)
    
    
    public final CommerceTransactionClient.ListServicesPagedResponse listServices(String parent)

Lists Services in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Service element : commerceTransactionClient.listServices(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for ListServicesRequest  
**Returns**  
---  
**Type** | **Description**  
`[CommerceTransactionClient.ListServicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionClient.ListServicesPagedResponse)` |   
  
### listServicesCallable()
    
    
    public final UnaryCallable<ListServicesRequest,ListServicesResponse> listServicesCallable()

Lists Services in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       ListServicesRequest request =
           ListServicesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListServicesResponse response =
             commerceTransactionClient.listServicesCallable().call(request);
         for (Service element : response.getServicesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListServicesRequest),[ListServicesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListServicesResponse)>` |   
  
### listServicesPagedCallable()
    
    
    public final UnaryCallable<ListServicesRequest,CommerceTransactionClient.ListServicesPagedResponse> listServicesPagedCallable()

Lists Services in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       ListServicesRequest request =
           ListServicesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Service> future =
           commerceTransactionClient.listServicesPagedCallable().futureCall(request);
       // Do something.
       for (Service element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListServicesRequest),[ListServicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionClient.ListServicesPagedResponse)>` |   
  
### listSkuGroups(@Nullable LocationName parent)
    
    
    public final CommerceTransactionClient.ListSkuGroupsPagedResponse listSkuGroups(@Nullable LocationName parent)

Lists SkuGroups for the given parent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (SkuGroup element : commerceTransactionClient.listSkuGroups(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.commerceproducer.v1beta.LocationName`  
Required. Parent value for ListSkuGroupsRequest  
**Returns**  
---  
**Type** | **Description**  
`[CommerceTransactionClient.ListSkuGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionClient.ListSkuGroupsPagedResponse)` |   
  
### listSkuGroups(ListSkuGroupsRequest request)
    
    
    public final CommerceTransactionClient.ListSkuGroupsPagedResponse listSkuGroups(ListSkuGroupsRequest request)

Lists SkuGroups for the given parent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       ListSkuGroupsRequest request =
           ListSkuGroupsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (SkuGroup element : commerceTransactionClient.listSkuGroups(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSkuGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListSkuGroupsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CommerceTransactionClient.ListSkuGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionClient.ListSkuGroupsPagedResponse)` |   
  
### listSkuGroups(String parent)
    
    
    public final CommerceTransactionClient.ListSkuGroupsPagedResponse listSkuGroups(String parent)

Lists SkuGroups for the given parent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (SkuGroup element : commerceTransactionClient.listSkuGroups(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for ListSkuGroupsRequest  
**Returns**  
---  
**Type** | **Description**  
`[CommerceTransactionClient.ListSkuGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionClient.ListSkuGroupsPagedResponse)` |   
  
### listSkuGroupsCallable()
    
    
    public final UnaryCallable<ListSkuGroupsRequest,ListSkuGroupsResponse> listSkuGroupsCallable()

Lists SkuGroups for the given parent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       ListSkuGroupsRequest request =
           ListSkuGroupsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListSkuGroupsResponse response =
             commerceTransactionClient.listSkuGroupsCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSkuGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListSkuGroupsRequest),[ListSkuGroupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListSkuGroupsResponse)>` |   
  
### listSkuGroupsPagedCallable()
    
    
    public final UnaryCallable<ListSkuGroupsRequest,CommerceTransactionClient.ListSkuGroupsPagedResponse> listSkuGroupsPagedCallable()

Lists SkuGroups for the given parent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       ListSkuGroupsRequest request =
           ListSkuGroupsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<SkuGroup> future =
           commerceTransactionClient.listSkuGroupsPagedCallable().futureCall(request);
       // Do something.
       for (SkuGroup element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSkuGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListSkuGroupsRequest),[ListSkuGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionClient.ListSkuGroupsPagedResponse)>` |   
  
### listSkus(@Nullable ServiceName parent)
    
    
    public final CommerceTransactionClient.ListSkusPagedResponse listSkus(@Nullable ServiceName parent)

Lists Skus for the given parent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       ServiceName parent = ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]");
       for (Sku element : commerceTransactionClient.listSkus(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.commerceproducer.v1beta.ServiceName`  
Required. Parent value for ListSkusRequest  
**Returns**  
---  
**Type** | **Description**  
`[CommerceTransactionClient.ListSkusPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionClient.ListSkusPagedResponse)` |   
  
### listSkus(ListSkusRequest request)
    
    
    public final CommerceTransactionClient.ListSkusPagedResponse listSkus(ListSkusRequest request)

Lists Skus for the given parent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       ListSkusRequest request =
           ListSkusRequest.newBuilder()
               .setParent(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Sku element : commerceTransactionClient.listSkus(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSkusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListSkusRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CommerceTransactionClient.ListSkusPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionClient.ListSkusPagedResponse)` |   
  
### listSkus(String parent)
    
    
    public final CommerceTransactionClient.ListSkusPagedResponse listSkus(String parent)

Lists Skus for the given parent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       String parent = ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString();
       for (Sku element : commerceTransactionClient.listSkus(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for ListSkusRequest  
**Returns**  
---  
**Type** | **Description**  
`[CommerceTransactionClient.ListSkusPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionClient.ListSkusPagedResponse)` |   
  
### listSkusCallable()
    
    
    public final UnaryCallable<ListSkusRequest,ListSkusResponse> listSkusCallable()

Lists Skus for the given parent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       ListSkusRequest request =
           ListSkusRequest.newBuilder()
               .setParent(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListSkusResponse response = commerceTransactionClient.listSkusCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSkusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListSkusRequest),[ListSkusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListSkusResponse)>` |   
  
### listSkusPagedCallable()
    
    
    public final UnaryCallable<ListSkusRequest,CommerceTransactionClient.ListSkusPagedResponse> listSkusPagedCallable()

Lists Skus for the given parent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       ListSkusRequest request =
           ListSkusRequest.newBuilder()
               .setParent(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Sku> future = commerceTransactionClient.listSkusPagedCallable().futureCall(request);
       // Do something.
       for (Sku element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSkusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListSkusRequest),[ListSkusPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionClient.ListSkusPagedResponse)>` |   
  
### listStandardOffers(@Nullable ServiceName parent)
    
    
    public final CommerceTransactionClient.ListStandardOffersPagedResponse listStandardOffers(@Nullable ServiceName parent)

Lists StandardOffers for the given parent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       ServiceName parent = ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]");
       for (StandardOffer element :
           commerceTransactionClient.listStandardOffers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.commerceproducer.v1beta.ServiceName`  
Required. Parent value for ListStandardOffersRequest  
**Returns**  
---  
**Type** | **Description**  
`[CommerceTransactionClient.ListStandardOffersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionClient.ListStandardOffersPagedResponse)` |   
  
### listStandardOffers(ListStandardOffersRequest request)
    
    
    public final CommerceTransactionClient.ListStandardOffersPagedResponse listStandardOffers(ListStandardOffersRequest request)

Lists StandardOffers for the given parent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       ListStandardOffersRequest request =
           ListStandardOffersRequest.newBuilder()
               .setParent(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (StandardOffer element :
           commerceTransactionClient.listStandardOffers(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListStandardOffersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListStandardOffersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CommerceTransactionClient.ListStandardOffersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionClient.ListStandardOffersPagedResponse)` |   
  
### listStandardOffers(String parent)
    
    
    public final CommerceTransactionClient.ListStandardOffersPagedResponse listStandardOffers(String parent)

Lists StandardOffers for the given parent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       String parent = ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString();
       for (StandardOffer element :
           commerceTransactionClient.listStandardOffers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for ListStandardOffersRequest  
**Returns**  
---  
**Type** | **Description**  
`[CommerceTransactionClient.ListStandardOffersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionClient.ListStandardOffersPagedResponse)` |   
  
### listStandardOffersCallable()
    
    
    public final UnaryCallable<ListStandardOffersRequest,ListStandardOffersResponse> listStandardOffersCallable()

Lists StandardOffers for the given parent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       ListStandardOffersRequest request =
           ListStandardOffersRequest.newBuilder()
               .setParent(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListStandardOffersResponse response =
             commerceTransactionClient.listStandardOffersCallable().call(request);
         for (StandardOffer element : response.getStandardOffersList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListStandardOffersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListStandardOffersRequest),[ListStandardOffersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListStandardOffersResponse)>` |   
  
### listStandardOffersPagedCallable()
    
    
    public final UnaryCallable<ListStandardOffersRequest,CommerceTransactionClient.ListStandardOffersPagedResponse> listStandardOffersPagedCallable()

Lists StandardOffers for the given parent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       ListStandardOffersRequest request =
           ListStandardOffersRequest.newBuilder()
               .setParent(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<StandardOffer> future =
           commerceTransactionClient.listStandardOffersPagedCallable().futureCall(request);
       // Do something.
       for (StandardOffer element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListStandardOffersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListStandardOffersRequest),[ListStandardOffersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionClient.ListStandardOffersPagedResponse)>` |   
  
### publishPrivateOffer(@Nullable PrivateOfferName name)
    
    
    public final PrivateOffer publishPrivateOffer(@Nullable PrivateOfferName name)

Publishes the target PrivateOffer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       PrivateOfferName name = PrivateOfferName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_OFFER]");
       PrivateOffer response = commerceTransactionClient.publishPrivateOffer(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.commerceproducer.v1beta.PrivateOfferName`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[PrivateOffer](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOffer)` |   
  
### publishPrivateOffer(PublishPrivateOfferRequest request)
    
    
    public final PrivateOffer publishPrivateOffer(PublishPrivateOfferRequest request)

Publishes the target PrivateOffer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       PublishPrivateOfferRequest request =
           PublishPrivateOfferRequest.newBuilder()
               .setName(PrivateOfferName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_OFFER]").toString())
               .setValidateOnly(true)
               .build();
       PrivateOffer response = commerceTransactionClient.publishPrivateOffer(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PublishPrivateOfferRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PublishPrivateOfferRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateOffer](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOffer)` |   
  
### publishPrivateOffer(String name)
    
    
    public final PrivateOffer publishPrivateOffer(String name)

Publishes the target PrivateOffer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       String name = PrivateOfferName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_OFFER]").toString();
       PrivateOffer response = commerceTransactionClient.publishPrivateOffer(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[PrivateOffer](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOffer)` |   
  
### publishPrivateOfferCallable()
    
    
    public final UnaryCallable<PublishPrivateOfferRequest,PrivateOffer> publishPrivateOfferCallable()

Publishes the target PrivateOffer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       PublishPrivateOfferRequest request =
           PublishPrivateOfferRequest.newBuilder()
               .setName(PrivateOfferName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_OFFER]").toString())
               .setValidateOnly(true)
               .build();
       ApiFuture<PrivateOffer> future =
           commerceTransactionClient.publishPrivateOfferCallable().futureCall(request);
       // Do something.
       PrivateOffer response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PublishPrivateOfferRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PublishPrivateOfferRequest),[PrivateOffer](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOffer)>` |   
  
### resolveAmendmentTarget(@Nullable LocationName parent, @Nullable BillingAccountName targetBillingAccount, @Nullable StandardOfferName baseStandardOffer)
    
    
    public final ResolveAmendmentTargetResponse resolveAmendmentTarget(@Nullable LocationName parent, @Nullable BillingAccountName targetBillingAccount, @Nullable StandardOfferName baseStandardOffer)

Resolves the existing offer that must be amended when creating a new PrivateOffer. Use this method to determine the correct amendment target before creating or publishing an offer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       BillingAccountName targetBillingAccount = BillingAccountName.of("[BILLING_ACCOUNT]");
       StandardOfferName baseStandardOffer =
           StandardOfferName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[STANDARD_OFFER]");
       ResolveAmendmentTargetResponse response =
           commerceTransactionClient.resolveAmendmentTarget(
               parent, targetBillingAccount, baseStandardOffer);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.commerceproducer.v1beta.LocationName`  
Required. Parent value for ResolveAmendmentTargetRequest  
`targetBillingAccount` | `@org.jspecify.annotations.Nullable com.google.cloud.commerceproducer.v1beta.BillingAccountName`  
Required. The customer's billing account targeted by the offer. This is the billing account for which the new private offer will be created on. Format: billingAccounts/{billing_account}.  
`baseStandardOffer` | `@org.jspecify.annotations.Nullable com.google.cloud.commerceproducer.v1beta.StandardOfferName`  
Required. The base standard offer that the private offer will be based on. Format: projects/{project}/locations/{location}/services/{service}/standardOffers/{standard_offer}.  
**Returns**  
---  
**Type** | **Description**  
`[ResolveAmendmentTargetResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ResolveAmendmentTargetResponse)` |   
  
### resolveAmendmentTarget(@Nullable LocationName parent, @Nullable BillingAccountName targetBillingAccount, String baseStandardOffer)
    
    
    public final ResolveAmendmentTargetResponse resolveAmendmentTarget(@Nullable LocationName parent, @Nullable BillingAccountName targetBillingAccount, String baseStandardOffer)

Resolves the existing offer that must be amended when creating a new PrivateOffer. Use this method to determine the correct amendment target before creating or publishing an offer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       BillingAccountName targetBillingAccount = BillingAccountName.of("[BILLING_ACCOUNT]");
       String baseStandardOffer =
           StandardOfferName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[STANDARD_OFFER]")
               .toString();
       ResolveAmendmentTargetResponse response =
           commerceTransactionClient.resolveAmendmentTarget(
               parent, targetBillingAccount, baseStandardOffer);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.commerceproducer.v1beta.LocationName`  
Required. Parent value for ResolveAmendmentTargetRequest  
`targetBillingAccount` | `@org.jspecify.annotations.Nullable com.google.cloud.commerceproducer.v1beta.BillingAccountName`  
Required. The customer's billing account targeted by the offer. This is the billing account for which the new private offer will be created on. Format: billingAccounts/{billing_account}.  
`baseStandardOffer` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The base standard offer that the private offer will be based on. Format: projects/{project}/locations/{location}/services/{service}/standardOffers/{standard_offer}.  
**Returns**  
---  
**Type** | **Description**  
`[ResolveAmendmentTargetResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ResolveAmendmentTargetResponse)` |   
  
### resolveAmendmentTarget(@Nullable LocationName parent, String targetBillingAccount, @Nullable StandardOfferName baseStandardOffer)
    
    
    public final ResolveAmendmentTargetResponse resolveAmendmentTarget(@Nullable LocationName parent, String targetBillingAccount, @Nullable StandardOfferName baseStandardOffer)

Resolves the existing offer that must be amended when creating a new PrivateOffer. Use this method to determine the correct amendment target before creating or publishing an offer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       String targetBillingAccount = BillingAccountName.of("[BILLING_ACCOUNT]").toString();
       StandardOfferName baseStandardOffer =
           StandardOfferName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[STANDARD_OFFER]");
       ResolveAmendmentTargetResponse response =
           commerceTransactionClient.resolveAmendmentTarget(
               parent, targetBillingAccount, baseStandardOffer);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.commerceproducer.v1beta.LocationName`  
Required. Parent value for ResolveAmendmentTargetRequest  
`targetBillingAccount` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The customer's billing account targeted by the offer. This is the billing account for which the new private offer will be created on. Format: billingAccounts/{billing_account}.  
`baseStandardOffer` | `@org.jspecify.annotations.Nullable com.google.cloud.commerceproducer.v1beta.StandardOfferName`  
Required. The base standard offer that the private offer will be based on. Format: projects/{project}/locations/{location}/services/{service}/standardOffers/{standard_offer}.  
**Returns**  
---  
**Type** | **Description**  
`[ResolveAmendmentTargetResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ResolveAmendmentTargetResponse)` |   
  
### resolveAmendmentTarget(@Nullable LocationName parent, String targetBillingAccount, String baseStandardOffer)
    
    
    public final ResolveAmendmentTargetResponse resolveAmendmentTarget(@Nullable LocationName parent, String targetBillingAccount, String baseStandardOffer)

Resolves the existing offer that must be amended when creating a new PrivateOffer. Use this method to determine the correct amendment target before creating or publishing an offer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       String targetBillingAccount = BillingAccountName.of("[BILLING_ACCOUNT]").toString();
       String baseStandardOffer =
           StandardOfferName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[STANDARD_OFFER]")
               .toString();
       ResolveAmendmentTargetResponse response =
           commerceTransactionClient.resolveAmendmentTarget(
               parent, targetBillingAccount, baseStandardOffer);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.commerceproducer.v1beta.LocationName`  
Required. Parent value for ResolveAmendmentTargetRequest  
`targetBillingAccount` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The customer's billing account targeted by the offer. This is the billing account for which the new private offer will be created on. Format: billingAccounts/{billing_account}.  
`baseStandardOffer` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The base standard offer that the private offer will be based on. Format: projects/{project}/locations/{location}/services/{service}/standardOffers/{standard_offer}.  
**Returns**  
---  
**Type** | **Description**  
`[ResolveAmendmentTargetResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ResolveAmendmentTargetResponse)` |   
  
### resolveAmendmentTarget(ResolveAmendmentTargetRequest request)
    
    
    public final ResolveAmendmentTargetResponse resolveAmendmentTarget(ResolveAmendmentTargetRequest request)

Resolves the existing offer that must be amended when creating a new PrivateOffer. Use this method to determine the correct amendment target before creating or publishing an offer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       ResolveAmendmentTargetRequest request =
           ResolveAmendmentTargetRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setTargetBillingAccount(BillingAccountName.of("[BILLING_ACCOUNT]").toString())
               .setBaseStandardOffer(
                   StandardOfferName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[STANDARD_OFFER]")
                       .toString())
               .build();
       ResolveAmendmentTargetResponse response =
           commerceTransactionClient.resolveAmendmentTarget(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ResolveAmendmentTargetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ResolveAmendmentTargetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ResolveAmendmentTargetResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ResolveAmendmentTargetResponse)` |   
  
### resolveAmendmentTarget(String parent, @Nullable BillingAccountName targetBillingAccount, @Nullable StandardOfferName baseStandardOffer)
    
    
    public final ResolveAmendmentTargetResponse resolveAmendmentTarget(String parent, @Nullable BillingAccountName targetBillingAccount, @Nullable StandardOfferName baseStandardOffer)

Resolves the existing offer that must be amended when creating a new PrivateOffer. Use this method to determine the correct amendment target before creating or publishing an offer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       BillingAccountName targetBillingAccount = BillingAccountName.of("[BILLING_ACCOUNT]");
       StandardOfferName baseStandardOffer =
           StandardOfferName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[STANDARD_OFFER]");
       ResolveAmendmentTargetResponse response =
           commerceTransactionClient.resolveAmendmentTarget(
               parent, targetBillingAccount, baseStandardOffer);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for ResolveAmendmentTargetRequest  
`targetBillingAccount` | `@org.jspecify.annotations.Nullable com.google.cloud.commerceproducer.v1beta.BillingAccountName`  
Required. The customer's billing account targeted by the offer. This is the billing account for which the new private offer will be created on. Format: billingAccounts/{billing_account}.  
`baseStandardOffer` | `@org.jspecify.annotations.Nullable com.google.cloud.commerceproducer.v1beta.StandardOfferName`  
Required. The base standard offer that the private offer will be based on. Format: projects/{project}/locations/{location}/services/{service}/standardOffers/{standard_offer}.  
**Returns**  
---  
**Type** | **Description**  
`[ResolveAmendmentTargetResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ResolveAmendmentTargetResponse)` |   
  
### resolveAmendmentTarget(String parent, @Nullable BillingAccountName targetBillingAccount, String baseStandardOffer)
    
    
    public final ResolveAmendmentTargetResponse resolveAmendmentTarget(String parent, @Nullable BillingAccountName targetBillingAccount, String baseStandardOffer)

Resolves the existing offer that must be amended when creating a new PrivateOffer. Use this method to determine the correct amendment target before creating or publishing an offer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       BillingAccountName targetBillingAccount = BillingAccountName.of("[BILLING_ACCOUNT]");
       String baseStandardOffer =
           StandardOfferName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[STANDARD_OFFER]")
               .toString();
       ResolveAmendmentTargetResponse response =
           commerceTransactionClient.resolveAmendmentTarget(
               parent, targetBillingAccount, baseStandardOffer);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for ResolveAmendmentTargetRequest  
`targetBillingAccount` | `@org.jspecify.annotations.Nullable com.google.cloud.commerceproducer.v1beta.BillingAccountName`  
Required. The customer's billing account targeted by the offer. This is the billing account for which the new private offer will be created on. Format: billingAccounts/{billing_account}.  
`baseStandardOffer` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The base standard offer that the private offer will be based on. Format: projects/{project}/locations/{location}/services/{service}/standardOffers/{standard_offer}.  
**Returns**  
---  
**Type** | **Description**  
`[ResolveAmendmentTargetResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ResolveAmendmentTargetResponse)` |   
  
### resolveAmendmentTarget(String parent, String targetBillingAccount, @Nullable StandardOfferName baseStandardOffer)
    
    
    public final ResolveAmendmentTargetResponse resolveAmendmentTarget(String parent, String targetBillingAccount, @Nullable StandardOfferName baseStandardOffer)

Resolves the existing offer that must be amended when creating a new PrivateOffer. Use this method to determine the correct amendment target before creating or publishing an offer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       String targetBillingAccount = BillingAccountName.of("[BILLING_ACCOUNT]").toString();
       StandardOfferName baseStandardOffer =
           StandardOfferName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[STANDARD_OFFER]");
       ResolveAmendmentTargetResponse response =
           commerceTransactionClient.resolveAmendmentTarget(
               parent, targetBillingAccount, baseStandardOffer);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for ResolveAmendmentTargetRequest  
`targetBillingAccount` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The customer's billing account targeted by the offer. This is the billing account for which the new private offer will be created on. Format: billingAccounts/{billing_account}.  
`baseStandardOffer` | `@org.jspecify.annotations.Nullable com.google.cloud.commerceproducer.v1beta.StandardOfferName`  
Required. The base standard offer that the private offer will be based on. Format: projects/{project}/locations/{location}/services/{service}/standardOffers/{standard_offer}.  
**Returns**  
---  
**Type** | **Description**  
`[ResolveAmendmentTargetResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ResolveAmendmentTargetResponse)` |   
  
### resolveAmendmentTarget(String parent, String targetBillingAccount, String baseStandardOffer)
    
    
    public final ResolveAmendmentTargetResponse resolveAmendmentTarget(String parent, String targetBillingAccount, String baseStandardOffer)

Resolves the existing offer that must be amended when creating a new PrivateOffer. Use this method to determine the correct amendment target before creating or publishing an offer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       String targetBillingAccount = BillingAccountName.of("[BILLING_ACCOUNT]").toString();
       String baseStandardOffer =
           StandardOfferName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[STANDARD_OFFER]")
               .toString();
       ResolveAmendmentTargetResponse response =
           commerceTransactionClient.resolveAmendmentTarget(
               parent, targetBillingAccount, baseStandardOffer);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for ResolveAmendmentTargetRequest  
`targetBillingAccount` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The customer's billing account targeted by the offer. This is the billing account for which the new private offer will be created on. Format: billingAccounts/{billing_account}.  
`baseStandardOffer` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The base standard offer that the private offer will be based on. Format: projects/{project}/locations/{location}/services/{service}/standardOffers/{standard_offer}.  
**Returns**  
---  
**Type** | **Description**  
`[ResolveAmendmentTargetResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ResolveAmendmentTargetResponse)` |   
  
### resolveAmendmentTargetCallable()
    
    
    public final UnaryCallable<ResolveAmendmentTargetRequest,ResolveAmendmentTargetResponse> resolveAmendmentTargetCallable()

Resolves the existing offer that must be amended when creating a new PrivateOffer. Use this method to determine the correct amendment target before creating or publishing an offer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       ResolveAmendmentTargetRequest request =
           ResolveAmendmentTargetRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setTargetBillingAccount(BillingAccountName.of("[BILLING_ACCOUNT]").toString())
               .setBaseStandardOffer(
                   StandardOfferName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[STANDARD_OFFER]")
                       .toString())
               .build();
       ApiFuture<ResolveAmendmentTargetResponse> future =
           commerceTransactionClient.resolveAmendmentTargetCallable().futureCall(request);
       // Do something.
       ResolveAmendmentTargetResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ResolveAmendmentTargetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ResolveAmendmentTargetRequest),[ResolveAmendmentTargetResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ResolveAmendmentTargetResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updatePrivateOffer(PrivateOffer privateOffer, FieldMask updateMask)
    
    
    public final PrivateOffer updatePrivateOffer(PrivateOffer privateOffer, FieldMask updateMask)

Updates the target PrivateOffer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       PrivateOffer privateOffer = PrivateOffer.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       PrivateOffer response =
           commerceTransactionClient.updatePrivateOffer(privateOffer, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`privateOffer` | `[PrivateOffer](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOffer)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. The special value "*" means full replacement. If unspecified, all fields present in the request will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateOffer](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOffer)` |   
  
### updatePrivateOffer(UpdatePrivateOfferRequest request)
    
    
    public final PrivateOffer updatePrivateOffer(UpdatePrivateOfferRequest request)

Updates the target PrivateOffer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       UpdatePrivateOfferRequest request =
           UpdatePrivateOfferRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setPrivateOffer(PrivateOffer.newBuilder().build())
               .build();
       PrivateOffer response = commerceTransactionClient.updatePrivateOffer(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdatePrivateOfferRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.UpdatePrivateOfferRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateOffer](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOffer)` |   
  
### updatePrivateOfferCallable()
    
    
    public final UnaryCallable<UpdatePrivateOfferRequest,PrivateOffer> updatePrivateOfferCallable()

Updates the target PrivateOffer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       UpdatePrivateOfferRequest request =
           UpdatePrivateOfferRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setPrivateOffer(PrivateOffer.newBuilder().build())
               .build();
       ApiFuture<PrivateOffer> future =
           commerceTransactionClient.updatePrivateOfferCallable().futureCall(request);
       // Do something.
       PrivateOffer response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdatePrivateOfferRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.UpdatePrivateOfferRequest),[PrivateOffer](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOffer)>` |   
  
### updatePrivateOfferDocument(PrivateOfferDocument privateOfferDocument, FieldMask updateMask)
    
    
    public final PrivateOfferDocument updatePrivateOfferDocument(PrivateOfferDocument privateOfferDocument, FieldMask updateMask)

Updates the target PrivateOfferDocument.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       PrivateOfferDocument privateOfferDocument = PrivateOfferDocument.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       PrivateOfferDocument response =
           commerceTransactionClient.updatePrivateOfferDocument(privateOfferDocument, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`privateOfferDocument` | `[PrivateOfferDocument](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOfferDocument)`  
Required. The resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. The special value "*" means full replacement. If unspecified, all fields present in the request will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateOfferDocument](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOfferDocument)` |   
  
### updatePrivateOfferDocument(UpdatePrivateOfferDocumentRequest request)
    
    
    public final PrivateOfferDocument updatePrivateOfferDocument(UpdatePrivateOfferDocumentRequest request)

Updates the target PrivateOfferDocument.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       UpdatePrivateOfferDocumentRequest request =
           UpdatePrivateOfferDocumentRequest.newBuilder()
               .setPrivateOfferDocument(PrivateOfferDocument.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       PrivateOfferDocument response = commerceTransactionClient.updatePrivateOfferDocument(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdatePrivateOfferDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.UpdatePrivateOfferDocumentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateOfferDocument](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOfferDocument)` |   
  
### updatePrivateOfferDocumentCallable()
    
    
    public final UnaryCallable<UpdatePrivateOfferDocumentRequest,PrivateOfferDocument> updatePrivateOfferDocumentCallable()

Updates the target PrivateOfferDocument.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CommerceTransactionClient commerceTransactionClient = CommerceTransactionClient.create()) {
       UpdatePrivateOfferDocumentRequest request =
           UpdatePrivateOfferDocumentRequest.newBuilder()
               .setPrivateOfferDocument(PrivateOfferDocument.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<PrivateOfferDocument> future =
           commerceTransactionClient.updatePrivateOfferDocumentCallable().futureCall(request);
       // Do something.
       PrivateOfferDocument response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdatePrivateOfferDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.UpdatePrivateOfferDocumentRequest),[PrivateOfferDocument](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOfferDocument)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
