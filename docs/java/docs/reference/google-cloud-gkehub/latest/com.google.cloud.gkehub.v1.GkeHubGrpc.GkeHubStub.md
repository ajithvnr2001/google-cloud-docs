---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.GkeHubGrpc.GkeHubStub
title: Class GkeHubGrpc.GkeHubStub (1.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:44:33.224830+00:00
---

# Class GkeHubGrpc.GkeHubStub (1.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.GkeHubGrpc.GkeHubStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class GkeHubGrpc.GkeHubStub (1.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.99.0 (latest)  1.95.0  1.94.0  1.93.0  1.91.0  1.88.0  1.87.0  1.85.0  1.83.0  1.82.0  1.81.0  1.80.0  1.78.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.70.0  1.68.0  1.67.0  1.64.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.6  1.2.1  1.1.0  1.0.1  0.5.4 
    
    
    public static final class GkeHubGrpc.GkeHubStub extends AbstractAsyncStub<GkeHubGrpc.GkeHubStub>

A stub to allow clients to do asynchronous rpc calls to service GkeHub.

The GKE Hub service handles the registration of many Kubernetes clusters to Google Cloud, and the management of multi-cluster features over those clusters. The GKE Hub service operates on the following resources:

  * Membership
  * Feature GKE Hub is currently available in the global region and all regions in <https://cloud.google.com/compute/docs/regions-zones>. Feature is only available in global region while membership is global region and all the regions. **Membership management may be non-trivial:** it is recommended to use one of the Google-provided client libraries or tools where possible when working with Membership resources.



## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractAsyncStub > GkeHubGrpc.GkeHubStub

## Inherited Members

io.grpc.stub.AbstractAsyncStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractAsyncStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

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
    
    
    protected GkeHubGrpc.GkeHubStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[GkeHubGrpc.GkeHubStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.GkeHubGrpc.GkeHubStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createFeature(CreateFeatureRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createFeature(CreateFeatureRequest request, StreamObserver<Operation> responseObserver)

Adds a new Feature.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.CreateFeatureRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createFleet(CreateFleetRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createFleet(CreateFleetRequest request, StreamObserver<Operation> responseObserver)

Creates a fleet.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFleetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.CreateFleetRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createMembership(CreateMembershipRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createMembership(CreateMembershipRequest request, StreamObserver<Operation> responseObserver)

Creates a new Membership. **This is currently only supported for GKE clusters on Google Cloud**. To register other clusters, follow the instructions at <https://cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster>.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateMembershipRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.CreateMembershipRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createMembershipBinding(CreateMembershipBindingRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createMembershipBinding(CreateMembershipBindingRequest request, StreamObserver<Operation> responseObserver)

Creates a MembershipBinding.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateMembershipBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.CreateMembershipBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createMembershipRBACRoleBinding(CreateMembershipRBACRoleBindingRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createMembershipRBACRoleBinding(CreateMembershipRBACRoleBindingRequest request, StreamObserver<Operation> responseObserver)

Creates a Membership RBACRoleBinding.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateMembershipRBACRoleBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.CreateMembershipRBACRoleBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createScope(CreateScopeRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createScope(CreateScopeRequest request, StreamObserver<Operation> responseObserver)

Creates a Scope.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateScopeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.CreateScopeRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createScopeNamespace(CreateScopeNamespaceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createScopeNamespace(CreateScopeNamespaceRequest request, StreamObserver<Operation> responseObserver)

Creates a fleet namespace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateScopeNamespaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.CreateScopeNamespaceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createScopeRBACRoleBinding(CreateScopeRBACRoleBindingRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createScopeRBACRoleBinding(CreateScopeRBACRoleBindingRequest request, StreamObserver<Operation> responseObserver)

Creates a Scope RBACRoleBinding.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateScopeRBACRoleBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.CreateScopeRBACRoleBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteFeature(DeleteFeatureRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteFeature(DeleteFeatureRequest request, StreamObserver<Operation> responseObserver)

Removes a Feature.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.DeleteFeatureRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteFleet(DeleteFleetRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteFleet(DeleteFleetRequest request, StreamObserver<Operation> responseObserver)

Removes a Fleet. There must be no memberships remaining in the Fleet.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFleetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.DeleteFleetRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteMembership(DeleteMembershipRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteMembership(DeleteMembershipRequest request, StreamObserver<Operation> responseObserver)

Removes a Membership. **This is currently only supported for GKE clusters on Google Cloud**. To unregister other clusters, follow the instructions at <https://cloud.google.com/anthos/multicluster-management/connect/unregistering-a-cluster>.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteMembershipRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.DeleteMembershipRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteMembershipBinding(DeleteMembershipBindingRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteMembershipBinding(DeleteMembershipBindingRequest request, StreamObserver<Operation> responseObserver)

Deletes a MembershipBinding.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteMembershipBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.DeleteMembershipBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteMembershipRBACRoleBinding(DeleteMembershipRBACRoleBindingRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteMembershipRBACRoleBinding(DeleteMembershipRBACRoleBindingRequest request, StreamObserver<Operation> responseObserver)

Deletes a Membership RBACRoleBinding.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteMembershipRBACRoleBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.DeleteMembershipRBACRoleBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteScope(DeleteScopeRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteScope(DeleteScopeRequest request, StreamObserver<Operation> responseObserver)

Deletes a Scope.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteScopeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.DeleteScopeRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteScopeNamespace(DeleteScopeNamespaceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteScopeNamespace(DeleteScopeNamespaceRequest request, StreamObserver<Operation> responseObserver)

Deletes a fleet namespace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteScopeNamespaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.DeleteScopeNamespaceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteScopeRBACRoleBinding(DeleteScopeRBACRoleBindingRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteScopeRBACRoleBinding(DeleteScopeRBACRoleBindingRequest request, StreamObserver<Operation> responseObserver)

Deletes a Scope RBACRoleBinding.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteScopeRBACRoleBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.DeleteScopeRBACRoleBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### generateConnectManifest(GenerateConnectManifestRequest request, StreamObserver<GenerateConnectManifestResponse> responseObserver)
    
    
    public void generateConnectManifest(GenerateConnectManifestRequest request, StreamObserver<GenerateConnectManifestResponse> responseObserver)

Generates the manifest for deployment of the GKE connect agent. **This method is used internally by Google-provided libraries.** Most clients should not need to call this method directly.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateConnectManifestRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.GenerateConnectManifestRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[GenerateConnectManifestResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.GenerateConnectManifestResponse)>`  
  
  
### generateMembershipRBACRoleBindingYAML(GenerateMembershipRBACRoleBindingYAMLRequest request, StreamObserver<GenerateMembershipRBACRoleBindingYAMLResponse> responseObserver)
    
    
    public void generateMembershipRBACRoleBindingYAML(GenerateMembershipRBACRoleBindingYAMLRequest request, StreamObserver<GenerateMembershipRBACRoleBindingYAMLResponse> responseObserver)

Generates a YAML of the RBAC policies for the specified RoleBinding and its associated impersonation resources.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateMembershipRBACRoleBindingYAMLRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.GenerateMembershipRBACRoleBindingYAMLRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[GenerateMembershipRBACRoleBindingYAMLResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.GenerateMembershipRBACRoleBindingYAMLResponse)>`  
  
  
### getFeature(GetFeatureRequest request, StreamObserver<Feature> responseObserver)
    
    
    public void getFeature(GetFeatureRequest request, StreamObserver<Feature> responseObserver)

Gets details of a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.GetFeatureRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.Feature)>`  
  
  
### getFleet(GetFleetRequest request, StreamObserver<Fleet> responseObserver)
    
    
    public void getFleet(GetFleetRequest request, StreamObserver<Fleet> responseObserver)

Returns the details of a fleet.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFleetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.GetFleetRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Fleet](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.Fleet)>`  
  
  
### getMembership(GetMembershipRequest request, StreamObserver<Membership> responseObserver)
    
    
    public void getMembership(GetMembershipRequest request, StreamObserver<Membership> responseObserver)

Gets the details of a Membership.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMembershipRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.GetMembershipRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Membership](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.Membership)>`  
  
  
### getMembershipBinding(GetMembershipBindingRequest request, StreamObserver<MembershipBinding> responseObserver)
    
    
    public void getMembershipBinding(GetMembershipBindingRequest request, StreamObserver<MembershipBinding> responseObserver)

Returns the details of a MembershipBinding.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMembershipBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.GetMembershipBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[MembershipBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.MembershipBinding)>`  
  
  
### getMembershipRBACRoleBinding(GetMembershipRBACRoleBindingRequest request, StreamObserver<RBACRoleBinding> responseObserver)
    
    
    public void getMembershipRBACRoleBinding(GetMembershipRBACRoleBindingRequest request, StreamObserver<RBACRoleBinding> responseObserver)

Returns the details of a Membership RBACRoleBinding.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMembershipRBACRoleBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.GetMembershipRBACRoleBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[RBACRoleBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.RBACRoleBinding)>`  
  
  
### getScope(GetScopeRequest request, StreamObserver<Scope> responseObserver)
    
    
    public void getScope(GetScopeRequest request, StreamObserver<Scope> responseObserver)

Returns the details of a Scope.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetScopeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.GetScopeRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Scope](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.Scope)>`  
  
  
### getScopeNamespace(GetScopeNamespaceRequest request, StreamObserver<Namespace> responseObserver)
    
    
    public void getScopeNamespace(GetScopeNamespaceRequest request, StreamObserver<Namespace> responseObserver)

Returns the details of a fleet namespace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetScopeNamespaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.GetScopeNamespaceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Namespace](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.Namespace)>`  
  
  
### getScopeRBACRoleBinding(GetScopeRBACRoleBindingRequest request, StreamObserver<RBACRoleBinding> responseObserver)
    
    
    public void getScopeRBACRoleBinding(GetScopeRBACRoleBindingRequest request, StreamObserver<RBACRoleBinding> responseObserver)

Returns the details of a Scope RBACRoleBinding.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetScopeRBACRoleBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.GetScopeRBACRoleBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[RBACRoleBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.RBACRoleBinding)>`  
  
  
### listBoundMemberships(ListBoundMembershipsRequest request, StreamObserver<ListBoundMembershipsResponse> responseObserver)
    
    
    public void listBoundMemberships(ListBoundMembershipsRequest request, StreamObserver<ListBoundMembershipsResponse> responseObserver)

Lists Memberships bound to a Scope. The response includes relevant Memberships from all regions.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBoundMembershipsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListBoundMembershipsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListBoundMembershipsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListBoundMembershipsResponse)>`  
  
  
### listFeatures(ListFeaturesRequest request, StreamObserver<ListFeaturesResponse> responseObserver)
    
    
    public void listFeatures(ListFeaturesRequest request, StreamObserver<ListFeaturesResponse> responseObserver)

Lists Features in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFeaturesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListFeaturesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListFeaturesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListFeaturesResponse)>`  
  
  
### listFleets(ListFleetsRequest request, StreamObserver<ListFleetsResponse> responseObserver)
    
    
    public void listFleets(ListFleetsRequest request, StreamObserver<ListFleetsResponse> responseObserver)

Returns all fleets within an organization or a project that the caller has access to.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFleetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListFleetsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListFleetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListFleetsResponse)>`  
  
  
### listMembershipBindings(ListMembershipBindingsRequest request, StreamObserver<ListMembershipBindingsResponse> responseObserver)
    
    
    public void listMembershipBindings(ListMembershipBindingsRequest request, StreamObserver<ListMembershipBindingsResponse> responseObserver)

Lists MembershipBindings.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMembershipBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListMembershipBindingsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListMembershipBindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListMembershipBindingsResponse)>`  
  
  
### listMembershipRBACRoleBindings(ListMembershipRBACRoleBindingsRequest request, StreamObserver<ListMembershipRBACRoleBindingsResponse> responseObserver)
    
    
    public void listMembershipRBACRoleBindings(ListMembershipRBACRoleBindingsRequest request, StreamObserver<ListMembershipRBACRoleBindingsResponse> responseObserver)

Lists all Membership RBACRoleBindings.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMembershipRBACRoleBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListMembershipRBACRoleBindingsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListMembershipRBACRoleBindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListMembershipRBACRoleBindingsResponse)>`  
  
  
### listMemberships(ListMembershipsRequest request, StreamObserver<ListMembershipsResponse> responseObserver)
    
    
    public void listMemberships(ListMembershipsRequest request, StreamObserver<ListMembershipsResponse> responseObserver)

Lists Memberships in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMembershipsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListMembershipsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListMembershipsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListMembershipsResponse)>`  
  
  
### listPermittedScopes(ListPermittedScopesRequest request, StreamObserver<ListPermittedScopesResponse> responseObserver)
    
    
    public void listPermittedScopes(ListPermittedScopesRequest request, StreamObserver<ListPermittedScopesResponse> responseObserver)

Lists permitted Scopes.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPermittedScopesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListPermittedScopesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListPermittedScopesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListPermittedScopesResponse)>`  
  
  
### listScopeNamespaces(ListScopeNamespacesRequest request, StreamObserver<ListScopeNamespacesResponse> responseObserver)
    
    
    public void listScopeNamespaces(ListScopeNamespacesRequest request, StreamObserver<ListScopeNamespacesResponse> responseObserver)

Lists fleet namespaces.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListScopeNamespacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListScopeNamespacesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListScopeNamespacesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListScopeNamespacesResponse)>`  
  
  
### listScopeRBACRoleBindings(ListScopeRBACRoleBindingsRequest request, StreamObserver<ListScopeRBACRoleBindingsResponse> responseObserver)
    
    
    public void listScopeRBACRoleBindings(ListScopeRBACRoleBindingsRequest request, StreamObserver<ListScopeRBACRoleBindingsResponse> responseObserver)

Lists all Scope RBACRoleBindings.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListScopeRBACRoleBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListScopeRBACRoleBindingsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListScopeRBACRoleBindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListScopeRBACRoleBindingsResponse)>`  
  
  
### listScopes(ListScopesRequest request, StreamObserver<ListScopesResponse> responseObserver)
    
    
    public void listScopes(ListScopesRequest request, StreamObserver<ListScopesResponse> responseObserver)

Lists Scopes.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListScopesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListScopesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListScopesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListScopesResponse)>`  
  
  
### updateFeature(UpdateFeatureRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateFeature(UpdateFeatureRequest request, StreamObserver<Operation> responseObserver)

Updates an existing Feature.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.UpdateFeatureRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateFleet(UpdateFleetRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateFleet(UpdateFleetRequest request, StreamObserver<Operation> responseObserver)

Updates a fleet.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFleetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.UpdateFleetRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateMembership(UpdateMembershipRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateMembership(UpdateMembershipRequest request, StreamObserver<Operation> responseObserver)

Updates an existing Membership.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateMembershipRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.UpdateMembershipRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateMembershipBinding(UpdateMembershipBindingRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateMembershipBinding(UpdateMembershipBindingRequest request, StreamObserver<Operation> responseObserver)

Updates a MembershipBinding.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateMembershipBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.UpdateMembershipBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateMembershipRBACRoleBinding(UpdateMembershipRBACRoleBindingRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateMembershipRBACRoleBinding(UpdateMembershipRBACRoleBindingRequest request, StreamObserver<Operation> responseObserver)

Updates a Membership RBACRoleBinding.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateMembershipRBACRoleBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.UpdateMembershipRBACRoleBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateScope(UpdateScopeRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateScope(UpdateScopeRequest request, StreamObserver<Operation> responseObserver)

Updates a scopes.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateScopeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.UpdateScopeRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateScopeNamespace(UpdateScopeNamespaceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateScopeNamespace(UpdateScopeNamespaceRequest request, StreamObserver<Operation> responseObserver)

Updates a fleet namespace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateScopeNamespaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.UpdateScopeNamespaceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateScopeRBACRoleBinding(UpdateScopeRBACRoleBindingRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateScopeRBACRoleBinding(UpdateScopeRBACRoleBindingRequest request, StreamObserver<Operation> responseObserver)

Updates a Scope RBACRoleBinding.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateScopeRBACRoleBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.UpdateScopeRBACRoleBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
