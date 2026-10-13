---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1.DomainsGrpc
title: Class DomainsGrpc (1.96.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:53:16.849694+00:00
---

# Class DomainsGrpc (1.96.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1.DomainsGrpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DomainsGrpc (1.96.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.96.0 (latest)  1.92.0  1.91.0  1.90.0  1.88.0  1.85.0  1.84.0  1.82.0  1.80.0  1.79.0  1.78.0  1.77.0  1.75.0  1.73.0  1.72.0  1.71.0  1.70.0  1.69.0  1.67.0  1.65.0  1.64.0  1.61.0  1.60.0  1.59.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.6  0.7.0  0.6.1  0.5.4 
    
    
    public final class DomainsGrpc

The Cloud Domains API enables management and configuration of domain names.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DomainsGrpc

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

### bindService(DomainsGrpc.AsyncService service)
    
    
    public static final ServerServiceDefinition bindService(DomainsGrpc.AsyncService service)

**Parameter**  
---  
**Name** | **Description**  
`service` | `[DomainsGrpc.AsyncService](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1.DomainsGrpc.AsyncService)`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServerServiceDefinition` |   
  
### getConfigureContactSettingsMethod()
    
    
    public static MethodDescriptor<ConfigureContactSettingsRequest,Operation> getConfigureContactSettingsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ConfigureContactSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1.ConfigureContactSettingsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getConfigureDnsSettingsMethod()
    
    
    public static MethodDescriptor<ConfigureDnsSettingsRequest,Operation> getConfigureDnsSettingsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ConfigureDnsSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1.ConfigureDnsSettingsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getConfigureManagementSettingsMethod()
    
    
    public static MethodDescriptor<ConfigureManagementSettingsRequest,Operation> getConfigureManagementSettingsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ConfigureManagementSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1.ConfigureManagementSettingsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getDeleteRegistrationMethod()
    
    
    public static MethodDescriptor<DeleteRegistrationRequest,Operation> getDeleteRegistrationMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteRegistrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1.DeleteRegistrationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getExportRegistrationMethod()
    
    
    public static MethodDescriptor<ExportRegistrationRequest,Operation> getExportRegistrationMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ExportRegistrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1.ExportRegistrationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getGetRegistrationMethod()
    
    
    public static MethodDescriptor<GetRegistrationRequest,Registration> getGetRegistrationMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetRegistrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1.GetRegistrationRequest),[Registration](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1.Registration)>` |   
  
### getListRegistrationsMethod()
    
    
    public static MethodDescriptor<ListRegistrationsRequest,ListRegistrationsResponse> getListRegistrationsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListRegistrationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1.ListRegistrationsRequest),[ListRegistrationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1.ListRegistrationsResponse)>` |   
  
### getRegisterDomainMethod()
    
    
    public static MethodDescriptor<RegisterDomainRequest,Operation> getRegisterDomainMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[RegisterDomainRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1.RegisterDomainRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getResetAuthorizationCodeMethod()
    
    
    public static MethodDescriptor<ResetAuthorizationCodeRequest,AuthorizationCode> getResetAuthorizationCodeMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ResetAuthorizationCodeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1.ResetAuthorizationCodeRequest),[AuthorizationCode](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1.AuthorizationCode)>` |   
  
### getRetrieveAuthorizationCodeMethod()
    
    
    public static MethodDescriptor<RetrieveAuthorizationCodeRequest,AuthorizationCode> getRetrieveAuthorizationCodeMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[RetrieveAuthorizationCodeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1.RetrieveAuthorizationCodeRequest),[AuthorizationCode](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1.AuthorizationCode)>` |   
  
### getRetrieveRegisterParametersMethod()
    
    
    public static MethodDescriptor<RetrieveRegisterParametersRequest,RetrieveRegisterParametersResponse> getRetrieveRegisterParametersMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[RetrieveRegisterParametersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1.RetrieveRegisterParametersRequest),[RetrieveRegisterParametersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1.RetrieveRegisterParametersResponse)>` |   
  
### getRetrieveTransferParametersMethod()
    
    
    public static MethodDescriptor<RetrieveTransferParametersRequest,RetrieveTransferParametersResponse> getRetrieveTransferParametersMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[RetrieveTransferParametersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1.RetrieveTransferParametersRequest),[RetrieveTransferParametersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1.RetrieveTransferParametersResponse)>` |   
  
### getSearchDomainsMethod()
    
    
    public static MethodDescriptor<SearchDomainsRequest,SearchDomainsResponse> getSearchDomainsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[SearchDomainsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1.SearchDomainsRequest),[SearchDomainsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1.SearchDomainsResponse)>` |   
  
### getServiceDescriptor()
    
    
    public static ServiceDescriptor getServiceDescriptor()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServiceDescriptor` |   
  
### getTransferDomainMethod()
    
    
    public static MethodDescriptor<TransferDomainRequest,Operation> getTransferDomainMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[TransferDomainRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1.TransferDomainRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getUpdateRegistrationMethod()
    
    
    public static MethodDescriptor<UpdateRegistrationRequest,Operation> getUpdateRegistrationMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateRegistrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1.UpdateRegistrationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### newBlockingStub(Channel channel)
    
    
    public static DomainsGrpc.DomainsBlockingStub newBlockingStub(Channel channel)

Creates a new blocking-style stub that supports unary and streaming output calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[DomainsGrpc.DomainsBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1.DomainsGrpc.DomainsBlockingStub)` |   
  
### newBlockingV2Stub(Channel channel)
    
    
    public static DomainsGrpc.DomainsBlockingV2Stub newBlockingV2Stub(Channel channel)

Creates a new blocking-style stub that supports all types of calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[DomainsGrpc.DomainsBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1.DomainsGrpc.DomainsBlockingV2Stub)` |   
  
### newFutureStub(Channel channel)
    
    
    public static DomainsGrpc.DomainsFutureStub newFutureStub(Channel channel)

Creates a new ListenableFuture-style stub that supports unary calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[DomainsGrpc.DomainsFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1.DomainsGrpc.DomainsFutureStub)` |   
  
### newStub(Channel channel)
    
    
    public static DomainsGrpc.DomainsStub newStub(Channel channel)

Creates a new async stub that supports all call types for the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[DomainsGrpc.DomainsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1.DomainsGrpc.DomainsStub)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
