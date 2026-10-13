---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DomainsGrpc.DomainsFutureStub
title: Class DomainsGrpc.DomainsFutureStub (1.96.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:15:57.293722+00:00
---

# Class DomainsGrpc.DomainsFutureStub (1.96.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DomainsGrpc.DomainsFutureStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DomainsGrpc.DomainsFutureStub (1.96.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.96.0 (latest)  1.92.0  1.91.0  1.90.0  1.88.0  1.85.0  1.84.0  1.82.0  1.80.0  1.79.0  1.78.0  1.77.0  1.75.0  1.73.0  1.72.0  1.71.0  1.70.0  1.69.0  1.67.0  1.65.0  1.64.0  1.61.0  1.60.0  1.59.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.6  0.7.0  0.6.1  0.5.4 
    
    
    public static final class DomainsGrpc.DomainsFutureStub extends AbstractFutureStub<DomainsGrpc.DomainsFutureStub>

A stub to allow clients to do ListenableFuture-style rpc calls to service Domains.

The Cloud Domains API enables management and configuration of domain names.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractFutureStub > DomainsGrpc.DomainsFutureStub

## Inherited Members

io.grpc.stub.AbstractFutureStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractFutureStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.<T>withOption(io.grpc.CallOptions.Key<T>,T)

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.getCallOptions()

io.grpc.stub.AbstractStub.getChannel()

io.grpc.stub.AbstractStub.withCallCredentials(io.grpc.CallCredentials)

io.grpc.stub.AbstractStub.withChannel(io.grpc.Channel)

io.grpc.stub.AbstractStub.withCompression(java.lang.String)

io.grpc.stub.AbstractStub.withDeadline(io.grpc.Deadline)

io.grpc.stub.AbstractStub.withDeadlineAfter(java.time.Duration)

io.grpc.stub.AbstractStub.withDeadlineAfter(long,java.util.concurrent.TimeUnit)

io.grpc.stub.AbstractStub.withExecutor(java.util.concurrent.Executor)

io.grpc.stub.AbstractStub.withInterceptors(io.grpc.ClientInterceptor...)

io.grpc.stub.AbstractStub.withMaxInboundMessageSize(int)

io.grpc.stub.AbstractStub.withMaxOutboundMessageSize(int)

io.grpc.stub.AbstractStub.withOnReadyThreshold(int)

io.grpc.stub.AbstractStub.withWaitForReady()

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

## Methods 

### build(Channel channel, CallOptions callOptions)
    
    
    protected DomainsGrpc.DomainsFutureStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[DomainsGrpc.DomainsFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DomainsGrpc.DomainsFutureStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### configureContactSettings(ConfigureContactSettingsRequest request)
    
    
    public ListenableFuture<Operation> configureContactSettings(ConfigureContactSettingsRequest request)

Updates a `Registration`'s contact settings. Some changes require confirmation by the domain's registrant contact .

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ConfigureContactSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ConfigureContactSettingsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### configureDnsSettings(ConfigureDnsSettingsRequest request)
    
    
    public ListenableFuture<Operation> configureDnsSettings(ConfigureDnsSettingsRequest request)

Updates a `Registration`'s DNS settings.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ConfigureDnsSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ConfigureDnsSettingsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### configureManagementSettings(ConfigureManagementSettingsRequest request)
    
    
    public ListenableFuture<Operation> configureManagementSettings(ConfigureManagementSettingsRequest request)

Updates a `Registration`'s management settings.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ConfigureManagementSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ConfigureManagementSettingsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteRegistration(DeleteRegistrationRequest request)
    
    
    public ListenableFuture<Operation> deleteRegistration(DeleteRegistrationRequest request)

Deletes a `Registration` resource. This method works on any `Registration` resource using [Subscription or Commitment billing](https://docs.cloud.google.com/domains/pricing#billing-models), provided that the resource was created at least 1 day in the past. For `Registration` resources using [Monthly billing](https://docs.cloud.google.com/domains/pricing#billing-models), this method works if:

  * `state` is `EXPORTED` with `expire_time` in the past
  * `state` is `REGISTRATION_FAILED`
  * `state` is `TRANSFER_FAILED` When an active registration is successfully deleted, you can continue to use the domain in [Google Domains](https://domains.google/) until it expires. The calling user becomes the domain's sole owner in Google Domains, and permissions for the domain are subsequently managed there. The domain does not renew automatically unless the new owner sets up billing in Google Domains.



**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRegistrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DeleteRegistrationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### exportRegistration(ExportRegistrationRequest request)
    
    
    public ListenableFuture<Operation> exportRegistration(ExportRegistrationRequest request)

Exports a `Registration` resource, such that it is no longer managed by Cloud Domains. When an active domain is successfully exported, you can continue to use the domain in [Google Domains](https://domains.google/) until it expires. The calling user becomes the domain's sole owner in Google Domains, and permissions for the domain are subsequently managed there. The domain does not renew automatically unless the new owner sets up billing in Google Domains.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportRegistrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ExportRegistrationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getRegistration(GetRegistrationRequest request)
    
    
    public ListenableFuture<Registration> getRegistration(GetRegistrationRequest request)

Gets the details of a `Registration` resource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRegistrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.GetRegistrationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration)>` |   
  
### listRegistrations(ListRegistrationsRequest request)
    
    
    public ListenableFuture<ListRegistrationsResponse> listRegistrations(ListRegistrationsRequest request)

Lists the `Registration` resources in a project.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRegistrationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ListRegistrationsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListRegistrationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ListRegistrationsResponse)>` |   
  
### registerDomain(RegisterDomainRequest request)
    
    
    public ListenableFuture<Operation> registerDomain(RegisterDomainRequest request)

Registers a new domain name and creates a corresponding `Registration` resource. Call `RetrieveRegisterParameters` first to check availability of the domain name and determine parameters like price that are needed to build a call to this method. A successful call creates a `Registration` resource in state `REGISTRATION_PENDING`, which resolves to `ACTIVE` within 1-2 minutes, indicating that the domain was successfully registered. If the resource ends up in state `REGISTRATION_FAILED`, it indicates that the domain was not registered successfully, and you can safely delete the resource and retry registration.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RegisterDomainRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RegisterDomainRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### resetAuthorizationCode(ResetAuthorizationCodeRequest request)
    
    
    public ListenableFuture<AuthorizationCode> resetAuthorizationCode(ResetAuthorizationCodeRequest request)

Resets the authorization code of the `Registration` to a new random string. You can call this method only after 60 days have elapsed since the initial domain registration.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ResetAuthorizationCodeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ResetAuthorizationCodeRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[AuthorizationCode](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.AuthorizationCode)>` |   
  
### retrieveAuthorizationCode(RetrieveAuthorizationCodeRequest request)
    
    
    public ListenableFuture<AuthorizationCode> retrieveAuthorizationCode(RetrieveAuthorizationCodeRequest request)

Gets the authorization code of the `Registration` for the purpose of transferring the domain to another registrar. You can call this method only after 60 days have elapsed since the initial domain registration.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RetrieveAuthorizationCodeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RetrieveAuthorizationCodeRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[AuthorizationCode](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.AuthorizationCode)>` |   
  
### retrieveRegisterParameters(RetrieveRegisterParametersRequest request)
    
    
    public ListenableFuture<RetrieveRegisterParametersResponse> retrieveRegisterParameters(RetrieveRegisterParametersRequest request)

Gets parameters needed to register a new domain name, including price and up-to-date availability. Use the returned values to call `RegisterDomain`.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RetrieveRegisterParametersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RetrieveRegisterParametersRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[RetrieveRegisterParametersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RetrieveRegisterParametersResponse)>` |   
  
### retrieveTransferParameters(RetrieveTransferParametersRequest request)
    
    
    public ListenableFuture<RetrieveTransferParametersResponse> retrieveTransferParameters(RetrieveTransferParametersRequest request)

Gets parameters needed to transfer a domain name from another registrar to Cloud Domains. For domains managed by Google Domains, transferring to Cloud Domains is not supported. Use the returned values to call `TransferDomain`.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RetrieveTransferParametersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RetrieveTransferParametersRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[RetrieveTransferParametersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RetrieveTransferParametersResponse)>` |   
  
### searchDomains(SearchDomainsRequest request)
    
    
    public ListenableFuture<SearchDomainsResponse> searchDomains(SearchDomainsRequest request)

Searches for available domain names similar to the provided query. Availability results from this method are approximate; call `RetrieveRegisterParameters` on a domain before registering to confirm availability.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SearchDomainsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.SearchDomainsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[SearchDomainsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.SearchDomainsResponse)>` |   
  
### transferDomain(TransferDomainRequest request)
    
    
    public ListenableFuture<Operation> transferDomain(TransferDomainRequest request)

Transfers a domain name from another registrar to Cloud Domains. For domains managed by Google Domains, transferring to Cloud Domains is not supported. Before calling this method, go to the domain's current registrar to unlock the domain for transfer and retrieve the domain's transfer authorization code. Then call `RetrieveTransferParameters` to confirm that the domain is unlocked and to get values needed to build a call to this method. A successful call creates a `Registration` resource in state `TRANSFER_PENDING`. It can take several days to complete the transfer process. The registrant can often speed up this process by approving the transfer through the current registrar, either by clicking a link in an email from the registrar or by visiting the registrar's website. A few minutes after transfer approval, the resource transitions to state `ACTIVE`, indicating that the transfer was successful. If the transfer is rejected or the request expires without being approved, the resource can end up in state `TRANSFER_FAILED`. If transfer fails, you can safely delete the resource and retry the transfer.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TransferDomainRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.TransferDomainRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateRegistration(UpdateRegistrationRequest request)
    
    
    public ListenableFuture<Operation> updateRegistration(UpdateRegistrationRequest request)

Updates select fields of a `Registration` resource, notably `labels`. To update other fields, use the appropriate custom update method:

  * To update management settings, see `ConfigureManagementSettings`
  * To update DNS configuration, see `ConfigureDnsSettings`
  * To update contact information, see `ConfigureContactSettings`



**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateRegistrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.UpdateRegistrationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
