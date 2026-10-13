---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.AssuredWorkloadsServiceGrpc.AsyncService
title: Interface AssuredWorkloadsServiceGrpc.AsyncService (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:48:22.487482+00:00
---

# Interface AssuredWorkloadsServiceGrpc.AsyncService (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.AssuredWorkloadsServiceGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AssuredWorkloadsServiceGrpc.AsyncService (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.81.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.1.0  2.0.0  1.1.0  1.0.4  0.9.0  0.8.2 
    
    
    public static interface AssuredWorkloadsServiceGrpc.AsyncService

Service to manage AssuredWorkloads.

## Methods 

### acknowledgeViolation(AcknowledgeViolationRequest request, StreamObserver<AcknowledgeViolationResponse> responseObserver)
    
    
    public default void acknowledgeViolation(AcknowledgeViolationRequest request, StreamObserver<AcknowledgeViolationResponse> responseObserver)

Acknowledges an existing violation. By acknowledging a violation, users acknowledge the existence of a compliance violation in their workload and decide to ignore it due to a valid business justification. Acknowledgement is a permanent operation and it cannot be reverted.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AcknowledgeViolationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.AcknowledgeViolationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AcknowledgeViolationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.AcknowledgeViolationResponse)>`  
  
  
### createWorkload(CreateWorkloadRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createWorkload(CreateWorkloadRequest request, StreamObserver<Operation> responseObserver)

Creates Assured Workload.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateWorkloadRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.CreateWorkloadRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteWorkload(DeleteWorkloadRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteWorkload(DeleteWorkloadRequest request, StreamObserver<Empty> responseObserver)

Deletes the workload. Make sure that workload's direct children are already in a deleted state, otherwise the request will fail with a FAILED_PRECONDITION error.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteWorkloadRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.DeleteWorkloadRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### getViolation(GetViolationRequest request, StreamObserver<Violation> responseObserver)
    
    
    public default void getViolation(GetViolationRequest request, StreamObserver<Violation> responseObserver)

Retrieves Assured Workload Violation based on ID.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetViolationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.GetViolationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Violation](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.Violation)>`  
  
  
### getWorkload(GetWorkloadRequest request, StreamObserver<Workload> responseObserver)
    
    
    public default void getWorkload(GetWorkloadRequest request, StreamObserver<Workload> responseObserver)

Gets Assured Workload associated with a CRM Node

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetWorkloadRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.GetWorkloadRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Workload](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.Workload)>`  
  
  
### listViolations(ListViolationsRequest request, StreamObserver<ListViolationsResponse> responseObserver)
    
    
    public default void listViolations(ListViolationsRequest request, StreamObserver<ListViolationsResponse> responseObserver)

Lists the Violations in the AssuredWorkload Environment. Callers may also choose to read across multiple Workloads as per [AIP-159](https://google.aip.dev/159) by using '-' (the hyphen or dash character) as a wildcard character instead of workload-id in the parent. Format `organizations/{org_id}/locations/{location}/workloads/-`

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListViolationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.ListViolationsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListViolationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.ListViolationsResponse)>`  
  
  
### listWorkloads(ListWorkloadsRequest request, StreamObserver<ListWorkloadsResponse> responseObserver)
    
    
    public default void listWorkloads(ListWorkloadsRequest request, StreamObserver<ListWorkloadsResponse> responseObserver)

Lists Assured Workloads under a CRM Node.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListWorkloadsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.ListWorkloadsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListWorkloadsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.ListWorkloadsResponse)>`  
  
  
### restrictAllowedResources(RestrictAllowedResourcesRequest request, StreamObserver<RestrictAllowedResourcesResponse> responseObserver)
    
    
    public default void restrictAllowedResources(RestrictAllowedResourcesRequest request, StreamObserver<RestrictAllowedResourcesResponse> responseObserver)

Restrict the list of resources allowed in the Workload environment. The current list of allowed products can be found at <https://cloud.google.com/assured-workloads/docs/supported-products> In addition to assuredworkloads.workload.update permission, the user should also have orgpolicy.policy.set permission on the folder resource to use this functionality.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestrictAllowedResourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.RestrictAllowedResourcesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[RestrictAllowedResourcesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.RestrictAllowedResourcesResponse)>`  
  
  
### updateWorkload(UpdateWorkloadRequest request, StreamObserver<Workload> responseObserver)
    
    
    public default void updateWorkload(UpdateWorkloadRequest request, StreamObserver<Workload> responseObserver)

Updates an existing workload. Currently allows updating of workload display_name and labels. For force updates don't set etag field in the Workload. Only one update operation per workload can be in progress.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateWorkloadRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.UpdateWorkloadRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Workload](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.Workload)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
