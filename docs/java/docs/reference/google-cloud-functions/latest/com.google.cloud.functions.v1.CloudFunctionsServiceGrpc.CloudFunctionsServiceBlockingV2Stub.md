---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-functions/latest/com.google.cloud.functions.v1.CloudFunctionsServiceGrpc.CloudFunctionsServiceBlockingV2Stub
title: Class CloudFunctionsServiceGrpc.CloudFunctionsServiceBlockingV2Stub (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:29:20.241395+00:00
---

# Class CloudFunctionsServiceGrpc.CloudFunctionsServiceBlockingV2Stub (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-functions/latest/com.google.cloud.functions.v1.CloudFunctionsServiceGrpc.CloudFunctionsServiceBlockingV2Stub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CloudFunctionsServiceGrpc.CloudFunctionsServiceBlockingV2Stub (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.83.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.4  2.4.3  2.3.6 
    
    
    public static final class CloudFunctionsServiceGrpc.CloudFunctionsServiceBlockingV2Stub extends AbstractBlockingStub<CloudFunctionsServiceGrpc.CloudFunctionsServiceBlockingV2Stub>

A stub to allow clients to do synchronous rpc calls to service CloudFunctionsService.

A service that application uses to manipulate triggers and functions.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > CloudFunctionsServiceGrpc.CloudFunctionsServiceBlockingV2Stub

## Inherited Members

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

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
    
    
    protected CloudFunctionsServiceGrpc.CloudFunctionsServiceBlockingV2Stub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudFunctionsServiceGrpc.CloudFunctionsServiceBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-functions/latest/com.google.cloud.functions.v1.CloudFunctionsServiceGrpc.CloudFunctionsServiceBlockingV2Stub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### callFunction(CallFunctionRequest request)
    
    
    public CallFunctionResponse callFunction(CallFunctionRequest request)

Synchronously invokes a deployed Cloud Function. To be used for testing purposes as very limited traffic is allowed. For more information on the actual limits, refer to [Rate Limits](https://cloud.google.com/functions/quotas#rate_limits).

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CallFunctionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-functions/latest/com.google.cloud.functions.v1.CallFunctionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CallFunctionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-functions/latest/com.google.cloud.functions.v1.CallFunctionResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createFunction(CreateFunctionRequest request)
    
    
    public Operation createFunction(CreateFunctionRequest request)

Creates a new function. If a function with the given name already exists in the specified project, the long running operation will return `ALREADY_EXISTS` error.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateFunctionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-functions/latest/com.google.cloud.functions.v1.CreateFunctionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteFunction(DeleteFunctionRequest request)
    
    
    public Operation deleteFunction(DeleteFunctionRequest request)

Deletes a function with the given name from the specified project. If the given function is used by some trigger, the trigger will be updated to remove this function.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteFunctionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-functions/latest/com.google.cloud.functions.v1.DeleteFunctionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### generateDownloadUrl(GenerateDownloadUrlRequest request)
    
    
    public GenerateDownloadUrlResponse generateDownloadUrl(GenerateDownloadUrlRequest request)

Returns a signed URL for downloading deployed function source code. The URL is only valid for a limited period and should be used within minutes after generation. For more information about the signed URL usage see: <https://cloud.google.com/storage/docs/access-control/signed-urls>

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GenerateDownloadUrlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-functions/latest/com.google.cloud.functions.v1.GenerateDownloadUrlRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GenerateDownloadUrlResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-functions/latest/com.google.cloud.functions.v1.GenerateDownloadUrlResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### generateUploadUrl(GenerateUploadUrlRequest request)
    
    
    public GenerateUploadUrlResponse generateUploadUrl(GenerateUploadUrlRequest request)

Returns a signed URL for uploading a function source code. For more information about the signed URL usage see: <https://cloud.google.com/storage/docs/access-control/signed-urls>. Once the function source code upload is complete, the used signed URL should be provided in CreateFunction or UpdateFunction request as a reference to the function source code. When uploading source code to the generated signed URL, please follow these restrictions:

  * Source file type should be a zip file.
  * Source file size should not exceed 100MB limit.
  * No credentials should be attached - the signed URLs provide access to the target bucket using internal service identity; if credentials were attached, the identity from the credentials would be used, but that identity does not have permissions to upload files to the URL. When making a HTTP PUT request, these two headers need to be specified:
  * `content-type: application/zip`
  * `x-goog-content-length-range: 0,104857600` And this header SHOULD NOT be specified:
  * `Authorization: Bearer YOUR_TOKEN`



**Parameter**  
---  
**Name** | **Description**  
`request` | `[GenerateUploadUrlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-functions/latest/com.google.cloud.functions.v1.GenerateUploadUrlRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GenerateUploadUrlResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-functions/latest/com.google.cloud.functions.v1.GenerateUploadUrlResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getFunction(GetFunctionRequest request)
    
    
    public CloudFunction getFunction(GetFunctionRequest request)

Returns a function with the given name from the requested project.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetFunctionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-functions/latest/com.google.cloud.functions.v1.GetFunctionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudFunction](https://docs.cloud.google.com/java/docs/reference/google-cloud-functions/latest/com.google.cloud.functions.v1.CloudFunction)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public Policy getIamPolicy(GetIamPolicyRequest request)

Gets the IAM access control policy for a function. Returns an empty policy if the function exists and does not have a policy set.

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.GetIamPolicyRequest`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listFunctions(ListFunctionsRequest request)
    
    
    public ListFunctionsResponse listFunctions(ListFunctionsRequest request)

Returns a list of functions that belong to the requested project.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListFunctionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-functions/latest/com.google.cloud.functions.v1.ListFunctionsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListFunctionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-functions/latest/com.google.cloud.functions.v1.ListFunctionsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### setIamPolicy(SetIamPolicyRequest request)
    
    
    public Policy setIamPolicy(SetIamPolicyRequest request)

Sets the IAM access control policy on the specified function. Replaces any existing policy.

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.SetIamPolicyRequest`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### testIamPermissions(TestIamPermissionsRequest request)
    
    
    public TestIamPermissionsResponse testIamPermissions(TestIamPermissionsRequest request)

Tests the specified permissions against the IAM access control policy for a function. If the function does not exist, this will return an empty set of permissions, not a NOT_FOUND error.

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.TestIamPermissionsRequest`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.TestIamPermissionsResponse` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateFunction(UpdateFunctionRequest request)
    
    
    public Operation updateFunction(UpdateFunctionRequest request)

Updates existing function.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateFunctionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-functions/latest/com.google.cloud.functions.v1.UpdateFunctionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
