---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.ServicesGrpc.AsyncService
title: Interface ServicesGrpc.AsyncService (0.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:26:02.946029+00:00
---

# Interface ServicesGrpc.AsyncService (0.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.ServicesGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ServicesGrpc.AsyncService (0.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.99.0 (latest)  0.95.0  0.94.0  0.93.0  0.91.0  0.88.0  0.87.0  0.85.0  0.83.0  0.82.0  0.80.0  0.78.0  0.76.0  0.75.0  0.74.0  0.73.0  0.72.0  0.70.0  0.68.0  0.67.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.5  0.2.1  0.1.2 
    
    
    public static interface ServicesGrpc.AsyncService

Cloud Run Service Control Plane API

## Methods 

### createService(CreateServiceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createService(CreateServiceRequest request, StreamObserver<Operation> responseObserver)

Creates a new Service in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.CreateServiceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteService(DeleteServiceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteService(DeleteServiceRequest request, StreamObserver<Operation> responseObserver)

Deletes a Service. This will cause the Service to stop serving traffic and will delete all revisions.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.DeleteServiceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### getIamPolicy(GetIamPolicyRequest request, StreamObserver<Policy> responseObserver)
    
    
    public default void getIamPolicy(GetIamPolicyRequest request, StreamObserver<Policy> responseObserver)

Gets the IAM Access Control policy currently in effect for the given Cloud Run Service. This result does not include any inherited policies.

**Parameters**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.GetIamPolicyRequest`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<com.google.iam.v1.Policy>`  
  
  
### getService(GetServiceRequest request, StreamObserver<Service> responseObserver)
    
    
    public default void getService(GetServiceRequest request, StreamObserver<Service> responseObserver)

Gets information about a Service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.GetServiceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Service)>`  
  
  
### listServices(ListServicesRequest request, StreamObserver<ListServicesResponse> responseObserver)
    
    
    public default void listServices(ListServicesRequest request, StreamObserver<ListServicesResponse> responseObserver)

Lists Services. Results are sorted by creation time, descending.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.ListServicesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListServicesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.ListServicesResponse)>`  
  
  
### setIamPolicy(SetIamPolicyRequest request, StreamObserver<Policy> responseObserver)
    
    
    public default void setIamPolicy(SetIamPolicyRequest request, StreamObserver<Policy> responseObserver)

Sets the IAM Access control policy for the specified Service. Overwrites any existing policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.SetIamPolicyRequest`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<com.google.iam.v1.Policy>`  
  
  
### testIamPermissions(TestIamPermissionsRequest request, StreamObserver<TestIamPermissionsResponse> responseObserver)
    
    
    public default void testIamPermissions(TestIamPermissionsRequest request, StreamObserver<TestIamPermissionsResponse> responseObserver)

Returns permissions that a caller has on the specified Project. There are no permissions required for making this API call.

**Parameters**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.TestIamPermissionsRequest`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<com.google.iam.v1.TestIamPermissionsResponse>`  
  
  
### updateService(UpdateServiceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void updateService(UpdateServiceRequest request, StreamObserver<Operation> responseObserver)

Updates a Service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.UpdateServiceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
