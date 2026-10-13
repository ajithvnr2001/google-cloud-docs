---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.HsmManagementGrpc.AsyncService
title: Interface HsmManagementGrpc.AsyncService (2.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:06:46.852046+00:00
---

# Interface HsmManagementGrpc.AsyncService (2.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.HsmManagementGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface HsmManagementGrpc.AsyncService (2.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.102.0 (latest)  2.98.0  2.97.0  2.96.0  2.94.0  2.91.0  2.90.0  2.88.0  2.86.0  2.85.0  2.84.0  2.83.0  2.81.0  2.79.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.67.0  2.66.0  2.65.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.8  2.5.3  2.4.4  2.3.1 
    
    
    public static interface HsmManagementGrpc.AsyncService

Google Cloud HSM Management Service Provides interfaces for managing HSM instances. Implements a REST model with the following objects:

  * SingleTenantHsmInstance
  * SingleTenantHsmInstanceProposal



## Methods 

### approveSingleTenantHsmInstanceProposal(ApproveSingleTenantHsmInstanceProposalRequest request, StreamObserver<ApproveSingleTenantHsmInstanceProposalResponse> responseObserver)
    
    
    public default void approveSingleTenantHsmInstanceProposal(ApproveSingleTenantHsmInstanceProposalRequest request, StreamObserver<ApproveSingleTenantHsmInstanceProposalResponse> responseObserver)

Approves a SingleTenantHsmInstanceProposal for a given SingleTenantHsmInstance. The proposal must be in the PENDING state.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ApproveSingleTenantHsmInstanceProposalRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ApproveSingleTenantHsmInstanceProposalRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ApproveSingleTenantHsmInstanceProposalResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ApproveSingleTenantHsmInstanceProposalResponse)>`  
  
  
### createSingleTenantHsmInstance(CreateSingleTenantHsmInstanceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createSingleTenantHsmInstance(CreateSingleTenantHsmInstanceRequest request, StreamObserver<Operation> responseObserver)

Creates a new SingleTenantHsmInstance in a given Project and Location. User must create a RegisterTwoFactorAuthKeys proposal with this single-tenant HSM instance to finish setup of the instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSingleTenantHsmInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CreateSingleTenantHsmInstanceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createSingleTenantHsmInstanceProposal(CreateSingleTenantHsmInstanceProposalRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createSingleTenantHsmInstanceProposal(CreateSingleTenantHsmInstanceProposalRequest request, StreamObserver<Operation> responseObserver)

Creates a new SingleTenantHsmInstanceProposal for a given SingleTenantHsmInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSingleTenantHsmInstanceProposalRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CreateSingleTenantHsmInstanceProposalRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteSingleTenantHsmInstanceProposal(DeleteSingleTenantHsmInstanceProposalRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteSingleTenantHsmInstanceProposal(DeleteSingleTenantHsmInstanceProposalRequest request, StreamObserver<Empty> responseObserver)

Deletes a SingleTenantHsmInstanceProposal.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSingleTenantHsmInstanceProposalRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.DeleteSingleTenantHsmInstanceProposalRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### executeSingleTenantHsmInstanceProposal(ExecuteSingleTenantHsmInstanceProposalRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void executeSingleTenantHsmInstanceProposal(ExecuteSingleTenantHsmInstanceProposalRequest request, StreamObserver<Operation> responseObserver)

Executes a SingleTenantHsmInstanceProposal for a given SingleTenantHsmInstance. The proposal must be in the APPROVED state.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExecuteSingleTenantHsmInstanceProposalRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ExecuteSingleTenantHsmInstanceProposalRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### getSingleTenantHsmInstance(GetSingleTenantHsmInstanceRequest request, StreamObserver<SingleTenantHsmInstance> responseObserver)
    
    
    public default void getSingleTenantHsmInstance(GetSingleTenantHsmInstanceRequest request, StreamObserver<SingleTenantHsmInstance> responseObserver)

Returns metadata for a given SingleTenantHsmInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSingleTenantHsmInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.GetSingleTenantHsmInstanceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SingleTenantHsmInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.SingleTenantHsmInstance)>`  
  
  
### getSingleTenantHsmInstanceProposal(GetSingleTenantHsmInstanceProposalRequest request, StreamObserver<SingleTenantHsmInstanceProposal> responseObserver)
    
    
    public default void getSingleTenantHsmInstanceProposal(GetSingleTenantHsmInstanceProposalRequest request, StreamObserver<SingleTenantHsmInstanceProposal> responseObserver)

Returns metadata for a given SingleTenantHsmInstanceProposal.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSingleTenantHsmInstanceProposalRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.GetSingleTenantHsmInstanceProposalRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SingleTenantHsmInstanceProposal](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.SingleTenantHsmInstanceProposal)>`  
  
  
### listSingleTenantHsmInstanceProposals(ListSingleTenantHsmInstanceProposalsRequest request, StreamObserver<ListSingleTenantHsmInstanceProposalsResponse> responseObserver)
    
    
    public default void listSingleTenantHsmInstanceProposals(ListSingleTenantHsmInstanceProposalsRequest request, StreamObserver<ListSingleTenantHsmInstanceProposalsResponse> responseObserver)

Lists SingleTenantHsmInstanceProposals.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSingleTenantHsmInstanceProposalsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ListSingleTenantHsmInstanceProposalsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListSingleTenantHsmInstanceProposalsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ListSingleTenantHsmInstanceProposalsResponse)>`  
  
  
### listSingleTenantHsmInstances(ListSingleTenantHsmInstancesRequest request, StreamObserver<ListSingleTenantHsmInstancesResponse> responseObserver)
    
    
    public default void listSingleTenantHsmInstances(ListSingleTenantHsmInstancesRequest request, StreamObserver<ListSingleTenantHsmInstancesResponse> responseObserver)

Lists SingleTenantHsmInstances.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSingleTenantHsmInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ListSingleTenantHsmInstancesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListSingleTenantHsmInstancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ListSingleTenantHsmInstancesResponse)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
