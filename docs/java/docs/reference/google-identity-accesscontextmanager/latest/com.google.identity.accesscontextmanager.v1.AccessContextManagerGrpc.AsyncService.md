---
url: https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.AccessContextManagerGrpc.AsyncService
title: Interface AccessContextManagerGrpc.AsyncService (1.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:23:24.077692+00:00
---

# Interface AccessContextManagerGrpc.AsyncService (1.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.AccessContextManagerGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AccessContextManagerGrpc.AsyncService (1.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.100.0 (latest)  1.96.0  1.95.0  1.94.0  1.92.0  1.89.0  1.88.0  1.86.0  1.84.0  1.83.0  1.82.0  1.81.0  1.79.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.71.0  1.69.0  1.68.0  1.65.0  1.64.0  1.63.0  1.61.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.5  1.3.1  1.2.10 
    
    
    public static interface AccessContextManagerGrpc.AsyncService

API for setting [access levels] [google.identity.accesscontextmanager.v1.AccessLevel] and [service perimeters] [google.identity.accesscontextmanager.v1.ServicePerimeter] for Google Cloud projects. Each organization has one [access policy] [google.identity.accesscontextmanager.v1.AccessPolicy] that contains the [access levels] [google.identity.accesscontextmanager.v1.AccessLevel] and [service perimeters] [google.identity.accesscontextmanager.v1.ServicePerimeter]. This [access policy] [google.identity.accesscontextmanager.v1.AccessPolicy] is applicable to all resources in the organization. AccessPolicies

## Methods 

### commitServicePerimeters(CommitServicePerimetersRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void commitServicePerimeters(CommitServicePerimetersRequest request, StreamObserver<Operation> responseObserver)

Commits the dry-run specification for all the [service perimeters] [google.identity.accesscontextmanager.v1.ServicePerimeter] in an access policy. A commit operation on a service perimeter involves copying its `spec` field to the `status` field of the service perimeter. Only [service perimeters] [google.identity.accesscontextmanager.v1.ServicePerimeter] with `use_explicit_dry_run_spec` field set to true are affected by a commit operation. The long-running operation from this RPC has a successful status after the dry-run specifications for all the [service perimeters] [google.identity.accesscontextmanager.v1.ServicePerimeter] have been committed. If a commit fails, it causes the long-running operation to return an error response and the entire commit operation is cancelled. When successful, the Operation.response field contains CommitServicePerimetersResponse. The `dry_run` and the `spec` fields are cleared after a successful commit operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CommitServicePerimetersRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.CommitServicePerimetersRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createAccessLevel(CreateAccessLevelRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createAccessLevel(CreateAccessLevelRequest request, StreamObserver<Operation> responseObserver)

Creates an [access level] [google.identity.accesscontextmanager.v1.AccessLevel]. The long-running operation from this RPC has a successful status after the [access level] [google.identity.accesscontextmanager.v1.AccessLevel] propagates to long-lasting storage. If [access levels] [google.identity.accesscontextmanager.v1.AccessLevel] contain errors, an error response is returned for the first error encountered.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAccessLevelRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.CreateAccessLevelRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createAccessPolicy(AccessPolicy request, StreamObserver<Operation> responseObserver)
    
    
    public default void createAccessPolicy(AccessPolicy request, StreamObserver<Operation> responseObserver)

Creates an access policy. This method fails if the organization already has an access policy. The long-running operation has a successful status after the access policy propagates to long-lasting storage. Syntactic and basic semantic errors are returned in `metadata` as a BadRequest proto.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AccessPolicy](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.AccessPolicy)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createGcpUserAccessBinding(CreateGcpUserAccessBindingRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createGcpUserAccessBinding(CreateGcpUserAccessBindingRequest request, StreamObserver<Operation> responseObserver)

Creates a [GcpUserAccessBinding] [google.identity.accesscontextmanager.v1.GcpUserAccessBinding]. If the client specifies a [name] [google.identity.accesscontextmanager.v1.GcpUserAccessBinding.name], the server ignores it. Fails if a resource already exists with the same [group_key] [google.identity.accesscontextmanager.v1.GcpUserAccessBinding.group_key]. Completion of this long-running operation does not necessarily signify that the new binding is deployed onto all affected users, which may take more time.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGcpUserAccessBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.CreateGcpUserAccessBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createServicePerimeter(CreateServicePerimeterRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createServicePerimeter(CreateServicePerimeterRequest request, StreamObserver<Operation> responseObserver)

Creates a [service perimeter] [google.identity.accesscontextmanager.v1.ServicePerimeter]. The long-running operation from this RPC has a successful status after the [service perimeter] [google.identity.accesscontextmanager.v1.ServicePerimeter] propagates to long-lasting storage. If a [service perimeter] [google.identity.accesscontextmanager.v1.ServicePerimeter] contains errors, an error response is returned for the first error encountered.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateServicePerimeterRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.CreateServicePerimeterRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteAccessLevel(DeleteAccessLevelRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteAccessLevel(DeleteAccessLevelRequest request, StreamObserver<Operation> responseObserver)

Deletes an [access level] [google.identity.accesscontextmanager.v1.AccessLevel] based on the resource name. The long-running operation from this RPC has a successful status after the [access level] [google.identity.accesscontextmanager.v1.AccessLevel] has been removed from long-lasting storage.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAccessLevelRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.DeleteAccessLevelRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteAccessPolicy(DeleteAccessPolicyRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteAccessPolicy(DeleteAccessPolicyRequest request, StreamObserver<Operation> responseObserver)

Deletes an [access policy] [google.identity.accesscontextmanager.v1.AccessPolicy] based on the resource name. The long-running operation has a successful status after the [access policy] [google.identity.accesscontextmanager.v1.AccessPolicy] is removed from long-lasting storage.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAccessPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.DeleteAccessPolicyRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteGcpUserAccessBinding(DeleteGcpUserAccessBindingRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteGcpUserAccessBinding(DeleteGcpUserAccessBindingRequest request, StreamObserver<Operation> responseObserver)

Deletes a [GcpUserAccessBinding] [google.identity.accesscontextmanager.v1.GcpUserAccessBinding]. Completion of this long-running operation does not necessarily signify that the binding deletion is deployed onto all affected users, which may take more time.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGcpUserAccessBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.DeleteGcpUserAccessBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteServicePerimeter(DeleteServicePerimeterRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteServicePerimeter(DeleteServicePerimeterRequest request, StreamObserver<Operation> responseObserver)

Deletes a [service perimeter] [google.identity.accesscontextmanager.v1.ServicePerimeter] based on the resource name. The long-running operation from this RPC has a successful status after the [service perimeter] [google.identity.accesscontextmanager.v1.ServicePerimeter] is removed from long-lasting storage.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteServicePerimeterRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.DeleteServicePerimeterRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### getAccessLevel(GetAccessLevelRequest request, StreamObserver<AccessLevel> responseObserver)
    
    
    public default void getAccessLevel(GetAccessLevelRequest request, StreamObserver<AccessLevel> responseObserver)

Gets an [access level] [google.identity.accesscontextmanager.v1.AccessLevel] based on the resource name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAccessLevelRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.GetAccessLevelRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AccessLevel](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.AccessLevel)>`  
  
  
### getAccessPolicy(GetAccessPolicyRequest request, StreamObserver<AccessPolicy> responseObserver)
    
    
    public default void getAccessPolicy(GetAccessPolicyRequest request, StreamObserver<AccessPolicy> responseObserver)

Returns an [access policy] [google.identity.accesscontextmanager.v1.AccessPolicy] based on the name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAccessPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.GetAccessPolicyRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AccessPolicy](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.AccessPolicy)>`  
  
  
### getGcpUserAccessBinding(GetGcpUserAccessBindingRequest request, StreamObserver<GcpUserAccessBinding> responseObserver)
    
    
    public default void getGcpUserAccessBinding(GetGcpUserAccessBindingRequest request, StreamObserver<GcpUserAccessBinding> responseObserver)

Gets the [GcpUserAccessBinding] [google.identity.accesscontextmanager.v1.GcpUserAccessBinding] with the given name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGcpUserAccessBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.GetGcpUserAccessBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[GcpUserAccessBinding](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.GcpUserAccessBinding)>`  
  
  
### getIamPolicy(GetIamPolicyRequest request, StreamObserver<Policy> responseObserver)
    
    
    public default void getIamPolicy(GetIamPolicyRequest request, StreamObserver<Policy> responseObserver)

Gets the IAM policy for the specified Access Context Manager access policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.GetIamPolicyRequest`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<com.google.iam.v1.Policy>`  
  
  
### getServicePerimeter(GetServicePerimeterRequest request, StreamObserver<ServicePerimeter> responseObserver)
    
    
    public default void getServicePerimeter(GetServicePerimeterRequest request, StreamObserver<ServicePerimeter> responseObserver)

Gets a [service perimeter] [google.identity.accesscontextmanager.v1.ServicePerimeter] based on the resource name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetServicePerimeterRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.GetServicePerimeterRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ServicePerimeter](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeter)>`  
  
  
### listAccessLevels(ListAccessLevelsRequest request, StreamObserver<ListAccessLevelsResponse> responseObserver)
    
    
    public default void listAccessLevels(ListAccessLevelsRequest request, StreamObserver<ListAccessLevelsResponse> responseObserver)

Lists all [access levels] [google.identity.accesscontextmanager.v1.AccessLevel] for an access policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAccessLevelsRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ListAccessLevelsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListAccessLevelsResponse](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ListAccessLevelsResponse)>`  
  
  
### listAccessPolicies(ListAccessPoliciesRequest request, StreamObserver<ListAccessPoliciesResponse> responseObserver)
    
    
    public default void listAccessPolicies(ListAccessPoliciesRequest request, StreamObserver<ListAccessPoliciesResponse> responseObserver)

Lists all [access policies] [google.identity.accesscontextmanager.v1.AccessPolicy] in an organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAccessPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ListAccessPoliciesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListAccessPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ListAccessPoliciesResponse)>`  
  
  
### listGcpUserAccessBindings(ListGcpUserAccessBindingsRequest request, StreamObserver<ListGcpUserAccessBindingsResponse> responseObserver)
    
    
    public default void listGcpUserAccessBindings(ListGcpUserAccessBindingsRequest request, StreamObserver<ListGcpUserAccessBindingsResponse> responseObserver)

Lists all [GcpUserAccessBindings] [google.identity.accesscontextmanager.v1.GcpUserAccessBinding] for a Google Cloud organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGcpUserAccessBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ListGcpUserAccessBindingsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListGcpUserAccessBindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ListGcpUserAccessBindingsResponse)>`  
  
  
### listServicePerimeters(ListServicePerimetersRequest request, StreamObserver<ListServicePerimetersResponse> responseObserver)
    
    
    public default void listServicePerimeters(ListServicePerimetersRequest request, StreamObserver<ListServicePerimetersResponse> responseObserver)

Lists all [service perimeters] [google.identity.accesscontextmanager.v1.ServicePerimeter] for an access policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListServicePerimetersRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ListServicePerimetersRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListServicePerimetersResponse](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ListServicePerimetersResponse)>`  
  
  
### replaceAccessLevels(ReplaceAccessLevelsRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void replaceAccessLevels(ReplaceAccessLevelsRequest request, StreamObserver<Operation> responseObserver)

Replaces all existing [access levels] [google.identity.accesscontextmanager.v1.AccessLevel] in an [access policy] [google.identity.accesscontextmanager.v1.AccessPolicy] with the [access levels] [google.identity.accesscontextmanager.v1.AccessLevel] provided. This is done atomically. The long-running operation from this RPC has a successful status after all replacements propagate to long-lasting storage. If the replacement contains errors, an error response is returned for the first error encountered. Upon error, the replacement is cancelled, and existing [access levels] [google.identity.accesscontextmanager.v1.AccessLevel] are not affected. The Operation.response field contains ReplaceAccessLevelsResponse. Removing [access levels] [google.identity.accesscontextmanager.v1.AccessLevel] contained in existing [service perimeters] [google.identity.accesscontextmanager.v1.ServicePerimeter] result in an error.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReplaceAccessLevelsRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ReplaceAccessLevelsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### replaceServicePerimeters(ReplaceServicePerimetersRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void replaceServicePerimeters(ReplaceServicePerimetersRequest request, StreamObserver<Operation> responseObserver)

Replace all existing [service perimeters] [google.identity.accesscontextmanager.v1.ServicePerimeter] in an [access policy] [google.identity.accesscontextmanager.v1.AccessPolicy] with the [service perimeters] [google.identity.accesscontextmanager.v1.ServicePerimeter] provided. This is done atomically. The long-running operation from this RPC has a successful status after all replacements propagate to long-lasting storage. Replacements containing errors result in an error response for the first error encountered. Upon an error, replacement are cancelled and existing [service perimeters] [google.identity.accesscontextmanager.v1.ServicePerimeter] are not affected. The Operation.response field contains ReplaceServicePerimetersResponse.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReplaceServicePerimetersRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ReplaceServicePerimetersRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### setIamPolicy(SetIamPolicyRequest request, StreamObserver<Policy> responseObserver)
    
    
    public default void setIamPolicy(SetIamPolicyRequest request, StreamObserver<Policy> responseObserver)

Sets the IAM policy for the specified Access Context Manager access policy. This method replaces the existing IAM policy on the access policy. The IAM policy controls the set of users who can perform specific operations on the Access Context Manager access policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.SetIamPolicyRequest`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<com.google.iam.v1.Policy>`  
  
  
### testIamPermissions(TestIamPermissionsRequest request, StreamObserver<TestIamPermissionsResponse> responseObserver)
    
    
    public default void testIamPermissions(TestIamPermissionsRequest request, StreamObserver<TestIamPermissionsResponse> responseObserver)

Returns the IAM permissions that the caller has on the specified Access Context Manager resource. The resource can be an AccessPolicy, AccessLevel, or ServicePerimeter. This method does not support other resources.

**Parameters**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.TestIamPermissionsRequest`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<com.google.iam.v1.TestIamPermissionsResponse>`  
  
  
### updateAccessLevel(UpdateAccessLevelRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void updateAccessLevel(UpdateAccessLevelRequest request, StreamObserver<Operation> responseObserver)

Updates an [access level] [google.identity.accesscontextmanager.v1.AccessLevel]. The long-running operation from this RPC has a successful status after the changes to the [access level] [google.identity.accesscontextmanager.v1.AccessLevel] propagate to long-lasting storage. If [access levels] [google.identity.accesscontextmanager.v1.AccessLevel] contain errors, an error response is returned for the first error encountered.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAccessLevelRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.UpdateAccessLevelRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateAccessPolicy(UpdateAccessPolicyRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void updateAccessPolicy(UpdateAccessPolicyRequest request, StreamObserver<Operation> responseObserver)

Updates an [access policy] [google.identity.accesscontextmanager.v1.AccessPolicy]. The long-running operation from this RPC has a successful status after the changes to the [access policy] [google.identity.accesscontextmanager.v1.AccessPolicy] propagate to long-lasting storage.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAccessPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.UpdateAccessPolicyRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateGcpUserAccessBinding(UpdateGcpUserAccessBindingRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void updateGcpUserAccessBinding(UpdateGcpUserAccessBindingRequest request, StreamObserver<Operation> responseObserver)

Updates a [GcpUserAccessBinding] [google.identity.accesscontextmanager.v1.GcpUserAccessBinding]. Completion of this long-running operation does not necessarily signify that the changed binding is deployed onto all affected users, which may take more time.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGcpUserAccessBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.UpdateGcpUserAccessBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateServicePerimeter(UpdateServicePerimeterRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void updateServicePerimeter(UpdateServicePerimeterRequest request, StreamObserver<Operation> responseObserver)

Updates a [service perimeter] [google.identity.accesscontextmanager.v1.ServicePerimeter]. The long-running operation from this RPC has a successful status after the [service perimeter] [google.identity.accesscontextmanager.v1.ServicePerimeter] propagates to long-lasting storage. If a [service perimeter] [google.identity.accesscontextmanager.v1.ServicePerimeter] contains errors, an error response is returned for the first error encountered.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateServicePerimeterRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.UpdateServicePerimeterRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
