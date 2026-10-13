---
url: https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.stub.UserListGlobalLicenseServiceStub
title: Class UserListGlobalLicenseServiceStub (0.20.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:15:46.536706+00:00
---

# Class UserListGlobalLicenseServiceStub (0.20.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.stub.UserListGlobalLicenseServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class UserListGlobalLicenseServiceStub (0.20.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.0 (latest)  0.16.0  0.15.0  0.14.0  0.12.0  0.9.0  0.8.0  0.6.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public abstract class UserListGlobalLicenseServiceStub implements BackgroundResource

Base stub class for the UserListGlobalLicenseService service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > UserListGlobalLicenseServiceStub

## Implements

[BackgroundResource](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.BackgroundResource.html)

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

## Constructors 

### UserListGlobalLicenseServiceStub()
    
    
    public UserListGlobalLicenseServiceStub()

## Methods 

### close()
    
    
    public abstract void close()

### createUserListGlobalLicenseCallable()
    
    
    public UnaryCallable<CreateUserListGlobalLicenseRequest,UserListGlobalLicense> createUserListGlobalLicenseCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateUserListGlobalLicenseRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.CreateUserListGlobalLicenseRequest),[UserListGlobalLicense](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserListGlobalLicense)>` |   
  
### getUserListGlobalLicenseCallable()
    
    
    public UnaryCallable<GetUserListGlobalLicenseRequest,UserListGlobalLicense> getUserListGlobalLicenseCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetUserListGlobalLicenseRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.GetUserListGlobalLicenseRequest),[UserListGlobalLicense](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserListGlobalLicense)>` |   
  
### listUserListGlobalLicenseCustomerInfosCallable()
    
    
    public UnaryCallable<ListUserListGlobalLicenseCustomerInfosRequest,ListUserListGlobalLicenseCustomerInfosResponse> listUserListGlobalLicenseCustomerInfosCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUserListGlobalLicenseCustomerInfosRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.ListUserListGlobalLicenseCustomerInfosRequest),[ListUserListGlobalLicenseCustomerInfosResponse](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.ListUserListGlobalLicenseCustomerInfosResponse)>` |   
  
### listUserListGlobalLicenseCustomerInfosPagedCallable()
    
    
    public UnaryCallable<ListUserListGlobalLicenseCustomerInfosRequest,UserListGlobalLicenseServiceClient.ListUserListGlobalLicenseCustomerInfosPagedResponse> listUserListGlobalLicenseCustomerInfosPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUserListGlobalLicenseCustomerInfosRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.ListUserListGlobalLicenseCustomerInfosRequest),[ListUserListGlobalLicenseCustomerInfosPagedResponse](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserListGlobalLicenseServiceClient.ListUserListGlobalLicenseCustomerInfosPagedResponse)>` |   
  
### listUserListGlobalLicensesCallable()
    
    
    public UnaryCallable<ListUserListGlobalLicensesRequest,ListUserListGlobalLicensesResponse> listUserListGlobalLicensesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUserListGlobalLicensesRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.ListUserListGlobalLicensesRequest),[ListUserListGlobalLicensesResponse](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.ListUserListGlobalLicensesResponse)>` |   
  
### listUserListGlobalLicensesPagedCallable()
    
    
    public UnaryCallable<ListUserListGlobalLicensesRequest,UserListGlobalLicenseServiceClient.ListUserListGlobalLicensesPagedResponse> listUserListGlobalLicensesPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUserListGlobalLicensesRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.ListUserListGlobalLicensesRequest),[ListUserListGlobalLicensesPagedResponse](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserListGlobalLicenseServiceClient.ListUserListGlobalLicensesPagedResponse)>` |   
  
### updateUserListGlobalLicenseCallable()
    
    
    public UnaryCallable<UpdateUserListGlobalLicenseRequest,UserListGlobalLicense> updateUserListGlobalLicenseCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateUserListGlobalLicenseRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UpdateUserListGlobalLicenseRequest),[UserListGlobalLicense](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserListGlobalLicense)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
