---
url: https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserListGlobalLicenseServiceGrpc.AsyncService
title: Interface UserListGlobalLicenseServiceGrpc.AsyncService (0.20.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:03:45.111289+00:00
---

# Interface UserListGlobalLicenseServiceGrpc.AsyncService (0.20.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserListGlobalLicenseServiceGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface UserListGlobalLicenseServiceGrpc.AsyncService (0.20.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.0 (latest)  0.16.0  0.15.0  0.14.0  0.12.0  0.9.0  0.8.0  0.6.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface UserListGlobalLicenseServiceGrpc.AsyncService

Service for managing user list global licenses. Delete is not a supported operation for UserListGlobalLicenses. Callers should update the license status to DISABLED to instead to deactivate a license. This feature is only available to data partners.

## Methods 

### createUserListGlobalLicense(CreateUserListGlobalLicenseRequest request, StreamObserver<UserListGlobalLicense> responseObserver)
    
    
    public default void createUserListGlobalLicense(CreateUserListGlobalLicenseRequest request, StreamObserver<UserListGlobalLicense> responseObserver)

Creates a user list global license. This feature is only available to data partners.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateUserListGlobalLicenseRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.CreateUserListGlobalLicenseRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[UserListGlobalLicense](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserListGlobalLicense)>`  
  
  
### getUserListGlobalLicense(GetUserListGlobalLicenseRequest request, StreamObserver<UserListGlobalLicense> responseObserver)
    
    
    public default void getUserListGlobalLicense(GetUserListGlobalLicenseRequest request, StreamObserver<UserListGlobalLicense> responseObserver)

Retrieves a user list global license. This feature is only available to data partners.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetUserListGlobalLicenseRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.GetUserListGlobalLicenseRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[UserListGlobalLicense](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserListGlobalLicense)>`  
  
  
### listUserListGlobalLicenseCustomerInfos(ListUserListGlobalLicenseCustomerInfosRequest request, StreamObserver<ListUserListGlobalLicenseCustomerInfosResponse> responseObserver)
    
    
    public default void listUserListGlobalLicenseCustomerInfos(ListUserListGlobalLicenseCustomerInfosRequest request, StreamObserver<ListUserListGlobalLicenseCustomerInfosResponse> responseObserver)

Lists all customer info for a user list global license. This feature is only available to data partners.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListUserListGlobalLicenseCustomerInfosRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.ListUserListGlobalLicenseCustomerInfosRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListUserListGlobalLicenseCustomerInfosResponse](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.ListUserListGlobalLicenseCustomerInfosResponse)>`  
  
  
### listUserListGlobalLicenses(ListUserListGlobalLicensesRequest request, StreamObserver<ListUserListGlobalLicensesResponse> responseObserver)
    
    
    public default void listUserListGlobalLicenses(ListUserListGlobalLicensesRequest request, StreamObserver<ListUserListGlobalLicensesResponse> responseObserver)

Lists all user list global licenses owned by the parent account. This feature is only available to data partners.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListUserListGlobalLicensesRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.ListUserListGlobalLicensesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListUserListGlobalLicensesResponse](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.ListUserListGlobalLicensesResponse)>`  
  
  
### updateUserListGlobalLicense(UpdateUserListGlobalLicenseRequest request, StreamObserver<UserListGlobalLicense> responseObserver)
    
    
    public default void updateUserListGlobalLicense(UpdateUserListGlobalLicenseRequest request, StreamObserver<UserListGlobalLicense> responseObserver)

Updates a user list global license. This feature is only available to data partners.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateUserListGlobalLicenseRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UpdateUserListGlobalLicenseRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[UserListGlobalLicense](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserListGlobalLicense)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
