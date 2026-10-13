---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.PolicyTagManagerGrpc.AsyncService
title: Interface PolicyTagManagerGrpc.AsyncService (1.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:15:47.276523+00:00
---

# Interface PolicyTagManagerGrpc.AsyncService (1.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.PolicyTagManagerGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface PolicyTagManagerGrpc.AsyncService (1.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.101.0 (latest)  1.100.0  1.99.0  1.97.0  1.94.0  1.93.0  1.91.0  1.89.0  1.88.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.76.0  1.74.0  1.73.0  1.70.0  1.69.0  1.68.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.60.0  1.59.0  1.58.0  1.57.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.5  1.8.4  1.7.2  1.6.2  1.5.4 
    
    
    public static interface PolicyTagManagerGrpc.AsyncService

Policy Tag Manager API service allows you to manage your policy tags and taxonomies. Policy tags are used to tag BigQuery columns and apply additional access control policies. A taxonomy is a hierarchical grouping of policy tags that classify data along a common axis.

## Methods 

### createPolicyTag(CreatePolicyTagRequest request, StreamObserver<PolicyTag> responseObserver)
    
    
    public default void createPolicyTag(CreatePolicyTagRequest request, StreamObserver<PolicyTag> responseObserver)

Creates a policy tag in a taxonomy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreatePolicyTagRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.CreatePolicyTagRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[PolicyTag](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.PolicyTag)>`  
  
  
### createTaxonomy(CreateTaxonomyRequest request, StreamObserver<Taxonomy> responseObserver)
    
    
    public default void createTaxonomy(CreateTaxonomyRequest request, StreamObserver<Taxonomy> responseObserver)

Creates a taxonomy in a specified project. The taxonomy is initially empty, that is, it doesn't contain policy tags.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTaxonomyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.CreateTaxonomyRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Taxonomy](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Taxonomy)>`  
  
  
### deletePolicyTag(DeletePolicyTagRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deletePolicyTag(DeletePolicyTagRequest request, StreamObserver<Empty> responseObserver)

Deletes a policy tag together with the following:

  * All of its descendant policy tags, if any
  * Policies associated with the policy tag and its descendants
  * References from BigQuery table schema of the policy tag and its descendants



**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeletePolicyTagRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.DeletePolicyTagRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### deleteTaxonomy(DeleteTaxonomyRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteTaxonomy(DeleteTaxonomyRequest request, StreamObserver<Empty> responseObserver)

Deletes a taxonomy, including all policy tags in this taxonomy, their associated policies, and the policy tags references from BigQuery columns.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTaxonomyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.DeleteTaxonomyRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### getIamPolicy(GetIamPolicyRequest request, StreamObserver<Policy> responseObserver)
    
    
    public default void getIamPolicy(GetIamPolicyRequest request, StreamObserver<Policy> responseObserver)

Gets the IAM policy for a policy tag or a taxonomy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.GetIamPolicyRequest`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<com.google.iam.v1.Policy>`  
  
  
### getPolicyTag(GetPolicyTagRequest request, StreamObserver<PolicyTag> responseObserver)
    
    
    public default void getPolicyTag(GetPolicyTagRequest request, StreamObserver<PolicyTag> responseObserver)

Gets a policy tag.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPolicyTagRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.GetPolicyTagRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[PolicyTag](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.PolicyTag)>`  
  
  
### getTaxonomy(GetTaxonomyRequest request, StreamObserver<Taxonomy> responseObserver)
    
    
    public default void getTaxonomy(GetTaxonomyRequest request, StreamObserver<Taxonomy> responseObserver)

Gets a taxonomy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTaxonomyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.GetTaxonomyRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Taxonomy](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Taxonomy)>`  
  
  
### listPolicyTags(ListPolicyTagsRequest request, StreamObserver<ListPolicyTagsResponse> responseObserver)
    
    
    public default void listPolicyTags(ListPolicyTagsRequest request, StreamObserver<ListPolicyTagsResponse> responseObserver)

Lists all policy tags in a taxonomy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPolicyTagsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ListPolicyTagsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListPolicyTagsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ListPolicyTagsResponse)>`  
  
  
### listTaxonomies(ListTaxonomiesRequest request, StreamObserver<ListTaxonomiesResponse> responseObserver)
    
    
    public default void listTaxonomies(ListTaxonomiesRequest request, StreamObserver<ListTaxonomiesResponse> responseObserver)

Lists all taxonomies in a project in a particular location that you have a permission to view.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTaxonomiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ListTaxonomiesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListTaxonomiesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ListTaxonomiesResponse)>`  
  
  
### setIamPolicy(SetIamPolicyRequest request, StreamObserver<Policy> responseObserver)
    
    
    public default void setIamPolicy(SetIamPolicyRequest request, StreamObserver<Policy> responseObserver)

Sets the IAM policy for a policy tag or a taxonomy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.SetIamPolicyRequest`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<com.google.iam.v1.Policy>`  
  
  
### testIamPermissions(TestIamPermissionsRequest request, StreamObserver<TestIamPermissionsResponse> responseObserver)
    
    
    public default void testIamPermissions(TestIamPermissionsRequest request, StreamObserver<TestIamPermissionsResponse> responseObserver)

Returns your permissions on a specified policy tag or taxonomy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.TestIamPermissionsRequest`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<com.google.iam.v1.TestIamPermissionsResponse>`  
  
  
### updatePolicyTag(UpdatePolicyTagRequest request, StreamObserver<PolicyTag> responseObserver)
    
    
    public default void updatePolicyTag(UpdatePolicyTagRequest request, StreamObserver<PolicyTag> responseObserver)

Updates a policy tag, including its display name, description, and parent policy tag.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdatePolicyTagRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.UpdatePolicyTagRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[PolicyTag](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.PolicyTag)>`  
  
  
### updateTaxonomy(UpdateTaxonomyRequest request, StreamObserver<Taxonomy> responseObserver)
    
    
    public default void updateTaxonomy(UpdateTaxonomyRequest request, StreamObserver<Taxonomy> responseObserver)

Updates a taxonomy, including its display name, description, and activated policy types.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateTaxonomyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.UpdateTaxonomyRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Taxonomy](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Taxonomy)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
