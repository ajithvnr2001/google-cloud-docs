---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DomainsClient
title: Class DomainsClient (1.96.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:53:36.534591+00:00
---

# Class DomainsClient (1.96.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DomainsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DomainsClient (1.96.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.96.0 (latest)  1.92.0  1.91.0  1.90.0  1.88.0  1.85.0  1.84.0  1.82.0  1.80.0  1.79.0  1.78.0  1.77.0  1.75.0  1.73.0  1.72.0  1.71.0  1.70.0  1.69.0  1.67.0  1.65.0  1.64.0  1.61.0  1.60.0  1.59.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.6  0.7.0  0.6.1  0.5.4 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-domains/google-cloud-domains/src/main/java/com/google/cloud/domains/v1beta1/DomainsClient.java)| [Product Reference](https://cloud.google.com/domains)  
---|---  
  
Service Description: The Cloud Domains API enables management and configuration of domain names.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       LocationName location = LocationName.of("[PROJECT]", "[LOCATION]");
       String query = "query107944136";
       SearchDomainsResponse response = domainsClient.searchDomains(location, query);
     }
     

Note: close() needs to be called on the DomainsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
SearchDomains |  Searches for available domain names similar to the provided query.  Availability results from this method are approximate; call `RetrieveRegisterParameters` on a domain before registering to confirm availability. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * searchDomains(SearchDomainsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * searchDomains(LocationName location, String query) 
  * searchDomains(String location, String query) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * searchDomainsCallable() 

  
RetrieveRegisterParameters |  Gets parameters needed to register a new domain name, including price and up-to-date availability. Use the returned values to call `RegisterDomain`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * retrieveRegisterParameters(RetrieveRegisterParametersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * retrieveRegisterParameters(LocationName location, String domainName) 
  * retrieveRegisterParameters(String location, String domainName) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * retrieveRegisterParametersCallable() 

  
RegisterDomain |  Registers a new domain name and creates a corresponding `Registration` resource.  Call `RetrieveRegisterParameters` first to check availability of the domain name and determine parameters like price that are needed to build a call to this method.  A successful call creates a `Registration` resource in state `REGISTRATION_PENDING`, which resolves to `ACTIVE` within 1-2 minutes, indicating that the domain was successfully registered. If the resource ends up in state `REGISTRATION_FAILED`, it indicates that the domain was not registered successfully, and you can safely delete the resource and retry registration. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * registerDomainAsync(RegisterDomainRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * registerDomainAsync(LocationName parent, Registration registration, Money yearlyPrice) 
  * registerDomainAsync(String parent, Registration registration, Money yearlyPrice) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * registerDomainOperationCallable() 
  * registerDomainCallable() 

  
RetrieveTransferParameters |  Gets parameters needed to transfer a domain name from another registrar to Cloud Domains. For domains managed by Google Domains, transferring to Cloud Domains is not supported.  Use the returned values to call `TransferDomain`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * retrieveTransferParameters(RetrieveTransferParametersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * retrieveTransferParameters(LocationName location, String domainName) 
  * retrieveTransferParameters(String location, String domainName) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * retrieveTransferParametersCallable() 

  
TransferDomain |  Transfers a domain name from another registrar to Cloud Domains. For domains managed by Google Domains, transferring to Cloud Domains is not supported.  Before calling this method, go to the domain's current registrar to unlock the domain for transfer and retrieve the domain's transfer authorization code. Then call `RetrieveTransferParameters` to confirm that the domain is unlocked and to get values needed to build a call to this method.  A successful call creates a `Registration` resource in state `TRANSFER_PENDING`. It can take several days to complete the transfer process. The registrant can often speed up this process by approving the transfer through the current registrar, either by clicking a link in an email from the registrar or by visiting the registrar's website.  A few minutes after transfer approval, the resource transitions to state `ACTIVE`, indicating that the transfer was successful. If the transfer is rejected or the request expires without being approved, the resource can end up in state `TRANSFER_FAILED`. If transfer fails, you can safely delete the resource and retry the transfer. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * transferDomainAsync(TransferDomainRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * transferDomainAsync(LocationName parent, Registration registration, Money yearlyPrice, AuthorizationCode authorizationCode) 
  * transferDomainAsync(String parent, Registration registration, Money yearlyPrice, AuthorizationCode authorizationCode) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * transferDomainOperationCallable() 
  * transferDomainCallable() 

  
ListRegistrations |  Lists the `Registration` resources in a project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listRegistrations(ListRegistrationsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listRegistrations(LocationName parent) 
  * listRegistrations(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listRegistrationsPagedCallable() 
  * listRegistrationsCallable() 

  
GetRegistration |  Gets the details of a `Registration` resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getRegistration(GetRegistrationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getRegistration(RegistrationName name) 
  * getRegistration(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getRegistrationCallable() 

  
UpdateRegistration |  Updates select fields of a `Registration` resource, notably `labels`. To update other fields, use the appropriate custom update method: 

  * To update management settings, see `ConfigureManagementSettings`
  * To update DNS configuration, see `ConfigureDnsSettings`
  * To update contact information, see `ConfigureContactSettings`

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateRegistrationAsync(UpdateRegistrationRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateRegistrationAsync(Registration registration, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateRegistrationOperationCallable() 
  * updateRegistrationCallable() 

  
ConfigureManagementSettings |  Updates a `Registration`'s management settings. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * configureManagementSettingsAsync(ConfigureManagementSettingsRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * configureManagementSettingsAsync(RegistrationName registration, ManagementSettings managementSettings, FieldMask updateMask) 
  * configureManagementSettingsAsync(String registration, ManagementSettings managementSettings, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * configureManagementSettingsOperationCallable() 
  * configureManagementSettingsCallable() 

  
ConfigureDnsSettings |  Updates a `Registration`'s DNS settings. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * configureDnsSettingsAsync(ConfigureDnsSettingsRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * configureDnsSettingsAsync(RegistrationName registration, DnsSettings dnsSettings, FieldMask updateMask) 
  * configureDnsSettingsAsync(String registration, DnsSettings dnsSettings, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * configureDnsSettingsOperationCallable() 
  * configureDnsSettingsCallable() 

  
ConfigureContactSettings |  Updates a `Registration`'s contact settings. Some changes require confirmation by the domain's registrant contact . |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * configureContactSettingsAsync(ConfigureContactSettingsRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * configureContactSettingsAsync(RegistrationName registration, ContactSettings contactSettings, FieldMask updateMask) 
  * configureContactSettingsAsync(String registration, ContactSettings contactSettings, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * configureContactSettingsOperationCallable() 
  * configureContactSettingsCallable() 

  
ExportRegistration |  Exports a `Registration` resource, such that it is no longer managed by Cloud Domains.  When an active domain is successfully exported, you can continue to use the domain in [Google Domains](https://domains.google/) until it expires. The calling user becomes the domain's sole owner in Google Domains, and permissions for the domain are subsequently managed there. The domain does not renew automatically unless the new owner sets up billing in Google Domains. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * exportRegistrationAsync(ExportRegistrationRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * exportRegistrationAsync(RegistrationName name) 
  * exportRegistrationAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * exportRegistrationOperationCallable() 
  * exportRegistrationCallable() 

  
DeleteRegistration |  Deletes a `Registration` resource.  This method works on any `Registration` resource using [Subscription or Commitment billing](https://docs.cloud.google.com/domains/pricing#billing-models), provided that the resource was created at least 1 day in the past.  For `Registration` resources using [Monthly billing](https://docs.cloud.google.com/domains/pricing#billing-models), this method works if: 

  * `state` is `EXPORTED` with `expire_time` in the past 
  * `state` is `REGISTRATION_FAILED`
  * `state` is `TRANSFER_FAILED`

When an active registration is successfully deleted, you can continue to use the domain in [Google Domains](https://domains.google/) until it expires. The calling user becomes the domain's sole owner in Google Domains, and permissions for the domain are subsequently managed there. The domain does not renew automatically unless the new owner sets up billing in Google Domains. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteRegistrationAsync(DeleteRegistrationRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteRegistrationAsync(RegistrationName name) 
  * deleteRegistrationAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteRegistrationOperationCallable() 
  * deleteRegistrationCallable() 

  
RetrieveAuthorizationCode |  Gets the authorization code of the `Registration` for the purpose of transferring the domain to another registrar.  You can call this method only after 60 days have elapsed since the initial domain registration. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * retrieveAuthorizationCode(RetrieveAuthorizationCodeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * retrieveAuthorizationCode(RegistrationName registration) 
  * retrieveAuthorizationCode(String registration) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * retrieveAuthorizationCodeCallable() 

  
ResetAuthorizationCode |  Resets the authorization code of the `Registration` to a new random string.  You can call this method only after 60 days have elapsed since the initial domain registration. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * resetAuthorizationCode(ResetAuthorizationCodeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * resetAuthorizationCode(RegistrationName registration) 
  * resetAuthorizationCode(String registration) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * resetAuthorizationCodeCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of DomainsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DomainsSettings domainsSettings =
         DomainsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     DomainsClient domainsClient = DomainsClient.create(domainsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DomainsSettings domainsSettings = DomainsSettings.newBuilder().setEndpoint(myEndpoint).build();
     DomainsClient domainsClient = DomainsClient.create(domainsSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DomainsSettings domainsSettings = DomainsSettings.newHttpJsonBuilder().build();
     DomainsClient domainsClient = DomainsClient.create(domainsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DomainsClient

## Static Methods 

### create()
    
    
    public static final DomainsClient create()

Constructs an instance of DomainsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[DomainsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DomainsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DomainsSettings settings)
    
    
    public static final DomainsClient create(DomainsSettings settings)

Constructs an instance of DomainsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DomainsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DomainsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DomainsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DomainsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DomainsStub stub)
    
    
    public static final DomainsClient create(DomainsStub stub)

Constructs an instance of DomainsClient, using the given stub for making calls. This is for advanced usage - prefer using create(DomainsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DomainsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.stub.DomainsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DomainsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DomainsClient)` |   
  
## Constructors 

### DomainsClient(DomainsSettings settings)
    
    
    protected DomainsClient(DomainsSettings settings)

Constructs an instance of DomainsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DomainsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DomainsSettings)`  
  
  
### DomainsClient(DomainsStub stub)
    
    
    protected DomainsClient(DomainsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DomainsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.stub.DomainsStub)`  
  
  
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
  
### close()
    
    
    public final void close()

### configureContactSettingsAsync(@Nullable RegistrationName registration, ContactSettings contactSettings, FieldMask updateMask)
    
    
    public final OperationFuture<Registration,OperationMetadata> configureContactSettingsAsync(@Nullable RegistrationName registration, ContactSettings contactSettings, FieldMask updateMask)

Updates a `Registration`'s contact settings. Some changes require confirmation by the domain's registrant contact .

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       RegistrationName registration =
           RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]");
       ContactSettings contactSettings = ContactSettings.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Registration response =
           domainsClient
               .configureContactSettingsAsync(registration, contactSettings, updateMask)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`registration` | `@org.jspecify.annotations.Nullable com.google.cloud.domains.v1beta1.RegistrationName`  
Required. The name of the `Registration` whose contact settings are being updated, in the format `projects/*/locations/*/registrations/*`.  
`contactSettings` | `[ContactSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ContactSettings)`  
Fields of the `ContactSettings` to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The field mask describing which fields to update as a comma-separated list. For example, if only the registrant contact is being updated, the `update_mask` is `"registrant_contact"`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.OperationMetadata)>` |   
  
### configureContactSettingsAsync(ConfigureContactSettingsRequest request)
    
    
    public final OperationFuture<Registration,OperationMetadata> configureContactSettingsAsync(ConfigureContactSettingsRequest request)

Updates a `Registration`'s contact settings. Some changes require confirmation by the domain's registrant contact .

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       ConfigureContactSettingsRequest request =
           ConfigureContactSettingsRequest.newBuilder()
               .setRegistration(
                   RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]").toString())
               .setContactSettings(ContactSettings.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .addAllContactNotices(new ArrayList<ContactNotice>())
               .setValidateOnly(true)
               .build();
       Registration response = domainsClient.configureContactSettingsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ConfigureContactSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ConfigureContactSettingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.OperationMetadata)>` |   
  
### configureContactSettingsAsync(String registration, ContactSettings contactSettings, FieldMask updateMask)
    
    
    public final OperationFuture<Registration,OperationMetadata> configureContactSettingsAsync(String registration, ContactSettings contactSettings, FieldMask updateMask)

Updates a `Registration`'s contact settings. Some changes require confirmation by the domain's registrant contact .

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       String registration =
           RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]").toString();
       ContactSettings contactSettings = ContactSettings.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Registration response =
           domainsClient
               .configureContactSettingsAsync(registration, contactSettings, updateMask)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`registration` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the `Registration` whose contact settings are being updated, in the format `projects/*/locations/*/registrations/*`.  
`contactSettings` | `[ContactSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ContactSettings)`  
Fields of the `ContactSettings` to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The field mask describing which fields to update as a comma-separated list. For example, if only the registrant contact is being updated, the `update_mask` is `"registrant_contact"`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.OperationMetadata)>` |   
  
### configureContactSettingsCallable()
    
    
    public final UnaryCallable<ConfigureContactSettingsRequest,Operation> configureContactSettingsCallable()

Updates a `Registration`'s contact settings. Some changes require confirmation by the domain's registrant contact .

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       ConfigureContactSettingsRequest request =
           ConfigureContactSettingsRequest.newBuilder()
               .setRegistration(
                   RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]").toString())
               .setContactSettings(ContactSettings.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .addAllContactNotices(new ArrayList<ContactNotice>())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           domainsClient.configureContactSettingsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ConfigureContactSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ConfigureContactSettingsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### configureContactSettingsOperationCallable()
    
    
    public final OperationCallable<ConfigureContactSettingsRequest,Registration,OperationMetadata> configureContactSettingsOperationCallable()

Updates a `Registration`'s contact settings. Some changes require confirmation by the domain's registrant contact .

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       ConfigureContactSettingsRequest request =
           ConfigureContactSettingsRequest.newBuilder()
               .setRegistration(
                   RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]").toString())
               .setContactSettings(ContactSettings.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .addAllContactNotices(new ArrayList<ContactNotice>())
               .setValidateOnly(true)
               .build();
       OperationFuture<Registration, OperationMetadata> future =
           domainsClient.configureContactSettingsOperationCallable().futureCall(request);
       // Do something.
       Registration response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ConfigureContactSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ConfigureContactSettingsRequest),[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.OperationMetadata)>` |   
  
### configureDnsSettingsAsync(@Nullable RegistrationName registration, DnsSettings dnsSettings, FieldMask updateMask)
    
    
    public final OperationFuture<Registration,OperationMetadata> configureDnsSettingsAsync(@Nullable RegistrationName registration, DnsSettings dnsSettings, FieldMask updateMask)

Updates a `Registration`'s DNS settings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       RegistrationName registration =
           RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]");
       DnsSettings dnsSettings = DnsSettings.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Registration response =
           domainsClient.configureDnsSettingsAsync(registration, dnsSettings, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`registration` | `@org.jspecify.annotations.Nullable com.google.cloud.domains.v1beta1.RegistrationName`  
Required. The name of the `Registration` whose DNS settings are being updated, in the format `projects/*/locations/*/registrations/*`.  
`dnsSettings` | `[DnsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DnsSettings)`  
Fields of the `DnsSettings` to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The field mask describing which fields to update as a comma-separated list. For example, if only the name servers are being updated for an existing Custom DNS configuration, the `update_mask` is `"custom_dns.name_servers"`. When changing the DNS provider from one type to another, pass the new provider's field name as part of the field mask. For example, when changing from a Google Domains DNS configuration to a Custom DNS configuration, the `update_mask` is `"custom_dns"`. //  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.OperationMetadata)>` |   
  
### configureDnsSettingsAsync(ConfigureDnsSettingsRequest request)
    
    
    public final OperationFuture<Registration,OperationMetadata> configureDnsSettingsAsync(ConfigureDnsSettingsRequest request)

Updates a `Registration`'s DNS settings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       ConfigureDnsSettingsRequest request =
           ConfigureDnsSettingsRequest.newBuilder()
               .setRegistration(
                   RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]").toString())
               .setDnsSettings(DnsSettings.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       Registration response = domainsClient.configureDnsSettingsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ConfigureDnsSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ConfigureDnsSettingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.OperationMetadata)>` |   
  
### configureDnsSettingsAsync(String registration, DnsSettings dnsSettings, FieldMask updateMask)
    
    
    public final OperationFuture<Registration,OperationMetadata> configureDnsSettingsAsync(String registration, DnsSettings dnsSettings, FieldMask updateMask)

Updates a `Registration`'s DNS settings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       String registration =
           RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]").toString();
       DnsSettings dnsSettings = DnsSettings.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Registration response =
           domainsClient.configureDnsSettingsAsync(registration, dnsSettings, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`registration` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the `Registration` whose DNS settings are being updated, in the format `projects/*/locations/*/registrations/*`.  
`dnsSettings` | `[DnsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DnsSettings)`  
Fields of the `DnsSettings` to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The field mask describing which fields to update as a comma-separated list. For example, if only the name servers are being updated for an existing Custom DNS configuration, the `update_mask` is `"custom_dns.name_servers"`. When changing the DNS provider from one type to another, pass the new provider's field name as part of the field mask. For example, when changing from a Google Domains DNS configuration to a Custom DNS configuration, the `update_mask` is `"custom_dns"`. //  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.OperationMetadata)>` |   
  
### configureDnsSettingsCallable()
    
    
    public final UnaryCallable<ConfigureDnsSettingsRequest,Operation> configureDnsSettingsCallable()

Updates a `Registration`'s DNS settings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       ConfigureDnsSettingsRequest request =
           ConfigureDnsSettingsRequest.newBuilder()
               .setRegistration(
                   RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]").toString())
               .setDnsSettings(DnsSettings.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           domainsClient.configureDnsSettingsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ConfigureDnsSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ConfigureDnsSettingsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### configureDnsSettingsOperationCallable()
    
    
    public final OperationCallable<ConfigureDnsSettingsRequest,Registration,OperationMetadata> configureDnsSettingsOperationCallable()

Updates a `Registration`'s DNS settings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       ConfigureDnsSettingsRequest request =
           ConfigureDnsSettingsRequest.newBuilder()
               .setRegistration(
                   RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]").toString())
               .setDnsSettings(DnsSettings.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<Registration, OperationMetadata> future =
           domainsClient.configureDnsSettingsOperationCallable().futureCall(request);
       // Do something.
       Registration response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ConfigureDnsSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ConfigureDnsSettingsRequest),[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.OperationMetadata)>` |   
  
### configureManagementSettingsAsync(@Nullable RegistrationName registration, ManagementSettings managementSettings, FieldMask updateMask)
    
    
    public final OperationFuture<Registration,OperationMetadata> configureManagementSettingsAsync(@Nullable RegistrationName registration, ManagementSettings managementSettings, FieldMask updateMask)

Updates a `Registration`'s management settings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       RegistrationName registration =
           RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]");
       ManagementSettings managementSettings = ManagementSettings.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Registration response =
           domainsClient
               .configureManagementSettingsAsync(registration, managementSettings, updateMask)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`registration` | `@org.jspecify.annotations.Nullable com.google.cloud.domains.v1beta1.RegistrationName`  
Required. The name of the `Registration` whose management settings are being updated, in the format `projects/*/locations/*/registrations/*`.  
`managementSettings` | `[ManagementSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ManagementSettings)`  
Fields of the `ManagementSettings` to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The field mask describing which fields to update as a comma-separated list. For example, if only the transfer lock is being updated, the `update_mask` is `"transfer_lock_state"`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.OperationMetadata)>` |   
  
### configureManagementSettingsAsync(ConfigureManagementSettingsRequest request)
    
    
    public final OperationFuture<Registration,OperationMetadata> configureManagementSettingsAsync(ConfigureManagementSettingsRequest request)

Updates a `Registration`'s management settings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       ConfigureManagementSettingsRequest request =
           ConfigureManagementSettingsRequest.newBuilder()
               .setRegistration(
                   RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]").toString())
               .setManagementSettings(ManagementSettings.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Registration response = domainsClient.configureManagementSettingsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ConfigureManagementSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ConfigureManagementSettingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.OperationMetadata)>` |   
  
### configureManagementSettingsAsync(String registration, ManagementSettings managementSettings, FieldMask updateMask)
    
    
    public final OperationFuture<Registration,OperationMetadata> configureManagementSettingsAsync(String registration, ManagementSettings managementSettings, FieldMask updateMask)

Updates a `Registration`'s management settings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       String registration =
           RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]").toString();
       ManagementSettings managementSettings = ManagementSettings.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Registration response =
           domainsClient
               .configureManagementSettingsAsync(registration, managementSettings, updateMask)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`registration` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the `Registration` whose management settings are being updated, in the format `projects/*/locations/*/registrations/*`.  
`managementSettings` | `[ManagementSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ManagementSettings)`  
Fields of the `ManagementSettings` to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The field mask describing which fields to update as a comma-separated list. For example, if only the transfer lock is being updated, the `update_mask` is `"transfer_lock_state"`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.OperationMetadata)>` |   
  
### configureManagementSettingsCallable()
    
    
    public final UnaryCallable<ConfigureManagementSettingsRequest,Operation> configureManagementSettingsCallable()

Updates a `Registration`'s management settings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       ConfigureManagementSettingsRequest request =
           ConfigureManagementSettingsRequest.newBuilder()
               .setRegistration(
                   RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]").toString())
               .setManagementSettings(ManagementSettings.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           domainsClient.configureManagementSettingsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ConfigureManagementSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ConfigureManagementSettingsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### configureManagementSettingsOperationCallable()
    
    
    public final OperationCallable<ConfigureManagementSettingsRequest,Registration,OperationMetadata> configureManagementSettingsOperationCallable()

Updates a `Registration`'s management settings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       ConfigureManagementSettingsRequest request =
           ConfigureManagementSettingsRequest.newBuilder()
               .setRegistration(
                   RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]").toString())
               .setManagementSettings(ManagementSettings.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       OperationFuture<Registration, OperationMetadata> future =
           domainsClient.configureManagementSettingsOperationCallable().futureCall(request);
       // Do something.
       Registration response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ConfigureManagementSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ConfigureManagementSettingsRequest),[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.OperationMetadata)>` |   
  
### deleteRegistrationAsync(@Nullable RegistrationName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteRegistrationAsync(@Nullable RegistrationName name)

Deletes a `Registration` resource.

This method works on any `Registration` resource using [Subscription or Commitment billing](https://docs.cloud.google.com/domains/pricing#billing-models), provided that the resource was created at least 1 day in the past.

For `Registration` resources using [Monthly billing](https://docs.cloud.google.com/domains/pricing#billing-models), this method works if:

  * `state` is `EXPORTED` with `expire_time` in the past 
  * `state` is `REGISTRATION_FAILED`
  * `state` is `TRANSFER_FAILED`



When an active registration is successfully deleted, you can continue to use the domain in [Google Domains](https://domains.google/) until it expires. The calling user becomes the domain's sole owner in Google Domains, and permissions for the domain are subsequently managed there. The domain does not renew automatically unless the new owner sets up billing in Google Domains.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       RegistrationName name = RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]");
       domainsClient.deleteRegistrationAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.domains.v1beta1.RegistrationName`  
Required. The name of the `Registration` to delete, in the format `projects/*/locations/*/registrations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.OperationMetadata)>` |   
  
### deleteRegistrationAsync(DeleteRegistrationRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteRegistrationAsync(DeleteRegistrationRequest request)

Deletes a `Registration` resource.

This method works on any `Registration` resource using [Subscription or Commitment billing](https://docs.cloud.google.com/domains/pricing#billing-models), provided that the resource was created at least 1 day in the past.

For `Registration` resources using [Monthly billing](https://docs.cloud.google.com/domains/pricing#billing-models), this method works if:

  * `state` is `EXPORTED` with `expire_time` in the past 
  * `state` is `REGISTRATION_FAILED`
  * `state` is `TRANSFER_FAILED`



When an active registration is successfully deleted, you can continue to use the domain in [Google Domains](https://domains.google/) until it expires. The calling user becomes the domain's sole owner in Google Domains, and permissions for the domain are subsequently managed there. The domain does not renew automatically unless the new owner sets up billing in Google Domains.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       DeleteRegistrationRequest request =
           DeleteRegistrationRequest.newBuilder()
               .setName(RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]").toString())
               .build();
       domainsClient.deleteRegistrationAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRegistrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DeleteRegistrationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.OperationMetadata)>` |   
  
### deleteRegistrationAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteRegistrationAsync(String name)

Deletes a `Registration` resource.

This method works on any `Registration` resource using [Subscription or Commitment billing](https://docs.cloud.google.com/domains/pricing#billing-models), provided that the resource was created at least 1 day in the past.

For `Registration` resources using [Monthly billing](https://docs.cloud.google.com/domains/pricing#billing-models), this method works if:

  * `state` is `EXPORTED` with `expire_time` in the past 
  * `state` is `REGISTRATION_FAILED`
  * `state` is `TRANSFER_FAILED`



When an active registration is successfully deleted, you can continue to use the domain in [Google Domains](https://domains.google/) until it expires. The calling user becomes the domain's sole owner in Google Domains, and permissions for the domain are subsequently managed there. The domain does not renew automatically unless the new owner sets up billing in Google Domains.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       String name = RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]").toString();
       domainsClient.deleteRegistrationAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the `Registration` to delete, in the format `projects/*/locations/*/registrations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.OperationMetadata)>` |   
  
### deleteRegistrationCallable()
    
    
    public final UnaryCallable<DeleteRegistrationRequest,Operation> deleteRegistrationCallable()

Deletes a `Registration` resource.

This method works on any `Registration` resource using [Subscription or Commitment billing](https://docs.cloud.google.com/domains/pricing#billing-models), provided that the resource was created at least 1 day in the past.

For `Registration` resources using [Monthly billing](https://docs.cloud.google.com/domains/pricing#billing-models), this method works if:

  * `state` is `EXPORTED` with `expire_time` in the past 
  * `state` is `REGISTRATION_FAILED`
  * `state` is `TRANSFER_FAILED`



When an active registration is successfully deleted, you can continue to use the domain in [Google Domains](https://domains.google/) until it expires. The calling user becomes the domain's sole owner in Google Domains, and permissions for the domain are subsequently managed there. The domain does not renew automatically unless the new owner sets up billing in Google Domains.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       DeleteRegistrationRequest request =
           DeleteRegistrationRequest.newBuilder()
               .setName(RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]").toString())
               .build();
       ApiFuture<Operation> future = domainsClient.deleteRegistrationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteRegistrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DeleteRegistrationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteRegistrationOperationCallable()
    
    
    public final OperationCallable<DeleteRegistrationRequest,Empty,OperationMetadata> deleteRegistrationOperationCallable()

Deletes a `Registration` resource.

This method works on any `Registration` resource using [Subscription or Commitment billing](https://docs.cloud.google.com/domains/pricing#billing-models), provided that the resource was created at least 1 day in the past.

For `Registration` resources using [Monthly billing](https://docs.cloud.google.com/domains/pricing#billing-models), this method works if:

  * `state` is `EXPORTED` with `expire_time` in the past 
  * `state` is `REGISTRATION_FAILED`
  * `state` is `TRANSFER_FAILED`



When an active registration is successfully deleted, you can continue to use the domain in [Google Domains](https://domains.google/) until it expires. The calling user becomes the domain's sole owner in Google Domains, and permissions for the domain are subsequently managed there. The domain does not renew automatically unless the new owner sets up billing in Google Domains.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       DeleteRegistrationRequest request =
           DeleteRegistrationRequest.newBuilder()
               .setName(RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]").toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           domainsClient.deleteRegistrationOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteRegistrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DeleteRegistrationRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.OperationMetadata)>` |   
  
### exportRegistrationAsync(@Nullable RegistrationName name)
    
    
    public final OperationFuture<Registration,OperationMetadata> exportRegistrationAsync(@Nullable RegistrationName name)

Exports a `Registration` resource, such that it is no longer managed by Cloud Domains.

When an active domain is successfully exported, you can continue to use the domain in [Google Domains](https://domains.google/) until it expires. The calling user becomes the domain's sole owner in Google Domains, and permissions for the domain are subsequently managed there. The domain does not renew automatically unless the new owner sets up billing in Google Domains.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       RegistrationName name = RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]");
       Registration response = domainsClient.exportRegistrationAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.domains.v1beta1.RegistrationName`  
Required. The name of the `Registration` to export, in the format `projects/*/locations/*/registrations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.OperationMetadata)>` |   
  
### exportRegistrationAsync(ExportRegistrationRequest request)
    
    
    public final OperationFuture<Registration,OperationMetadata> exportRegistrationAsync(ExportRegistrationRequest request)

Exports a `Registration` resource, such that it is no longer managed by Cloud Domains.

When an active domain is successfully exported, you can continue to use the domain in [Google Domains](https://domains.google/) until it expires. The calling user becomes the domain's sole owner in Google Domains, and permissions for the domain are subsequently managed there. The domain does not renew automatically unless the new owner sets up billing in Google Domains.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       ExportRegistrationRequest request =
           ExportRegistrationRequest.newBuilder()
               .setName(RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]").toString())
               .build();
       Registration response = domainsClient.exportRegistrationAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportRegistrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ExportRegistrationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.OperationMetadata)>` |   
  
### exportRegistrationAsync(String name)
    
    
    public final OperationFuture<Registration,OperationMetadata> exportRegistrationAsync(String name)

Exports a `Registration` resource, such that it is no longer managed by Cloud Domains.

When an active domain is successfully exported, you can continue to use the domain in [Google Domains](https://domains.google/) until it expires. The calling user becomes the domain's sole owner in Google Domains, and permissions for the domain are subsequently managed there. The domain does not renew automatically unless the new owner sets up billing in Google Domains.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       String name = RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]").toString();
       Registration response = domainsClient.exportRegistrationAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the `Registration` to export, in the format `projects/*/locations/*/registrations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.OperationMetadata)>` |   
  
### exportRegistrationCallable()
    
    
    public final UnaryCallable<ExportRegistrationRequest,Operation> exportRegistrationCallable()

Exports a `Registration` resource, such that it is no longer managed by Cloud Domains.

When an active domain is successfully exported, you can continue to use the domain in [Google Domains](https://domains.google/) until it expires. The calling user becomes the domain's sole owner in Google Domains, and permissions for the domain are subsequently managed there. The domain does not renew automatically unless the new owner sets up billing in Google Domains.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       ExportRegistrationRequest request =
           ExportRegistrationRequest.newBuilder()
               .setName(RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]").toString())
               .build();
       ApiFuture<Operation> future = domainsClient.exportRegistrationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ExportRegistrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ExportRegistrationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### exportRegistrationOperationCallable()
    
    
    public final OperationCallable<ExportRegistrationRequest,Registration,OperationMetadata> exportRegistrationOperationCallable()

Exports a `Registration` resource, such that it is no longer managed by Cloud Domains.

When an active domain is successfully exported, you can continue to use the domain in [Google Domains](https://domains.google/) until it expires. The calling user becomes the domain's sole owner in Google Domains, and permissions for the domain are subsequently managed there. The domain does not renew automatically unless the new owner sets up billing in Google Domains.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       ExportRegistrationRequest request =
           ExportRegistrationRequest.newBuilder()
               .setName(RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]").toString())
               .build();
       OperationFuture<Registration, OperationMetadata> future =
           domainsClient.exportRegistrationOperationCallable().futureCall(request);
       // Do something.
       Registration response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ExportRegistrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ExportRegistrationRequest),[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.OperationMetadata)>` |   
  
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
  
### getRegistration(@Nullable RegistrationName name)
    
    
    public final Registration getRegistration(@Nullable RegistrationName name)

Gets the details of a `Registration` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       RegistrationName name = RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]");
       Registration response = domainsClient.getRegistration(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.domains.v1beta1.RegistrationName`  
Required. The name of the `Registration` to get, in the format `projects/*/locations/*/registrations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration)` |   
  
### getRegistration(GetRegistrationRequest request)
    
    
    public final Registration getRegistration(GetRegistrationRequest request)

Gets the details of a `Registration` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       GetRegistrationRequest request =
           GetRegistrationRequest.newBuilder()
               .setName(RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]").toString())
               .build();
       Registration response = domainsClient.getRegistration(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRegistrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.GetRegistrationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration)` |   
  
### getRegistration(String name)
    
    
    public final Registration getRegistration(String name)

Gets the details of a `Registration` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       String name = RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]").toString();
       Registration response = domainsClient.getRegistration(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the `Registration` to get, in the format `projects/*/locations/*/registrations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration)` |   
  
### getRegistrationCallable()
    
    
    public final UnaryCallable<GetRegistrationRequest,Registration> getRegistrationCallable()

Gets the details of a `Registration` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       GetRegistrationRequest request =
           GetRegistrationRequest.newBuilder()
               .setName(RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]").toString())
               .build();
       ApiFuture<Registration> future = domainsClient.getRegistrationCallable().futureCall(request);
       // Do something.
       Registration response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRegistrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.GetRegistrationRequest),[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration)>` |   
  
### getSettings()
    
    
    public final @Nullable DomainsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.domains.v1beta1.DomainsSettings` |   
  
### getStub()
    
    
    public DomainsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DomainsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.stub.DomainsStub)` |   
  
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
  
### listRegistrations(@Nullable LocationName parent)
    
    
    public final DomainsClient.ListRegistrationsPagedResponse listRegistrations(@Nullable LocationName parent)

Lists the `Registration` resources in a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Registration element : domainsClient.listRegistrations(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.domains.v1beta1.LocationName`  
Required. The project and location from which to list `Registration`s, specified in the format `projects/*/locations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[DomainsClient.ListRegistrationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DomainsClient.ListRegistrationsPagedResponse)` |   
  
### listRegistrations(ListRegistrationsRequest request)
    
    
    public final DomainsClient.ListRegistrationsPagedResponse listRegistrations(ListRegistrationsRequest request)

Lists the `Registration` resources in a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       ListRegistrationsRequest request =
           ListRegistrationsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (Registration element : domainsClient.listRegistrations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRegistrationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ListRegistrationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DomainsClient.ListRegistrationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DomainsClient.ListRegistrationsPagedResponse)` |   
  
### listRegistrations(String parent)
    
    
    public final DomainsClient.ListRegistrationsPagedResponse listRegistrations(String parent)

Lists the `Registration` resources in a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Registration element : domainsClient.listRegistrations(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location from which to list `Registration`s, specified in the format `projects/*/locations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[DomainsClient.ListRegistrationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DomainsClient.ListRegistrationsPagedResponse)` |   
  
### listRegistrationsCallable()
    
    
    public final UnaryCallable<ListRegistrationsRequest,ListRegistrationsResponse> listRegistrationsCallable()

Lists the `Registration` resources in a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       ListRegistrationsRequest request =
           ListRegistrationsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListRegistrationsResponse response =
             domainsClient.listRegistrationsCallable().call(request);
         for (Registration element : response.getRegistrationsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegistrationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ListRegistrationsRequest),[ListRegistrationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ListRegistrationsResponse)>` |   
  
### listRegistrationsPagedCallable()
    
    
    public final UnaryCallable<ListRegistrationsRequest,DomainsClient.ListRegistrationsPagedResponse> listRegistrationsPagedCallable()

Lists the `Registration` resources in a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       ListRegistrationsRequest request =
           ListRegistrationsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<Registration> future =
           domainsClient.listRegistrationsPagedCallable().futureCall(request);
       // Do something.
       for (Registration element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegistrationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ListRegistrationsRequest),[ListRegistrationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DomainsClient.ListRegistrationsPagedResponse)>` |   
  
### registerDomainAsync(@Nullable LocationName parent, Registration registration, Money yearlyPrice)
    
    
    public final OperationFuture<Registration,OperationMetadata> registerDomainAsync(@Nullable LocationName parent, Registration registration, Money yearlyPrice)

Registers a new domain name and creates a corresponding `Registration` resource.

Call `RetrieveRegisterParameters` first to check availability of the domain name and determine parameters like price that are needed to build a call to this method.

A successful call creates a `Registration` resource in state `REGISTRATION_PENDING`, which resolves to `ACTIVE` within 1-2 minutes, indicating that the domain was successfully registered. If the resource ends up in state `REGISTRATION_FAILED`, it indicates that the domain was not registered successfully, and you can safely delete the resource and retry registration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Registration registration = Registration.newBuilder().build();
       Money yearlyPrice = Money.newBuilder().build();
       Registration response =
           domainsClient.registerDomainAsync(parent, registration, yearlyPrice).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.domains.v1beta1.LocationName`  
Required. The parent resource of the `Registration`. Must be in the format `projects/*/locations/*`.  
`registration` | `[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration)`  
Required. The complete `Registration` resource to be created.  
`yearlyPrice` | `com.google.type.Money`  
Required. Yearly price to register or renew the domain. The value that should be put here can be obtained from RetrieveRegisterParameters or SearchDomains calls.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.OperationMetadata)>` |   
  
### registerDomainAsync(RegisterDomainRequest request)
    
    
    public final OperationFuture<Registration,OperationMetadata> registerDomainAsync(RegisterDomainRequest request)

Registers a new domain name and creates a corresponding `Registration` resource.

Call `RetrieveRegisterParameters` first to check availability of the domain name and determine parameters like price that are needed to build a call to this method.

A successful call creates a `Registration` resource in state `REGISTRATION_PENDING`, which resolves to `ACTIVE` within 1-2 minutes, indicating that the domain was successfully registered. If the resource ends up in state `REGISTRATION_FAILED`, it indicates that the domain was not registered successfully, and you can safely delete the resource and retry registration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       RegisterDomainRequest request =
           RegisterDomainRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setRegistration(Registration.newBuilder().build())
               .addAllDomainNotices(new ArrayList<DomainNotice>())
               .addAllContactNotices(new ArrayList<ContactNotice>())
               .setYearlyPrice(Money.newBuilder().build())
               .setValidateOnly(true)
               .build();
       Registration response = domainsClient.registerDomainAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RegisterDomainRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RegisterDomainRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.OperationMetadata)>` |   
  
### registerDomainAsync(String parent, Registration registration, Money yearlyPrice)
    
    
    public final OperationFuture<Registration,OperationMetadata> registerDomainAsync(String parent, Registration registration, Money yearlyPrice)

Registers a new domain name and creates a corresponding `Registration` resource.

Call `RetrieveRegisterParameters` first to check availability of the domain name and determine parameters like price that are needed to build a call to this method.

A successful call creates a `Registration` resource in state `REGISTRATION_PENDING`, which resolves to `ACTIVE` within 1-2 minutes, indicating that the domain was successfully registered. If the resource ends up in state `REGISTRATION_FAILED`, it indicates that the domain was not registered successfully, and you can safely delete the resource and retry registration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Registration registration = Registration.newBuilder().build();
       Money yearlyPrice = Money.newBuilder().build();
       Registration response =
           domainsClient.registerDomainAsync(parent, registration, yearlyPrice).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource of the `Registration`. Must be in the format `projects/*/locations/*`.  
`registration` | `[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration)`  
Required. The complete `Registration` resource to be created.  
`yearlyPrice` | `com.google.type.Money`  
Required. Yearly price to register or renew the domain. The value that should be put here can be obtained from RetrieveRegisterParameters or SearchDomains calls.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.OperationMetadata)>` |   
  
### registerDomainCallable()
    
    
    public final UnaryCallable<RegisterDomainRequest,Operation> registerDomainCallable()

Registers a new domain name and creates a corresponding `Registration` resource.

Call `RetrieveRegisterParameters` first to check availability of the domain name and determine parameters like price that are needed to build a call to this method.

A successful call creates a `Registration` resource in state `REGISTRATION_PENDING`, which resolves to `ACTIVE` within 1-2 minutes, indicating that the domain was successfully registered. If the resource ends up in state `REGISTRATION_FAILED`, it indicates that the domain was not registered successfully, and you can safely delete the resource and retry registration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       RegisterDomainRequest request =
           RegisterDomainRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setRegistration(Registration.newBuilder().build())
               .addAllDomainNotices(new ArrayList<DomainNotice>())
               .addAllContactNotices(new ArrayList<ContactNotice>())
               .setYearlyPrice(Money.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future = domainsClient.registerDomainCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RegisterDomainRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RegisterDomainRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### registerDomainOperationCallable()
    
    
    public final OperationCallable<RegisterDomainRequest,Registration,OperationMetadata> registerDomainOperationCallable()

Registers a new domain name and creates a corresponding `Registration` resource.

Call `RetrieveRegisterParameters` first to check availability of the domain name and determine parameters like price that are needed to build a call to this method.

A successful call creates a `Registration` resource in state `REGISTRATION_PENDING`, which resolves to `ACTIVE` within 1-2 minutes, indicating that the domain was successfully registered. If the resource ends up in state `REGISTRATION_FAILED`, it indicates that the domain was not registered successfully, and you can safely delete the resource and retry registration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       RegisterDomainRequest request =
           RegisterDomainRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setRegistration(Registration.newBuilder().build())
               .addAllDomainNotices(new ArrayList<DomainNotice>())
               .addAllContactNotices(new ArrayList<ContactNotice>())
               .setYearlyPrice(Money.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<Registration, OperationMetadata> future =
           domainsClient.registerDomainOperationCallable().futureCall(request);
       // Do something.
       Registration response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RegisterDomainRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RegisterDomainRequest),[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.OperationMetadata)>` |   
  
### resetAuthorizationCode(@Nullable RegistrationName registration)
    
    
    public final AuthorizationCode resetAuthorizationCode(@Nullable RegistrationName registration)

Resets the authorization code of the `Registration` to a new random string.

You can call this method only after 60 days have elapsed since the initial domain registration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       RegistrationName registration =
           RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]");
       AuthorizationCode response = domainsClient.resetAuthorizationCode(registration);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`registration` | `@org.jspecify.annotations.Nullable com.google.cloud.domains.v1beta1.RegistrationName`  
Required. The name of the `Registration` whose authorization code is being reset, in the format `projects/*/locations/*/registrations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[AuthorizationCode](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.AuthorizationCode)` |   
  
### resetAuthorizationCode(ResetAuthorizationCodeRequest request)
    
    
    public final AuthorizationCode resetAuthorizationCode(ResetAuthorizationCodeRequest request)

Resets the authorization code of the `Registration` to a new random string.

You can call this method only after 60 days have elapsed since the initial domain registration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       ResetAuthorizationCodeRequest request =
           ResetAuthorizationCodeRequest.newBuilder()
               .setRegistration(
                   RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]").toString())
               .build();
       AuthorizationCode response = domainsClient.resetAuthorizationCode(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ResetAuthorizationCodeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ResetAuthorizationCodeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AuthorizationCode](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.AuthorizationCode)` |   
  
### resetAuthorizationCode(String registration)
    
    
    public final AuthorizationCode resetAuthorizationCode(String registration)

Resets the authorization code of the `Registration` to a new random string.

You can call this method only after 60 days have elapsed since the initial domain registration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       String registration =
           RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]").toString();
       AuthorizationCode response = domainsClient.resetAuthorizationCode(registration);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`registration` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the `Registration` whose authorization code is being reset, in the format `projects/*/locations/*/registrations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[AuthorizationCode](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.AuthorizationCode)` |   
  
### resetAuthorizationCodeCallable()
    
    
    public final UnaryCallable<ResetAuthorizationCodeRequest,AuthorizationCode> resetAuthorizationCodeCallable()

Resets the authorization code of the `Registration` to a new random string.

You can call this method only after 60 days have elapsed since the initial domain registration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       ResetAuthorizationCodeRequest request =
           ResetAuthorizationCodeRequest.newBuilder()
               .setRegistration(
                   RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]").toString())
               .build();
       ApiFuture<AuthorizationCode> future =
           domainsClient.resetAuthorizationCodeCallable().futureCall(request);
       // Do something.
       AuthorizationCode response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ResetAuthorizationCodeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ResetAuthorizationCodeRequest),[AuthorizationCode](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.AuthorizationCode)>` |   
  
### retrieveAuthorizationCode(@Nullable RegistrationName registration)
    
    
    public final AuthorizationCode retrieveAuthorizationCode(@Nullable RegistrationName registration)

Gets the authorization code of the `Registration` for the purpose of transferring the domain to another registrar.

You can call this method only after 60 days have elapsed since the initial domain registration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       RegistrationName registration =
           RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]");
       AuthorizationCode response = domainsClient.retrieveAuthorizationCode(registration);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`registration` | `@org.jspecify.annotations.Nullable com.google.cloud.domains.v1beta1.RegistrationName`  
Required. The name of the `Registration` whose authorization code is being retrieved, in the format `projects/*/locations/*/registrations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[AuthorizationCode](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.AuthorizationCode)` |   
  
### retrieveAuthorizationCode(RetrieveAuthorizationCodeRequest request)
    
    
    public final AuthorizationCode retrieveAuthorizationCode(RetrieveAuthorizationCodeRequest request)

Gets the authorization code of the `Registration` for the purpose of transferring the domain to another registrar.

You can call this method only after 60 days have elapsed since the initial domain registration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       RetrieveAuthorizationCodeRequest request =
           RetrieveAuthorizationCodeRequest.newBuilder()
               .setRegistration(
                   RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]").toString())
               .build();
       AuthorizationCode response = domainsClient.retrieveAuthorizationCode(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RetrieveAuthorizationCodeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RetrieveAuthorizationCodeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AuthorizationCode](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.AuthorizationCode)` |   
  
### retrieveAuthorizationCode(String registration)
    
    
    public final AuthorizationCode retrieveAuthorizationCode(String registration)

Gets the authorization code of the `Registration` for the purpose of transferring the domain to another registrar.

You can call this method only after 60 days have elapsed since the initial domain registration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       String registration =
           RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]").toString();
       AuthorizationCode response = domainsClient.retrieveAuthorizationCode(registration);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`registration` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the `Registration` whose authorization code is being retrieved, in the format `projects/*/locations/*/registrations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[AuthorizationCode](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.AuthorizationCode)` |   
  
### retrieveAuthorizationCodeCallable()
    
    
    public final UnaryCallable<RetrieveAuthorizationCodeRequest,AuthorizationCode> retrieveAuthorizationCodeCallable()

Gets the authorization code of the `Registration` for the purpose of transferring the domain to another registrar.

You can call this method only after 60 days have elapsed since the initial domain registration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       RetrieveAuthorizationCodeRequest request =
           RetrieveAuthorizationCodeRequest.newBuilder()
               .setRegistration(
                   RegistrationName.of("[PROJECT]", "[LOCATION]", "[REGISTRATION]").toString())
               .build();
       ApiFuture<AuthorizationCode> future =
           domainsClient.retrieveAuthorizationCodeCallable().futureCall(request);
       // Do something.
       AuthorizationCode response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RetrieveAuthorizationCodeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RetrieveAuthorizationCodeRequest),[AuthorizationCode](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.AuthorizationCode)>` |   
  
### retrieveRegisterParameters(@Nullable LocationName location, String domainName)
    
    
    public final RetrieveRegisterParametersResponse retrieveRegisterParameters(@Nullable LocationName location, String domainName)

Gets parameters needed to register a new domain name, including price and up-to-date availability. Use the returned values to call `RegisterDomain`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       LocationName location = LocationName.of("[PROJECT]", "[LOCATION]");
       String domainName = "domainName-1244085905";
       RetrieveRegisterParametersResponse response =
           domainsClient.retrieveRegisterParameters(location, domainName);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`location` | `@org.jspecify.annotations.Nullable com.google.cloud.domains.v1beta1.LocationName`  
Required. The location. Must be in the format `projects/*/locations/*`.  
`domainName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The domain name. Unicode domain names must be expressed in Punycode format.  
**Returns**  
---  
**Type** | **Description**  
`[RetrieveRegisterParametersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RetrieveRegisterParametersResponse)` |   
  
### retrieveRegisterParameters(RetrieveRegisterParametersRequest request)
    
    
    public final RetrieveRegisterParametersResponse retrieveRegisterParameters(RetrieveRegisterParametersRequest request)

Gets parameters needed to register a new domain name, including price and up-to-date availability. Use the returned values to call `RegisterDomain`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       RetrieveRegisterParametersRequest request =
           RetrieveRegisterParametersRequest.newBuilder()
               .setDomainName("domainName-1244085905")
               .setLocation(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .build();
       RetrieveRegisterParametersResponse response =
           domainsClient.retrieveRegisterParameters(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RetrieveRegisterParametersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RetrieveRegisterParametersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RetrieveRegisterParametersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RetrieveRegisterParametersResponse)` |   
  
### retrieveRegisterParameters(String location, String domainName)
    
    
    public final RetrieveRegisterParametersResponse retrieveRegisterParameters(String location, String domainName)

Gets parameters needed to register a new domain name, including price and up-to-date availability. Use the returned values to call `RegisterDomain`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       String location = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       String domainName = "domainName-1244085905";
       RetrieveRegisterParametersResponse response =
           domainsClient.retrieveRegisterParameters(location, domainName);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`location` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The location. Must be in the format `projects/*/locations/*`.  
`domainName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The domain name. Unicode domain names must be expressed in Punycode format.  
**Returns**  
---  
**Type** | **Description**  
`[RetrieveRegisterParametersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RetrieveRegisterParametersResponse)` |   
  
### retrieveRegisterParametersCallable()
    
    
    public final UnaryCallable<RetrieveRegisterParametersRequest,RetrieveRegisterParametersResponse> retrieveRegisterParametersCallable()

Gets parameters needed to register a new domain name, including price and up-to-date availability. Use the returned values to call `RegisterDomain`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       RetrieveRegisterParametersRequest request =
           RetrieveRegisterParametersRequest.newBuilder()
               .setDomainName("domainName-1244085905")
               .setLocation(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .build();
       ApiFuture<RetrieveRegisterParametersResponse> future =
           domainsClient.retrieveRegisterParametersCallable().futureCall(request);
       // Do something.
       RetrieveRegisterParametersResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RetrieveRegisterParametersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RetrieveRegisterParametersRequest),[RetrieveRegisterParametersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RetrieveRegisterParametersResponse)>` |   
  
### retrieveTransferParameters(@Nullable LocationName location, String domainName)
    
    
    public final RetrieveTransferParametersResponse retrieveTransferParameters(@Nullable LocationName location, String domainName)

Gets parameters needed to transfer a domain name from another registrar to Cloud Domains. For domains managed by Google Domains, transferring to Cloud Domains is not supported.

Use the returned values to call `TransferDomain`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       LocationName location = LocationName.of("[PROJECT]", "[LOCATION]");
       String domainName = "domainName-1244085905";
       RetrieveTransferParametersResponse response =
           domainsClient.retrieveTransferParameters(location, domainName);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`location` | `@org.jspecify.annotations.Nullable com.google.cloud.domains.v1beta1.LocationName`  
Required. The location. Must be in the format `projects/*/locations/*`.  
`domainName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The domain name. Unicode domain names must be expressed in Punycode format.  
**Returns**  
---  
**Type** | **Description**  
`[RetrieveTransferParametersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RetrieveTransferParametersResponse)` |   
  
### retrieveTransferParameters(RetrieveTransferParametersRequest request)
    
    
    public final RetrieveTransferParametersResponse retrieveTransferParameters(RetrieveTransferParametersRequest request)

Gets parameters needed to transfer a domain name from another registrar to Cloud Domains. For domains managed by Google Domains, transferring to Cloud Domains is not supported.

Use the returned values to call `TransferDomain`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       RetrieveTransferParametersRequest request =
           RetrieveTransferParametersRequest.newBuilder()
               .setDomainName("domainName-1244085905")
               .setLocation(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .build();
       RetrieveTransferParametersResponse response =
           domainsClient.retrieveTransferParameters(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RetrieveTransferParametersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RetrieveTransferParametersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RetrieveTransferParametersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RetrieveTransferParametersResponse)` |   
  
### retrieveTransferParameters(String location, String domainName)
    
    
    public final RetrieveTransferParametersResponse retrieveTransferParameters(String location, String domainName)

Gets parameters needed to transfer a domain name from another registrar to Cloud Domains. For domains managed by Google Domains, transferring to Cloud Domains is not supported.

Use the returned values to call `TransferDomain`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       String location = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       String domainName = "domainName-1244085905";
       RetrieveTransferParametersResponse response =
           domainsClient.retrieveTransferParameters(location, domainName);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`location` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The location. Must be in the format `projects/*/locations/*`.  
`domainName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The domain name. Unicode domain names must be expressed in Punycode format.  
**Returns**  
---  
**Type** | **Description**  
`[RetrieveTransferParametersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RetrieveTransferParametersResponse)` |   
  
### retrieveTransferParametersCallable()
    
    
    public final UnaryCallable<RetrieveTransferParametersRequest,RetrieveTransferParametersResponse> retrieveTransferParametersCallable()

Gets parameters needed to transfer a domain name from another registrar to Cloud Domains. For domains managed by Google Domains, transferring to Cloud Domains is not supported.

Use the returned values to call `TransferDomain`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       RetrieveTransferParametersRequest request =
           RetrieveTransferParametersRequest.newBuilder()
               .setDomainName("domainName-1244085905")
               .setLocation(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .build();
       ApiFuture<RetrieveTransferParametersResponse> future =
           domainsClient.retrieveTransferParametersCallable().futureCall(request);
       // Do something.
       RetrieveTransferParametersResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RetrieveTransferParametersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RetrieveTransferParametersRequest),[RetrieveTransferParametersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RetrieveTransferParametersResponse)>` |   
  
### searchDomains(@Nullable LocationName location, String query)
    
    
    public final SearchDomainsResponse searchDomains(@Nullable LocationName location, String query)

Searches for available domain names similar to the provided query.

Availability results from this method are approximate; call `RetrieveRegisterParameters` on a domain before registering to confirm availability.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       LocationName location = LocationName.of("[PROJECT]", "[LOCATION]");
       String query = "query107944136";
       SearchDomainsResponse response = domainsClient.searchDomains(location, query);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`location` | `@org.jspecify.annotations.Nullable com.google.cloud.domains.v1beta1.LocationName`  
Required. The location. Must be in the format `projects/*/locations/*`.  
`query` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. String used to search for available domain names.  
**Returns**  
---  
**Type** | **Description**  
`[SearchDomainsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.SearchDomainsResponse)` |   
  
### searchDomains(SearchDomainsRequest request)
    
    
    public final SearchDomainsResponse searchDomains(SearchDomainsRequest request)

Searches for available domain names similar to the provided query.

Availability results from this method are approximate; call `RetrieveRegisterParameters` on a domain before registering to confirm availability.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       SearchDomainsRequest request =
           SearchDomainsRequest.newBuilder()
               .setQuery("query107944136")
               .setLocation(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .build();
       SearchDomainsResponse response = domainsClient.searchDomains(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SearchDomainsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.SearchDomainsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SearchDomainsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.SearchDomainsResponse)` |   
  
### searchDomains(String location, String query)
    
    
    public final SearchDomainsResponse searchDomains(String location, String query)

Searches for available domain names similar to the provided query.

Availability results from this method are approximate; call `RetrieveRegisterParameters` on a domain before registering to confirm availability.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       String location = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       String query = "query107944136";
       SearchDomainsResponse response = domainsClient.searchDomains(location, query);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`location` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The location. Must be in the format `projects/*/locations/*`.  
`query` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. String used to search for available domain names.  
**Returns**  
---  
**Type** | **Description**  
`[SearchDomainsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.SearchDomainsResponse)` |   
  
### searchDomainsCallable()
    
    
    public final UnaryCallable<SearchDomainsRequest,SearchDomainsResponse> searchDomainsCallable()

Searches for available domain names similar to the provided query.

Availability results from this method are approximate; call `RetrieveRegisterParameters` on a domain before registering to confirm availability.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       SearchDomainsRequest request =
           SearchDomainsRequest.newBuilder()
               .setQuery("query107944136")
               .setLocation(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .build();
       ApiFuture<SearchDomainsResponse> future =
           domainsClient.searchDomainsCallable().futureCall(request);
       // Do something.
       SearchDomainsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchDomainsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.SearchDomainsRequest),[SearchDomainsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.SearchDomainsResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### transferDomainAsync(@Nullable LocationName parent, Registration registration, Money yearlyPrice, AuthorizationCode authorizationCode)
    
    
    public final OperationFuture<Registration,OperationMetadata> transferDomainAsync(@Nullable LocationName parent, Registration registration, Money yearlyPrice, AuthorizationCode authorizationCode)

Transfers a domain name from another registrar to Cloud Domains. For domains managed by Google Domains, transferring to Cloud Domains is not supported.

Before calling this method, go to the domain's current registrar to unlock the domain for transfer and retrieve the domain's transfer authorization code. Then call `RetrieveTransferParameters` to confirm that the domain is unlocked and to get values needed to build a call to this method.

A successful call creates a `Registration` resource in state `TRANSFER_PENDING`. It can take several days to complete the transfer process. The registrant can often speed up this process by approving the transfer through the current registrar, either by clicking a link in an email from the registrar or by visiting the registrar's website.

A few minutes after transfer approval, the resource transitions to state `ACTIVE`, indicating that the transfer was successful. If the transfer is rejected or the request expires without being approved, the resource can end up in state `TRANSFER_FAILED`. If transfer fails, you can safely delete the resource and retry the transfer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Registration registration = Registration.newBuilder().build();
       Money yearlyPrice = Money.newBuilder().build();
       AuthorizationCode authorizationCode = AuthorizationCode.newBuilder().build();
       Registration response =
           domainsClient
               .transferDomainAsync(parent, registration, yearlyPrice, authorizationCode)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.domains.v1beta1.LocationName`  
Required. The parent resource of the `Registration`. Must be in the format `projects/*/locations/*`.  
`registration` | `[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration)`  
Required. The complete `Registration` resource to be created. You can leave `registration.dns_settings` unset to import the domain's current DNS configuration from its current registrar. Use this option only if you are sure that the domain's current DNS service does not cease upon transfer, as is often the case for DNS services provided for free by the registrar.  
`yearlyPrice` | `com.google.type.Money`  
Required. Acknowledgement of the price to transfer or renew the domain for one year. Call `RetrieveTransferParameters` to obtain the price, which you must acknowledge.  
`authorizationCode` | `[AuthorizationCode](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.AuthorizationCode)`  
The domain's transfer authorization code. You can obtain this from the domain's current registrar.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.OperationMetadata)>` |   
  
### transferDomainAsync(TransferDomainRequest request)
    
    
    public final OperationFuture<Registration,OperationMetadata> transferDomainAsync(TransferDomainRequest request)

Transfers a domain name from another registrar to Cloud Domains. For domains managed by Google Domains, transferring to Cloud Domains is not supported.

Before calling this method, go to the domain's current registrar to unlock the domain for transfer and retrieve the domain's transfer authorization code. Then call `RetrieveTransferParameters` to confirm that the domain is unlocked and to get values needed to build a call to this method.

A successful call creates a `Registration` resource in state `TRANSFER_PENDING`. It can take several days to complete the transfer process. The registrant can often speed up this process by approving the transfer through the current registrar, either by clicking a link in an email from the registrar or by visiting the registrar's website.

A few minutes after transfer approval, the resource transitions to state `ACTIVE`, indicating that the transfer was successful. If the transfer is rejected or the request expires without being approved, the resource can end up in state `TRANSFER_FAILED`. If transfer fails, you can safely delete the resource and retry the transfer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       TransferDomainRequest request =
           TransferDomainRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setRegistration(Registration.newBuilder().build())
               .addAllContactNotices(new ArrayList<ContactNotice>())
               .setYearlyPrice(Money.newBuilder().build())
               .setAuthorizationCode(AuthorizationCode.newBuilder().build())
               .setValidateOnly(true)
               .build();
       Registration response = domainsClient.transferDomainAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TransferDomainRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.TransferDomainRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.OperationMetadata)>` |   
  
### transferDomainAsync(String parent, Registration registration, Money yearlyPrice, AuthorizationCode authorizationCode)
    
    
    public final OperationFuture<Registration,OperationMetadata> transferDomainAsync(String parent, Registration registration, Money yearlyPrice, AuthorizationCode authorizationCode)

Transfers a domain name from another registrar to Cloud Domains. For domains managed by Google Domains, transferring to Cloud Domains is not supported.

Before calling this method, go to the domain's current registrar to unlock the domain for transfer and retrieve the domain's transfer authorization code. Then call `RetrieveTransferParameters` to confirm that the domain is unlocked and to get values needed to build a call to this method.

A successful call creates a `Registration` resource in state `TRANSFER_PENDING`. It can take several days to complete the transfer process. The registrant can often speed up this process by approving the transfer through the current registrar, either by clicking a link in an email from the registrar or by visiting the registrar's website.

A few minutes after transfer approval, the resource transitions to state `ACTIVE`, indicating that the transfer was successful. If the transfer is rejected or the request expires without being approved, the resource can end up in state `TRANSFER_FAILED`. If transfer fails, you can safely delete the resource and retry the transfer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Registration registration = Registration.newBuilder().build();
       Money yearlyPrice = Money.newBuilder().build();
       AuthorizationCode authorizationCode = AuthorizationCode.newBuilder().build();
       Registration response =
           domainsClient
               .transferDomainAsync(parent, registration, yearlyPrice, authorizationCode)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource of the `Registration`. Must be in the format `projects/*/locations/*`.  
`registration` | `[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration)`  
Required. The complete `Registration` resource to be created. You can leave `registration.dns_settings` unset to import the domain's current DNS configuration from its current registrar. Use this option only if you are sure that the domain's current DNS service does not cease upon transfer, as is often the case for DNS services provided for free by the registrar.  
`yearlyPrice` | `com.google.type.Money`  
Required. Acknowledgement of the price to transfer or renew the domain for one year. Call `RetrieveTransferParameters` to obtain the price, which you must acknowledge.  
`authorizationCode` | `[AuthorizationCode](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.AuthorizationCode)`  
The domain's transfer authorization code. You can obtain this from the domain's current registrar.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.OperationMetadata)>` |   
  
### transferDomainCallable()
    
    
    public final UnaryCallable<TransferDomainRequest,Operation> transferDomainCallable()

Transfers a domain name from another registrar to Cloud Domains. For domains managed by Google Domains, transferring to Cloud Domains is not supported.

Before calling this method, go to the domain's current registrar to unlock the domain for transfer and retrieve the domain's transfer authorization code. Then call `RetrieveTransferParameters` to confirm that the domain is unlocked and to get values needed to build a call to this method.

A successful call creates a `Registration` resource in state `TRANSFER_PENDING`. It can take several days to complete the transfer process. The registrant can often speed up this process by approving the transfer through the current registrar, either by clicking a link in an email from the registrar or by visiting the registrar's website.

A few minutes after transfer approval, the resource transitions to state `ACTIVE`, indicating that the transfer was successful. If the transfer is rejected or the request expires without being approved, the resource can end up in state `TRANSFER_FAILED`. If transfer fails, you can safely delete the resource and retry the transfer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       TransferDomainRequest request =
           TransferDomainRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setRegistration(Registration.newBuilder().build())
               .addAllContactNotices(new ArrayList<ContactNotice>())
               .setYearlyPrice(Money.newBuilder().build())
               .setAuthorizationCode(AuthorizationCode.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future = domainsClient.transferDomainCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TransferDomainRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.TransferDomainRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### transferDomainOperationCallable()
    
    
    public final OperationCallable<TransferDomainRequest,Registration,OperationMetadata> transferDomainOperationCallable()

Transfers a domain name from another registrar to Cloud Domains. For domains managed by Google Domains, transferring to Cloud Domains is not supported.

Before calling this method, go to the domain's current registrar to unlock the domain for transfer and retrieve the domain's transfer authorization code. Then call `RetrieveTransferParameters` to confirm that the domain is unlocked and to get values needed to build a call to this method.

A successful call creates a `Registration` resource in state `TRANSFER_PENDING`. It can take several days to complete the transfer process. The registrant can often speed up this process by approving the transfer through the current registrar, either by clicking a link in an email from the registrar or by visiting the registrar's website.

A few minutes after transfer approval, the resource transitions to state `ACTIVE`, indicating that the transfer was successful. If the transfer is rejected or the request expires without being approved, the resource can end up in state `TRANSFER_FAILED`. If transfer fails, you can safely delete the resource and retry the transfer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       TransferDomainRequest request =
           TransferDomainRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setRegistration(Registration.newBuilder().build())
               .addAllContactNotices(new ArrayList<ContactNotice>())
               .setYearlyPrice(Money.newBuilder().build())
               .setAuthorizationCode(AuthorizationCode.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<Registration, OperationMetadata> future =
           domainsClient.transferDomainOperationCallable().futureCall(request);
       // Do something.
       Registration response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[TransferDomainRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.TransferDomainRequest),[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.OperationMetadata)>` |   
  
### updateRegistrationAsync(Registration registration, FieldMask updateMask)
    
    
    public final OperationFuture<Registration,OperationMetadata> updateRegistrationAsync(Registration registration, FieldMask updateMask)

Updates select fields of a `Registration` resource, notably `labels`. To update other fields, use the appropriate custom update method:

  * To update management settings, see `ConfigureManagementSettings`
  * To update DNS configuration, see `ConfigureDnsSettings`
  * To update contact information, see `ConfigureContactSettings`



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       Registration registration = Registration.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Registration response = domainsClient.updateRegistrationAsync(registration, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`registration` | `[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration)`  
Fields of the `Registration` to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The field mask describing which fields to update as a comma-separated list. For example, if only the labels are being updated, the `update_mask` is `"labels"`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.OperationMetadata)>` |   
  
### updateRegistrationAsync(UpdateRegistrationRequest request)
    
    
    public final OperationFuture<Registration,OperationMetadata> updateRegistrationAsync(UpdateRegistrationRequest request)

Updates select fields of a `Registration` resource, notably `labels`. To update other fields, use the appropriate custom update method:

  * To update management settings, see `ConfigureManagementSettings`
  * To update DNS configuration, see `ConfigureDnsSettings`
  * To update contact information, see `ConfigureContactSettings`



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       UpdateRegistrationRequest request =
           UpdateRegistrationRequest.newBuilder()
               .setRegistration(Registration.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Registration response = domainsClient.updateRegistrationAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateRegistrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.UpdateRegistrationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.OperationMetadata)>` |   
  
### updateRegistrationCallable()
    
    
    public final UnaryCallable<UpdateRegistrationRequest,Operation> updateRegistrationCallable()

Updates select fields of a `Registration` resource, notably `labels`. To update other fields, use the appropriate custom update method:

  * To update management settings, see `ConfigureManagementSettings`
  * To update DNS configuration, see `ConfigureDnsSettings`
  * To update contact information, see `ConfigureContactSettings`



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       UpdateRegistrationRequest request =
           UpdateRegistrationRequest.newBuilder()
               .setRegistration(Registration.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Operation> future = domainsClient.updateRegistrationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateRegistrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.UpdateRegistrationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateRegistrationOperationCallable()
    
    
    public final OperationCallable<UpdateRegistrationRequest,Registration,OperationMetadata> updateRegistrationOperationCallable()

Updates select fields of a `Registration` resource, notably `labels`. To update other fields, use the appropriate custom update method:

  * To update management settings, see `ConfigureManagementSettings`
  * To update DNS configuration, see `ConfigureDnsSettings`
  * To update contact information, see `ConfigureContactSettings`



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DomainsClient domainsClient = DomainsClient.create()) {
       UpdateRegistrationRequest request =
           UpdateRegistrationRequest.newBuilder()
               .setRegistration(Registration.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       OperationFuture<Registration, OperationMetadata> future =
           domainsClient.updateRegistrationOperationCallable().futureCall(request);
       // Do something.
       Registration response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateRegistrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.UpdateRegistrationRequest),[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
