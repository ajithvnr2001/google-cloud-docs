---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1beta2.SecretManagerServiceGrpc.SecretManagerServiceStub
title: Class SecretManagerServiceGrpc.SecretManagerServiceStub (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:12:20.226105+00:00
---

# Class SecretManagerServiceGrpc.SecretManagerServiceStub (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1beta2.SecretManagerServiceGrpc.SecretManagerServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SecretManagerServiceGrpc.SecretManagerServiceStub (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.10  2.2.0  2.1.7  2.0.7 
    
    
    public static final class SecretManagerServiceGrpc.SecretManagerServiceStub extends AbstractAsyncStub<SecretManagerServiceGrpc.SecretManagerServiceStub>

A stub to allow clients to do asynchronous rpc calls to service SecretManagerService.

Secret Manager Service Manages secrets and operations using those secrets. Implements a REST model with the following objects:

  * Secret
  * SecretVersion



## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractAsyncStub > SecretManagerServiceGrpc.SecretManagerServiceStub

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

### accessSecretVersion(AccessSecretVersionRequest request, StreamObserver<AccessSecretVersionResponse> responseObserver)
    
    
    public void accessSecretVersion(AccessSecretVersionRequest request, StreamObserver<AccessSecretVersionResponse> responseObserver)

Accesses a SecretVersion. This call returns the secret data. `projects/*/secrets/*/versions/latest` is an alias to the most recently created SecretVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AccessSecretVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1beta2.AccessSecretVersionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AccessSecretVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1beta2.AccessSecretVersionResponse)>`  
  
  
### addSecretVersion(AddSecretVersionRequest request, StreamObserver<SecretVersion> responseObserver)
    
    
    public void addSecretVersion(AddSecretVersionRequest request, StreamObserver<SecretVersion> responseObserver)

Creates a new SecretVersion containing secret data and attaches it to an existing Secret.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddSecretVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1beta2.AddSecretVersionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SecretVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1beta2.SecretVersion)>`  
  
  
### build(Channel channel, CallOptions callOptions)
    
    
    protected SecretManagerServiceGrpc.SecretManagerServiceStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecretManagerServiceGrpc.SecretManagerServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1beta2.SecretManagerServiceGrpc.SecretManagerServiceStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createSecret(CreateSecretRequest request, StreamObserver<Secret> responseObserver)
    
    
    public void createSecret(CreateSecretRequest request, StreamObserver<Secret> responseObserver)

Creates a new Secret containing no SecretVersions.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSecretRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1beta2.CreateSecretRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1beta2.Secret)>`  
  
  
### deleteSecret(DeleteSecretRequest request, StreamObserver<Empty> responseObserver)
    
    
    public void deleteSecret(DeleteSecretRequest request, StreamObserver<Empty> responseObserver)

Deletes a Secret.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSecretRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1beta2.DeleteSecretRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### destroySecretVersion(DestroySecretVersionRequest request, StreamObserver<SecretVersion> responseObserver)
    
    
    public void destroySecretVersion(DestroySecretVersionRequest request, StreamObserver<SecretVersion> responseObserver)

Destroys a SecretVersion. Sets the state of the SecretVersion to DESTROYED and irrevocably destroys the secret data.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DestroySecretVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1beta2.DestroySecretVersionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SecretVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1beta2.SecretVersion)>`  
  
  
### disableSecretVersion(DisableSecretVersionRequest request, StreamObserver<SecretVersion> responseObserver)
    
    
    public void disableSecretVersion(DisableSecretVersionRequest request, StreamObserver<SecretVersion> responseObserver)

Disables a SecretVersion. Sets the state of the SecretVersion to DISABLED.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DisableSecretVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1beta2.DisableSecretVersionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SecretVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1beta2.SecretVersion)>`  
  
  
### enableSecretVersion(EnableSecretVersionRequest request, StreamObserver<SecretVersion> responseObserver)
    
    
    public void enableSecretVersion(EnableSecretVersionRequest request, StreamObserver<SecretVersion> responseObserver)

Enables a SecretVersion. Sets the state of the SecretVersion to ENABLED.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[EnableSecretVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1beta2.EnableSecretVersionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SecretVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1beta2.SecretVersion)>`  
  
  
### getIamPolicy(GetIamPolicyRequest request, StreamObserver<Policy> responseObserver)
    
    
    public void getIamPolicy(GetIamPolicyRequest request, StreamObserver<Policy> responseObserver)

Gets the access control policy for a secret. Returns empty policy if the secret exists and does not have a policy set.

**Parameters**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.GetIamPolicyRequest`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<com.google.iam.v1.Policy>`  
  
  
### getSecret(GetSecretRequest request, StreamObserver<Secret> responseObserver)
    
    
    public void getSecret(GetSecretRequest request, StreamObserver<Secret> responseObserver)

Gets metadata for a given Secret.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSecretRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1beta2.GetSecretRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1beta2.Secret)>`  
  
  
### getSecretVersion(GetSecretVersionRequest request, StreamObserver<SecretVersion> responseObserver)
    
    
    public void getSecretVersion(GetSecretVersionRequest request, StreamObserver<SecretVersion> responseObserver)

Gets metadata for a SecretVersion. `projects/*/secrets/*/versions/latest` is an alias to the most recently created SecretVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSecretVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1beta2.GetSecretVersionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SecretVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1beta2.SecretVersion)>`  
  
  
### listSecretVersions(ListSecretVersionsRequest request, StreamObserver<ListSecretVersionsResponse> responseObserver)
    
    
    public void listSecretVersions(ListSecretVersionsRequest request, StreamObserver<ListSecretVersionsResponse> responseObserver)

Lists SecretVersions. This call does not return secret data.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSecretVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1beta2.ListSecretVersionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListSecretVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1beta2.ListSecretVersionsResponse)>`  
  
  
### listSecrets(ListSecretsRequest request, StreamObserver<ListSecretsResponse> responseObserver)
    
    
    public void listSecrets(ListSecretsRequest request, StreamObserver<ListSecretsResponse> responseObserver)

Lists Secrets.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSecretsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1beta2.ListSecretsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListSecretsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1beta2.ListSecretsResponse)>`  
  
  
### setIamPolicy(SetIamPolicyRequest request, StreamObserver<Policy> responseObserver)
    
    
    public void setIamPolicy(SetIamPolicyRequest request, StreamObserver<Policy> responseObserver)

Sets the access control policy on the specified secret. Replaces any existing policy. Permissions on SecretVersions are enforced according to the policy set on the associated Secret.

**Parameters**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.SetIamPolicyRequest`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<com.google.iam.v1.Policy>`  
  
  
### testIamPermissions(TestIamPermissionsRequest request, StreamObserver<TestIamPermissionsResponse> responseObserver)
    
    
    public void testIamPermissions(TestIamPermissionsRequest request, StreamObserver<TestIamPermissionsResponse> responseObserver)

Returns permissions that a caller has for the specified secret. If the secret does not exist, this call returns an empty set of permissions, not a NOT_FOUND error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

**Parameters**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.TestIamPermissionsRequest`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<com.google.iam.v1.TestIamPermissionsResponse>`  
  
  
### updateSecret(UpdateSecretRequest request, StreamObserver<Secret> responseObserver)
    
    
    public void updateSecret(UpdateSecretRequest request, StreamObserver<Secret> responseObserver)

Updates metadata of an existing Secret.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSecretRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1beta2.UpdateSecretRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1beta2.Secret)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
